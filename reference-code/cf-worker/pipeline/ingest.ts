/**
 * Modular Subject Ingestion & Semantic Linking Pipeline
 * Inserts modular subject nodes into D1, generates Workers AI embeddings,
 * inserts vectors into Cloudflare Vectorize, and computes cross-subject semantic edges.
 */

export interface SubjectNodeInput {
  id: string;
  subject: string;
  topic: string;
  subtopic?: string;
  era?: string;
  title: string;
  summary: string;
  canonical_facts: string[];
  prerequisites?: string[];
  media_type?: string;
  media_urls?: string[];
}

export class IngestionEngine {
  private db: D1Database;
  private vectorize: VectorizeIndex;
  private ai: any;

  constructor(db: D1Database, vectorize: VectorizeIndex, ai: any) {
    this.db = db;
    this.vectorize = vectorize;
    this.ai = ai;
  }

  /**
   * Ingest a batch of nodes for a specific Subject Lens
   */
  async ingestSubjectNodes(nodes: SubjectNodeInput[]): Promise<{ ingested: number; vectorsCreated: number }> {
    let count = 0;
    let vectors = 0;

    for (const node of nodes) {
      // 1. Insert or Replace into D1 master_nodes
      await this.db
        .prepare(
          `INSERT OR REPLACE INTO master_nodes 
          (id, subject, topic, subtopic, era, title, summary, canonical_facts, prerequisites)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`
        )
        .bind(
          node.id,
          node.subject,
          node.topic,
          node.subtopic || null,
          node.era || null,
          node.title,
          node.summary,
          JSON.stringify(node.canonical_facts || []),
          JSON.stringify(node.prerequisites || [])
        )
        .run();

      count++;

      // 2. Attach Media if provided
      if (node.media_urls && node.media_urls.length > 0) {
        for (const url of node.media_urls) {
          const mediaId = `media_${node.id}_${Date.now()}`;
          await this.db
            .prepare(
              `INSERT OR REPLACE INTO node_media (id, node_id, media_type, r2_url, caption)
              VALUES (?, ?, ?, ?, ?)`
            )
            .bind(mediaId, node.id, node.media_type || "image", url, node.title)
            .run();
        }
      }

      // 3. Generate Semantic Embeddings via Workers AI
      const textToEmbed = `${node.title}: ${node.summary}. Facts: ${node.canonical_facts.join(" ")}`;
      try {
        const embeddings = await this.ai.run("@cf/baai/bge-base-en-v1.5", {
          text: [textToEmbed]
        });

        let vectorValues = embeddings.data[0];
        if (vectorValues) {
          if (vectorValues.length > 768) vectorValues = vectorValues.slice(0, 768);
          // Upsert vector into Cloudflare Vectorize
          await this.vectorize.upsert([
            {
              id: node.id,
              values: vectorValues,
              metadata: {
                subject: node.subject,
                topic: node.topic,
                title: node.title
              }
            }
          ]);
          vectors++;
        }
      } catch (err) {
        console.warn(`Vector generation skipped for ${node.id}:`, err);
      }
    }

    return { ingested: count, vectorsCreated: vectors };
  }

  /**
   * Compute true cross-subject semantic edges using Vectorize nearest-neighbor search
   */
  async computeCrossSubjectSemanticEdges(
    sourceNodeId: string,
    sourceSubject: string,
    similarityThreshold: number = 0.75
  ): Promise<{ edgesCreated: number }> {
    // 1. Fetch source node vector or summary
    const nodeRes = await this.db
      .prepare(`SELECT id, title, summary, canonical_facts FROM master_nodes WHERE id = ?`)
      .bind(sourceNodeId)
      .first<{ id: string; title: string; summary: string; canonical_facts: string }>();

    if (!nodeRes) return { edgesCreated: 0 };

    const textToEmbed = `${nodeRes.title}: ${nodeRes.summary}`;
    const embeddings = await this.ai.run("@cf/baai/bge-base-en-v1.5", {
      text: [textToEmbed]
    });

    let vectorValues = embeddings.data[0];
    if (!vectorValues) return { edgesCreated: 0 };
    if (vectorValues.length > 768) vectorValues = vectorValues.slice(0, 768);

    // 2. Query Vectorize for top 10 nearest neighbors
    const matches = await this.vectorize.query(vectorValues, { topK: 10 });
    let edgesCreated = 0;

    for (const match of matches.matches) {
      // Filter out self and same subject (we want cross-subject relationships)
      if (match.id === sourceNodeId) continue;
      const targetSubject = match.metadata?.subject as string;
      if (targetSubject === sourceSubject) continue;

      if (match.score >= similarityThreshold) {
        await this.db
          .prepare(
            `INSERT OR REPLACE INTO semantic_edges 
            (source_node_id, target_node_id, source_subject, target_subject, similarity_score, reasoning)
            VALUES (?, ?, ?, ?, ?, ?)`
          )
          .bind(
            sourceNodeId,
            match.id,
            sourceSubject,
            targetSubject || "unknown",
            match.score,
            `Semantic vector similarity (${(match.score * 100).toFixed(1)}%)`
          )
          .run();

        edgesCreated++;
      }
    }

    return { edgesCreated };
  }
}
