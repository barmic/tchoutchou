'use strict';

const CACHE_VERSION = '__CACHE_VERSION__';
const CACHE_NAME = `tchoutchou-${CACHE_VERSION}`;

const SHELL_ASSETS = [
  './',
  'index.html',
  'manifest.webmanifest',
  'manifest.json',
  'train192.png',
  'train512.png',
];

// Precache only the format the page will request: AVIF when the browser can
// decode it, PNG otherwise. Detection decodes a real AVIF file.
async function supportsAvif() {
  try {
    const res = await fetch('train192.avif');
    if (!res.ok) return false;
    const bitmap = await createImageBitmap(await res.blob());
    bitmap.close();
    return true;
  } catch {
    return false;
  }
}

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.addAll(SHELL_ASSETS);
    const res = await fetch('manifest.json', { cache: 'no-cache' });
    const manifest = await res.json();
    const avif = await supportsAvif();
    const imgUrls = [];
    for (const [color, files] of Object.entries(manifest)) {
      for (const f of files) {
        const name = avif ? f.replace(/\.png$/i, '.avif') : f;
        imgUrls.push(`${color}/${encodeURI(name)}`);
      }
    }
    // Précache tolérant : une image qui échoue (404, coupure cellulaire) ne doit
    // pas rejeter tout l'install, sinon le SW ne s'active jamais. Les trous sont
    // rattrapés par le backfill du handler fetch à la prochaine consultation en ligne.
    await Promise.allSettled(imgUrls.map((u) => cache.add(u)));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(
      keys
        .filter((k) => k.startsWith('tchoutchou-') && k !== CACHE_NAME)
        .map((k) => caches.delete(k))
    );
    await self.clients.claim();
  })());
});

function isAvif(url) {
  return url.pathname.toLowerCase().endsWith('.avif');
}

// An AVIF missing offline (e.g. PNG precached after a failed detection) is
// served from its cached PNG sibling.
function pngFallback(url) {
  return caches.match(url.pathname.replace(/\.avif$/i, '.png'));
}

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  event.respondWith((async () => {
    const cached = await caches.match(req);
    if (cached) return cached;
    try {
      const res = await fetch(req);
      // Backfill : remettre en cache ce qui n'avait pas été précaché (images
      // manquées par le précache tolérant) pour que ce soit dispo offline ensuite.
      if (res && res.ok) {
        const cache = await caches.open(CACHE_NAME);
        cache.put(req, res.clone());
      }
      if (res && !res.ok && isAvif(url)) {
        const png = await pngFallback(url);
        if (png) return png;
      }
      return res;
    } catch (err) {
      if (isAvif(url)) {
        const png = await pngFallback(url);
        if (png) return png;
      }
      if (req.mode === 'navigate') {
        const fallback = await caches.match('index.html');
        if (fallback) return fallback;
      }
      throw err;
    }
  })());
});
