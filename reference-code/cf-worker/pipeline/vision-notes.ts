/**
 * Vision Notes Processing Engine
 * Transcribes paper/pencil handwritten note scans & diagrams using Workers AI Vision Models.
 * Extracts key concepts, definitions, and relationships into Knowledge Graph nodes.
 */

export interface ExtractedVisionNode {
  title: string;
  topic: string;
  summary: string;
  canonical_facts: string[];
  suggested_subject: string;
}

export interface VisionExtractionResult {
  ocr_transcript: string;
  extracted_nodes: ExtractedVisionNode[];
  raw_reasoning: string;
}

export class VisionNotesEngine {
  private ai: any;

  constructor(aiBinding: any) {
    this.ai = aiBinding;
  }

  /**
   * Process a handwritten paper/pencil note image buffer or base64 string
   */
  async processHandwrittenNote(
    imageBase64: string,
    subjectContext: string = "general"
  ): Promise<VisionExtractionResult> {
    const prompt = `You are an expert academic tutor and knowledge graph architect.
Analyze this image of handwritten pencil and paper notes (Subject context: ${subjectContext}).

Tasks:
1. Provide an exact OCR transcription of all readable handwritten text, equations, and diagrams.
2. Extract distinct atomic Knowledge Graph concepts from the notes.

Format your output STRICTLY as a JSON object with this key structure:
{
  "ocr_transcript": "full text transcription...",
  "extracted_nodes": [
    {
      "title": "Concept Title",
      "topic": "Topic Category",
      "summary": "Clear, concise summary of the concept derived from notes",
      "canonical_facts": ["Fact 1", "Fact 2"],
      "suggested_subject": "${subjectContext}"
    }
  ],
  "raw_reasoning": "Brief explanation of how concepts were extracted"
}`;

    try {
      // Use Llama 3.2 11B Vision Instruct model on Workers AI
      const response = await this.ai.run("@cf/meta/llama-3.2-11b-vision-instruct", {
        image: Array.from(Buffer.from(imageBase64, "base64")),
        prompt: prompt,
        max_tokens: 1024
      });

      const responseText = response.response || JSON.stringify(response);
      
      // Parse JSON from response
      const jsonMatch = responseText.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const parsed = JSON.parse(jsonMatch[0]);
        return {
          ocr_transcript: parsed.ocr_transcript || responseText,
          extracted_nodes: parsed.extracted_nodes || [],
          raw_reasoning: parsed.raw_reasoning || "Successfully extracted."
        };
      }

      return {
        ocr_transcript: responseText,
        extracted_nodes: [],
        raw_reasoning: "Failed to parse structured JSON, raw response saved."
      };
    } catch (err: any) {
      console.error("Vision notes processing error:", err);
      throw new Error(`Vision AI extraction failed: ${err.message}`);
    }
  }
}
