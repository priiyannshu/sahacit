import fs from 'fs';
import path from 'path';

// Phased Ingestion Target: Core NCERT Polity & Economics
const TARGET_DIRS = [
  path.resolve(process.cwd(), 'app/data/processed/ncert/polity'),
  path.resolve(process.cwd(), 'app/data/processed/ncert/economics')
];

const API_URL = 'https://22.priyanshukh1201.workers.dev/api/ingest/nodes';

async function delay(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function getJsonFilesFromDirs(dirs: string[]): string[] {
  const fileList: string[] = [];
  dirs.forEach(dir => {
    if (fs.existsSync(dir)) {
      const files = fs.readdirSync(dir);
      files.forEach(f => {
        if (f.endsWith('.json') && !f.startsWith('_')) {
          fileList.push(path.join(dir, f));
        }
      });
    }
  });
  return fileList;
}

async function startPhasedIngestion() {
  console.log("==================================================");
  console.log("Phase 1 Ingestion: Core NCERT Polity & Economics");
  console.log("Strategy: Direct Ingestion + Store Vectors First");
  console.log("==================================================\n");

  const jsonFiles = getJsonFilesFromDirs(TARGET_DIRS);
  console.log(`Found ${jsonFiles.length} chapter files in Polity & Economics.`);

  let totalNodesCount = 0;
  let successCount = 0;
  let vectorsCount = 0;

  for (let fileIndex = 0; fileIndex < jsonFiles.length; fileIndex++) {
    const filePath = jsonFiles[fileIndex];
    try {
      const rawData = fs.readFileSync(filePath, 'utf-8');
      const data = JSON.parse(rawData);

      if (!data.nodes || !Array.isArray(data.nodes)) {
        continue;
      }

      const subject = data.metadata?.subject || path.basename(path.dirname(filePath));
      const chapterTitle = data.metadata?.chapter || 'NCERT Chapter';

      console.log(`[File ${fileIndex + 1}/${jsonFiles.length}] Processing ${path.basename(filePath)} (${data.nodes.length} nodes)...`);

      // Format nodes directly from processed json
      const formattedNodes = data.nodes.map((n: any) => ({
        id: n.id,
        subject: n.subject || subject,
        topic: chapterTitle,
        title: n.label || n.title || n.id,
        summary: n.detail || n.summary || '',
        canonical_facts: n.canonical_facts || []
      }));

      totalNodesCount += formattedNodes.length;

      // Ingest in chunks of 5
      const CHUNK_SIZE = 5;
      for (let i = 0; i < formattedNodes.length; i += CHUNK_SIZE) {
        const chunk = formattedNodes.slice(i, i + CHUNK_SIZE);

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
            console.log(`  ✓ Ingested ${result.ingested} nodes (${result.vectorsCreated} vectors)`);
          } else {
            console.error(`  ✕ API Error:`, result.error);
          }
        } catch (err: any) {
          console.error(`  ✕ Network Error:`, err.message);
        }

        await delay(1200);
      }
    } catch (err: any) {
      console.error(`Error reading ${filePath}:`, err.message);
    }
  }

  console.log(`\n==================================================`);
  console.log(`Phase 1 Complete!`);
  console.log(`Total Nodes Ingested: ${successCount}/${totalNodesCount}`);
  console.log(`Total Vectors Created: ${vectorsCount}`);
  console.log(`==================================================`);
}

startPhasedIngestion();
