import fs from 'fs';
import path from 'path';

/**
 * Gemini Subagent Ingestion Script
 * Ingests all chapter nodes from app/data/processed/ using the high-speed /api/ingest/batch-raw
 * endpoint (zero inline Cloudflare AI calls = ZERO rate limits).
 */

const API_BASE = 'https://22.priyanshukh1201.workers.dev';
const PROCESSED_DIR = path.resolve(process.cwd(), 'processed');

async function delay(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getAllJsonFiles(dirPath: string, files: string[] = []): string[] {
  if (!fs.existsSync(dirPath)) return files;
  for (const entry of fs.readdirSync(dirPath)) {
    const full = path.join(dirPath, entry);
    if (fs.statSync(full).isDirectory()) {
      getAllJsonFiles(full, files);
    } else if (entry.endsWith('.json') && !entry.startsWith('_') && !entry.includes('universe')) {
      files.push(full);
    }
  }
  return files;
}

async function fetchWithRetry(url: string, options: any, retries = 3): Promise<any> {
  for (let i = 0; i < retries; i++) {
    try {
      const resp = await fetch(url, options);
      if (resp.ok) return await resp.json();
      if (resp.status === 429) {
        console.warn(` Rate limit hit (429), backing off for ${2000 * (i + 1)}ms...`);
        await delay(2000 * (i + 1));
        continue;
      }
      throw new Error(`HTTP ${resp.status}`);
    } catch (err: any) {
      if (i === retries - 1) throw err;
      await delay(1000 * (i + 1));
    }
  }
}

async function startSubagentIngestion() {
  console.log('╔═══════════════════════════════════════════════════╗');
  console.log('║  22 Gemini Subagent High-Speed Ingestor           ║');
  console.log('║  Zero-Rate-Limit Batch Architecture              ║');
  console.log('╚═══════════════════════════════════════════════════╝\n');

  const jsonFiles = getAllJsonFiles(PROCESSED_DIR);
  console.log(`Found ${jsonFiles.length} chapter files across all subjects.\n`);

  // Step 1: Collect ALL nodes across all chapter files
  let allNodes: any[] = [];
  let fileCount = 0;

  for (const filePath of jsonFiles) {
    try {
      const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
      if (!data.nodes || !Array.isArray(data.nodes)) continue;

      const subject = data.metadata?.subject || path.basename(path.dirname(filePath));
      const chapterTitle = data.metadata?.chapter || path.basename(filePath, '.json');

      const formatted = data.nodes.map((n: any) => ({
        id: n.id,
        subject: n.subject || subject,
        topic: chapterTitle,
        title: n.label || n.title || n.id,
        summary: n.detail || n.summary || '',
        canonical_facts: n.canonical_facts || []
      }));

      allNodes.push(...formatted);
      fileCount++;
    } catch { /* skip broken files */ }
  }

  // Deduplicate nodes by ID
  const nodeMap = new Map<string, any>();
  for (const n of allNodes) {
    nodeMap.set(n.id, n);
  }
  const uniqueNodes = Array.from(nodeMap.values());

  console.log(`Collected ${uniqueNodes.length} unique concept nodes from ${fileCount} files.`);
  console.log(`Ingesting nodes into D1 Master KG via /api/ingest/batch-raw...\n`);

  // Ingest in batches of 50 nodes directly into D1
  const BATCH_SIZE = 50;
  let nodesIngested = 0;

  for (let i = 0; i < uniqueNodes.length; i += BATCH_SIZE) {
    const batch = uniqueNodes.slice(i, i + BATCH_SIZE);
    try {
      const result = await fetchWithRetry(`${API_BASE}/api/ingest/batch-raw`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nodes: batch })
      });
      if (result.success) {
        nodesIngested += result.ingested;
        process.stdout.write(`  ✓ Ingested nodes ${nodesIngested}/${uniqueNodes.length}\r`);
      }
    } catch (err: any) {
      console.error(`\n  ✕ Batch error at offset ${i}: ${err.message}`);
    }
    await delay(300);
  }

  console.log(`\n\n✅ STEP 1 COMPLETE: ${nodesIngested}/${uniqueNodes.length} nodes stored in Master KG D1!\n`);

  // Step 2: Populate Chapters (Narrative Layer)
  console.log('═══════════════════════════════════════════════════');
  console.log('  STEP 2: Populating Narrative Chapters');
  console.log('═══════════════════════════════════════════════════\n');

  let chaptersCreated = 0;
  for (let i = 0; i < jsonFiles.length; i++) {
    const filePath = jsonFiles[i];
    try {
      const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
      if (!data.nodes || !Array.isArray(data.nodes)) continue;

      const rel = path.relative(PROCESSED_DIR, filePath);
      const chapterId = rel.replace(/\.json$/, '').replace(/[\/\\]/g, '_');
      const sourceType = rel.startsWith('ncert') ? 'ncert' : 'reference_book';
      const subject = data.metadata?.subject || 'general';
      const title = data.metadata?.chapter || path.basename(filePath, '.json');
      const source = data.metadata?.source || 'NCERT';
      const nodeSequence = data.nodes.map((n: any) => n.id);

      const result = await fetchWithRetry(`${API_BASE}/api/chapters`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          id: chapterId,
          source,
          source_type: sourceType,
          subject,
          title,
          node_sequence: nodeSequence,
          total_nodes: nodeSequence.length
        })
      });

      if (result.success) chaptersCreated++;
    } catch { /* skip */ }
    await delay(100);
  }
  console.log(`✅ STEP 2 COMPLETE: ${chaptersCreated} chapters created!\n`);

  // Step 3: Populate PYQ Links (Application Layer)
  console.log('═══════════════════════════════════════════════════');
  console.log('  STEP 3: Populating PYQ → Node Links');
  console.log('═══════════════════════════════════════════════════\n');

  const PYQ_LINKS_PATH = path.resolve(PROCESSED_DIR, 'pyq/pyq_links.json');
  if (fs.existsSync(PYQ_LINKS_PATH)) {
    const raw = JSON.parse(fs.readFileSync(PYQ_LINKS_PATH, 'utf-8'));
    const pyqToNodes: Record<string, string[]> = raw.pyq_to_nodes;
    const entries = Object.entries(pyqToNodes).filter(([_, nodes]) => nodes.length > 0);

    let linksCreated = 0;
    const LINK_BATCH_SIZE = 50;

    for (let i = 0; i < entries.length; i += LINK_BATCH_SIZE) {
      const batch = entries.slice(i, i + LINK_BATCH_SIZE);
      const payload = batch.map(([pyqId, nodeIds]) => ({
        pyq_id: parseInt(pyqId),
        node_ids: nodeIds
      }));

      try {
        const result = await fetchWithRetry(`${API_BASE}/api/pyq-links`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ links: payload })
        });
        if (result.success) linksCreated += result.created;
      } catch { /* skip */ }
      await delay(200);
    }
    console.log(`✅ STEP 3 COMPLETE: ${linksCreated} PYQ links created!\n`);
  }

  console.log('╔═══════════════════════════════════════════════════╗');
  console.log('║  SUCCESS! Full Knowledge Infrastructure Hydrated  ║');
  console.log('╚═══════════════════════════════════════════════════╝');
}

startSubagentIngestion();
