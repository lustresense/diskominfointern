# Library Selection SIMRP

Tanggal seleksi: 2026-02-16
Ruang lingkup: frontend web (React + Vite)

## Tujuan
Dokumen ini menetapkan pustaka utama yang digunakan agar implementasi UI, state, dan tooling tetap konsisten selama pengembangan.

## Library Utama yang Dipakai
| Kategori | Library | Versi | Status | Alasan Teknis |
|---|---|---:|---|---|
| Framework UI | `react` + `react-dom` | 18.3.1 | Dipakai | Fondasi komponen dan rendering aplikasi |
| Build tool | `vite` | 6.3.5 | Dipakai | Dev server cepat dan build ringan |
| Styling | `tailwindcss` + `@tailwindcss/vite` | 4.1.12 | Dipakai | Utility-first styling dengan integrasi Vite |
| Utility class | `clsx`, `tailwind-merge`, `class-variance-authority` | 2.1.1 / 3.2.0 / 0.7.1 | Dipakai | Komposisi class name yang rapi dan konsisten |
| Headless UI | `@radix-ui/*` | bervariasi | Dipakai | Komponen aksesibel untuk dialog, select, tabs, dll |
| Icon | `lucide-react` | 0.487.0 | Dipakai | Katalog ikon konsisten untuk dashboard dan nav |
| Notifikasi | `sonner` | 2.0.3 | Dipakai | Toast feedback untuk aksi user/admin |
| Form | `react-hook-form` | 7.55.0 | Dipakai | Manajemen form yang ringan dan terstruktur |
| Visualisasi data | `recharts` | 2.15.2 | Dipakai | Grafik KPI dan ringkasan performa |
| Motion | `motion` | 12.23.24 | Dipakai terbatas | Animasi transisi elemen UI |
| Drawer mobile | `vaul` | 1.1.2 | Dipakai | Pengalaman drawer yang responsif |
| Date utility | `date-fns` | 3.6.0 | Dipakai terbatas | Format/manipulasi tanggal |

## Library Tersedia tapi Belum Jadi Prioritas Aktif
| Library | Versi | Status | Catatan |
|---|---:|---|---|
| `@mui/material`, `@mui/icons-material`, `@emotion/*` | 7.3.5 / 11.x | Cadangan | Belum jadi jalur utama karena stack UI saat ini berbasis Radix + Tailwind |
| `react-dnd`, `react-dnd-html5-backend` | 16.0.1 | Cadangan | Digunakan jika fitur drag-and-drop dibutuhkan |
| `react-slick`, `react-responsive-masonry`, `embla-carousel-react` | 0.31.0 / 2.7.1 / 8.6.0 | Cadangan | Dipakai jika ada kebutuhan layout/carousel khusus |

## Keputusan Teknis
- Jalur komponen utama: Radix primitives + utility styling Tailwind.
- Jalur ikon utama: `lucide-react`; hindari campur ikon dari banyak library dalam satu layar.
- Jalur notifikasi: standarkan ke `sonner`.
- Jalur chart: standarkan ke `recharts` untuk dashboard.

## Tindak Lanjut
- Audit dependency triwulan untuk mengurangi paket cadangan yang tidak dipakai.
- Tetapkan pedoman pemakaian per-library di dokumentasi frontend coding standards.
