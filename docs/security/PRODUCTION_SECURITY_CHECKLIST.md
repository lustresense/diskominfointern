# Security Checklist (Production)

Dokumen ini dipakai saat SIMRP/SIMREKAP dipublish ke server resmi.

## 1) Wajib set environment variable
- `SIMRP_ENV=production`
- `SIMRP_ALLOWED_ORIGINS=https://domain-frontend-kamu`
- `SIMRP_ADMIN_LOGIN_USERNAME=<username-admin-non-default>`
- `SIMRP_ADMIN_LOGIN_PASSWORD=<password-admin-kuat>`
- `SIMRP_SEED_ADMIN_PASSWORD=<password-seed-kuat>`

## 2) Rekomendasi hardening parameter
- `SIMRP_PBKDF2_ITERATIONS=210000` (atau lebih tinggi sesuai kapasitas server)
- `SIMRP_RATE_LIMIT_WINDOW_SECONDS=60`
- `SIMRP_RATE_LIMIT_AUTH_MAX=10`
- `SIMRP_RATE_LIMIT_MUTATION_MAX=120`
- `SIMRP_SESSION_TTL_HOURS=24`

## 3) Wajib di level infrastruktur
- Pakai HTTPS (TLS) end-to-end.
- Taruh API di belakang reverse proxy (Nginx/Caddy) + firewall.
- Buka port seperlunya (jangan expose DB ke publik).
- Aktifkan backup database terjadwal dan uji restore berkala.
- Simpan secret di secret manager/CI variable, bukan di repo.

## 4) Operasional keamanan
- Rotasi password admin berkala.
- Audit log login gagal dan lonjakan request `429`.
- Nonaktifkan akun demo di environment production.
- Lakukan dependency update rutin (frontend + backend).

## 5) Catatan penting
Tidak ada aplikasi yang bisa dijamin 100% anti-serangan. Target realistis adalah memperkecil attack surface, memperkuat kontrol akses, dan mempercepat deteksi-respons insiden.
