# MASTER PLAN 15 PEKAN (SKENARIO SISA)
## SIMREKAP - Eksekusi Day 26 sampai Day 100

Periode: Senin, 2 Maret 2026 - Jumat, 12 Juni 2026  
Skema: 15 pekan (W06-W20)

## Komposisi Tim (2 Orang)
- Kamu: `UX + Backend`
- Temanmu: `UI Design + Frontend`

Catatan:
- Orangnya tetap satu untuk UI dan FE.
- FE tetap wajib pegang integrasi API, bukan hanya desain.

## Fase + Milestone (15 Pekan)
## Fase A - Pra-Produksi Singkat (W06)
- M-A1: Scope MVP final.
- M-A2: Design thinking artifact final.
- M-A3: API contract baseline.

## Fase B - Produksi (W07-W16)
- M-B1: Auth, event, report, verify stabil.
- M-B2: XP, leaderboard, sertifikat/reward, dan mitra aktif.
- M-B3: Security baseline publish-ready.

## Fase C - Pasca-Produksi/Testing (W17-W20)
- M-C1: QA report lengkap.
- M-C2: Patch dan retest lulus.
- M-C3: Paket sidang + handover final.

## Roadmap Mingguan 15 Pekan
| Week | Rentang | Fase | Fokus Utama | Output |
|---|---|---|---|---|
| W06 | 2-6 Mar | Pra-Prod | Freeze MVP + kickoff sprint | Sprint-ready package |
| W07 | 9-13 Mar | Produksi | Auth dan role guard | Auth lintas role stabil |
| W08 | 16-20 Mar | Produksi | Event governance | Draft->approval->publish aktif |
| W09 | 23-27 Mar | Produksi | Participation flow | Join/checklist/complete stabil |
| W10 | 30 Mar-3 Apr | Produksi | Reporting submission | Report submission aktif |
| W11 | 6-10 Apr | Produksi | Verify + scoring | Verifikasi dan skor stabil |
| W12 | 13-17 Apr | Produksi | XP + leaderboard | Ranking kampung sinkron |
| W13 | 20-24 Apr | Produksi | Sertifikat + reward | Benefit relawan berjalan |
| W14 | 27 Apr-1 Mei | Produksi | Mitra module | Request->review aktif |
| W15 | 4-8 Mei | Produksi | Security hardening | Baseline security siap |
| W16 | 11-15 Mei | Produksi | Integrasi total + rehearsal | Candidate build demo |
| W17 | 18-22 Mei | Post/Test | QA execution | QA report + bugboard |
| W18 | 25-29 Mei | Post/Test | Bug fixing + retest | Stabilization build |
| W19 | 1-5 Jun | Post/Test | Final dokumen + pitch | Paket sidang siap |
| W20 | 8-12 Jun | Post/Test | UAT + handover + closing | Proyek ditutup rapi |

## Validasi Kalender Harian (Skenario 15 Pekan)
- Rentang eksekusi: `W06-W20` dengan `D26-D100` (75 hari kerja).
- Aturan: setiap pekan tetap `5 hari kerja` (`Senin-Jumat`).

| Week | Mapping Day | Rentang Tanggal | Hari Kerja |
|---|---|---|---|
| W06 | D26-D30 | 2-6 Mar 2026 | Senin-Jumat |
| W07 | D31-D35 | 9-13 Mar 2026 | Senin-Jumat |
| W08 | D36-D40 | 16-20 Mar 2026 | Senin-Jumat |
| W09 | D41-D45 | 23-27 Mar 2026 | Senin-Jumat |
| W10 | D46-D50 | 30 Mar-3 Apr 2026 | Senin-Jumat |
| W11 | D51-D55 | 6-10 Apr 2026 | Senin-Jumat |
| W12 | D56-D60 | 13-17 Apr 2026 | Senin-Jumat |
| W13 | D61-D65 | 20-24 Apr 2026 | Senin-Jumat |
| W14 | D66-D70 | 27 Apr-1 Mei 2026 | Senin-Jumat |
| W15 | D71-D75 | 4-8 Mei 2026 | Senin-Jumat |
| W16 | D76-D80 | 11-15 Mei 2026 | Senin-Jumat |
| W17 | D81-D85 | 18-22 Mei 2026 | Senin-Jumat |
| W18 | D86-D90 | 25-29 Mei 2026 | Senin-Jumat |
| W19 | D91-D95 | 1-5 Jun 2026 | Senin-Jumat |
| W20 | D96-D100 | 8-12 Jun 2026 | Senin-Jumat |

## Task Inti Mingguan (15 Pekan, 2 Orang)
| Week | Task Kamu (UX+BE) | Task Teman (UI+FE) | Kolaborasi API FE-BE |
|---|---|---|---|
| W06 | Freeze scope, acceptance criteria, API v1 | Final UI spec + FE setup sprint-ready | Review schema endpoint inti |
| W07 | Implement auth/session/RBAC | UI auth + FE login/register/guard | Sinkron error auth |
| W08 | Implement event draft/approval/publish | UI event + FE integrasi create/approve | Uji transisi status event |
| W09 | Implement join/checklist/complete | UI participation + FE join/complete | Uji kuota dan hak akses |
| W10 | Implement submit report + validasi | UI wizard report + FE submit/history | Review payload report |
| W11 | Implement verify/reject + scoring | UI verifikasi + FE status update | Uji side-effect skor |
| W12 | Implement XP pilar + leaderboard service | UI leaderboard/chart + FE fetch/update | Uji report->XP->rank |
| W13 | Implement sertifikat + redeem poin | UI sertifikat/reward + FE redeem flow | Uji transaksi poin |
| W14 | Implement API mitra + routing scope | UI form/review + FE flow mitra | Uji scope route |
| W15 | Hardening backend (input/rate-limit/CORS) | FE error handling/security state | Security regression |
| W16 | Integrasi final + seed data demo | UI polish + FE perf cleanup | Rehearsal E2E |
| W17 | Eksekusi QA backend + triage | QA UI/FE responsive/usability | Bugboard harian |
| W18 | Patch backend high-medium | Patch UI/FE high-medium | Retest patch |
| W19 | Final dokumen KP + script sidang | Final visual deck + demo FE flow | Dry-run presentasi |
| W20 | UAT final + closing report | Handover UI/FE + smoke test | Sign-off akhir |

## Guardrail Supaya FE Tidak Dinilai UI-Only
- Tiap pekan minimal ada 1 task FE integrasi API.
- Tiap pekan minimal ada 1 task FE untuk handling state/error/testing.
- Evidence FE wajib:
  - commit integrasi API,
  - bukti request/response sukses,
  - catatan bug dan perbaikan.

## Referensi Tabel Milestone No-Skip
- File CSV sinkron W06-W20 (D26-D100 tanpa hari loncat): `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv`
