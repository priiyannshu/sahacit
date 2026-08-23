import * as fs from "fs";
import * as path from "path";

/**
 * Seed Master D1 Database from processed PYQs and History Eras
 */
async function generateSeedingSql() {
  const pyqPath = path.join(process.cwd(), "processed", "pyq", "upsc_prelims_pyq.json");
  const sqlOutPath = path.join(process.cwd(), "migrations", "0002_seed_data.sql");

  console.log("Reading PYQ corpus...");
  if (!fs.existsSync(pyqPath)) {
    console.error("PYQ corpus file not found:", pyqPath);
    process.exit(1);
  }

  const rawData = fs.readFileSync(pyqPath, "utf-8");
  const pyqData = JSON.parse(rawData);
  const questions = pyqData.questions || [];

  console.log(`Found ${questions.length} PYQs. Generating SQL statements...`);

  const sqlStatements = ["-- Migration 0002: Seed PYQ Master Corpus\n"];

  questions.forEach((q, idx) => {
    const id = idx + 1;
    const year = q.year || 2025;
    const subject = String(q.subject || "General").replace(/'/g, "''");
    const topic = String(q.topic || "General").replace(/'/g, "''");
    const questionText = String(q.question || "").replace(/'/g, "''");
    const optionsJson = JSON.stringify(q.options || {}).replace(/'/g, "''");
    const correctOpt = String(q.answer || q.correct_option || "").replace(/'/g, "''");
    const explanation = String(q.explanation || "").replace(/'/g, "''");

    sqlStatements.push(
      `INSERT OR REPLACE INTO pyq_corpus (id, year, subject, topic, question_text, options, correct_option, explanation) VALUES (${id}, ${year}, '${subject}', '${topic}', '${questionText}', '${optionsJson}', '${correctOpt}', '${explanation}');`
    );
  });

  fs.writeFileSync(sqlOutPath, sqlStatements.join("\n"));
  console.log(`Successfully generated ${sqlOutPath} with ${questions.length} seed queries.`);
}

generateSeedingSql().catch(console.error);
