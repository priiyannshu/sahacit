-- Migration 0003: Multimodal Architecture, Vision Notes & Cross-Subject Semantic Edges

-- Multimodal Media Assets linked to Master Nodes (Images, Audio, Visuals)
CREATE TABLE IF NOT EXISTS node_media (
    id TEXT PRIMARY KEY,
    node_id TEXT NOT NULL,
    media_type TEXT NOT NULL, -- 'image', 'audio', 'handwritten_note'
    r2_url TEXT NOT NULL,
    caption TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(node_id) REFERENCES master_nodes(id)
);

-- Raw Handwritten Pencil & Paper Notes Processing Queue
CREATE TABLE IF NOT EXISTS handwritten_notes (
    id TEXT PRIMARY KEY,
    subject TEXT NOT NULL,
    r2_url TEXT NOT NULL,
    ocr_transcript TEXT,
    extracted_concepts_json TEXT, -- Extracted nodes/edges payload
    status TEXT NOT NULL DEFAULT 'PENDING', -- 'PENDING', 'PROCESSED', 'SEMANTIZED'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cross-Subject Semantic Connections with Reasoning
CREATE TABLE IF NOT EXISTS semantic_edges (
    source_node_id TEXT NOT NULL,
    target_node_id TEXT NOT NULL,
    source_subject TEXT NOT NULL,
    target_subject TEXT NOT NULL,
    similarity_score REAL NOT NULL,
    reasoning TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (source_node_id, target_node_id),
    FOREIGN KEY(source_node_id) REFERENCES master_nodes(id),
    FOREIGN KEY(target_node_id) REFERENCES master_nodes(id)
);

CREATE INDEX IF NOT EXISTS idx_node_media_node ON node_media(node_id);
CREATE INDEX IF NOT EXISTS idx_handwritten_subject ON handwritten_notes(subject);
CREATE INDEX IF NOT EXISTS idx_semantic_source_subject ON semantic_edges(source_subject);
CREATE INDEX IF NOT EXISTS idx_semantic_target_subject ON semantic_edges(target_subject);
