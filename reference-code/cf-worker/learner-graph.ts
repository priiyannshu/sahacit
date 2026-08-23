/**
 * Learner Cognitive Mirrored Knowledge Graph Engine
 * Operates on Durable Object SQLite (ctx.storage.sql)
 * Tracks user memory, mastery scores, Ebbinghaus decay, and misconception flags.
 */

export interface LearnerNodeState {
  master_node_id: string;
  status: "UNEXPLORED" | "LEARNING" | "MASTERED" | "FADING" | "MISUNDERSTOOD";
  mastery_score: number;       // 0.0 to 1.0 (Bayesian / IRT mastery score)
  retention_score: number;     // Current calculated retention after Ebbinghaus decay
  last_reviewed_at: number;    // Epoch timestamp ms
  half_life_days: number;      // Memory stability (in days)
  user_notes: string;          // User synthesis / memory hook notes
  misconceptions: string;      // JSON array of specific trap options user fell for
}

export interface QuizAttemptInput {
  master_node_id: string;
  pyq_id?: number;
  selected_option: string;
  is_correct: boolean;
  confidence_score: number;    // 1 (low) to 5 (high)
  time_spent_ms: number;
}

export class LearnerGraphEngine {
  private sql: DurableObjectStorage["sql"];

  constructor(sql: DurableObjectStorage["sql"]) {
    this.sql = sql;
    this.initSchema();
  }

  /**
   * Initialize SQLite schema inside Durable Object
   */
  private initSchema() {
    this.sql.exec(`
      CREATE TABLE IF NOT EXISTS learner_nodes (
        master_node_id TEXT PRIMARY KEY,
        status TEXT NOT NULL DEFAULT 'UNEXPLORED',
        mastery_score REAL NOT NULL DEFAULT 0.0,
        last_reviewed_at INTEGER NOT NULL,
        half_life_days REAL NOT NULL DEFAULT 1.0,
        user_notes TEXT DEFAULT '',
        misconceptions TEXT DEFAULT '[]'
      );

      CREATE TABLE IF NOT EXISTS attempt_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        master_node_id TEXT NOT NULL,
        pyq_id INTEGER,
        selected_option TEXT NOT NULL,
        is_correct INTEGER NOT NULL,
        confidence_score INTEGER NOT NULL,
        time_spent_ms INTEGER NOT NULL,
        timestamp INTEGER NOT NULL
      );

      CREATE INDEX IF NOT EXISTS idx_attempt_node ON attempt_logs(master_node_id);
    `);
  }

  /**
   * Ebbinghaus Forgetting Curve calculation
   * Retention R = exp(- (t / S))
   */
  public calculateRetention(lastReviewedMs: number, halfLifeDays: number): number {
    const elapsedDays = (Date.now() - lastReviewedMs) / (1000 * 60 * 60 * 24);
    if (elapsedDays <= 0) return 1.0;
    const decayConst = Math.LN2 / halfLifeDays;
    return Math.exp(-decayConst * elapsedDays);
  }

  /**
   * Record a quiz attempt and update cognitive node state
   */
  public recordAttempt(input: QuizAttemptInput): LearnerNodeState {
    const now = Date.now();

    // Log attempt history
    this.sql.exec(`
      INSERT INTO attempt_logs (master_node_id, pyq_id, selected_option, is_correct, confidence_score, time_spent_ms, timestamp)
      VALUES (?, ?, ?, ?, ?, ?, ?)
    `, input.master_node_id, input.pyq_id || null, input.selected_option, input.is_correct ? 1 : 0, input.confidence_score, input.time_spent_ms, now);

    // Fetch existing node state
    const existingCursor = this.sql.exec(`
      SELECT * FROM learner_nodes WHERE master_node_id = ?
    `, input.master_node_id);

    const existingRows = Array.from(existingCursor) as any[];

    let currentMastery = 0.1;
    let halfLifeDays = 1.0;
    let userNotes = "";
    let misconceptions: string[] = [];

    if (existingRows.length > 0) {
      const row = existingRows[0];
      currentMastery = row.mastery_score;
      halfLifeDays = row.half_life_days;
      userNotes = row.user_notes || "";
      try { misconceptions = JSON.parse(row.misconceptions || "[]"); } catch {}
    }

    // Bayesian Knowledge Tracing / Spaced Repetition Update
    let newMastery: number;
    let newHalfLife: number;

    if (input.is_correct) {
      const boost = 0.2 * (input.confidence_score / 5);
      newMastery = Math.min(1.0, currentMastery + boost);
      newHalfLife = halfLifeDays * (1.5 + (input.confidence_score * 0.3));
    } else {
      newMastery = Math.max(0.05, currentMastery - 0.25);
      newHalfLife = Math.max(0.5, halfLifeDays * 0.5);

      if (input.selected_option && !misconceptions.includes(input.selected_option)) {
        misconceptions.push(input.selected_option);
      }
    }

    // Determine status
    let status: LearnerNodeState["status"] = "LEARNING";
    if (newMastery >= 0.85) status = "MASTERED";
    else if (!input.is_correct && misconceptions.length > 0) status = "MISUNDERSTOOD";
    else if (this.calculateRetention(now, newHalfLife) < 0.5) status = "FADING";

    // Upsert into Durable Object SQLite
    this.sql.exec(`
      INSERT INTO learner_nodes (master_node_id, status, mastery_score, last_reviewed_at, half_life_days, user_notes, misconceptions)
      VALUES (?, ?, ?, ?, ?, ?, ?)
      ON CONFLICT(master_node_id) DO UPDATE SET
        status = excluded.status,
        mastery_score = excluded.mastery_score,
        last_reviewed_at = excluded.last_reviewed_at,
        half_life_days = excluded.half_life_days,
        user_notes = excluded.user_notes,
        misconceptions = excluded.misconceptions
    `, input.master_node_id, status, newMastery, now, newHalfLife, userNotes, JSON.stringify(misconceptions));

    return {
      master_node_id: input.master_node_id,
      status,
      mastery_score: newMastery,
      retention_score: 1.0,
      last_reviewed_at: now,
      half_life_days: newHalfLife,
      user_notes: userNotes,
      misconceptions: JSON.stringify(misconceptions)
    };
  }

