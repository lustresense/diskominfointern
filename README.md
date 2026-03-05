<div align="center">

# SIMRP
### Sistem Informasi Manajemen Relawan Kampung Pancasila

[![React](https://img.shields.io/badge/React-18.3-61DAFB?logo=react)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?logo=typescript)](https://www.typescriptlang.org)
[![Vite](https://img.shields.io/badge/Vite-6.x-646CFF?logo=vite)](https://vitejs.dev)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.x-06B6D4?logo=tailwindcss)](https://tailwindcss.com)
[![Supabase](https://img.shields.io/badge/Supabase-Backend-3ECF8E?logo=supabase)](https://supabase.com)

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
- Dual login: **Relawan** (Email/Password via Supabase Auth) & **Admin** (username/password)
- Registrasi dengan validasi kode pos Surabaya secara otomatis
- Role-Based Access Control (Relawan / Moderator / Admin)
- Session persistence dengan localStorage

### ✅ Gamification Engine
- 7 Level Progression System: *Pendatang Baru → Legend Kampung*
- Sistem poin otomatis berdasarkan aktivitas
- Badge System (expandable)
- Leaderboard antar relawan

### ✅ Event Management
- Browse event kampung dengan filter **4 Pilar**:
  - 🌱 Lingkungan · 🤝 Gotong Royong · 💼 Ekonomi Kreatif · 🛡️ Keamanan
- RSVP (gabung event), tracking status upcoming/completed
- 8 sample events sudah di-seed

### ✅ Reporting Wizard (Offline-First)
- 2-step wizard: **Upload Foto → Outcome Tags**
- GPS lock saat foto diambil
- Deteksi mode offline dengan indikator WiFi icon
- Draft mode: laporan tersimpan di localStorage saat offline

### ✅ Dashboard per Role
- **User Dashboard** — Home, Event, Profile, More (bottom navigation mobile)
- **Admin Dashboard** — statistik KPI, manajemen user & event, verifikasi laporan
- **Moderator Dashboard** — antrian laporan pending, quick approve/reject

### ✅ Geographic Data System
- Data lengkap 31 Kecamatan, 154 Kelurahan Surabaya
- Auto-fill kecamatan & kelurahan berdasarkan input kode pos
- Real-time validation dengan visual feedback

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

| Teknologi | Kegunaan |
|-----------|----------|
| Hono | Lightweight REST API framework (Deno Edge Runtime) |
| Supabase Auth | User authentication & session management |
| Supabase KV Store | Data persistence via PostgreSQL-backed key-value store |
| Supabase Edge Functions | Serverless API hosting |

---

## 📁 Struktur Proyek

```
diskominfointern/
│
├── 📄 index.html                    # HTML entry point (Vite requirement)
├── 📄 vite.config.ts                # Vite configuration
├── 📄 postcss.config.mjs            # PostCSS configuration
├── 📄 package.json                  # Dependencies & scripts
├── 📄 .env.example                  # Environment variables template
├── 📄 .gitignore
│
├── 📁 src/                          # Frontend source code
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
│   └── ��� assets/                   # Images, icons, logos, fonts
│
├── 📁 supabase/
│   └── 📁 functions/server/         # Hono REST API (Supabase Edge Function)
│       ├── index.tsx                # API routes & business logic (18 endpoints)
│       ├── kv_store.tsx             # KV Store interface
│       └── config.toml              # Edge function config
│
├── 📁 scripts/                      # Utility & automation scripts
│   ├── dev-local.mjs                # Local dev runner (frontend + API)
│   ├── seed_supabase.mjs            # Seed initial data to Supabase
│   ├── import_kodepos_surabaya.mjs  # Import Surabaya postal code data
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
- **npm** v8 atau lebih baru (bundled dengan Node.js)

Opsional (untuk backend production):
- Akun **Supabase** — [supabase.com](https://supabase.com)

### Instalasi

**1. Clone repository:**
```bash
git clone https://github.com/lustresense/diskominfointern.git
cd diskominfointern
```

**2. Install dependencies:**
```bash
npm install
```

**3. Siapkan environment variables:**
```bash
# macOS / Linux
cp .env.example .env.local

# Windows (Command Prompt)
copy .env.example .env.local
```

**4. Edit `.env.local`** dan sesuaikan nilai variabel dengan konfigurasi proyek kamu (lihat seksi [Environment Variables](#-environment-variables)).

---

## 🔧 Environment Variables

| Variable | Deskripsi | Contoh |
|----------|-----------|--------|
| `VITE_API_BASE_URL` | Base URL backend API | `http://127.0.0.1:8000/make-server-32aa5c5c` |
| `VITE_SUPABASE_URL` | Supabase project URL | `https://xxxx.supabase.co` |
| `VITE_SUPABASE_ANON_KEY` | Supabase anonymous key | `eyJhbGci...` |

> ⚠️ **Jangan pernah commit `.env.local`** ke repository.  
> File ini sudah terdaftar di `.gitignore`. Gunakan `.env.example` sebagai template.

---

## ▶️ Menjalankan Aplikasi

### Development (Frontend + Local API sekaligus)

```bash
npm run dev
```

Menjalankan secara bersamaan:
- 🌐 **Frontend** → `http://localhost:5173`
- ⚙️ **Local API** → `http://127.0.0.1:8000/make-server-32aa5c5c`

### Menjalankan Secara Terpisah

```bash
# Frontend saja
npm run dev:web

# Backend API saja
npm run api
```

### Build untuk Production

```bash
npm run build
```

Output build akan tersimpan di folder `dist/`.

### Verifikasi Backend

```bash
curl http://127.0.0.1:8000/make-server-32aa5c5c/health
```

---

## 🔑 Demo Accounts

| Role | Username / Email | Password | Cara Login |
|------|-----------------|----------|------------|
| **Admin** | `admin` | `admin` | Halaman `/login` → tab **"Admin"** |
| **Relawan** | Daftar baru via `/register` | (bebas) | Gunakan kode pos Surabaya, contoh: `60111` |
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
