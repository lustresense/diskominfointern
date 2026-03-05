# Asset Inventory SIMRP

Tanggal inventarisasi: 2026-02-16
Penanggung jawab: Tim frontend SIMRP

## Tujuan
Dokumen ini mencatat aset visual yang sudah tersedia, aset yang belum tersedia, dan standardisasi penempatan aset untuk implementasi UI yang konsisten.

## Ringkasan Temuan
- Aset gambar statis (`.png/.jpg/.svg/.webp`) belum ditemukan di repository.
- Icon UI menggunakan library `lucide-react` pada komponen dashboard dan UI primitives.
- Ikon gamifikasi tambahan menggunakan unicode emoji pada data badge.
- Tipografi utama menggunakan `Inter` dari Google Fonts.
- Aset logo resmi instansi belum terintegrasi di source code.

## Standardisasi Struktur Aset
Direktori berikut ditetapkan sebagai struktur baku:

- `src/assets/icons/` untuk ikon custom (SVG/PNG)
- `src/assets/images/` untuk gambar konten dan ilustrasi
- `src/assets/logos/` untuk logo brand/proyek/instansi
- `src/assets/fonts/` untuk file font lokal (jika migrasi dari CDN)

## Detail Inventaris
| Kategori | Sumber | Lokasi Saat Ini | Status | Catatan |
|---|---|---|---|---|
| Ikon UI utama | `lucide-react` | `src/app/components/**` | Tersedia | Dipakai lintas dashboard dan komponen UI |
| Ikon tambahan | Unicode emoji | `src/data/validatedBadges.ts` | Tersedia | Badge gamifikasi |
| Tipografi | Google Fonts `Inter` | `src/styles/fonts.css` | Tersedia | Import CDN aktif |
| Logo aplikasi | File aset logo | Belum ada | Perlu ditambahkan | Siapkan versi SVG + PNG |
| Gambar konten | File aset gambar | Belum ada | Perlu ditambahkan | Untuk hero/empty state/dokumentasi |

## Konvensi Penamaan
- Gunakan format `kebab-case` untuk semua file.
- Ikon: `icon-{nama-fungsi}.svg` (contoh: `icon-report.svg`).
- Logo: `logo-{entitas}-{varian}.svg` (contoh: `logo-simrp-primary.svg`).
- Gambar: `img-{konteks}-{indeks}.png` (contoh: `img-landing-01.png`).

## Tindak Lanjut
- Tambahkan logo resmi ke `src/assets/logos/`.
- Tambahkan aset visual pendukung halaman publik ke `src/assets/images/`.
- Evaluasi migrasi font dari CDN ke local font jika dibutuhkan untuk mode offline penuh.
