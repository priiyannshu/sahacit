# Demolition of Prelims — game layer

Five-player UPSC Prelims PYQ arena. Built on top of the curated 2,839-question corpus.

## Stack (Phase 1)

- **server/sync.py** — stdlib HTTP server, SQLite append-only tables.
- **static/** — PWA shell: `index.html`, `app.js` (IndexedDB + sync loop), `sw.js` (cache-first service worker), `manifest.webmanifest`.
- **Caddyfile** — serves `demolition-of-prelims.local`, reverse-proxies `/sync` + `/bootstrap` to the sync server.
- **launch.sh** — starts both; falls back to `python -m http.server` if Caddy is absent.

## Run locally

```
./launch.sh
```

Then open `http://localhost:8080/` (or `http://demolition-of-prelims.local/` once mDNS is configured).

## mDNS (so friends can visit `http://demolition-of-prelims.local/`)

```
sudo apt install avahi-daemon avahi-utils caddy
sudo systemctl enable --now avahi-daemon
avahi-publish -a -R demolition-of-prelims.local "$(hostname -I | awk '{print $1}')" &
```

Friends on Linux/Mac resolve `.local` natively. Windows friends need Bonjour installed or use the laptop's LAN IP.

## Users

`server/data/users.json` seeds on first boot with 5 placeholder rows. Edit display names before launch.

## Phase 2 scope (not yet built)

- Port the existing `eras/_pyq_interface/pyq_interface.html` UI under `/static/index.html` so friends can browse + mark-studied.
- Test flow: draw claimed-pool, render MCQs, record `test_attempts`, compute points = accuracy × √pool_size (derivation keeps max per area).
- Throne + leaderboard views (on-the-fly computation over the log; daily rotation at 00:00 IST).
- Era-badge detection (all-correct-in-one-sitting per era).

## Migration to Pi (later)

Hostname is stable (`demolition-of-prelims.local`) so friends' browsers transition transparently:
1. Install Caddy + avahi on Pi. Copy this `game/` dir.
2. Stop laptop's `launch.sh`; rsync `server/data/game.db` to Pi.
3. Start `launch.sh` on Pi. Done.
