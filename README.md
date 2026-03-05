<div align="center">

# SIMRP
### Sistem Informasi Manajemen Relawan Kampung Pancasila

[![React](https://img.shields.io/badge/React-18.3-61DAFB?logo=react)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?logo=typescript)](https://www.typescriptlang.org)
[![Vite](https://img.shields.io/badge/Vite-6.x-646CFF?logo=vite)](https://vitejs.dev)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.x-06B6D4?logo=tailwindcss)](https://tailwindcss.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-Python-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)](https://sqlite.org)

Aplikasi web **mobile-first** untuk manajemen relawan, event kampung, dan verifikasi laporan kegiatan  
berbasis **4 Pilar Pembangunan Kampung Pancasila** di Kota Surabaya.

**Project Owner:** Dinas Komunikasi dan Informatika (Diskominfo) Kota Surabaya  
**Version:** 1.0 MVP · **Status:** ✅ Production Ready

</div>

---

## 📋 Daftar Isi

- [Gambaran Umum](#-gambaran-umum)
- [Fitur Utama](#-fitur-utama)
- [Tech Stack](#-tech-stack)
- [Struktur Proyek](#-struktur-proyek)
- [Memulai](#-memulai)
- [Environment Variables](#-environment-variables)
- [Menjalankan Aplikasi](#-menjalankan-aplikasi)
- [Demo Accounts](#-demo-accounts)
- [Dokumentasi](#-dokumentasi)
- [Kontribusi](#-kontribusi)
- [Lisensi & Attributions](#-lisensi--attributions)

---

## 🌟 Gambaran Umum

SIMRP adalah platform digital untuk mendigitalisasi manajemen relawan kampung di Kota Surabaya.  
Sistem ini melayani tiga jenis pengguna:

| Role | Akses |
|------|-------|
| 👤 **Relawan / Warga** | Daftar, gabung event, buat laporan kegiatan, lihat poin & badge |
| 🛡️ **Moderator** | Verifikasi laporan dari relawan, approve/reject dengan kalkulasi poin otomatis |
| ⚙️ **Admin** | Kelola data relawan & event, pantau statistik program, manajemen penuh |

**Keunggulan utama:**
- 📱 **Mobile-First PWA** — didesain untuk pengguna smartphone
- 📡 **Offline-First Reporting** — laporan tersimpan sebagai draft saat tidak ada koneksi
- 🎮 **Gamification Engine** — 7 level progresif, sistem poin, badge, leaderboard
- 🗺️ **Geographic Intelligence** — validasi & auto-fill wilayah dari kode pos (31 kecamatan, 154 kelurahan Surabaya)

---

## 🎯 Fitur Utama

### ✅ Authentication & User Management
- Dual login: **Relawan** (Email/Password) & **Admin** (username/password)
- Registrasi dengan validasi kode pos Surabaya secara otomatis
- Role-Based Access Control: `user` / `ksh` / `moderator_t2` / `admin`
- Session token via custom auth (PBKDF2 password hashing)
- Rate limiting pada endpoint auth & mutasi

### ✅ Gamification Engine
- 7 Level Progression System: *Pendatang Baru → Legend Kampung*
- Sistem poin otomatis berdasarkan aktivitas & verifikasi laporan
- Badge System (expandable)
- Leaderboard antar relawan
- Temporary points & badge adjustment oleh admin

### ✅ Event Management
- Browse event kampung dengan filter **4 Pilar**:
  - 🌱 Lingkungan · 🤝 Gotong Royong · 💼 Ekonomi Kreatif · 🛡️ Keamanan
- Scope event: kelurahan / kecamatan / kota
- RSVP (gabung event), tracking status `upcoming` / `completed`
- Approval workflow oleh ASN/Admin

### ✅ Reporting Wizard (Offline-First)
- 2-step wizard: **Upload Foto → Outcome Tags**
- GPS lock saat foto diambil
- Deteksi mode offline dengan indikator WiFi icon
- Draft mode: laporan tersimpan di localStorage saat offline
- Laporan hanya bisa dibuat setelah event berstatus `completed`

### ✅ Dashboard per Role
- **User Dashboard** — Home, Event, Profile, More (bottom navigation mobile)
- **Admin Dashboard** — statistik KPI, manajemen user & event, verifikasi laporan, temporary adjustments
- **Moderator Dashboard** — antrian laporan pending, quick approve/reject

### ✅ Collaboration Request
- Form pengajuan kemitraan dari organisasi/lembaga luar
- Approval workflow oleh Moderator Tier 2 / Admin
- Scope: kelurahan / kecamatan / kota

### ✅ Geographic Data System
- Data lengkap 31 Kecamatan, 154 Kelurahan Surabaya di database SQLite
- Auto-fill kecamatan & kelurahan berdasarkan input kode pos
- REST endpoint `/kodepos/{code}` dan `/geo/options`

---

## 🛠️ Tech Stack

### Frontend

| Teknologi | Versi | Kegunaan |
|-----------|-------|----------|
| React | 18.3.1 | UI framework |
| TypeScript | 5.x | Static typing |
| Vite | 6.3.5 | Build tool & dev server |
| Tailwind CSS | 4.1.12 | Utility-first styling |
| Radix UI | various | Accessible headless UI components |
| Lucide React | 0.487.0 | Icon library |
| Recharts | 2.15.2 | Charts & data visualization |
| React Hook Form | 7.55.0 | Form state management |
| Sonner | 2.0.3 | Toast notifications |
| Vaul | 1.1.2 | Mobile drawer component |
| Motion | 12.23.24 | UI animations |
| date-fns | 3.6.0 | Date formatting & manipulation |

### Backend

| Teknologi | Versi | Kegunaan |
|-----------|-------|----------|
| Python | 3.10+ | Runtime bahasa backend |
| FastAPI | ≥0.111.0 | REST API framework |
| Uvicorn | ≥0.29.0 | ASGI server |
| Pydantic | ≥2.7.0 | Data validation & schema |
| SQLite | bawaan Python | Database lokal (file-based) |

### API Endpoints

| Prefix | Deskripsi |
|--------|-----------|
| `/auth` | Signup, login, admin-login, get me |
| `/events` | CRUD event, join, approve, complete |
| `/reports` | Buat & verifikasi laporan kegiatan |
| `/users` | Manajemen profil user |
| `/admin` | Assign role, temporary adjustments |
| `/collaboration-requests` | Form & review kemitraan |
| `/kodepos/{code}` | Lookup wilayah dari kode pos |
| `/geo/options` | Daftar semua kecamatan & kelurahan |
| `/geo/stats` | Statistik data geografis |
| `/health` | Health check endpoint |

---

## 📁 Struktur Proyek

```
diskominfointern/
│
├── 📄 index.html                    # HTML entry point (Vite)
├── 📄 vite.config.ts                # Vite configuration
├── 📄 postcss.config.mjs            # PostCSS configuration
├── 📄 package.json                  # Dependencies & npm scripts
├── 📄 .env.example                  # Environment variables template
├── 📄 .gitignore
│
├── 📁 src/                          # Frontend source code (React + TypeScript)
│   ├── main.tsx                     # Application entry point
│   ├── App.tsx                      # Root component & router
│   ├── 📁 app/                      # Page-level components & routing
│   ├── 📁 components/               # Shared reusable UI components
│   ├── 📁 features/                 # Feature modules (auth, event, report, dll)
│   ├── 📁 hooks/                    # Custom React hooks
│   ├── 📁 api/                      # HTTP client & API call handlers
│   ├── 📁 store/                    # Global state management
│   ├── 📁 data/                     # Static data (geographic, badges)
│   ├── 📁 types/                    # TypeScript type definitions
│   ├── 📁 utils/                    # Pure helper functions
│   ├── 📁 lib/                      # Third-party library wrappers
│   ├── 📁 styles/                   # Global CSS & design tokens
│   └── 📁 assets/                   # Images, icons, logos, fonts
│
├── 📁 server/                       # Backend source code (Python + FastAPI)
│   ├── main.py                      # FastAPI app entry point & middleware
│   ├── config.py                    # Konfigurasi env vars & settings
│   ├── database.py                  # SQLite connection & helpers
│   ├── requirements.txt             # Python dependencies
│   ├── 📁 routes/                   # API route handlers
│   │   ├── auth.py                  # Authentication endpoints
│   │   ├── events.py                # Event management endpoints
│   │   ├── reports.py               # Report endpoints
│   │   ├── users.py                 # User management endpoints
│   │   ├── admin.py                 # Admin-only endpoints
│   │   ├── collab.py                # Collaboration request endpoints
│   │   └── geo.py                   # Geographic data endpoints
│   ├── 📁 core/                     # Business logic & utilities
│   │   ├── auth.py                  # Auth helpers, session, hashing
│   │   ├── xp.py                    # XP/poin calculation logic
│   │   ├── security.py              # Rate limiting, headers
│   │   ├── validators.py            # Input validators
│   │   └── geo.py                   # Geographic data helpers
│   ├── 📁 models/                   # Pydantic request/response models
│   └── 📁 db/                       # Database schema & migrations
│       └── schema.py                # SQLite schema initialization
│
├── 📁 scripts/                      # Utility & automation scripts
│   ├── dev-local.mjs                # Local dev runner (frontend + API sekaligus)
│   ├── seed_supabase.mjs            # (Legacy) seed script
│   ├── import_kodepos_surabaya.mjs  # Import data kode pos Surabaya
│   ├── import_kodepos_from_geodata.mjs
│   └── loadEnv.mjs                  # Environment variable loader
│
└── 📁 docs/                         # Project documentation
    ├── 📁 guides/                   # User & developer guides
    │   ├── QUICKSTART.md            # Get running in 5 minutes
    │   ├── PETUNJUK_PENGGUNAAN.md   # User manual (Bahasa Indonesia)
    │   └── CONTRIBUTING.md          # Contribution guidelines
    ├── 📁 architecture/             # System design documents
    │   ├── GRAND_DESIGN_FINAL.md
    │   └── SITEMAP_IA_SIMRP.md
    ├── 📁 technical/                # Technical reference
    │   ├── LIBRARY_SELECTION.md     # Library decisions & rationale
    │   ├── ASSET_INVENTORY.md       # Visual asset inventory
    │   └── DEMO_ACCOUNTS.md         # Demo credentials
    ├── 📁 status/                   # Implementation status
    │   ├── SYSTEM_SUMMARY.md
    │   └── IMPLEMENTATION_STATUS.md
    ├── 📁 logbook/                  # Daily internship logbook
    │   ├── LOGBOOK_DAY15.md
    │   └── DAY15_SPRINT_BREAKDOWN_DRAFT.md
    └── 📁 legal/
        └── ATTRIBUTIONS.md
```

---

## 🚀 Memulai

### Prasyarat

Pastikan sudah terinstall:

- **Node.js** v18 atau lebih baru — [download](https://nodejs.org)
- **Python** 3.10 atau lebih baru — [download](https://python.org)
- **npm** v8+ (bundled dengan Node.js)
- **pip** (bundled dengan Python)

### Instalasi

**1. Clone repository:**
```bash
git clone https://github.com/lustresense/diskominfointern.git
cd diskominfointern
```

**2. Install dependencies frontend:**
```bash
npm install
```

**3. Install dependencies backend:**
```bash
pip install -r server/requirements.txt
```

**4. Siapkan environment variables:**
```bash
# macOS / Linux
cp .env.example .env.local

# Windows (Command Prompt)
copy .env.example .env.local
```

**5. Edit `.env.local`** sesuai konfigurasi lokal kamu (lihat seksi [Environment Variables](#-environment-variables)).

---

## 🔧 Environment Variables

Buat file `.env.local` berdasarkan `.env.example`:

| Variable | Deskripsi | Default |
|----------|-----------|---------|
| `VITE_API_BASE_URL` | Base URL backend API | `http://127.0.0.1:8000/make-server-32aa5c5c` |
| `SIMRP_ENV` | Mode environment | `development` |
| `SIMRP_DB_PATH` | Path ke file database SQLite | `./database/runtime/database.db` |
| `SIMRP_PBKDF2_ITERATIONS` | Iterasi hashing password | `210000` |
| `SIMRP_SESSION_TTL_HOURS` | Durasi sesi login (jam) | `168` (dev) / `24` (prod) |
| `SIMRP_ALLOWED_ORIGINS` | Origins yang diizinkan (production) | — |
| `SIMRP_ADMIN_LOGIN_USERNAME` | Username admin login | `admin` |
| `SIMRP_ADMIN_LOGIN_PASSWORD` | Password admin login | `admin` |
| `SIMRP_SEED_ADMIN_PASSWORD` | Password awal seed admin | `admin` |

> ⚠️ **Jangan pernah commit `.env.local`** ke repository.  
> File ini sudah terdaftar di `.gitignore`. Gunakan `.env.example` sebagai template.

---

## ▶️ Menjalankan Aplikasi

### Development (Frontend + Backend sekaligus)

```bash
npm run dev
```

Menjalankan secara bersamaan:
- 🌐 **Frontend** → `http://localhost:5173`
- ⚙️ **Backend API** → `http://127.0.0.1:8000/make-server-32aa5c5c`

### Menjalankan Secara Terpisah

```bash
# Frontend saja
npm run dev:web

# Backend API saja (FastAPI + Uvicorn)
npm run api
# atau langsung:
python -m uvicorn server.main:app --reload --host 127.0.0.1 --port 8000
```

### Build untuk Production

```bash
npm run build
```

Output build akan tersimpan di folder `dist/`.

### Verifikasi Backend

```bash
curl http://127.0.0.1:8000/make-server-32aa5c5c/health
# Expected: {"status": "ok"}
```

---

## 🔑 Demo Accounts

| Role | Username / Email | Password | Cara Login |
|------|-----------------|----------|------------|
| **Admin** | `admin` | `admin` | Halaman `/login` → tab **"Admin"** |
| **Relawan** | Daftar baru via `/register` | (bebas, min 8 karakter + kombinasi huruf-angka) | Gunakan kode pos Surabaya |
| **Moderator** | Dikonfigurasi via Admin Dashboard | — | Login sebagai user dengan role moderator |

**Contoh kode pos Surabaya yang valid:**
- `60111` → Keputih, Sukolilo (Surabaya Timur)
- `60175` → Genteng (Surabaya Pusat)
- `60243` → Wonokromo (Surabaya Selatan)

> 📄 Lihat daftar lengkap di [`docs/technical/DEMO_ACCOUNTS.md`](docs/technical/DEMO_ACCOUNTS.md)

---

## 📚 Dokumentasi

| Dokumen | Deskripsi |
|---------|-----------|
| [🚀 Quick Start Guide](docs/guides/QUICKSTART.md) | Jalankan aplikasi dalam 5 menit |
| [📖 Petunjuk Penggunaan](docs/guides/PETUNJUK_PENGGUNAAN.md) | Manual pengguna lengkap (Bahasa Indonesia) |
| [🤝 Contributing Guide](docs/guides/CONTRIBUTING.md) | Cara berkontribusi ke proyek ini |
| [🏗️ Grand Design](docs/architecture/GRAND_DESIGN_FINAL.md) | Desain arsitektur sistem secara menyeluruh |
| [🗺️ Sitemap & IA](docs/architecture/SITEMAP_IA_SIMRP.md) | Information architecture & alur navigasi |
| [📦 Library Selection](docs/technical/LIBRARY_SELECTION.md) | Keputusan teknis pemilihan library |
| [🖼️ Asset Inventory](docs/technical/ASSET_INVENTORY.md) | Inventaris & standarisasi aset visual |
| [🔑 Demo Accounts](docs/technical/DEMO_ACCOUNTS.md) | Akun demo untuk testing |
| [📊 System Summary](docs/status/SYSTEM_SUMMARY.md) | Ringkasan sistem yang sudah dibangun |
| [✅ Implementation Status](docs/status/IMPLEMENTATION_STATUS.md) | Status implementasi seluruh fitur |

---

## 🤝 Kontribusi

Proyek ini dikerjakan sebagai bagian dari program magang di **Diskominfo Kota Surabaya**.

Tertarik berkontribusi? Baca panduan lengkapnya di [`docs/guides/CONTRIBUTING.md`](docs/guides/CONTRIBUTING.md).

---

## ⚖️ Lisensi & Attributions

- Komponen UI dari [shadcn/ui](https://ui.shadcn.com/) — [MIT License](https://github.com/shadcn-ui/ui/blob/main/LICENSE.md)
- Foto dari [Unsplash](https://unsplash.com) — [Unsplash License](https://unsplash.com/license)

Lihat detail lengkap di [`docs/legal/ATTRIBUTIONS.md`](docs/legal/ATTRIBUTIONS.md).

---

<div align="center">

Dibuat dengan ❤️ untuk **Diskominfo Kota Surabaya**  
Program Magang — 2026

</div>
