# Contributing Guide

## Tujuan
Dokumen ini menjelaskan aturan kontribusi agar perubahan kode tetap konsisten dan mudah direview.

## Aturan Branch
- Gunakan branch terpisah per pekerjaan (contoh: `feat/user-report`, `fix/login-validation`, `docs/day17-readme-audit`).
- Hindari commit langsung ke branch utama.

## Standar Commit
- Gunakan pesan commit ringkas dan spesifik.
- Format yang disarankan: `type(scope): summary`.
- Contoh: `docs(logbook): add day16 and day17 entries`.

## Checklist Sebelum PR
- Pastikan aplikasi dapat dibuild: `npm run build`.
- Pastikan perubahan dokumentasi ikut diperbarui jika ada perubahan alur/fitur.
- Pastikan tidak ada file sementara/dev cache yang ikut ter-commit.

## Scope Review
- Validasi tujuan perubahan.
- Cek potensi regresi pada role user/moderator/admin.
- Cek konsistensi naming, struktur, dan dependency.
