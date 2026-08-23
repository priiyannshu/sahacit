import { DurableObject } from "cloudflare:workers";
import { LearnerGraphEngine, QuizAttemptInput } from "./learner-graph";
import { SocraticTutorEngine, SocraticChatContext } from "./socratic-tutor";

export interface Env {
  DB: D1Database;
  VECTOR_INDEX: VectorizeIndex;
  TUTOR_AGENT: DurableObjectNamespace;
  AI: any;
}

/**
 * UPSCTutorAgent - Stateful Socratic Agent running in Cloudflare Durable Objects.
 * Coordinates user session memory, Master KG verification, Workers AI tutoring, and Spaced Repetition drills.
 */
export class UPSCTutorAgent extends DurableObject<Env> {
  private learnerGraph: LearnerGraphEngine;
  private tutorEngine: SocraticTutorEngine;

  constructor(state: DurableObjectState, env: Env) {
    super(state, env);
    this.learnerGraph = new LearnerGraphEngine(state.storage.sql);
    this.tutorEngine = new SocraticTutorEngine(env.AI);
  }

  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);

    // Health check
    if (url.pathname.endsWith("/health")) {
      return Response.json({ status: "healthy", timestamp: new Date().toISOString() });
    }

    // Socratic Chat Endpoint (Workers AI + Learner Graph Context)
    if (url.pathname.endsWith("/chat") && request.method === "POST") {
      try {
        const body = (await request.json()) as SocraticChatContext;
        let learnerState = null;

        if (body.masterNodeId) {
          learnerState = this.learnerGraph.getNodeState(body.masterNodeId);
        }

        const context: SocraticChatContext = {
          ...body,
          learnerMasteryScore: learnerState?.mastery_score || body.learnerMasteryScore || 0,
          learnerStatus: learnerState?.status || body.learnerStatus || "UNEXPLORED",
          misconceptions: learnerState ? JSON.parse(learnerState.misconceptions || "[]") : body.misconceptions
        };

        const aiResponse = await this.tutorEngine.generateSocraticResponse(context);
        return Response.json({ success: true, response: aiResponse, learnerState });
      } catch (err: any) {
        return Response.json({ error: err.message }, { status: 500 });
      }
    }

    // Synthesis Evaluation Endpoint
    if (url.pathname.endsWith("/evaluate") && request.method === "POST") {
      try {
        const body = (await request.json()) as { userSynthesis: string; canonicalFacts: string[]; masterNodeId?: string };
        const result = await this.tutorEngine.evaluateUserSynthesis(body.userSynthesis, body.canonicalFacts || []);

        if (body.masterNodeId && result.isAccurate) {
          this.learnerGraph.recordAttempt({
            master_node_id: body.masterNodeId,
            selected_option: "SYNTHESIS_EVAL",
            is_correct: result.isAccurate,
            confidence_score: 4,
            time_spent_ms: 10000
          });
        }

        return Response.json({ success: true, evaluation: result });
      } catch (err: any) {
        return Response.json({ error: err.message }, { status: 500 });
      }
    }

    // Record Quiz Attempt
    if (url.pathname.endsWith("/attempt") && request.method === "POST") {
      try {
        const body = (await request.json()) as QuizAttemptInput;
        if (!body.master_node_id || body.is_correct === undefined) {
          return Response.json({ error: "Missing required fields master_node_id or is_correct" }, { status: 400 });
        }
        const updatedState = this.learnerGraph.recordAttempt(body);
        return Response.json({ success: true, nodeState: updatedState });
      } catch (err: any) {
        return Response.json({ error: err.message }, { status: 500 });
      }
    }

    // Get Subject Mastery Heatmap Overlay
    if (url.pathname.endsWith("/heatmap") && request.method === "POST") {
      try {
        const body = (await request.json()) as { master_node_ids: string[] };
        const heatmap = this.learnerGraph.getSubjectHeatmap(body.master_node_ids || []);
        return Response.json({ success: true, heatmap });
      } catch (err: any) {
        return Response.json({ error: err.message }, { status: 500 });
      }
    }

    // Get Spaced Repetition Queue
    if (url.pathname.endsWith("/queue")) {
      const limit = parseInt(url.searchParams.get("limit") || "10", 10);
      const queue = this.learnerGraph.getDueSpacedRepetitionQueue(limit);
      return Response.json({ success: true, queue });
    }

    // Get single node memory state
    if (url.pathname.includes("/node/")) {
      const parts = url.pathname.split("/node/");
      const nodeId = parts[1];
      const state = this.learnerGraph.getNodeState(nodeId);
      return Response.json({ success: true, nodeId, state });
    }

    return Response.json({ error: "Agent Endpoint Not Found" }, { status: 404 });
  }
}

/**
 * Main Cloudflare Worker Router & Edge Gateway
 */
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);

    // Route Agent & Learner Graph requests to Durable Object
    if (url.pathname.startsWith("/api/agent/")) {
      const id = env.TUTOR_AGENT.idFromName("default_learner_session");
      const stub = env.TUTOR_AGENT.get(id);
      return stub.fetch(request);
    }

    // Direct D1 Master Database Query Endpoint (Master KG Source of Truth)
    if (url.pathname === "/api/master/pyqs") {
      const subject = url.searchParams.get("subject");
      let query = "SELECT * FROM pyq_corpus ORDER BY year DESC LIMIT 50";
      let params: any[] = [];

      if (subject) {
        query = "SELECT * FROM pyq_corpus WHERE subject = ? ORDER BY year DESC LIMIT 50";
        params = [subject];
      }

      const { results } = await env.DB.prepare(query).bind(...params).all();
      return Response.json({ success: true, total: results.length, pyqs: results });
    }

    // Worker status endpoint
    if (url.pathname === "/api/status") {
      return Response.json({
        app: "Demolition of Prelims 2026",
        version: "2.0.0-agentic",
        status: "active",
        aiModel: "@cf/meta/llama-3.1-8b-instruct",
        learnerEngine: "Durable Object SQLite"
      });
    }

    return Response.json({ error: "Not Found" }, { status: 404 });
  }
};
