# Demo Accounts SIMRP

## Catatan Login
- Semua akun non-admin login dari halaman `/login` (email + password).
- Admin login dari halaman `/admin` (username + password), bukan email.

## Kredensial Demo
| Role | Tier/Mode | Nama | Username/Email | Password | Tujuan Demo |
|---|---|---|---|---|---|
| Admin | Super Admin | Administrator | `admin` (halaman `/admin`) | `admin` | Login admin, switch view, monitoring global |
| Moderator | Tier 1 (ASN) | Pak Raka ASN | `moderator1.demo@simrp.app` | `password123` | Buat draft kegiatan |
| Moderator | Tier 2 (Lurah) | Bu Sinta Lurah | `moderator2.demo@simrp.app` | `password123` | Approve draft skala kelurahan, verifikasi laporan |
| Moderator | Tier 2 (Camat) | Pak Dimas Camat | `moderator2.camat@simrp.app` | `password123` | Approve draft skala kecamatan |
| Moderator | Tier 3 | Pak Arif | `moderator3.demo@simrp.app` | `password123` | Monitoring agregat/insight |
| User | Relawan | Andi Relawan | `relawan.demo@simrp.app` | `password123` | Join event, submit laporan |
| User | Relawan | Nia Relawan | `relawan2.demo@simrp.app` | `password123` | Simulasi peserta tambahan |
| User | Relawan | Budi Relawan | `relawan3.demo@simrp.app` | `password123` | Simulasi peserta tambahan |
| User | KSH | Kak Esa | `ksh.demo@simrp.app` | `password123` | Tandai event selesai |

## Skenario Demo Cepat (Create -> Approve -> Join -> Report -> Verify)
1. Login `moderator1.demo@simrp.app`: buat draft event.
2. Login `moderator2.demo@simrp.app` atau `moderator2.camat@simrp.app`: approve draft sesuai scope.
3. Login relawan (`relawan.demo@simrp.app` / `relawan2.demo@simrp.app`): join event.
4. Login `ksh.demo@simrp.app`: tandai event selesai.
5. Login relawan yang sudah join: klik `Lapor Kegiatan` lalu submit report.
6. Login Tier 2/Admin: verifikasi report (approve/reject).
7. Cek tab `Leaderboards` untuk lihat perubahan ranking kampung.
