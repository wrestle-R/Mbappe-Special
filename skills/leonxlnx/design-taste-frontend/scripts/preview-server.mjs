import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';
import { gzipSync } from 'node:zlib';

function inside(root, file) {
  const rel = path.relative(root, file);
  return rel !== '..' && !rel.startsWith('..' + path.sep) && !path.isAbsolute(rel);
}

// Let nested pages reach shared assets while keeping an inferred root within the working project.
export function previewRoot(file, explicitRoot) {
  let root = explicitRoot ? path.resolve(explicitRoot) : path.dirname(file);
  const realFile = fs.realpathSync(file);
  if (!fs.statSync(realFile).isFile()) throw new Error(`the page is not a regular file: ${file}`);
  const cwd = process.cwd();
  if (!explicitRoot && inside(cwd, file)) {
    if (!inside(fs.realpathSync(cwd), realFile)) throw new Error(`the page is outside the working project: ${file}`);
    const refs = fs.readFileSync(file, 'utf8').matchAll(/(?:(?:src|href)\s*=\s*|\bfrom\s*|\bimport\s*\(?\s*|url\(\s*)["']?((?:\.\.\/)+)/g);
    let levels = 0;
    for (const match of refs) levels = Math.max(levels, match[1].length / 3);
    for (let i = 0; i < levels && root !== cwd; i++) root = path.dirname(root);
  }
  if (!inside(root, file) || !inside(fs.realpathSync(root), realFile)) {
    throw new Error(`the page is not inside the preview root ${root}: ${file}`);
  }
  return root;
}

// Callers bind the returned server to loopback. Validate symlink targets before reading a file.
export function createPreviewServer(root, mime, { index, gzip } = {}) {
  const realRoot = fs.realpathSync(root);
  const cache = new Map();
  return http.createServer((req, res) => {
    if (!/^(127\.0\.0\.1|localhost)(:\d+)?$/i.test(req.headers.host || '')) {
      return res.writeHead(403).end();
    }
    let pathname;
    try {
      pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    } catch {
      return res.writeHead(400).end();
    }

    try {
      let file = path.join(realRoot, pathname);
      if (!inside(realRoot, file)) return res.writeHead(403).end();
      if (index === 'slash' && pathname.endsWith('/')) file = path.join(file, 'index.html');
      let realFile = fs.realpathSync(file);
      if (!inside(realRoot, realFile)) return res.writeHead(403).end();
      if (index === 'directory' && fs.statSync(realFile).isDirectory()) {
        file = path.join(file, 'index.html');
        realFile = fs.realpathSync(path.join(realFile, 'index.html'));
        if (!inside(realRoot, realFile)) return res.writeHead(403).end();
      }
      const stat = fs.statSync(realFile);
      if (!stat.isFile()) return res.writeHead(404).end();

      const ext = path.extname(file).toLowerCase();
      const headers = { 'content-type': mime[ext] || 'application/octet-stream', 'cache-control': 'no-store' };
      if (gzip?.has(ext) && /gzip/.test(req.headers['accept-encoding'] || '')) {
        if (!cache.has(realFile)) cache.set(realFile, gzipSync(fs.readFileSync(realFile), { level: 6 }));
        headers['content-encoding'] = 'gzip';
        return res.writeHead(200, headers).end(cache.get(realFile));
      }
      headers['content-length'] = stat.size;
      const stream = fs.createReadStream(realFile);
      stream.on('error', error => res.destroy(error));
      res.on('close', () => stream.destroy());
      res.writeHead(200, headers);
      stream.pipe(res);
    } catch {
      res.writeHead(404).end('not found');
    }
  });
}
