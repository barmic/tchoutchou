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
    await cache.addAll(imgUrls);
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
      return await fetch(req);
    } catch (err) {
      if (req.mode === 'navigate') {
        const fallback = await caches.match('index.html');
        if (fallback) return fallback;
      }
      throw err;
    }
  })());
});
