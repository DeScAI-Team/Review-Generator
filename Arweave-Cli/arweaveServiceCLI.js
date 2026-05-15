import {upload, retrieve} from './arweaveService.js';
import fs from 'fs';

/**
 * Usage:
 *   node arweaveServiceCLI.js <filePath> [--out <downloadPath>] [--tag name=value ...]
 * Legacy: node arweaveServiceCLI.js <filePath> <downloadPath>  (same as --out <downloadPath>)
 */
function parseArgs(argv) {
  const tokens = argv.slice(2);
  const tags = [];
  let outPath = null;
  const positionals = [];
  for (let i = 0; i < tokens.length; i++) {
    const t = tokens[i];
    if (t === '--out' && i + 1 < tokens.length) {
      outPath = tokens[++i];
      continue;
    }
    if (t === '--tag' && i + 1 < tokens.length) {
      const raw = tokens[++i];
      const eq = raw.indexOf('=');
      if (eq > 0) {
        tags.push({ name: raw.slice(0, eq), value: raw.slice(eq + 1) });
      }
      continue;
    }
    if (!t.startsWith('-')) {
      positionals.push(t);
    }
  }
  let filePath = positionals[0] ?? null;
  if (!outPath && positionals.length >= 2) {
    outPath = positionals[1];
  }
  return { filePath, outPath, tags };
}

const { filePath, outPath: outputFile, tags } = parseArgs(process.argv);

if(!filePath){
  console.error('Error: Please provide a file path. Optional: --out <path> [--tag name=value ...]');
  process.exit(1);
}

async function runTest(){
  console.log('--- Starting Upload ---');
  const uploadInfo = await upload(filePath, { tags });
  
  if (uploadInfo.success) {
    console.log(`File is live at: ${uploadInfo.webUrl}`);
    
    if(outputFile){
      console.log('\n--- Starting Retrieval ---');
      const download = await retrieve(uploadInfo.txId);

      if (download.success && outputFile !== null){
        fs.writeFile(outputFile, Buffer.from(download.data), (err) => {
          if (err) {
            console.error('Error writing file:', err);
          } else {
            console.log('File written successfully to:', outputFile);
          }
        });
      }
    }
  } else {
    process.exit(1);
  }
}

runTest();
