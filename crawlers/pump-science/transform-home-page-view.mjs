import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const inPath = path.join(__dirname, "home-page-view.json");
const outPath = path.join(__dirname, "home-page-view.clean.json");

const root = JSON.parse(fs.readFileSync(inPath, "utf8"));
const tokens = root.tokens ?? [];

function interventionKeyOrder(key) {
  const m = /^intervention_(\d+)$/.exec(key ?? "");
  return m ? parseInt(m[1], 10) : 0;
}

function buildIntervention(t) {
  const arr = [...(t.interventions ?? [])].sort(
    (a, b) => interventionKeyOrder(a.key) - interventionKeyOrder(b.key),
  );
  let vals = arr
    .map((x) => String(x.value ?? "").trim())
    .filter(Boolean);
  if (vals.length === 0) {
    const a = String(t.intervention ?? "").trim();
    const b = String(t.intervention2 ?? "").trim();
    vals = [a, b].filter(Boolean);
  }
  if (vals.length <= 1) return vals[0] ?? "";
  return vals
    .map((v, i) => `compound ${i + 1}: ${v}`)
    .join("; ");
}

const slim = tokens.map((t) => ({
  id: t.id,
  mint: t.mint,
  ticker: t.ticker,
  intervention: buildIntervention(t),
}));

fs.writeFileSync(outPath, JSON.stringify(slim, null, 2), "utf8");
console.log("wrote", outPath, "rows", slim.length);
