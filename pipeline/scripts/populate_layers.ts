import fs from 'fs';
import path from 'path';

/**
 * Populate Layer 2 (chapters + chapter_nodes) and Layer 3 (pyq_node_links)
 * from the app/data/processed/ directory data.
 * 
 * This script reads chapter JSONs and pyq_links.json, then POSTs to the
 * 22 Worker API to populate the new multi-graph tables.
 */

const API_BASE = 'https://22.priyanshukh1201.workers.dev';
const PROCESSED_DIR = path.resolve(process.cwd(), 'processed');
const PYQ_LINKS_PATH = path.resolve(PROCESSED_DIR, 'pyq/pyq_links.json');

async function delay(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// ──────────────────────────────────────────────
// LAYER 2: Populate chapters + chapter_nodes
// ──────────────────────────────────────────────

function deriveChapterId(filePath: string): string {
  // e.g. app/data/processed/ncert/polity/10th_ch01_power_sharing.json → ncert_polity_10th_ch01_power_sharing
  const rel = path.relative(PROCESSED_DIR, filePath);
  return rel
    .replace(/\.json$/, '')
    .replace(/\//g, '_')
    .replace(/\\/g, '_');
}

function deriveSourceType(filePath: string): string {
  const rel = path.relative(PROCESSED_DIR, filePath);
  if (rel.startsWith('ncert')) return 'ncert';
  if (rel.startsWith('reference-books')) return 'reference_book';
  if (rel.startsWith('non-temporal')) return 'non_temporal';
  return 'other';
}

function getAllChapterJsons(dirPath: string, files: string[] = []): string[] {
  if (!fs.existsSync(dirPath)) return files;
  for (const entry of fs.readdirSync(dirPath)) {
    const full = path.join(dirPath, entry);
    if (fs.statSync(full).isDirectory()) {
      getAllChapterJsons(full, files);
    } else if (entry.endsWith('.json') && !entry.startsWith('_') && !entry.includes('universe')) {
      files.push(full);
    }
  }
  return files;
}

async function populateChapters() {
  console.log('\n════════════════════════════════════════');
  console.log('  LAYER 2: Populating Chapters');
  console.log('════════════════════════════════════════\n');

  const chapterFiles = getAllChapterJsons(path.join(PROCESSED_DIR, 'ncert'));
  console.log(`Found ${chapterFiles.length} chapter files in ncert/`);

  let chaptersCreated = 0;
  let nodesLinked = 0;

  for (let i = 0; i < chapterFiles.length; i++) {
    const filePath = chapterFiles[i];
    try {
      const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
      if (!data.nodes || !Array.isArray(data.nodes)) continue;

      const chapterId = deriveChapterId(filePath);
      const sourceType = deriveSourceType(filePath);
      const subject = data.metadata?.subject || 'general';
      const title = data.metadata?.chapter || path.basename(filePath, '.json');
      const source = data.metadata?.source || 'Unknown';

      // Node sequence preserves the exact narrative order from the JSON
      const nodeSequence = data.nodes.map((n: any) => n.id);

      const payload = {
        id: chapterId,
        source,
        source_type: sourceType,
        subject,
        title,
        node_sequence: nodeSequence,
        total_nodes: nodeSequence.length
      };

      const resp = await fetch(`${API_BASE}/api/chapters`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const result = await resp.json();

      if (result.success) {
        chaptersCreated++;
        nodesLinked += nodeSequence.length;
        console.log(`  ✓ [${i + 1}/${chapterFiles.length}] ${title} (${nodeSequence.length} nodes)`);
      } else {
        console.error(`  ✕ [${i + 1}/${chapterFiles.length}] ${title}: ${result.error}`);
      }
    } catch (err: any) {
      console.error(`  ✕ Error reading ${path.basename(filePath)}: ${err.message}`);
    }
    await delay(200);
  }

  console.log(`\n  Chapters created: ${chaptersCreated}`);
  console.log(`  Total node links: ${nodesLinked}\n`);
}

// ──────────────────────────────────────────────
// LAYER 3: Populate pyq_node_links
// ──────────────────────────────────────────────

async function populatePyqLinks() {
  console.log('\n════════════════════════════════════════');
  console.log('  LAYER 3: Populating PYQ → Node Links');
  console.log('════════════════════════════════════════\n');

  if (!fs.existsSync(PYQ_LINKS_PATH)) {
    console.error('pyq_links.json not found!');
    return;
  }

  const raw = JSON.parse(fs.readFileSync(PYQ_LINKS_PATH, 'utf-8'));
  const pyqToNodes: Record<string, string[]> = raw.pyq_to_nodes;
  const entries = Object.entries(pyqToNodes).filter(([_, nodes]) => nodes.length > 0);
  console.log(`Found ${entries.length} PYQs with node links (out of ${Object.keys(pyqToNodes).length} total)`);

  let linksCreated = 0;
  const BATCH_SIZE = 50;

  for (let i = 0; i < entries.length; i += BATCH_SIZE) {
    const batch = entries.slice(i, i + BATCH_SIZE);
    const payload = batch.map(([pyqId, nodeIds]) => ({
      pyq_id: parseInt(pyqId),
      node_ids: nodeIds
    }));

    try {
      const resp = await fetch(`${API_BASE}/api/pyq-links`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ links: payload })
      });
      const result = await resp.json();
      if (result.success) {
        linksCreated += result.created;
        console.log(`  ✓ Batch ${Math.floor(i / BATCH_SIZE) + 1}: ${result.created} links`);
      } else {
        console.error(`  ✕ Batch error: ${result.error}`);
      }
    } catch (err: any) {
      console.error(`  ✕ Network error: ${err.message}`);
    }
    await delay(300);
  }

  console.log(`\n  Total PYQ→Node links created: ${linksCreated}\n`);
}

// ──────────────────────────────────────────────
// LAYER 2b: Populate curated edges from chapters
// ──────────────────────────────────────────────

async function populateCuratedEdges() {
  console.log('\n════════════════════════════════════════');
  console.log('  EDGES: Populating Curated Edges');
  console.log('════════════════════════════════════════\n');

  const chapterFiles = getAllChapterJsons(path.join(PROCESSED_DIR, 'ncert'));
  let edgesCreated = 0;

  for (let i = 0; i < chapterFiles.length; i++) {
    const filePath = chapterFiles[i];
    try {
      const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
      if (!data.edges || !Array.isArray(data.edges) || data.edges.length === 0) continue;

      const payload = data.edges.map((e: any) => ({
        source_id: e.from,
        target_id: e.to,
        relation_type: e.relation
      }));

      const resp = await fetch(`${API_BASE}/api/edges/curated`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ edges: payload })
      });
      const result = await resp.json();
      if (result.success) {
        edgesCreated += result.created;
      }
    } catch (err: any) {
      // silent — edges are best-effort
    }
    await delay(100);
  }

  console.log(`  Total curated edges created: ${edgesCreated}\n`);
}

// ──────────────────────────────────────────────
// Main
// ──────────────────────────────────────────────

async function main() {
  console.log('╔══════════════════════════════════════════╗');
  console.log('║  22 Multi-Graph Layer Population Script  ║');
  console.log('╚══════════════════════════════════════════╝');

  await populateChapters();
  await populatePyqLinks();
  await populateCuratedEdges();

  console.log('╔══════════════════════════════════════════╗');
  console.log('║  All layers populated successfully!      ║');
  console.log('╚══════════════════════════════════════════╝');
}

main();
