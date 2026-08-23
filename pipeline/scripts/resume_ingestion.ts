import fs from 'fs';
import path from 'path';

// Resume Phase 1 ingestion from file 93 onwards (where network errors started)
const TARGET_DIRS = [
  path.resolve(process.cwd(), 'app/data/processed/ncert/polity'),
  path.resolve(process.cwd(), 'app/data/processed/ncert/economics')
];

const API_URL = 'https://22.priyanshukh1201.workers.dev/api/ingest/nodes';
const SKIP_FILES = 93; // Already completed ~93 files before errors

async function delay(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getJsonFilesFromDirs(dirs: string[]): string[] {
  const fileList: string[] = [];
  dirs.forEach(dir => {
    if (fs.existsSync(dir)) {
      const files = fs.readdirSync(dir);
      files.forEach(f => {
        if (f.endsWith('.json') && !f.startsWith('_') && !f.includes('universe')) {
          fileList.push(path.join(dir, f));
        }
      });
    }
  });
  return fileList;
}

async function resumeIngestion() {
  console.log("═══════════════════════════════════════════");
  console.log("  Resuming Phase 1: Polity & Economics");
  console.log("  Skipping first", SKIP_FILES, "files (already done)");
  console.log("  Longer delays to avoid rate limits");
  console.log("═══════════════════════════════════════════\n");

  const jsonFiles = getJsonFilesFromDirs(TARGET_DIRS);
  const remaining = jsonFiles.slice(SKIP_FILES);
  console.log(`Total files: ${jsonFiles.length}, Remaining: ${remaining.length}`);

  let successCount = 0;
  let vectorsCount = 0;

  for (let i = 0; i < remaining.length; i++) {
    const filePath = remaining[i];
    try {
      const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
      if (!data.nodes || !Array.isArray(data.nodes)) continue;

      const subject = data.metadata?.subject || 'general';
      const chapterTitle = data.metadata?.chapter || 'NCERT Chapter';

      console.log(`[${i + 1}/${remaining.length}] ${path.basename(filePath)} (${data.nodes.length} nodes)...`);

      const formattedNodes = data.nodes.map((n: any) => ({
        id: n.id,
        subject: n.subject || subject,
        topic: chapterTitle,
        title: n.label || n.title || n.id,
        summary: n.detail || n.summary || '',
        canonical_facts: n.canonical_facts || []
      }));

      // Smaller chunks of 3 with longer delays
      const CHUNK_SIZE = 3;
      for (let j = 0; j < formattedNodes.length; j += CHUNK_SIZE) {
        const chunk = formattedNodes.slice(j, j + CHUNK_SIZE);
        try {
          const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nodes: chunk })
          });
          const result = await response.json();
          if (result.success) {
            successCount += result.ingested;
            vectorsCount += result.vectorsCreated;
            process.stdout.write(`  ✓ ${result.ingested}/${result.vectorsCreated} `);
          } else {
            process.stdout.write(`  ✕ `);
          }
        } catch (err: any) {
          process.stdout.write(`  ✕net `);
        }
        await delay(2000);
      }
      console.log('');
    } catch (err: any) {
      console.error(`  Error: ${err.message}`);
    }
  }

  console.log(`\n═══════════════════════════════════════════`);
  console.log(`  Resume Complete: ${successCount} nodes, ${vectorsCount} vectors`);
  console.log(`═══════════════════════════════════════════`);

  // Now resume PYQ links
  console.log(`\n═══════════════════════════════════════════`);
  console.log(`  Resuming PYQ → Node Links (batch 9+)`);
  console.log(`═══════════════════════════════════════════\n`);

  const PYQ_LINKS_PATH = path.resolve(process.cwd(), 'app/data/processed/pyq/pyq_links.json');
  const raw = JSON.parse(fs.readFileSync(PYQ_LINKS_PATH, 'utf-8'));
  const pyqToNodes: Record<string, string[]> = raw.pyq_to_nodes;
  const entries = Object.entries(pyqToNodes).filter(([_, nodes]) => nodes.length > 0);

  // Skip first 400 entries (8 batches of 50 already done)
  const SKIP_ENTRIES = 400;
  const remainingEntries = entries.slice(SKIP_ENTRIES);
  console.log(`Remaining PYQ entries: ${remainingEntries.length}`);

  const BATCH_SIZE = 25; // Smaller batches
  let linksCreated = 0;

  for (let i = 0; i < remainingEntries.length; i += BATCH_SIZE) {
    const batch = remainingEntries.slice(i, i + BATCH_SIZE);
    const payload = batch.map(([pyqId, nodeIds]) => ({
      pyq_id: parseInt(pyqId),
      node_ids: nodeIds
    }));

    try {
      const resp = await fetch('https://22.priyanshukh1201.workers.dev/api/pyq-links', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ links: payload })
      });
      const result = await resp.json();
      if (result.success) {
        linksCreated += result.created;
        console.log(`  ✓ Batch ${Math.floor(i / BATCH_SIZE) + 1}: ${result.created} links`);
      } else {
        console.error(`  ✕ ${result.error}`);
      }
    } catch (err: any) {
      console.error(`  ✕ Network: ${err.message}`);
    }
    await delay(1500);
  }

  console.log(`\n  Total new PYQ→Node links: ${linksCreated}`);
  console.log(`\n═══ ALL DONE ═══`);
}

resumeIngestion();
