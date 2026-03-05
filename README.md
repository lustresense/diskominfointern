# SIMRP (Sistem Informasi Manajemen Relawan & Program)

SIMRP adalah aplikasi web untuk manajemen relawan, event kampung, kolaborasi mitra, dan verifikasi laporan berbasis wilayah Surabaya.

## Tech Stack

- Frontend: React + TypeScript + Vite + Tailwind
- Backend: FastAPI (Python)
- Database: SQLite

## Struktur Utama

- `server/`: backend FastAPI modular (`core`, `db`, `models`, `routes`)
- `src/`: frontend React
- `docs/`: dokumentasi project
- `database/backups/`: backup database

## Prasyarat

- Node.js 18+
- Python 3.10+

## Setup Lokal

1. Install dependency frontend:
   `npm install`
2. Install dependency backend:
   `python -m pip install -r server/requirements.txt`
3. Salin env template:
   `copy .env.example .env.local` (Windows) atau `cp .env.example .env.local` (Unix)
4. Pastikan `VITE_API_BASE_URL` di `.env.local` mengarah ke:
   `http://127.0.0.1:8000/make-server-32aa5c5c`

## Menjalankan Aplikasi

1. Jalankan backend API:
   `npm run api`
2. Jalankan frontend:
   `npm run dev:web`
3. Atau jalankan keduanya bersamaan:
   `npm run dev`

## Health Check

- Endpoint health:
  `http://127.0.0.1:8000/make-server-32aa5c5c/health`

## Demo Accounts

- Lihat file: `DEMO_ACCOUNTS.md`

## Build Frontend

- `npm run build`

## Catatan Git

- `.env.local` dipakai untuk local demo/dev dan **tetap ada di lokal**.
- `.env.local` tidak boleh di-track Git.
- Template env yang di-push ke repo adalah `.env.example`.
