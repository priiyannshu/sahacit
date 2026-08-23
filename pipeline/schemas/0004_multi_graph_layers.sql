-- Migration 0004: 4-Layered Multi-Graph Schema
-- Adds Narrative Layer (chapters), Application Layer (PYQ links + attempts),
-- and Personal State Layer (node mastery + chapter progress).

-- ============================================================
-- LAYER 2: NARRATIVE LAYER (Chapters as Ordered Paths)
-- ============================================================

-- A chapter is a pedagogical path through the Core Knowledge Layer.
-- Multiple chapters from different books can point at the SAME node.
CREATE TABLE IF NOT EXISTS chapters (
    id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    source_type TEXT NOT NULL DEFAULT 'ncert',
    subject TEXT NOT NULL,
    title TEXT NOT NULL,
    node_sequence TEXT NOT NULL,
    total_nodes INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_chapters_subject ON chapters(subject);
CREATE INDEX IF NOT EXISTS idx_chapters_source_type ON chapters(source_type);

-- Denormalized junction for fast "which chapters cover this node?" lookups.
CREATE TABLE IF NOT EXISTS chapter_nodes (
    chapter_id TEXT NOT NULL,
    node_id TEXT NOT NULL,
    seq_position INTEGER NOT NULL,
    PRIMARY KEY (chapter_id, node_id),
    FOREIGN KEY(chapter_id) REFERENCES chapters(id),
    FOREIGN KEY(node_id) REFERENCES master_nodes(id)
);

CREATE INDEX IF NOT EXISTS idx_chapter_nodes_node ON chapter_nodes(node_id);
CREATE INDEX IF NOT EXISTS idx_chapter_nodes_seq ON chapter_nodes(chapter_id, seq_position);

-- ============================================================
-- LAYER 3: APPLICATION LAYER (PYQ ↔ Node Links + Attempts)
-- ============================================================

-- Many-to-many: which concept nodes does each PYQ test?
CREATE TABLE IF NOT EXISTS pyq_node_links (
    pyq_id INTEGER NOT NULL,
    node_id TEXT NOT NULL,
    PRIMARY KEY (pyq_id, node_id),
    FOREIGN KEY(pyq_id) REFERENCES pyq_corpus(id),
    FOREIGN KEY(node_id) REFERENCES master_nodes(id)
);

CREATE INDEX IF NOT EXISTS idx_pyq_node_links_node ON pyq_node_links(node_id);

-- Every attempt on a PYQ is logged here.
CREATE TABLE IF NOT EXISTS pyq_attempts (
    id TEXT PRIMARY KEY,
    pyq_id INTEGER NOT NULL,
    chosen_option TEXT NOT NULL,
    is_correct INTEGER NOT NULL,
    time_taken_ms INTEGER,
    confidence TEXT,
    attempted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(pyq_id) REFERENCES pyq_corpus(id)
);

CREATE INDEX IF NOT EXISTS idx_pyq_attempts_pyq ON pyq_attempts(pyq_id);
CREATE INDEX IF NOT EXISTS idx_pyq_attempts_time ON pyq_attempts(attempted_at);

-- ============================================================
-- LAYER 4: PERSONAL STATE LAYER (The Heatmap)
-- ============================================================

-- Per-node cognitive state. The overlay that makes the heatmap glow.
CREATE TABLE IF NOT EXISTS node_mastery (
    node_id TEXT PRIMARY KEY,
    mastery_score REAL NOT NULL DEFAULT 0.0,
    encounter_count INTEGER NOT NULL DEFAULT 0,
    correct_count INTEGER NOT NULL DEFAULT 0,
    incorrect_count INTEGER NOT NULL DEFAULT 0,
    last_encountered_at TIMESTAMP,
    last_tested_at TIMESTAMP,
    decay_rate REAL NOT NULL DEFAULT 0.3,
    next_review_at TIMESTAMP,
    FOREIGN KEY(node_id) REFERENCES master_nodes(id)
);

CREATE INDEX IF NOT EXISTS idx_node_mastery_score ON node_mastery(mastery_score);
CREATE INDEX IF NOT EXISTS idx_node_mastery_review ON node_mastery(next_review_at);

-- Chapter-level reading progress (progressive bookmark).
CREATE TABLE IF NOT EXISTS chapter_progress (
    chapter_id TEXT PRIMARY KEY,
    last_node_position INTEGER NOT NULL DEFAULT 0,
    completed INTEGER NOT NULL DEFAULT 0,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY(chapter_id) REFERENCES chapters(id)
);
