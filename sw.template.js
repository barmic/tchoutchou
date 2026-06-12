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

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.addAll(SHELL_ASSETS);
    const res = await fetch('manifest.json', { cache: 'no-cache' });
    const manifest = await res.json();
    const imgUrls = [];
    for (const [color, files] of Object.entries(manifest)) {
      for (const f of files) imgUrls.push(`${color}/${encodeURI(f)}`);
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
      return res;
    } catch (err) {
      if (req.mode === 'navigate') {
        const fallback = await caches.match('index.html');
        if (fallback) return fallback;
      }
      throw err;
    }
  })());
});