  /**
   * Get single node memory state
   */
  public getNodeState(masterNodeId: string): LearnerNodeState | null {
    const cursor = this.sql.exec(`SELECT * FROM learner_nodes WHERE master_node_id = ?`, masterNodeId);
    const rows = Array.from(cursor) as any[];
    if (rows.length === 0) return null;

    const row = rows[0];
    const retention = this.calculateRetention(row.last_reviewed_at, row.half_life_days);

    let status = row.status;
    if (status === "MASTERED" && retention < 0.6) status = "FADING";

    return {
      master_node_id: row.master_node_id,
      status,
      mastery_score: row.mastery_score,
      retention_score: retention,
      last_reviewed_at: row.last_reviewed_at,
      half_life_days: row.half_life_days,
      user_notes: row.user_notes || "",
      misconceptions: row.misconceptions || "[]"
    };
  }

  /**
   * Generate heatmap overlay comparing Master Nodes against Learner State
   */
  public getSubjectHeatmap(masterNodeIds: string[]): Record<string, LearnerNodeState> {
    const heatmap: Record<string, LearnerNodeState> = {};
    const cursor = this.sql.exec(`SELECT * FROM learner_nodes`);
    const rows = Array.from(cursor) as any[];

    const dbMap = new Map<string, any>();
    rows.forEach(r => dbMap.set(r.master_node_id, r));

    masterNodeIds.forEach(id => {
      if (dbMap.has(id)) {
        const row = dbMap.get(id);
        const retention = this.calculateRetention(row.last_reviewed_at, row.half_life_days);
        let status = row.status;
        if (status === "MASTERED" && retention < 0.6) status = "FADING";

        heatmap[id] = {
          master_node_id: id,
          status,
          mastery_score: row.mastery_score,
          retention_score: retention,
          last_reviewed_at: row.last_reviewed_at,
          half_life_days: row.half_life_days,
          user_notes: row.user_notes || "",
          misconceptions: row.misconceptions || "[]"
        };
      } else {
        heatmap[id] = {
          master_node_id: id,
          status: "UNEXPLORED",
          mastery_score: 0.0,
          retention_score: 0.0,
          last_reviewed_at: 0,
          half_life_days: 1.0,
          user_notes: "",
          misconceptions: "[]"
        };
      }
    });

    return heatmap;
  }

  /**
   * Fetch Spaced Repetition queue for items due for review
   */
  public getDueSpacedRepetitionQueue(limit: number = 10): LearnerNodeState[] {
    const cursor = this.sql.exec(`SELECT * FROM learner_nodes ORDER BY last_reviewed_at ASC`);
    const rows = Array.from(cursor) as any[];
    const dueQueue: LearnerNodeState[] = [];

    for (const row of rows) {
      const retention = this.calculateRetention(row.last_reviewed_at, row.half_life_days);
      if (retention < 0.7 || row.status === "FADING" || row.status === "MISUNDERSTOOD") {
        dueQueue.push({
          master_node_id: row.master_node_id,
          status: row.status,
          mastery_score: row.mastery_score,
          retention_score: retention,
          last_reviewed_at: row.last_reviewed_at,
          half_life_days: row.half_life_days,
          user_notes: row.user_notes || "",
          misconceptions: row.misconceptions || "[]"
        });
      }
      if (dueQueue.length >= limit) break;
    }

    return dueQueue;
  }
}
