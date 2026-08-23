-- Migration 0001: Master Subject Knowledge Graph & PYQ Corpus Schema

-- Master Knowledge Graph Nodes (Domain Source of Truth)
CREATE TABLE IF NOT EXISTS master_nodes (
    id TEXT PRIMARY KEY,
    subject TEXT NOT NULL,
    topic TEXT NOT NULL,
    subtopic TEXT,
    era TEXT,
    title TEXT NOT NULL,
    summary TEXT,
    canonical_facts TEXT, -- JSON array of core assertions
    prerequisites TEXT,   -- JSON array of parent node IDs
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Master Knowledge Graph Edges
CREATE TABLE IF NOT EXISTS master_edges (
    id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL,
    target_id TEXT NOT NULL,
    relation_type TEXT NOT NULL, -- causes, precedes, amends, contrasts_with
    FOREIGN KEY(source_id) REFERENCES master_nodes(id),
    FOREIGN KEY(target_id) REFERENCES master_nodes(id)
);

-- Structured PYQ Corpus (2,839 official questions)
CREATE TABLE IF NOT EXISTS pyq_corpus (
    id INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    subject TEXT NOT NULL,
    topic TEXT NOT NULL,
    question_text TEXT NOT NULL,
    options TEXT NOT NULL,         -- JSON object {a, b, c, d}
    correct_option TEXT,
    explanation TEXT,
    linked_nodes TEXT              -- JSON array of master node IDs
);

-- Reference Text Chunks (for RAG context expansion)
CREATE TABLE IF NOT EXISTS reference_chunks (
    id TEXT PRIMARY KEY,
    source_book TEXT NOT NULL,
    chapter TEXT,
    section TEXT,
    content TEXT NOT NULL,
    vector_id TEXT
);

-- Performance Indexes
CREATE INDEX IF NOT EXISTS idx_master_nodes_subject ON master_nodes(subject);
CREATE INDEX IF NOT EXISTS idx_master_nodes_topic ON master_nodes(topic);
CREATE INDEX IF NOT EXISTS idx_master_nodes_era ON master_nodes(era);
CREATE INDEX IF NOT EXISTS idx_pyq_subject ON pyq_corpus(subject);
CREATE INDEX IF NOT EXISTS idx_pyq_year ON pyq_corpus(year);
