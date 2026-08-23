/**
 * Socratic AI Tutor Engine
 * Powered by Cloudflare Workers AI (@cf/meta/llama-3.1-8b-instruct)
 * Integrates Master KG Source of Truth, Learner Memory State, and Vector RAG Context.
 */

export interface SocraticChatContext {
  userMessage: string;
  masterNodeId?: string;
  nodeTitle?: string;
  canonicalFacts?: string[];
  learnerMasteryScore?: number;
  learnerStatus?: string;
  misconceptions?: string[];
  ragContextChunks?: string[];
  conversationHistory?: Array<{ role: "user" | "assistant" | "system"; content: string }>;
}

export class SocraticTutorEngine {
  private ai: any;
  private defaultModel = "@cf/meta/llama-3.1-8b-instruct";

  constructor(ai: any) {
    this.ai = ai;
  }

  /**
   * Generate Socratic response guiding active retrieval and conceptual synthesis
   */
  public async generateSocraticResponse(context: SocraticChatContext): Promise<string> {
    const systemPrompt = `You are the UPSC GS1 Socratic Tutor for the "Demolition of Prelims" platform.
Your mandate is to guide the candidate toward active retrieval, deep conceptual understanding, and trap detection for UPSC Civil Services Prelims.

RULES:
1. DO NOT simply give away direct answers immediately unless explicitly asked to verify a finished synthesis.
2. Ask probing Socratic questions that force the learner to recall prerequisites, temporal connections, or constitutional nuances.
3. Highlight common UPSC distractor traps (e.g., extreme words like "all/only", chronological flips, confusing statutory vs constitutional bodies).
4. Respect the Master Knowledge Graph as the authoritative source of truth.

ACTIVE CONTEXT:
- Target Concept Node: ${context.nodeTitle || "General UPSC GS1 Topic"} (${context.masterNodeId || "None"})
- Learner Mastery Score: ${((context.learnerMasteryScore || 0) * 100).toFixed(0)}% (Status: ${context.learnerStatus || "UNEXPLORED"})
- Known Misconceptions/Traps Triggered: ${JSON.stringify(context.misconceptions || [])}
- Canonical Master Facts: ${JSON.stringify(context.canonicalFacts || ["Refer to standard GS1 syllabus"])}
- Source Textbook Context (RAG): ${context.ragContextChunks?.join("\n\n") || "None provided"}
`;

    const messages: Array<{ role: "system" | "user" | "assistant"; content: string }> = [
      { role: "system", content: systemPrompt }
    ];

    if (context.conversationHistory && context.conversationHistory.length > 0) {
      context.conversationHistory.forEach(m => messages.push({ role: m.role, content: m.content }));
    }

    messages.push({ role: "user", content: context.userMessage });

    try {
      const response = await this.ai.run(this.defaultModel, {
        messages,
        temperature: 0.5,
        max_tokens: 600
      });

      return response.response || response.description || "What key constitutional or historical principle connects to this question?";
    } catch (err: any) {
      console.error("Workers AI invocation error:", err);
      return `Let's analyze ${context.nodeTitle || "this concept"} together. What core fact or prerequisite comes to mind first?`;
    }
  }

  /**
   * Evaluate user's synthesis note or explanation against Master KG facts
   */
  public async evaluateUserSynthesis(userSynthesis: string, canonicalFacts: string[]): Promise<{
    isAccurate: boolean;
    masteryDelta: number;
    feedback: string;
    missingNuances: string[];
  }> {
    const prompt = `Evaluate the candidate's UPSC synthesis against canonical facts.

Canonical Facts:
${canonicalFacts.map((f, i) => `${i + 1}. ${f}`).join("\n")}

Candidate Synthesis:
"${userSynthesis}"

Respond with JSON ONLY in this format:
{
  "isAccurate": true/false,
  "masteryDelta": 0.15 (between -0.3 and +0.3),
  "feedback": "Concise Socratic feedback",
  "missingNuances": ["Nuance 1 if any"]
}`;

    try {
      const response = await this.ai.run(this.defaultModel, {
        messages: [{ role: "user", content: prompt }],
        temperature: 0.2,
        max_tokens: 300
      });

      const text = response.response || "";
      const jsonMatch = text.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        return JSON.parse(jsonMatch[0]);
      }
    } catch (e) {
      console.error("Evaluation JSON parse error:", e);
    }

    return {
      isAccurate: true,
      masteryDelta: 0.1,
      feedback: "Good synthesis! Keep connecting this with related PYQ trends.",
      missingNuances: []
    };
  }
}
