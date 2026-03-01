# LOGBOOK HARIAN W06-W20 (DUA ORANG, RINCI PER PIC)
## SIMREKAP - Format Harian Day 26 sampai Day 100

Komposisi tim:
- Farchan: `UX + Backend`
- Ikram: `UI Design + Frontend`

Aturan isi harian:
- Setiap Day berisi 2 entri terpisah: `Farchan` dan `Ikram`.
- Masing-masing entri wajib punya `Aktivitas`, `Uraian Kegiatan`, `Output`, dan `Lampiran` sendiri.
- Status default semua Day: `[RENCANA]` lalu diubah ke `[TERLAKSANA]` saat selesai.

## Validasi Kalender W06-W20 (5 Hari Kerja per Pekan)
| Week | Day ID | Rentang Tanggal | Hari Kerja |
|---|---|---|---|
| W06 | D26-D30 | 2 Mar - 6 Mar 2026 | Senin-Jumat |
| W07 | D31-D35 | 9 Mar - 13 Mar 2026 | Senin-Jumat |
| W08 | D36-D40 | 16 Mar - 20 Mar 2026 | Senin-Jumat |
| W09 | D41-D45 | 23 Mar - 27 Mar 2026 | Senin-Jumat |
| W10 | D46-D50 | 30 Mar - 3 Apr 2026 | Senin-Jumat |
| W11 | D51-D55 | 6 Apr - 10 Apr 2026 | Senin-Jumat |
| W12 | D56-D60 | 13 Apr - 17 Apr 2026 | Senin-Jumat |
| W13 | D61-D65 | 20 Apr - 24 Apr 2026 | Senin-Jumat |
| W14 | D66-D70 | 27 Apr - 1 Mei 2026 | Senin-Jumat |
| W15 | D71-D75 | 4 Mei - 8 Mei 2026 | Senin-Jumat |
| W16 | D76-D80 | 11 Mei - 15 Mei 2026 | Senin-Jumat |
| W17 | D81-D85 | 18 Mei - 22 Mei 2026 | Senin-Jumat |
| W18 | D86-D90 | 25 Mei - 29 Mei 2026 | Senin-Jumat |
| W19 | D91-D95 | 1 Jun - 5 Jun 2026 | Senin-Jumat |
| W20 | D96-D100 | 8 Jun - 12 Jun 2026 | Senin-Jumat |

Referensi sinkron wajib:
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md`
- `docs/logbook/PROJECT_MANAGEMENT_15_WEEKS_SIMREKAP.md`
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md`
- `docs/logbook/logbook.md`
- `docs/logbook/MILESTONE_TABLE_W06_W20_NO_SKIP.csv`

## PEKAN 6 (W06): Pra-Produksi Final

Status Pekan: Proyeksi
Milestone Aktif: M1 PREPARATION
Task Utama: Setup dan Freeze Scope

### Day 26 (Senin, 2 Mar 2026): Freeze scope MVP dan audit screen map
Status: [RENCANA]
Milestone/Task: M1 PREPARATION / Setup dan Freeze Scope

#### Entri Farchan (UX+Backend)
Aktivitas: Freeze scope MVP dan rapikan backlog prioritas.
Uraian Kegiatan (Logbook):
"Hari ini fokus saya di 'Freeze scope MVP dan audit screen map' adalah Freeze scope MVP dan rapikan backlog prioritas. Saya mulai dengan ngerapihin backlog dan dependency backend biar batas kerja sprint jelas, lalu mengunci keputusan teknis yang paling ngaruh ke alur lanjutan. Sebelum close, saya validasi lagi keputusan yang diambil supaya output hari ini 'Scope MVP final + screen map' bisa langsung dipakai tim tanpa ambigu."
Output Farchan:
- Artefak UX+Backend harian selesai: Freeze scope MVP dan rapikan backlog prioritas.
- Outcome harian terukur: Scope MVP final + screen map.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 49-63: baseline target mingguan W06-W20.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 70-95: definisi peran aktor dan kebutuhan sistem.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 23-39: struktur IA dan role workspace.

#### Entri Ikram (UI+Frontend)
Aktivitas: Audit ulang screen Figma aktif dan mapping ke modul FE.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Audit ulang screen Figma aktif dan mapping ke modul FE. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M1 PREPARATION / Setup dan Freeze Scope. Setelah sinkronisasi final, 'Scope MVP final + screen map' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Audit ulang screen Figma aktif dan mapping ke modul FE.
- Outcome harian terukur: Scope MVP final + screen map.
Lampiran Ikram (Bukti Screenshot):
- `docs/ASSET_INVENTORY.md` baris 9-31: baseline aset visual dan struktur folder aset.
- `docs/LIBRARY_SELECTION.md` baris 10-23: stack UI/FE resmi untuk sprint produksi.
- `src/app/App.tsx` baris 46-49 dan 138-144: baseline state auth/view pada app shell.

### Day 27 (Selasa, 3 Mar 2026): API contract v1 dan baseline FE
Status: [RENCANA]
Milestone/Task: M1 PREPARATION / Setup dan Freeze Scope

#### Entri Farchan (UX+Backend)
Aktivitas: Finalkan API contract v1 untuk auth/event/report.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalkan API contract v1 untuk auth/event/report sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'API contract v1 + FE baseline' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Finalkan API contract v1 untuk auth/event/report.
- Outcome harian terukur: API contract v1 + FE baseline.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 49-63: baseline target mingguan W06-W20.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 70-95: definisi peran aktor dan kebutuhan sistem.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 23-39: struktur IA dan role workspace.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalkan design token dan setup struktur FE sprint-ready.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalkan design token dan setup struktur FE sprint-ready sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'API contract v1 + FE baseline' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Finalkan design token dan setup struktur FE sprint-ready.
- Outcome harian terukur: API contract v1 + FE baseline.
Lampiran Ikram (Bukti Screenshot):
- `docs/ASSET_INVENTORY.md` baris 9-31: baseline aset visual dan struktur folder aset.
- `docs/LIBRARY_SELECTION.md` baris 10-23: stack UI/FE resmi untuk sprint produksi.
- `src/app/App.tsx` baris 46-49 dan 138-144: baseline state auth/view pada app shell.

### Day 28 (Rabu, 4 Mar 2026): Validasi design thinking artifact
Status: [RENCANA]
Milestone/Task: M1 PREPARATION / Setup dan Freeze Scope

#### Entri Farchan (UX+Backend)
Aktivitas: Finalisasi persona, journey map, dan problem framing.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalisasi persona, journey map, dan problem framing sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Dokumen persona/journey + component map' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Finalisasi persona, journey map, dan problem framing.
- Outcome harian terukur: Dokumen persona/journey + component map.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 49-63: baseline target mingguan W06-W20.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 70-95: definisi peran aktor dan kebutuhan sistem.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 23-39: struktur IA dan role workspace.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sinkronkan wireframe akhir ke struktur komponen FE.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Sinkronkan wireframe akhir ke struktur komponen FE. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M1 PREPARATION / Setup dan Freeze Scope. Setelah sinkronisasi final, 'Dokumen persona/journey + component map' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Sinkronkan wireframe akhir ke struktur komponen FE.
- Outcome harian terukur: Dokumen persona/journey + component map.
Lampiran Ikram (Bukti Screenshot):
- `docs/ASSET_INVENTORY.md` baris 9-31: baseline aset visual dan struktur folder aset.
- `docs/LIBRARY_SELECTION.md` baris 10-23: stack UI/FE resmi untuk sprint produksi.
- `src/app/App.tsx` baris 46-49 dan 138-144: baseline state auth/view pada app shell.

### Day 29 (Kamis, 5 Mar 2026): Acceptance criteria sprint 1
Status: [RENCANA]
Milestone/Task: M1 PREPARATION / Setup dan Freeze Scope

#### Entri Farchan (UX+Backend)
Aktivitas: Tetapkan acceptance criteria dan DoD untuk fitur sprint 1.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Tetapkan acceptance criteria dan DoD untuk fitur sprint 1 dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'DoD sprint 1 + app shell aktif' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Tetapkan acceptance criteria dan DoD untuk fitur sprint 1.
- Outcome harian terukur: DoD sprint 1 + app shell aktif.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 49-63: baseline target mingguan W06-W20.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 70-95: definisi peran aktor dan kebutuhan sistem.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 23-39: struktur IA dan role workspace.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement route skeleton dan state dasar app shell.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement route skeleton dan state dasar app shell pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'DoD sprint 1 + app shell aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement route skeleton dan state dasar app shell.
- Outcome harian terukur: DoD sprint 1 + app shell aktif.
Lampiran Ikram (Bukti Screenshot):
- `docs/ASSET_INVENTORY.md` baris 9-31: baseline aset visual dan struktur folder aset.
- `docs/LIBRARY_SELECTION.md` baris 10-23: stack UI/FE resmi untuk sprint produksi.
- `src/app/App.tsx` baris 46-49 dan 138-144: baseline state auth/view pada app shell.

### Day 30 (Jumat, 6 Mar 2026): Sprint planning W07
Status: [RENCANA]
Milestone/Task: M1 PREPARATION / Setup dan Freeze Scope

#### Entri Farchan (UX+Backend)
Aktivitas: Kunci sprint planning W07 dan risk register.
Uraian Kegiatan (Logbook):
"Hari ini fokus saya di 'Sprint planning W07' adalah Kunci sprint planning W07 dan risk register. Saya mulai dengan ngerapihin backlog dan dependency backend biar batas kerja sprint jelas, lalu mengunci keputusan teknis yang paling ngaruh ke alur lanjutan. Sebelum close, saya validasi lagi keputusan yang diambil supaya output hari ini 'Sprint backlog W07' bisa langsung dipakai tim tanpa ambigu."
Output Farchan:
- Artefak UX+Backend harian selesai: Kunci sprint planning W07 dan risk register.
- Outcome harian terukur: Sprint backlog W07.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 49-63: baseline target mingguan W06-W20.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 70-95: definisi peran aktor dan kebutuhan sistem.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 23-39: struktur IA dan role workspace.

#### Entri Ikram (UI+Frontend)
Aktivitas: Final review readiness UI+FE untuk sprint berikutnya.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Final review readiness UI+FE untuk sprint berikutnya sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Sprint backlog W07' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Final review readiness UI+FE untuk sprint berikutnya.
- Outcome harian terukur: Sprint backlog W07.
Lampiran Ikram (Bukti Screenshot):
- `docs/ASSET_INVENTORY.md` baris 9-31: baseline aset visual dan struktur folder aset.
- `docs/LIBRARY_SELECTION.md` baris 10-23: stack UI/FE resmi untuk sprint produksi.
- `src/app/App.tsx` baris 46-49 dan 138-144: baseline state auth/view pada app shell.

## PEKAN 7 (W07): Auth dan Role Guard

Status Pekan: Proyeksi
Milestone Aktif: M2 AUTH SYSTEM
Task Utama: Authentication dan Role

### Day 31 (Senin, 9 Mar 2026): Validasi login register
Status: [RENCANA]
Milestone/Task: M2 AUTH SYSTEM / Authentication dan Role

#### Entri Farchan (UX+Backend)
Aktivitas: Implement validasi signup/login backend.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement validasi signup/login backend pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Flow login/register jalan' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement validasi signup/login backend.
- Outcome harian terukur: Flow login/register jalan.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1211-1291: endpoint `auth/signup`, `auth/login`, `auth/admin-login`.
- `server/local_api.py` baris 240-252: `create_session()` dan `user_from_token()`.
- `server/local_api.py` baris 24-26 dan 120: policy auth/security dan rate limiting.

#### Entri Ikram (UI+Frontend)
Aktivitas: Desain state auth loading-error-success dan implement form FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Desain state auth loading-error-success dan implement form FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Flow login/register jalan' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Desain state auth loading-error-success dan implement form FE.
- Outcome harian terukur: Flow login/register jalan.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 30-44: login flow dan validasi role awal.
- `src/app/components/AdminLoginPage.tsx` baris 28-29 dan `src/app/components/RegisterPage.tsx` baris 176-177: admin login + signup FE.
- `src/app/App.tsx` baris 46-49 dan 184-190: token storage dan route guard view.

### Day 32 (Selasa, 10 Mar 2026): Session dan route guard
Status: [RENCANA]
Milestone/Task: M2 AUTH SYSTEM / Authentication dan Role

#### Entri Farchan (UX+Backend)
Aktivitas: Implement session, auth me, dan logout backend.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement session, auth me, dan logout backend pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Session flow stabil' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement session, auth me, dan logout backend.
- Outcome harian terukur: Session flow stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1211-1291: endpoint `auth/signup`, `auth/login`, `auth/admin-login`.
- `server/local_api.py` baris 240-252: `create_session()` dan `user_from_token()`.
- `server/local_api.py` baris 24-26 dan 120: policy auth/security dan rate limiting.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi token storage dan route guard FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi token storage dan route guard FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Session flow stabil' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi token storage dan route guard FE.
- Outcome harian terukur: Session flow stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 30-44: login flow dan validasi role awal.
- `src/app/components/AdminLoginPage.tsx` baris 28-29 dan `src/app/components/RegisterPage.tsx` baris 176-177: admin login + signup FE.
- `src/app/App.tsx` baris 46-49 dan 184-190: token storage dan route guard view.

### Day 33 (Rabu, 11 Mar 2026): Permission per role
Status: [RENCANA]
Milestone/Task: M2 AUTH SYSTEM / Authentication dan Role

#### Entri Farchan (UX+Backend)
Aktivitas: Implement mapping permission per role.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement mapping permission per role pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Role-based view aktif' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement mapping permission per role.
- Outcome harian terukur: Role-based view aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1211-1291: endpoint `auth/signup`, `auth/login`, `auth/admin-login`.
- `server/local_api.py` baris 240-252: `create_session()` dan `user_from_token()`.
- `server/local_api.py` baris 24-26 dan 120: policy auth/security dan rate limiting.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sesuaikan menu UI per role dan conditional rendering FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Sesuaikan menu UI per role dan conditional rendering FE dalam konteks 'Permission per role'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M2 AUTH SYSTEM / Authentication dan Role. Hasil 'Role-based view aktif' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Sesuaikan menu UI per role dan conditional rendering FE.
- Outcome harian terukur: Role-based view aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 30-44: login flow dan validasi role awal.
- `src/app/components/AdminLoginPage.tsx` baris 28-29 dan `src/app/components/RegisterPage.tsx` baris 176-177: admin login + signup FE.
- `src/app/App.tsx` baris 46-49 dan 184-190: token storage dan route guard view.

### Day 34 (Kamis, 12 Mar 2026): Standarisasi error auth
Status: [RENCANA]
Milestone/Task: M2 AUTH SYSTEM / Authentication dan Role

#### Entri Farchan (UX+Backend)
Aktivitas: Stabilkan model error auth 400/401/429.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilkan model error auth 400/401/429 untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Error auth sinkron' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Stabilkan model error auth 400/401/429.
- Outcome harian terukur: Error auth sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1211-1291: endpoint `auth/signup`, `auth/login`, `auth/admin-login`.
- `server/local_api.py` baris 240-252: `create_session()` dan `user_from_token()`.
- `server/local_api.py` baris 24-26 dan 120: policy auth/security dan rate limiting.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement error handling auth di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement error handling auth di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Error auth sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement error handling auth di FE.
- Outcome harian terukur: Error auth sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 30-44: login flow dan validasi role awal.
- `src/app/components/AdminLoginPage.tsx` baris 28-29 dan `src/app/components/RegisterPage.tsx` baris 176-177: admin login + signup FE.
- `src/app/App.tsx` baris 46-49 dan 184-190: token storage dan route guard view.

### Day 35 (Jumat, 13 Mar 2026): Retest auth E2E
Status: [RENCANA]
Milestone/Task: M2 AUTH SYSTEM / Authentication dan Role

#### Entri Farchan (UX+Backend)
Aktivitas: Retest auth end-to-end lintas role.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest auth end-to-end lintas role. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Auth lintas role stabil' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Retest auth end-to-end lintas role.
- Outcome harian terukur: Auth lintas role stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1211-1291: endpoint `auth/signup`, `auth/login`, `auth/admin-login`.
- `server/local_api.py` baris 240-252: `create_session()` dan `user_from_token()`.
- `server/local_api.py` baris 24-26 dan 120: policy auth/security dan rate limiting.

#### Entri Ikram (UI+Frontend)
Aktivitas: Polish UI/FE auth dan catat defect.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Polish UI/FE auth dan catat defect dalam konteks 'Retest auth E2E'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M2 AUTH SYSTEM / Authentication dan Role. Hasil 'Auth lintas role stabil' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Polish UI/FE auth dan catat defect.
- Outcome harian terukur: Auth lintas role stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LoginPage.tsx` baris 30-44: login flow dan validasi role awal.
- `src/app/components/AdminLoginPage.tsx` baris 28-29 dan `src/app/components/RegisterPage.tsx` baris 176-177: admin login + signup FE.
- `src/app/App.tsx` baris 46-49 dan 184-190: token storage dan route guard view.

## PEKAN 8 (W08): Event Draft Approval Publish

Status Pekan: Proyeksi
Milestone Aktif: M3 EVENT MODULE
Task Utama: Event Management

### Day 36 (Senin, 16 Mar 2026): Rule create event
Status: [RENCANA]
Milestone/Task: M3 EVENT MODULE / Event Management

#### Entri Farchan (UX+Backend)
Aktivitas: Validasi rule create event untuk scope pilar kuota.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Validasi rule create event untuk scope pilar kuota. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M3 EVENT MODULE / Event Management. Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Create event draft aktif' punya dasar teknis yang jelas."
Output Farchan:
- Artefak UX+Backend harian selesai: Validasi rule create event untuk scope pilar kuota.
- Outcome harian terukur: Create event draft aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1358-1452: create event dan approval workflow backend.
- `server/local_api.py` baris 365-387: struktur tabel `events` dan state lifecycle.
- `server/local_api.py` baris 1433-1457: transisi approval dan publish readiness.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalisasi UI form event dan implement submit FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalisasi UI form event dan implement submit FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Create event draft aktif' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Finalisasi UI form event dan implement submit FE.
- Outcome harian terukur: Create event draft aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 223-224 dan 359-360: create event dari FE.
- `src/app/components/ModeratorDashboard.tsx` baris 284-285: approval action event di FE.
- `src/app/components/UserDashboard.tsx` baris 47-48: sinkron fetch event untuk user view.

### Day 37 (Selasa, 17 Mar 2026): Draft event list
Status: [RENCANA]
Milestone/Task: M3 EVENT MODULE / Event Management

#### Entri Farchan (UX+Backend)
Aktivitas: Stabilkan endpoint create draft event.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilkan endpoint create draft event untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Draft list sinkron' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Stabilkan endpoint create draft event.
- Outcome harian terukur: Draft list sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1358-1452: create event dan approval workflow backend.
- `server/local_api.py` baris 365-387: struktur tabel `events` dan state lifecycle.
- `server/local_api.py` baris 1433-1457: transisi approval dan publish readiness.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi daftar draft event moderator di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi daftar draft event moderator di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Draft list sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi daftar draft event moderator di FE.
- Outcome harian terukur: Draft list sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 223-224 dan 359-360: create event dari FE.
- `src/app/components/ModeratorDashboard.tsx` baris 284-285: approval action event di FE.
- `src/app/components/UserDashboard.tsx` baris 47-48: sinkron fetch event untuk user view.

### Day 38 (Rabu, 18 Mar 2026): Approval reject flow
Status: [RENCANA]
Milestone/Task: M3 EVENT MODULE / Event Management

#### Entri Farchan (UX+Backend)
Aktivitas: Implement endpoint approval/reject event.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement endpoint approval/reject event pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Approval flow aktif' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement endpoint approval/reject event.
- Outcome harian terukur: Approval flow aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1358-1452: create event dan approval workflow backend.
- `server/local_api.py` baris 365-387: struktur tabel `events` dan state lifecycle.
- `server/local_api.py` baris 1433-1457: transisi approval dan publish readiness.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement aksi approve/reject di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement aksi approve/reject di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Approval flow aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement aksi approve/reject di FE.
- Outcome harian terukur: Approval flow aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 223-224 dan 359-360: create event dari FE.
- `src/app/components/ModeratorDashboard.tsx` baris 284-285: approval action event di FE.
- `src/app/components/UserDashboard.tsx` baris 47-48: sinkron fetch event untuk user view.

### Day 39 (Kamis, 19 Mar 2026): Publish status event
Status: [RENCANA]
Milestone/Task: M3 EVENT MODULE / Event Management

#### Entri Farchan (UX+Backend)
Aktivitas: Pastikan publish event sesuai status backend.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Pastikan publish event sesuai status backend pada konteks 'Publish status event'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M3 EVENT MODULE / Event Management. Setelah selesai, saya pastikan 'Event publish tampil benar' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Pastikan publish event sesuai status backend.
- Outcome harian terukur: Event publish tampil benar.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1358-1452: create event dan approval workflow backend.
- `server/local_api.py` baris 365-387: struktur tabel `events` dan state lifecycle.
- `server/local_api.py` baris 1433-1457: transisi approval dan publish readiness.

#### Entri Ikram (UI+Frontend)
Aktivitas: Update kartu event dan badge status FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Update kartu event dan badge status FE dalam konteks 'Publish status event'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M3 EVENT MODULE / Event Management. Hasil 'Event publish tampil benar' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Update kartu event dan badge status FE.
- Outcome harian terukur: Event publish tampil benar.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 223-224 dan 359-360: create event dari FE.
- `src/app/components/ModeratorDashboard.tsx` baris 284-285: approval action event di FE.
- `src/app/components/UserDashboard.tsx` baris 47-48: sinkron fetch event untuk user view.

### Day 40 (Jumat, 20 Mar 2026): Uji E2E event governance
Status: [RENCANA]
Milestone/Task: M3 EVENT MODULE / Event Management

#### Entri Farchan (UX+Backend)
Aktivitas: Uji E2E draft sampai approval sampai publish.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji E2E draft sampai approval sampai publish. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Event governance stabil' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Uji E2E draft sampai approval sampai publish.
- Outcome harian terukur: Event governance stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1358-1452: create event dan approval workflow backend.
- `server/local_api.py` baris 365-387: struktur tabel `events` dan state lifecycle.
- `server/local_api.py` baris 1433-1457: transisi approval dan publish readiness.

#### Entri Ikram (UI+Frontend)
Aktivitas: Refinement UI/FE pasca uji alur event.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Refinement UI/FE pasca uji alur event dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Event governance stabil' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: Refinement UI/FE pasca uji alur event.
- Outcome harian terukur: Event governance stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 223-224 dan 359-360: create event dari FE.
- `src/app/components/ModeratorDashboard.tsx` baris 284-285: approval action event di FE.
- `src/app/components/UserDashboard.tsx` baris 47-48: sinkron fetch event untuk user view.

## PEKAN 9 (W09): Participation Flow

Status Pekan: Proyeksi
Milestone Aktif: M4 PARTICIPATION
Task Utama: Join dan Completion

### Day 41 (Senin, 23 Mar 2026): Rule join event
Status: [RENCANA]
Milestone/Task: M4 PARTICIPATION / Join dan Completion

#### Entri Farchan (UX+Backend)
Aktivitas: Implement rule join event quota duplicate status.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement rule join event quota duplicate status pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Join flow valid' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement rule join event quota duplicate status.
- Outcome harian terukur: Join flow valid.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1457-1510: endpoint join event dan complete event.
- `server/local_api.py` baris 365-404: relasi `events` dan `event_participation`.
- `server/local_api.py` baris 1082-1124: endpoint list event untuk validasi status.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement tombol join dan state full closed.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement tombol join dan state full closed pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Join flow valid' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement tombol join dan state full closed.
- Outcome harian terukur: Join flow valid.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: request join event dari FE.
- `src/app/components/UserDashboard.tsx` baris 111-112: trigger complete event oleh KSH/user.
- `src/app/components/UserDashboard.tsx` baris 47-48: refresh event state pasca join/complete.

### Day 42 (Selasa, 24 Mar 2026): Riwayat partisipasi
Status: [RENCANA]
Milestone/Task: M4 PARTICIPATION / Join dan Completion

#### Entri Farchan (UX+Backend)
Aktivitas: Implement endpoint riwayat partisipasi.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement endpoint riwayat partisipasi pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'History partisipasi tampil' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement endpoint riwayat partisipasi.
- Outcome harian terukur: History partisipasi tampil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1457-1510: endpoint join event dan complete event.
- `server/local_api.py` baris 365-404: relasi `events` dan `event_participation`.
- `server/local_api.py` baris 1082-1124: endpoint list event untuk validasi status.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi halaman riwayat partisipasi FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi halaman riwayat partisipasi FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'History partisipasi tampil' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi halaman riwayat partisipasi FE.
- Outcome harian terukur: History partisipasi tampil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: request join event dari FE.
- `src/app/components/UserDashboard.tsx` baris 111-112: trigger complete event oleh KSH/user.
- `src/app/components/UserDashboard.tsx` baris 47-48: refresh event state pasca join/complete.

### Day 43 (Rabu, 25 Mar 2026): Complete event oleh KSH
Status: [RENCANA]
Milestone/Task: M4 PARTICIPATION / Join dan Completion

#### Entri Farchan (UX+Backend)
Aktivitas: Implement complete event oleh KSH.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement complete event oleh KSH pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Complete flow aktif' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement complete event oleh KSH.
- Outcome harian terukur: Complete flow aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1457-1510: endpoint join event dan complete event.
- `server/local_api.py` baris 365-404: relasi `events` dan `event_participation`.
- `server/local_api.py` baris 1082-1124: endpoint list event untuk validasi status.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement CTA complete khusus KSH di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement CTA complete khusus KSH di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Complete flow aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement CTA complete khusus KSH di FE.
- Outcome harian terukur: Complete flow aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: request join event dari FE.
- `src/app/components/UserDashboard.tsx` baris 111-112: trigger complete event oleh KSH/user.
- `src/app/components/UserDashboard.tsx` baris 47-48: refresh event state pasca join/complete.

### Day 44 (Kamis, 26 Mar 2026): Checklist attendance
Status: [RENCANA]
Milestone/Task: M4 PARTICIPATION / Join dan Completion

#### Entri Farchan (UX+Backend)
Aktivitas: Validasi checklist kehadiran dan transisi status.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Validasi checklist kehadiran dan transisi status. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M4 PARTICIPATION / Join dan Completion. Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Attendance sinkron' punya dasar teknis yang jelas."
Output Farchan:
- Artefak UX+Backend harian selesai: Validasi checklist kehadiran dan transisi status.
- Outcome harian terukur: Attendance sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1457-1510: endpoint join event dan complete event.
- `server/local_api.py` baris 365-404: relasi `events` dan `event_participation`.
- `server/local_api.py` baris 1082-1124: endpoint list event untuk validasi status.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi checklist attendance FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi checklist attendance FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Attendance sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi checklist attendance FE.
- Outcome harian terukur: Attendance sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: request join event dari FE.
- `src/app/components/UserDashboard.tsx` baris 111-112: trigger complete event oleh KSH/user.
- `src/app/components/UserDashboard.tsx` baris 47-48: refresh event state pasca join/complete.

### Day 45 (Jumat, 27 Mar 2026): Retest participation flow
Status: [RENCANA]
Milestone/Task: M4 PARTICIPATION / Join dan Completion

#### Entri Farchan (UX+Backend)
Aktivitas: Retest join attendance complete.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest join attendance complete. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Participation stabil' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Retest join attendance complete.
- Outcome harian terukur: Participation stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1457-1510: endpoint join event dan complete event.
- `server/local_api.py` baris 365-404: relasi `events` dan `event_participation`.
- `server/local_api.py` baris 1082-1124: endpoint list event untuk validasi status.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug participation pada UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug participation pada UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Participation stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Patch bug participation pada UI/FE.
- Outcome harian terukur: Participation stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: request join event dari FE.
- `src/app/components/UserDashboard.tsx` baris 111-112: trigger complete event oleh KSH/user.
- `src/app/components/UserDashboard.tsx` baris 47-48: refresh event state pasca join/complete.

## PEKAN 10 (W10): Submit Report

Status Pekan: Proyeksi
Milestone Aktif: M4 PARTICIPATION
Task Utama: Reporting Submission

### Day 46 (Senin, 30 Mar 2026): Payload wizard report
Status: [RENCANA]
Milestone/Task: M4 PARTICIPATION / Reporting Submission

#### Entri Farchan (UX+Backend)
Aktivitas: Finalkan payload report step 1 dan step 2.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalkan payload report step 1 dan step 2 sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Step 1 aktif' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Finalkan payload report step 1 dan step 2.
- Outcome harian terukur: Step 1 aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1518-1575: handler submit report dan validasi proses.
- `server/local_api.py` baris 411-426: struktur tabel `event_reports`.
- `server/local_api.py` baris 1126-1157: endpoint history `reports`.

#### Entri Ikram (UI+Frontend)
Aktivitas: Bangun wizard report step 1 di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Bangun wizard report step 1 di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Step 1 aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Bangun wizard report step 1 di FE.
- Outcome harian terukur: Step 1 aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 92-98: submit payload laporan ke API.
- `src/app/components/ReportingWizard.tsx` baris 182 dan 316: field wizard + submit control.
- `src/app/components/UserDashboard.tsx` baris 67-68: fetch history laporan user.

### Day 47 (Selasa, 31 Mar 2026): Submit report endpoint
Status: [RENCANA]
Milestone/Task: M4 PARTICIPATION / Reporting Submission

#### Entri Farchan (UX+Backend)
Aktivitas: Implement submit report endpoint beserta validasi.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement submit report endpoint beserta validasi pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Submit report jalan' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement submit report endpoint beserta validasi.
- Outcome harian terukur: Submit report jalan.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1518-1575: handler submit report dan validasi proses.
- `server/local_api.py` baris 411-426: struktur tabel `event_reports`.
- `server/local_api.py` baris 1126-1157: endpoint history `reports`.

#### Entri Ikram (UI+Frontend)
Aktivitas: Bangun wizard step 2 dan validasi FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Bangun wizard step 2 dan validasi FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Submit report jalan' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Bangun wizard step 2 dan validasi FE.
- Outcome harian terukur: Submit report jalan.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 92-98: submit payload laporan ke API.
- `src/app/components/ReportingWizard.tsx` baris 182 dan 316: field wizard + submit control.
- `src/app/components/UserDashboard.tsx` baris 67-68: fetch history laporan user.

### Day 48 (Rabu, 1 Apr 2026): Validasi bukti laporan
Status: [RENCANA]
Milestone/Task: M4 PARTICIPATION / Reporting Submission

#### Entri Farchan (UX+Backend)
Aktivitas: Atur validasi media proof laporan.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Atur validasi media proof laporan. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M4 PARTICIPATION / Reporting Submission. Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Bukti laporan tervalidasi' punya dasar teknis yang jelas."
Output Farchan:
- Artefak UX+Backend harian selesai: Atur validasi media proof laporan.
- Outcome harian terukur: Bukti laporan tervalidasi.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1518-1575: handler submit report dan validasi proses.
- `server/local_api.py` baris 411-426: struktur tabel `event_reports`.
- `server/local_api.py` baris 1126-1157: endpoint history `reports`.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement behavior upload dan proof field di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement behavior upload dan proof field di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Bukti laporan tervalidasi' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement behavior upload dan proof field di FE.
- Outcome harian terukur: Bukti laporan tervalidasi.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 92-98: submit payload laporan ke API.
- `src/app/components/ReportingWizard.tsx` baris 182 dan 316: field wizard + submit control.
- `src/app/components/UserDashboard.tsx` baris 67-68: fetch history laporan user.

### Day 49 (Kamis, 2 Apr 2026): Sinkron status report
Status: [RENCANA]
Milestone/Task: M4 PARTICIPATION / Reporting Submission

#### Entri Farchan (UX+Backend)
Aktivitas: Sinkron status report pending di backend.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Sinkron status report pending di backend. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M4 PARTICIPATION / Reporting Submission. Setelah itu saya catat poin koreksi dan konfirmasi final biar 'History report sinkron' punya dasar teknis yang jelas."
Output Farchan:
- Artefak UX+Backend harian selesai: Sinkron status report pending di backend.
- Outcome harian terukur: History report sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1518-1575: handler submit report dan validasi proses.
- `server/local_api.py` baris 411-426: struktur tabel `event_reports`.
- `server/local_api.py` baris 1126-1157: endpoint history `reports`.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi history report user di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi history report user di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'History report sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi history report user di FE.
- Outcome harian terukur: History report sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 92-98: submit payload laporan ke API.
- `src/app/components/ReportingWizard.tsx` baris 182 dan 316: field wizard + submit control.
- `src/app/components/UserDashboard.tsx` baris 67-68: fetch history laporan user.

### Day 50 (Jumat, 3 Apr 2026): E2E reporting
Status: [RENCANA]
Milestone/Task: M4 PARTICIPATION / Reporting Submission

#### Entri Farchan (UX+Backend)
Aktivitas: Uji E2E report submission.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji E2E report submission. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Reporting stabil' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Uji E2E report submission.
- Outcome harian terukur: Reporting stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1518-1575: handler submit report dan validasi proses.
- `server/local_api.py` baris 411-426: struktur tabel `event_reports`.
- `server/local_api.py` baris 1126-1157: endpoint history `reports`.

#### Entri Ikram (UI+Frontend)
Aktivitas: Refinement wizard report di UI/FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Refinement wizard report di UI/FE dalam konteks 'E2E reporting'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M4 PARTICIPATION / Reporting Submission. Hasil 'Reporting stabil' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Refinement wizard report di UI/FE.
- Outcome harian terukur: Reporting stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ReportingWizard.tsx` baris 92-98: submit payload laporan ke API.
- `src/app/components/ReportingWizard.tsx` baris 182 dan 316: field wizard + submit control.
- `src/app/components/UserDashboard.tsx` baris 67-68: fetch history laporan user.

## PEKAN 11 (W11): Verify dan Scoring Dasar

Status Pekan: Proyeksi
Milestone Aktif: M5 GAMIFICATION
Task Utama: Verify dan Scoring

### Day 51 (Senin, 6 Apr 2026): Verify reject reason
Status: [RENCANA]
Milestone/Task: M5 GAMIFICATION / Verify dan Scoring

#### Entri Farchan (UX+Backend)
Aktivitas: Implement verify reject dan reason backend.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement verify reject dan reason backend pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Verify panel aktif' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement verify reject dan reason backend.
- Outcome harian terukur: Verify panel aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1576-1599: verify/reject report dan update status.
- `server/local_api.py` baris 862-875: `apply_xp()` sebagai scoring engine.
- `server/local_api.py` baris 458-503: `audit_logs` dan `temporary_adjustments` untuk jejak moderasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement panel verifikasi moderator FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement panel verifikasi moderator FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Verify panel aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement panel verifikasi moderator FE.
- Outcome harian terukur: Verify panel aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 249-250: verify/reject report dari panel moderator.
- `src/app/components/AdminDashboard.tsx` baris 130-131: verify report dari panel admin.
- `src/app/components/ModeratorDashboard.tsx` baris 170-171: inbox laporan untuk proses verifikasi.

### Day 52 (Selasa, 7 Apr 2026): Scoring dasar
Status: [RENCANA]
Milestone/Task: M5 GAMIFICATION / Verify dan Scoring

#### Entri Farchan (UX+Backend)
Aktivitas: Implement scoring dasar saat verify.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement scoring dasar saat verify pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Scoring sinkron' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement scoring dasar saat verify.
- Outcome harian terukur: Scoring sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1576-1599: verify/reject report dan update status.
- `server/local_api.py` baris 862-875: `apply_xp()` sebagai scoring engine.
- `server/local_api.py` baris 458-503: `audit_logs` dan `temporary_adjustments` untuk jejak moderasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Tampilkan feedback status dan skor di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Tampilkan feedback status dan skor di FE dalam konteks 'Scoring dasar'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M5 GAMIFICATION / Verify dan Scoring. Hasil 'Scoring sinkron' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Tampilkan feedback status dan skor di FE.
- Outcome harian terukur: Scoring sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 249-250: verify/reject report dari panel moderator.
- `src/app/components/AdminDashboard.tsx` baris 130-131: verify report dari panel admin.
- `src/app/components/ModeratorDashboard.tsx` baris 170-171: inbox laporan untuk proses verifikasi.

### Day 53 (Rabu, 8 Apr 2026): Audit trail report
Status: [RENCANA]
Milestone/Task: M5 GAMIFICATION / Verify dan Scoring

#### Entri Farchan (UX+Backend)
Aktivitas: Tambah audit trail status report.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Tambah audit trail status report. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M5 GAMIFICATION / Verify dan Scoring. Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Audit trail terbaca' punya dasar teknis yang jelas."
Output Farchan:
- Artefak UX+Backend harian selesai: Tambah audit trail status report.
- Outcome harian terukur: Audit trail terbaca.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1576-1599: verify/reject report dan update status.
- `server/local_api.py` baris 862-875: `apply_xp()` sebagai scoring engine.
- `server/local_api.py` baris 458-503: `audit_logs` dan `temporary_adjustments` untuk jejak moderasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement timeline status report FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement timeline status report FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Audit trail terbaca' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement timeline status report FE.
- Outcome harian terukur: Audit trail terbaca.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 249-250: verify/reject report dari panel moderator.
- `src/app/components/AdminDashboard.tsx` baris 130-131: verify report dari panel admin.
- `src/app/components/ModeratorDashboard.tsx` baris 170-171: inbox laporan untuk proses verifikasi.

### Day 54 (Kamis, 9 Apr 2026): Notifikasi status report
Status: [RENCANA]
Milestone/Task: M5 GAMIFICATION / Verify dan Scoring

#### Entri Farchan (UX+Backend)
Aktivitas: Stabilkan notifikasi status report backend.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilkan notifikasi status report backend untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Notifikasi status aktif' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Stabilkan notifikasi status report backend.
- Outcome harian terukur: Notifikasi status aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1576-1599: verify/reject report dan update status.
- `server/local_api.py` baris 862-875: `apply_xp()` sebagai scoring engine.
- `server/local_api.py` baris 458-503: `audit_logs` dan `temporary_adjustments` untuk jejak moderasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement indikator notifikasi FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement indikator notifikasi FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Notifikasi status aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement indikator notifikasi FE.
- Outcome harian terukur: Notifikasi status aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 249-250: verify/reject report dari panel moderator.
- `src/app/components/AdminDashboard.tsx` baris 130-131: verify report dari panel admin.
- `src/app/components/ModeratorDashboard.tsx` baris 170-171: inbox laporan untuk proses verifikasi.

### Day 55 (Jumat, 10 Apr 2026): Retest verify scoring
Status: [RENCANA]
Milestone/Task: M5 GAMIFICATION / Verify dan Scoring

#### Entri Farchan (UX+Backend)
Aktivitas: Retest verify dan scoring end-to-end.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest verify dan scoring end-to-end. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Verifikasi stabil' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Retest verify dan scoring end-to-end.
- Outcome harian terukur: Verifikasi stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1576-1599: verify/reject report dan update status.
- `server/local_api.py` baris 862-875: `apply_xp()` sebagai scoring engine.
- `server/local_api.py` baris 458-503: `audit_logs` dan `temporary_adjustments` untuk jejak moderasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug verifikasi pada UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug verifikasi pada UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Verifikasi stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Patch bug verifikasi pada UI/FE.
- Outcome harian terukur: Verifikasi stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 249-250: verify/reject report dari panel moderator.
- `src/app/components/AdminDashboard.tsx` baris 130-131: verify report dari panel admin.
- `src/app/components/ModeratorDashboard.tsx` baris 170-171: inbox laporan untuk proses verifikasi.

## PEKAN 12 (W12): XP dan Leaderboard

Status Pekan: Proyeksi
Milestone Aktif: M5 GAMIFICATION
Task Utama: XP dan Leaderboard

### Day 56 (Senin, 13 Apr 2026): Formula XP final
Status: [RENCANA]
Milestone/Task: M5 GAMIFICATION / XP dan Leaderboard

#### Entri Farchan (UX+Backend)
Aktivitas: Finalkan rumus XP kampung dan pilar.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalkan rumus XP kampung dan pilar sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Leaderboard awal aktif' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Finalkan rumus XP kampung dan pilar.
- Outcome harian terukur: Leaderboard awal aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 862-875: kalkulasi XP lintas peserta dan pilar.
- `server/local_api.py` baris 987-1002: endpoint `/kampung` untuk leaderboard.
- `server/local_api.py` baris 1595: update poin user setelah verifikasi report.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI leaderboard top ringkas.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI leaderboard top ringkas pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Leaderboard awal aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement UI leaderboard top ringkas.
- Outcome harian terukur: Leaderboard awal aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 87-88: fetch leaderboard kampung.
- `src/app/components/UserDashboard.tsx` baris 278-292: rendering tabel leaderboard FE.
- `src/data/levelingSystem.ts` baris 145-223: logic level dan progress UI.

### Day 57 (Selasa, 14 Apr 2026): Sinkron update rank
Status: [RENCANA]
Milestone/Task: M5 GAMIFICATION / XP dan Leaderboard

#### Entri Farchan (UX+Backend)
Aktivitas: Sinkron update XP pasca verify.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Sinkron update XP pasca verify. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M5 GAMIFICATION / XP dan Leaderboard. Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Rank update sinkron' punya dasar teknis yang jelas."
Output Farchan:
- Artefak UX+Backend harian selesai: Sinkron update XP pasca verify.
- Outcome harian terukur: Rank update sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 862-875: kalkulasi XP lintas peserta dan pilar.
- `server/local_api.py` baris 987-1002: endpoint `/kampung` untuk leaderboard.
- `server/local_api.py` baris 1595: update poin user setelah verifikasi report.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi rank card dan nilai XP FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi rank card dan nilai XP FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Rank update sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi rank card dan nilai XP FE.
- Outcome harian terukur: Rank update sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 87-88: fetch leaderboard kampung.
- `src/app/components/UserDashboard.tsx` baris 278-292: rendering tabel leaderboard FE.
- `src/data/levelingSystem.ts` baris 145-223: logic level dan progress UI.

### Day 58 (Rabu, 15 Apr 2026): Service progres pilar
Status: [RENCANA]
Milestone/Task: M5 GAMIFICATION / XP dan Leaderboard

#### Entri Farchan (UX+Backend)
Aktivitas: Stabilkan service progres 4 pilar.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilkan service progres 4 pilar untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Progress pilar tampil' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Stabilkan service progres 4 pilar.
- Outcome harian terukur: Progress pilar tampil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 862-875: kalkulasi XP lintas peserta dan pilar.
- `server/local_api.py` baris 987-1002: endpoint `/kampung` untuk leaderboard.
- `server/local_api.py` baris 1595: update poin user setelah verifikasi report.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi chart radar pilar FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi chart radar pilar FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Progress pilar tampil' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi chart radar pilar FE.
- Outcome harian terukur: Progress pilar tampil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 87-88: fetch leaderboard kampung.
- `src/app/components/UserDashboard.tsx` baris 278-292: rendering tabel leaderboard FE.
- `src/data/levelingSystem.ts` baris 145-223: logic level dan progress UI.

### Day 59 (Kamis, 16 Apr 2026): Rule akses leaderboard
Status: [RENCANA]
Milestone/Task: M5 GAMIFICATION / XP dan Leaderboard

#### Entri Farchan (UX+Backend)
Aktivitas: Atur aturan akses leaderboard.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Atur aturan akses leaderboard dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Akses leaderboard valid' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Atur aturan akses leaderboard.
- Outcome harian terukur: Akses leaderboard valid.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 862-875: kalkulasi XP lintas peserta dan pilar.
- `server/local_api.py` baris 987-1002: endpoint `/kampung` untuk leaderboard.
- `server/local_api.py` baris 1595: update poin user setelah verifikasi report.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement CTA login dan view all FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement CTA login dan view all FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Akses leaderboard valid' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement CTA login dan view all FE.
- Outcome harian terukur: Akses leaderboard valid.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 87-88: fetch leaderboard kampung.
- `src/app/components/UserDashboard.tsx` baris 278-292: rendering tabel leaderboard FE.
- `src/data/levelingSystem.ts` baris 145-223: logic level dan progress UI.

### Day 60 (Jumat, 17 Apr 2026): E2E report ke rank
Status: [RENCANA]
Milestone/Task: M5 GAMIFICATION / XP dan Leaderboard

#### Entri Farchan (UX+Backend)
Aktivitas: Uji E2E report ke XP ke leaderboard.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji E2E report ke XP ke leaderboard. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Leaderboard stabil' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Uji E2E report ke XP ke leaderboard.
- Outcome harian terukur: Leaderboard stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 862-875: kalkulasi XP lintas peserta dan pilar.
- `server/local_api.py` baris 987-1002: endpoint `/kampung` untuk leaderboard.
- `server/local_api.py` baris 1595: update poin user setelah verifikasi report.

#### Entri Ikram (UI+Frontend)
Aktivitas: Polish UI/FE leaderboard.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Polish UI/FE leaderboard dalam konteks 'E2E report ke rank'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M5 GAMIFICATION / XP dan Leaderboard. Hasil 'Leaderboard stabil' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Polish UI/FE leaderboard.
- Outcome harian terukur: Leaderboard stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/UserDashboard.tsx` baris 87-88: fetch leaderboard kampung.
- `src/app/components/UserDashboard.tsx` baris 278-292: rendering tabel leaderboard FE.
- `src/data/levelingSystem.ts` baris 145-223: logic level dan progress UI.

## PEKAN 13 (W13): Sertifikat dan Reward

Status Pekan: Proyeksi
Milestone Aktif: M6 REWARD dan MITRA
Task Utama: Certificate dan Reward

### Day 61 (Senin, 20 Apr 2026): Rule sertifikat
Status: [RENCANA]
Milestone/Task: M6 REWARD dan MITRA / Certificate dan Reward

#### Entri Farchan (UX+Backend)
Aktivitas: Definisikan rule 1 kegiatan 1 sertifikat.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Definisikan rule 1 kegiatan 1 sertifikat dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Rule sertifikat final' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Definisikan rule 1 kegiatan 1 sertifikat.
- Outcome harian terukur: Rule sertifikat final.
Lampiran Farchan (Bukti Screenshot):
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 147-148: rule 1 kegiatan 1 sertifikat.
- `server/local_api.py` baris 1595: mutasi poin sebagai basis reward.
- `server/local_api.py` baris 1637-1664: adjustment points/badges untuk skenario reward admin.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI riwayat sertifikat.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI riwayat sertifikat pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Rule sertifikat final' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement UI riwayat sertifikat.
- Outcome harian terukur: Rule sertifikat final.
Lampiran Ikram (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 187-230: validasi badge untuk reward context.
- `src/app/components/UserDashboard.tsx` baris 423: binding profil/riwayat untuk benefit user.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 34-70: acuan flow user untuk sertifikat dan progres.

### Day 62 (Selasa, 21 Apr 2026): Penerbitan sertifikat
Status: [RENCANA]
Milestone/Task: M6 REWARD dan MITRA / Certificate dan Reward

#### Entri Farchan (UX+Backend)
Aktivitas: Implement penerbitan sertifikat.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement penerbitan sertifikat pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Sertifikat dapat diakses' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement penerbitan sertifikat.
- Outcome harian terukur: Sertifikat dapat diakses.
Lampiran Farchan (Bukti Screenshot):
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 147-148: rule 1 kegiatan 1 sertifikat.
- `server/local_api.py` baris 1595: mutasi poin sebagai basis reward.
- `server/local_api.py` baris 1637-1664: adjustment points/badges untuk skenario reward admin.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi unduh sertifikat FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi unduh sertifikat FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Sertifikat dapat diakses' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi unduh sertifikat FE.
- Outcome harian terukur: Sertifikat dapat diakses.
Lampiran Ikram (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 187-230: validasi badge untuk reward context.
- `src/app/components/UserDashboard.tsx` baris 423: binding profil/riwayat untuk benefit user.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 34-70: acuan flow user untuk sertifikat dan progres.

### Day 63 (Rabu, 22 Apr 2026): Konversi poin voucher
Status: [RENCANA]
Milestone/Task: M6 REWARD dan MITRA / Certificate dan Reward

#### Entri Farchan (UX+Backend)
Aktivitas: Definisikan konversi poin ke voucher.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Definisikan konversi poin ke voucher dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Katalog reward aktif' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Definisikan konversi poin ke voucher.
- Outcome harian terukur: Katalog reward aktif.
Lampiran Farchan (Bukti Screenshot):
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 147-148: rule 1 kegiatan 1 sertifikat.
- `server/local_api.py` baris 1595: mutasi poin sebagai basis reward.
- `server/local_api.py` baris 1637-1664: adjustment points/badges untuk skenario reward admin.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI katalog reward.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI katalog reward pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Katalog reward aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement UI katalog reward.
- Outcome harian terukur: Katalog reward aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 187-230: validasi badge untuk reward context.
- `src/app/components/UserDashboard.tsx` baris 423: binding profil/riwayat untuk benefit user.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 34-70: acuan flow user untuk sertifikat dan progres.

### Day 64 (Kamis, 23 Apr 2026): Redeem poin
Status: [RENCANA]
Milestone/Task: M6 REWARD dan MITRA / Certificate dan Reward

#### Entri Farchan (UX+Backend)
Aktivitas: Implement redeem poin dan decrement saldo.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement redeem poin dan decrement saldo pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Redeem sinkron' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement redeem poin dan decrement saldo.
- Outcome harian terukur: Redeem sinkron.
Lampiran Farchan (Bukti Screenshot):
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 147-148: rule 1 kegiatan 1 sertifikat.
- `server/local_api.py` baris 1595: mutasi poin sebagai basis reward.
- `server/local_api.py` baris 1637-1664: adjustment points/badges untuk skenario reward admin.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi redeem flow FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi redeem flow FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Redeem sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi redeem flow FE.
- Outcome harian terukur: Redeem sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 187-230: validasi badge untuk reward context.
- `src/app/components/UserDashboard.tsx` baris 423: binding profil/riwayat untuk benefit user.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 34-70: acuan flow user untuk sertifikat dan progres.

### Day 65 (Jumat, 24 Apr 2026): Retest reward flow
Status: [RENCANA]
Milestone/Task: M6 REWARD dan MITRA / Certificate dan Reward

#### Entri Farchan (UX+Backend)
Aktivitas: Uji E2E sertifikat dan redeem.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji E2E sertifikat dan redeem. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Benefit relawan stabil' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Uji E2E sertifikat dan redeem.
- Outcome harian terukur: Benefit relawan stabil.
Lampiran Farchan (Bukti Screenshot):
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 147-148: rule 1 kegiatan 1 sertifikat.
- `server/local_api.py` baris 1595: mutasi poin sebagai basis reward.
- `server/local_api.py` baris 1637-1664: adjustment points/badges untuk skenario reward admin.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug reward UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug reward UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Benefit relawan stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Patch bug reward UI/FE.
- Outcome harian terukur: Benefit relawan stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/data/validatedBadges.ts` baris 187-230: validasi badge untuk reward context.
- `src/app/components/UserDashboard.tsx` baris 423: binding profil/riwayat untuk benefit user.
- `docs/guides/PETUNJUK_PENGGUNAAN.md` baris 34-70: acuan flow user untuk sertifikat dan progres.

## PEKAN 14 (W14): Kolaborasi Mitra

Status Pekan: Proyeksi
Milestone Aktif: M6 REWARD dan MITRA
Task Utama: Mitra External Flow

### Day 66 (Senin, 27 Apr 2026): Schema request mitra
Status: [RENCANA]
Milestone/Task: M6 REWARD dan MITRA / Mitra External Flow

#### Entri Farchan (UX+Backend)
Aktivitas: Definisikan schema request mitra dan scope.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Definisikan schema request mitra dan scope dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Form mitra aktif' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Definisikan schema request mitra dan scope.
- Outcome harian terukur: Form mitra aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1004-1014: fetch daftar collaboration request.
- `server/local_api.py` baris 1297-1336: submit dan approval collaboration request.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 110-118 dan 161-163: governance scope mitra.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement UI form mitra publik.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement UI form mitra publik pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Form mitra aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement UI form mitra publik.
- Outcome harian terukur: Form mitra aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 34-38: submit request mitra dari halaman publik.
- `src/app/components/ModeratorDashboard.tsx` baris 116-117: inbox request mitra pada FE moderator.
- `src/app/components/ModeratorDashboard.tsx` baris 316-317: approve/reject mitra dari FE.

### Day 67 (Selasa, 28 Apr 2026): Submit request mitra
Status: [RENCANA]
Milestone/Task: M6 REWARD dan MITRA / Mitra External Flow

#### Entri Farchan (UX+Backend)
Aktivitas: Implement endpoint submit mitra status pending.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement endpoint submit mitra status pending pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Submit mitra sukses' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement endpoint submit mitra status pending.
- Outcome harian terukur: Submit mitra sukses.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1004-1014: fetch daftar collaboration request.
- `server/local_api.py` baris 1297-1336: submit dan approval collaboration request.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 110-118 dan 161-163: governance scope mitra.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi submit request mitra FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi submit request mitra FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Submit mitra sukses' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi submit request mitra FE.
- Outcome harian terukur: Submit mitra sukses.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 34-38: submit request mitra dari halaman publik.
- `src/app/components/ModeratorDashboard.tsx` baris 116-117: inbox request mitra pada FE moderator.
- `src/app/components/ModeratorDashboard.tsx` baris 316-317: approve/reject mitra dari FE.

### Day 68 (Rabu, 29 Apr 2026): Routing request mitra
Status: [RENCANA]
Milestone/Task: M6 REWARD dan MITRA / Mitra External Flow

#### Entri Farchan (UX+Backend)
Aktivitas: Implement routing request by scope.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement routing request by scope pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Routing request sinkron' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement routing request by scope.
- Outcome harian terukur: Routing request sinkron.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1004-1014: fetch daftar collaboration request.
- `server/local_api.py` baris 1297-1336: submit dan approval collaboration request.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 110-118 dan 161-163: governance scope mitra.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi inbox review moderator FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi inbox review moderator FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Routing request sinkron' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi inbox review moderator FE.
- Outcome harian terukur: Routing request sinkron.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 34-38: submit request mitra dari halaman publik.
- `src/app/components/ModeratorDashboard.tsx` baris 116-117: inbox request mitra pada FE moderator.
- `src/app/components/ModeratorDashboard.tsx` baris 316-317: approve/reject mitra dari FE.

### Day 69 (Kamis, 30 Apr 2026): Approve reject mitra
Status: [RENCANA]
Milestone/Task: M6 REWARD dan MITRA / Mitra External Flow

#### Entri Farchan (UX+Backend)
Aktivitas: Implement approve reject request mitra.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement approve reject request mitra pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Review flow aktif' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement approve reject request mitra.
- Outcome harian terukur: Review flow aktif.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1004-1014: fetch daftar collaboration request.
- `server/local_api.py` baris 1297-1336: submit dan approval collaboration request.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 110-118 dan 161-163: governance scope mitra.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement aksi review mitra FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement aksi review mitra FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Review flow aktif' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement aksi review mitra FE.
- Outcome harian terukur: Review flow aktif.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 34-38: submit request mitra dari halaman publik.
- `src/app/components/ModeratorDashboard.tsx` baris 116-117: inbox request mitra pada FE moderator.
- `src/app/components/ModeratorDashboard.tsx` baris 316-317: approve/reject mitra dari FE.

### Day 70 (Jumat, 1 Mei 2026): E2E governance mitra
Status: [RENCANA]
Milestone/Task: M6 REWARD dan MITRA / Mitra External Flow

#### Entri Farchan (UX+Backend)
Aktivitas: Uji E2E submit sampai review mitra.
Uraian Kegiatan (Logbook):
"Aktivitas utama saya hari ini adalah Uji E2E submit sampai review mitra. Saya jalankan validasi dari skenario normal sampai edge case, terus saya cocokkan hasil aktual dengan acceptance criteria di milestone M6 REWARD dan MITRA / Mitra External Flow. Setelah itu saya catat poin koreksi dan konfirmasi final biar 'Governance mitra stabil' punya dasar teknis yang jelas."
Output Farchan:
- Artefak UX+Backend harian selesai: Uji E2E submit sampai review mitra.
- Outcome harian terukur: Governance mitra stabil.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1004-1014: fetch daftar collaboration request.
- `server/local_api.py` baris 1297-1336: submit dan approval collaboration request.
- `docs/architecture/GRAND_DESIGN_FINAL.md` baris 110-118 dan 161-163: governance scope mitra.

#### Entri Ikram (UI+Frontend)
Aktivitas: Patch bug mitra di UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Patch bug mitra di UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Governance mitra stabil' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Patch bug mitra di UI/FE.
- Outcome harian terukur: Governance mitra stabil.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/CollaborationPage.tsx` baris 34-38: submit request mitra dari halaman publik.
- `src/app/components/ModeratorDashboard.tsx` baris 116-117: inbox request mitra pada FE moderator.
- `src/app/components/ModeratorDashboard.tsx` baris 316-317: approve/reject mitra dari FE.

## PEKAN 15 (W15): Security Hardening

Status Pekan: Proyeksi
Milestone Aktif: M7 SECURITY dan INTEGRATION
Task Utama: Hardening Runtime

### Day 71 (Senin, 4 Mei 2026): Threat modeling
Status: [RENCANA]
Milestone/Task: M7 SECURITY dan INTEGRATION / Hardening Runtime

#### Entri Farchan (UX+Backend)
Aktivitas: Lakukan threat modeling dan checklist attack surface.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Lakukan threat modeling dan checklist attack surface pada konteks 'Threat modeling'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M7 SECURITY dan INTEGRATION / Hardening Runtime. Setelah selesai, saya pastikan 'Daftar risiko keamanan' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Lakukan threat modeling dan checklist attack surface.
- Outcome harian terukur: Daftar risiko keamanan.
Lampiran Farchan (Bukti Screenshot):
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: hardening env dan parameter keamanan.
- `server/local_api.py` baris 24-36 dan 99-108: env security, CORS allowlist, security headers.
- `server/local_api.py` baris 120: `rate_limited()` untuk throttle request mutasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Audit area UI/FE sensitif untuk produksi.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Audit area UI/FE sensitif untuk produksi. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M7 SECURITY dan INTEGRATION / Hardening Runtime. Setelah sinkronisasi final, 'Daftar risiko keamanan' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Audit area UI/FE sensitif untuk produksi.
- Outcome harian terukur: Daftar risiko keamanan.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 89 dan 124-151: unauthorized handling untuk keamanan sesi.
- `src/app/components/LoginPage.tsx` baris 30-44: state error auth saat hardening backend aktif.
- `src/app/App.tsx` baris 154-157: clear token/view saat logout untuk menutup celah session leak.

### Day 72 (Selasa, 5 Mei 2026): Hardening validasi input
Status: [RENCANA]
Milestone/Task: M7 SECURITY dan INTEGRATION / Hardening Runtime

#### Entri Farchan (UX+Backend)
Aktivitas: Perketat input validation backend.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Perketat input validation backend pada konteks 'Hardening validasi input'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M7 SECURITY dan INTEGRATION / Hardening Runtime. Setelah selesai, saya pastikan 'Validasi FE-BE konsisten' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Perketat input validation backend.
- Outcome harian terukur: Validasi FE-BE konsisten.
Lampiran Farchan (Bukti Screenshot):
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: hardening env dan parameter keamanan.
- `server/local_api.py` baris 24-36 dan 99-108: env security, CORS allowlist, security headers.
- `server/local_api.py` baris 120: `rate_limited()` untuk throttle request mutasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sinkron validasi input di FE.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Sinkron validasi input di FE. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M7 SECURITY dan INTEGRATION / Hardening Runtime. Setelah sinkronisasi final, 'Validasi FE-BE konsisten' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Sinkron validasi input di FE.
- Outcome harian terukur: Validasi FE-BE konsisten.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 89 dan 124-151: unauthorized handling untuk keamanan sesi.
- `src/app/components/LoginPage.tsx` baris 30-44: state error auth saat hardening backend aktif.
- `src/app/App.tsx` baris 154-157: clear token/view saat logout untuk menutup celah session leak.

### Day 73 (Rabu, 6 Mei 2026): Rate limit dan session policy
Status: [RENCANA]
Milestone/Task: M7 SECURITY dan INTEGRATION / Hardening Runtime

#### Entri Farchan (UX+Backend)
Aktivitas: Aktifkan rate limit dan session policy.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Aktifkan rate limit dan session policy pada konteks 'Rate limit dan session policy'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M7 SECURITY dan INTEGRATION / Hardening Runtime. Setelah selesai, saya pastikan 'Throttling flow aman' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Aktifkan rate limit dan session policy.
- Outcome harian terukur: Throttling flow aman.
Lampiran Farchan (Bukti Screenshot):
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: hardening env dan parameter keamanan.
- `server/local_api.py` baris 24-36 dan 99-108: env security, CORS allowlist, security headers.
- `server/local_api.py` baris 120: `rate_limited()` untuk throttle request mutasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement handling error 429 di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Implement handling error 429 di FE pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Throttling flow aman' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement handling error 429 di FE.
- Outcome harian terukur: Throttling flow aman.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 89 dan 124-151: unauthorized handling untuk keamanan sesi.
- `src/app/components/LoginPage.tsx` baris 30-44: state error auth saat hardening backend aktif.
- `src/app/App.tsx` baris 154-157: clear token/view saat logout untuk menutup celah session leak.

### Day 74 (Kamis, 7 Mei 2026): CORS dan security headers
Status: [RENCANA]
Milestone/Task: M7 SECURITY dan INTEGRATION / Hardening Runtime

#### Entri Farchan (UX+Backend)
Aktivitas: Konfigurasi CORS allowlist dan security headers.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Konfigurasi CORS allowlist dan security headers pada konteks 'CORS dan security headers'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M7 SECURITY dan INTEGRATION / Hardening Runtime. Setelah selesai, saya pastikan 'CORS security pass' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Konfigurasi CORS allowlist dan security headers.
- Outcome harian terukur: CORS security pass.
Lampiran Farchan (Bukti Screenshot):
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: hardening env dan parameter keamanan.
- `server/local_api.py` baris 24-36 dan 99-108: env security, CORS allowlist, security headers.
- `server/local_api.py` baris 120: `rate_limited()` untuk throttle request mutasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Uji perilaku FE pada mode production.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Uji perilaku FE pada mode production dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'CORS security pass' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: Uji perilaku FE pada mode production.
- Outcome harian terukur: CORS security pass.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 89 dan 124-151: unauthorized handling untuk keamanan sesi.
- `src/app/components/LoginPage.tsx` baris 30-44: state error auth saat hardening backend aktif.
- `src/app/App.tsx` baris 154-157: clear token/view saat logout untuk menutup celah session leak.

### Day 75 (Jumat, 8 Mei 2026): Security regression
Status: [RENCANA]
Milestone/Task: M7 SECURITY dan INTEGRATION / Hardening Runtime

#### Entri Farchan (UX+Backend)
Aktivitas: Jalankan security regression dan checklist publish.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Jalankan security regression dan checklist publish pada konteks 'Security regression'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M7 SECURITY dan INTEGRATION / Hardening Runtime. Setelah selesai, saya pastikan 'Baseline security siap' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Jalankan security regression dan checklist publish.
- Outcome harian terukur: Baseline security siap.
Lampiran Farchan (Bukti Screenshot):
- `docs/security/PRODUCTION_SECURITY_CHECKLIST.md` baris 5-17: hardening env dan parameter keamanan.
- `server/local_api.py` baris 24-36 dan 99-108: env security, CORS allowlist, security headers.
- `server/local_api.py` baris 120: `rate_limited()` untuk throttle request mutasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Regression FE pasca hardening.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Regression FE pasca hardening untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Baseline security siap' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Regression FE pasca hardening.
- Outcome harian terukur: Baseline security siap.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/ModeratorDashboard.tsx` baris 89 dan 124-151: unauthorized handling untuk keamanan sesi.
- `src/app/components/LoginPage.tsx` baris 30-44: state error auth saat hardening backend aktif.
- `src/app/App.tsx` baris 154-157: clear token/view saat logout untuk menutup celah session leak.

## PEKAN 16 (W16): Integrasi Total

Status Pekan: Proyeksi
Milestone Aktif: M7 SECURITY dan INTEGRATION
Task Utama: Integrasi dan Demo

### Day 76 (Senin, 11 Mei 2026): Integrasi lintas modul round 1
Status: [RENCANA]
Milestone/Task: M7 SECURITY dan INTEGRATION / Integrasi dan Demo

#### Entri Farchan (UX+Backend)
Aktivitas: Integrasi modul lintas domain round 1.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi modul lintas domain round 1 pada jalur UX+Backend. Saya pecah dulu task ke bagian inti, lanjut eksekusi logika proses dan kontrak datanya, lalu saya cek dampaknya ke endpoint/flow yang terkait supaya tidak ada regresi. Setelah pengujian lokal, output 'Integrasi lintas modul' saya kunci sebagai baseline kerja hari berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Integrasi modul lintas domain round 1.
- Outcome harian terukur: Integrasi lintas modul.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 19-29: startup local API untuk integrasi penuh.
- `DEMO_ACCOUNTS.md` baris 8-26: akun uji role-based untuk rehearsal.
- `server/local_api.py` baris 1211-1620: endpoint inti auth-event-report-admin untuk demo end-to-end.

#### Entri Ikram (UI+Frontend)
Aktivitas: Integrasi UI+FE round 1.
Uraian Kegiatan (Logbook):
"Hari ini saya implement Integrasi UI+FE round 1 pada sisi UI+Frontend. Saya kerjain dari slicing komponen, wiring state, sampai integrasi request-response ke API biar alurnya nyambung end-to-end. Setelah smoke test di role terkait, hasil 'Integrasi lintas modul' saya pastikan stabil untuk dipakai lanjut di task berikutnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Integrasi UI+FE round 1.
- Outcome harian terukur: Integrasi lintas modul.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 182-190: switch context role/view saat integrasi demo.
- `src/app/components/UserDashboard.tsx` baris 47-112: alur user end-to-end integrasi FE-BE.
- `src/app/components/ModeratorDashboard.tsx` baris 223-317: alur moderator end-to-end integrasi FE-BE.

### Day 77 (Selasa, 12 Mei 2026): Skenario demo role
Status: [RENCANA]
Milestone/Task: M7 SECURITY dan INTEGRATION / Integrasi dan Demo

#### Entri Farchan (UX+Backend)
Aktivitas: Susun skenario demo per role.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun skenario demo per role dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Script demo v1' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Susun skenario demo per role.
- Outcome harian terukur: Script demo v1.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 19-29: startup local API untuk integrasi penuh.
- `DEMO_ACCOUNTS.md` baris 8-26: akun uji role-based untuk rehearsal.
- `server/local_api.py` baris 1211-1620: endpoint inti auth-event-report-admin untuk demo end-to-end.

#### Entri Ikram (UI+Frontend)
Aktivitas: Siapkan alur demo di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Siapkan alur demo di FE dalam konteks 'Skenario demo role'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M7 SECURITY dan INTEGRATION / Integrasi dan Demo. Hasil 'Script demo v1' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Siapkan alur demo di FE.
- Outcome harian terukur: Script demo v1.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 182-190: switch context role/view saat integrasi demo.
- `src/app/components/UserDashboard.tsx` baris 47-112: alur user end-to-end integrasi FE-BE.
- `src/app/components/ModeratorDashboard.tsx` baris 223-317: alur moderator end-to-end integrasi FE-BE.

### Day 78 (Rabu, 13 Mei 2026): Seed data demo
Status: [RENCANA]
Milestone/Task: M7 SECURITY dan INTEGRATION / Integrasi dan Demo

#### Entri Farchan (UX+Backend)
Aktivitas: Siapkan seed data demo realistis.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Siapkan seed data demo realistis pada konteks 'Seed data demo'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M7 SECURITY dan INTEGRATION / Integrasi dan Demo. Setelah selesai, saya pastikan 'Demo data siap' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Siapkan seed data demo realistis.
- Outcome harian terukur: Demo data siap.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 19-29: startup local API untuk integrasi penuh.
- `DEMO_ACCOUNTS.md` baris 8-26: akun uji role-based untuk rehearsal.
- `server/local_api.py` baris 1211-1620: endpoint inti auth-event-report-admin untuk demo end-to-end.

#### Entri Ikram (UI+Frontend)
Aktivitas: Sinkron tampilan FE dengan seed data.
Uraian Kegiatan (Logbook):
"Aktivitas hari ini saya adalah Sinkron tampilan FE dengan seed data. Saya validasi tampilan, transisi state, dan respons error/loading supaya behavior FE tidak beda dengan aturan backend di milestone M7 SECURITY dan INTEGRATION / Integrasi dan Demo. Setelah sinkronisasi final, 'Demo data siap' saya pastikan sudah jelas dan bisa ditracking hasilnya."
Output Ikram:
- Artefak UI+Frontend harian selesai: Sinkron tampilan FE dengan seed data.
- Outcome harian terukur: Demo data siap.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 182-190: switch context role/view saat integrasi demo.
- `src/app/components/UserDashboard.tsx` baris 47-112: alur user end-to-end integrasi FE-BE.
- `src/app/components/ModeratorDashboard.tsx` baris 223-317: alur moderator end-to-end integrasi FE-BE.

### Day 79 (Kamis, 14 Mei 2026): Dry run UAT internal
Status: [RENCANA]
Milestone/Task: M7 SECURITY dan INTEGRATION / Integrasi dan Demo

#### Entri Farchan (UX+Backend)
Aktivitas: Lakukan dry run UAT internal.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Lakukan dry run UAT internal. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'UAT dry-run notes' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Lakukan dry run UAT internal.
- Outcome harian terukur: UAT dry-run notes.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 19-29: startup local API untuk integrasi penuh.
- `DEMO_ACCOUNTS.md` baris 8-26: akun uji role-based untuk rehearsal.
- `server/local_api.py` baris 1211-1620: endpoint inti auth-event-report-admin untuk demo end-to-end.

#### Entri Ikram (UI+Frontend)
Aktivitas: Polish UI/FE untuk demo.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Polish UI/FE untuk demo dalam konteks 'Dry run UAT internal'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M7 SECURITY dan INTEGRATION / Integrasi dan Demo. Hasil 'UAT dry-run notes' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Polish UI/FE untuk demo.
- Outcome harian terukur: UAT dry-run notes.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 182-190: switch context role/view saat integrasi demo.
- `src/app/components/UserDashboard.tsx` baris 47-112: alur user end-to-end integrasi FE-BE.
- `src/app/components/ModeratorDashboard.tsx` baris 223-317: alur moderator end-to-end integrasi FE-BE.

### Day 80 (Jumat, 15 Mei 2026): Freeze candidate build
Status: [RENCANA]
Milestone/Task: M7 SECURITY dan INTEGRATION / Integrasi dan Demo

#### Entri Farchan (UX+Backend)
Aktivitas: Freeze candidate build backend.
Uraian Kegiatan (Logbook):
"Hari ini fokus saya di 'Freeze candidate build' adalah Freeze candidate build backend. Saya mulai dengan ngerapihin backlog dan dependency backend biar batas kerja sprint jelas, lalu mengunci keputusan teknis yang paling ngaruh ke alur lanjutan. Sebelum close, saya validasi lagi keputusan yang diambil supaya output hari ini 'Candidate build' bisa langsung dipakai tim tanpa ambigu."
Output Farchan:
- Artefak UX+Backend harian selesai: Freeze candidate build backend.
- Outcome harian terukur: Candidate build.
Lampiran Farchan (Bukti Screenshot):
- `scripts/dev-local.mjs` baris 19-29: startup local API untuk integrasi penuh.
- `DEMO_ACCOUNTS.md` baris 8-26: akun uji role-based untuk rehearsal.
- `server/local_api.py` baris 1211-1620: endpoint inti auth-event-report-admin untuk demo end-to-end.

#### Entri Ikram (UI+Frontend)
Aktivitas: Final FE polish candidate.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Final FE polish candidate sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Candidate build' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Final FE polish candidate.
- Outcome harian terukur: Candidate build.
Lampiran Ikram (Bukti Screenshot):
- `src/app/App.tsx` baris 182-190: switch context role/view saat integrasi demo.
- `src/app/components/UserDashboard.tsx` baris 47-112: alur user end-to-end integrasi FE-BE.
- `src/app/components/ModeratorDashboard.tsx` baris 223-317: alur moderator end-to-end integrasi FE-BE.

## PEKAN 17 (W17): QA Execution

Status Pekan: Proyeksi
Milestone Aktif: M8 QA dan BUGFIX
Task Utama: Testing dan Triage

### Day 81 (Senin, 18 Mei 2026): Finalisasi test case
Status: [RENCANA]
Milestone/Task: M8 QA dan BUGFIX / Testing dan Triage

#### Entri Farchan (UX+Backend)
Aktivitas: Finalisasi test case backend.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalisasi test case backend sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Test plan final' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Finalisasi test case backend.
- Outcome harian terukur: Test plan final.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue yang diuji pada fase QA.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas fix dan triage status.
- `docs/status/SYSTEM_SUMMARY.md` baris 237-244 dan 253-262: checklist uji fungsional inti.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalisasi test case UI/FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalisasi test case UI/FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Test plan final' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Finalisasi test case UI/FE.
- Outcome harian terukur: Test plan final.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 70-131: area uji QA admin flow.
- `src/app/components/ModeratorDashboard.tsx` baris 223-285: area uji QA moderator flow.
- `src/app/components/UserDashboard.tsx` baris 47-112: area uji QA user flow.

### Day 82 (Selasa, 19 Mei 2026): Eksekusi test domain inti
Status: [RENCANA]
Milestone/Task: M8 QA dan BUGFIX / Testing dan Triage

#### Entri Farchan (UX+Backend)
Aktivitas: Eksekusi test auth event report.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Eksekusi test auth event report. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Laporan uji harian' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Eksekusi test auth event report.
- Outcome harian terukur: Laporan uji harian.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue yang diuji pada fase QA.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas fix dan triage status.
- `docs/status/SYSTEM_SUMMARY.md` baris 237-244 dan 253-262: checklist uji fungsional inti.

#### Entri Ikram (UI+Frontend)
Aktivitas: QA responsive dan flow FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke QA responsive dan flow FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Laporan uji harian' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: QA responsive dan flow FE.
- Outcome harian terukur: Laporan uji harian.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 70-131: area uji QA admin flow.
- `src/app/components/ModeratorDashboard.tsx` baris 223-285: area uji QA moderator flow.
- `src/app/components/UserDashboard.tsx` baris 47-112: area uji QA user flow.

### Day 83 (Rabu, 20 Mei 2026): Eksekusi test domain lanjutan
Status: [RENCANA]
Milestone/Task: M8 QA dan BUGFIX / Testing dan Triage

#### Entri Farchan (UX+Backend)
Aktivitas: Eksekusi test verify reward mitra.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Eksekusi test verify reward mitra. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Defect list update' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Eksekusi test verify reward mitra.
- Outcome harian terukur: Defect list update.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue yang diuji pada fase QA.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas fix dan triage status.
- `docs/status/SYSTEM_SUMMARY.md` baris 237-244 dan 253-262: checklist uji fungsional inti.

#### Entri Ikram (UI+Frontend)
Aktivitas: QA usability dan edge-case FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke QA usability dan edge-case FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Defect list update' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: QA usability dan edge-case FE.
- Outcome harian terukur: Defect list update.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 70-131: area uji QA admin flow.
- `src/app/components/ModeratorDashboard.tsx` baris 223-285: area uji QA moderator flow.
- `src/app/components/UserDashboard.tsx` baris 47-112: area uji QA user flow.

### Day 84 (Kamis, 21 Mei 2026): Triage defect
Status: [RENCANA]
Milestone/Task: M8 QA dan BUGFIX / Testing dan Triage

#### Entri Farchan (UX+Backend)
Aktivitas: Triage defect berdasarkan severity dan owner.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Triage defect berdasarkan severity dan owner pada konteks 'Triage defect'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M8 QA dan BUGFIX / Testing dan Triage. Setelah selesai, saya pastikan 'Bugboard terurut' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Triage defect berdasarkan severity dan owner.
- Outcome harian terukur: Bugboard terurut.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue yang diuji pada fase QA.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas fix dan triage status.
- `docs/status/SYSTEM_SUMMARY.md` baris 237-244 dan 253-262: checklist uji fungsional inti.

#### Entri Ikram (UI+Frontend)
Aktivitas: Reproduksi bug dan kumpulkan evidence FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Reproduksi bug dan kumpulkan evidence FE dalam konteks 'Triage defect'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M8 QA dan BUGFIX / Testing dan Triage. Hasil 'Bugboard terurut' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Reproduksi bug dan kumpulkan evidence FE.
- Outcome harian terukur: Bugboard terurut.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 70-131: area uji QA admin flow.
- `src/app/components/ModeratorDashboard.tsx` baris 223-285: area uji QA moderator flow.
- `src/app/components/UserDashboard.tsx` baris 47-112: area uji QA user flow.

### Day 85 (Jumat, 22 Mei 2026): Patch plan W18
Status: [RENCANA]
Milestone/Task: M8 QA dan BUGFIX / Testing dan Triage

#### Entri Farchan (UX+Backend)
Aktivitas: Susun patch plan untuk W18.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun patch plan untuk W18 dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Rencana patch final' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Susun patch plan untuk W18.
- Outcome harian terukur: Rencana patch final.
Lampiran Farchan (Bukti Screenshot):
- `docs/status/IMPLEMENTATION_STATUS.md` baris 43-92: daftar issue yang diuji pada fase QA.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: prioritas fix dan triage status.
- `docs/status/SYSTEM_SUMMARY.md` baris 237-244 dan 253-262: checklist uji fungsional inti.

#### Entri Ikram (UI+Frontend)
Aktivitas: Susun patch plan UI/FE untuk W18.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun patch plan UI/FE untuk W18 dengan nentuin struktur UI, prioritas aksi pengguna, dan kebutuhan data tiap layar. Saya pastikan keputusan desainnya tetap implementable di FE, bukan berhenti di visual saja. Output 'Rencana patch final' saya susun biar tim bisa lanjut kerja dengan acuan yang konkret."
Output Ikram:
- Artefak UI+Frontend harian selesai: Susun patch plan UI/FE untuk W18.
- Outcome harian terukur: Rencana patch final.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/AdminDashboard.tsx` baris 70-131: area uji QA admin flow.
- `src/app/components/ModeratorDashboard.tsx` baris 223-285: area uji QA moderator flow.
- `src/app/components/UserDashboard.tsx` baris 47-112: area uji QA user flow.

## PEKAN 18 (W18): Bug Fixing

Status Pekan: Proyeksi
Milestone Aktif: M8 QA dan BUGFIX
Task Utama: Patch dan Stabilization

### Day 86 (Senin, 25 Mei 2026): Fix high severity
Status: [RENCANA]
Milestone/Task: M8 QA dan BUGFIX / Patch dan Stabilization

#### Entri Farchan (UX+Backend)
Aktivitas: Fix bug high severity backend.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug high severity backend untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Patch high severity' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Fix bug high severity backend.
- Outcome harian terukur: Patch high severity.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1202-1694: area route mutasi untuk patch dan stabilisasi.
- `server/local_api.py` baris 1358-1620: domain event-report-admin yang paling sering dipatch.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: update status defect pasca patch.

#### Entri Ikram (UI+Frontend)
Aktivitas: Fix bug high severity UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug high severity UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Patch high severity' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Fix bug high severity UI/FE.
- Outcome harian terukur: Patch high severity.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: retest join flow setelah patch.
- `src/app/components/ReportingWizard.tsx` baris 92-98: retest submit laporan setelah patch.
- `src/app/components/AdminGodMode.tsx` baris 111-144: retest role assignment setelah patch.

### Day 87 (Selasa, 26 Mei 2026): Fix medium batch 1
Status: [RENCANA]
Milestone/Task: M8 QA dan BUGFIX / Patch dan Stabilization

#### Entri Farchan (UX+Backend)
Aktivitas: Fix bug medium batch 1 backend.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug medium batch 1 backend untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Patch medium batch 1' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Fix bug medium batch 1 backend.
- Outcome harian terukur: Patch medium batch 1.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1202-1694: area route mutasi untuk patch dan stabilisasi.
- `server/local_api.py` baris 1358-1620: domain event-report-admin yang paling sering dipatch.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: update status defect pasca patch.

#### Entri Ikram (UI+Frontend)
Aktivitas: Fix bug medium batch 1 UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix bug medium batch 1 UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Patch medium batch 1' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Fix bug medium batch 1 UI/FE.
- Outcome harian terukur: Patch medium batch 1.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: retest join flow setelah patch.
- `src/app/components/ReportingWizard.tsx` baris 92-98: retest submit laporan setelah patch.
- `src/app/components/AdminGodMode.tsx` baris 111-144: retest role assignment setelah patch.

### Day 88 (Rabu, 27 Mei 2026): Retest patch
Status: [RENCANA]
Milestone/Task: M8 QA dan BUGFIX / Patch dan Stabilization

#### Entri Farchan (UX+Backend)
Aktivitas: Retest patch backend.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest patch backend. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Retest report' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Retest patch backend.
- Outcome harian terukur: Retest report.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1202-1694: area route mutasi untuk patch dan stabilisasi.
- `server/local_api.py` baris 1358-1620: domain event-report-admin yang paling sering dipatch.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: update status defect pasca patch.

#### Entri Ikram (UI+Frontend)
Aktivitas: Retest patch FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Retest patch FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Retest report' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: Retest patch FE.
- Outcome harian terukur: Retest report.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: retest join flow setelah patch.
- `src/app/components/ReportingWizard.tsx` baris 92-98: retest submit laporan setelah patch.
- `src/app/components/AdminGodMode.tsx` baris 111-144: retest role assignment setelah patch.

### Day 89 (Kamis, 28 Mei 2026): Fix critical path sisa
Status: [RENCANA]
Milestone/Task: M8 QA dan BUGFIX / Patch dan Stabilization

#### Entri Farchan (UX+Backend)
Aktivitas: Fix sisa bug critical path backend.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix sisa bug critical path backend untuk nambah kestabilan backend. Saya beresin area yang rawan gagal, rapihin validasi dan perilaku error, lalu verifikasi ulang jalur kritis supaya perubahan tidak ngebuka masalah baru. Dengan itu, 'Patch critical closed' bisa dipakai sebagai pondasi yang lebih aman untuk fase berikutnya."
Output Farchan:
- Artefak UX+Backend harian selesai: Fix sisa bug critical path backend.
- Outcome harian terukur: Patch critical closed.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1202-1694: area route mutasi untuk patch dan stabilisasi.
- `server/local_api.py` baris 1358-1620: domain event-report-admin yang paling sering dipatch.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: update status defect pasca patch.

#### Entri Ikram (UI+Frontend)
Aktivitas: Fix sisa bug critical path UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Fix sisa bug critical path UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Patch critical closed' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Fix sisa bug critical path UI/FE.
- Outcome harian terukur: Patch critical closed.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: retest join flow setelah patch.
- `src/app/components/ReportingWizard.tsx` baris 92-98: retest submit laporan setelah patch.
- `src/app/components/AdminGodMode.tsx` baris 111-144: retest role assignment setelah patch.

### Day 90 (Jumat, 29 Mei 2026): Stabilization build
Status: [RENCANA]
Milestone/Task: M8 QA dan BUGFIX / Patch dan Stabilization

#### Entri Farchan (UX+Backend)
Aktivitas: Susun stabilization build backend.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun stabilization build backend dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Stabilization build final' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Susun stabilization build backend.
- Outcome harian terukur: Stabilization build final.
Lampiran Farchan (Bukti Screenshot):
- `server/local_api.py` baris 1202-1694: area route mutasi untuk patch dan stabilisasi.
- `server/local_api.py` baris 1358-1620: domain event-report-admin yang paling sering dipatch.
- `docs/status/IMPLEMENTATION_STATUS.md` baris 107-123: update status defect pasca patch.

#### Entri Ikram (UI+Frontend)
Aktivitas: Stabilization pass UI/FE.
Uraian Kegiatan (Logbook):
"Fokus saya hari ini adalah Stabilization pass UI/FE untuk nguatin sisi frontend. Saya rapihin error handling, behavior responsif, dan konsistensi state pada flow yang paling sering dipakai. Setelah retest cepat, 'Stabilization build final' saya konfirmasi supaya siap dipakai di tahap penutupan sprint."
Output Ikram:
- Artefak UI+Frontend harian selesai: Stabilization pass UI/FE.
- Outcome harian terukur: Stabilization build final.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/EventList.tsx` baris 42-43: retest join flow setelah patch.
- `src/app/components/ReportingWizard.tsx` baris 92-98: retest submit laporan setelah patch.
- `src/app/components/AdminGodMode.tsx` baris 111-144: retest role assignment setelah patch.

## PEKAN 19 (W19): Dokumen dan Pitch

Status Pekan: Proyeksi
Milestone Aktif: M9 FINAL
Task Utama: Finalisasi Dokumen Sidang

### Day 91 (Senin, 1 Jun 2026): Update dokumen final
Status: [RENCANA]
Milestone/Task: M9 FINAL / Finalisasi Dokumen Sidang

#### Entri Farchan (UX+Backend)
Aktivitas: Update grand design final berbasis implementasi.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Update grand design final berbasis implementasi sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Dokumen + visual final' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Update grand design final berbasis implementasi.
- Outcome harian terukur: Dokumen + visual final.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 19-26: peta dokumentasi final proyek.
- `docs/README.md` baris 5-16: indeks dokumen untuk paket sidang.
- `docs/logbook/logbook.md` baris 350-418, 686-754, 1526-1594: baseline progres implementasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Siapkan capture UI dan flow final.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Siapkan capture UI dan flow final sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Dokumen + visual final' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Siapkan capture UI dan flow final.
- Outcome harian terukur: Dokumen + visual final.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LandingPage.tsx` baris 20-30 dan 75-108: capture final landing flow.
- `src/app/components/CollaborationPage.tsx` baris 58-74 dan 104-168: capture final flow mitra.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 166-206: acuan visual alur untuk deck final.

### Day 92 (Selasa, 2 Jun 2026): Finalisasi logbook bukti
Status: [RENCANA]
Milestone/Task: M9 FINAL / Finalisasi Dokumen Sidang

#### Entri Farchan (UX+Backend)
Aktivitas: Finalisasi logbook dan bukti teknis.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalisasi logbook dan bukti teknis sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Arsip bukti siap' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Finalisasi logbook dan bukti teknis.
- Outcome harian terukur: Arsip bukti siap.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 19-26: peta dokumentasi final proyek.
- `docs/README.md` baris 5-16: indeks dokumen untuk paket sidang.
- `docs/logbook/logbook.md` baris 350-418, 686-754, 1526-1594: baseline progres implementasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Rapikan file desain dan aset FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Rapikan file desain dan aset FE dalam konteks 'Finalisasi logbook bukti'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M9 FINAL / Finalisasi Dokumen Sidang. Hasil 'Arsip bukti siap' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Rapikan file desain dan aset FE.
- Outcome harian terukur: Arsip bukti siap.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LandingPage.tsx` baris 20-30 dan 75-108: capture final landing flow.
- `src/app/components/CollaborationPage.tsx` baris 58-74 dan 104-168: capture final flow mitra.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 166-206: acuan visual alur untuk deck final.

### Day 93 (Rabu, 3 Jun 2026): Finalisasi narasi presentasi
Status: [RENCANA]
Milestone/Task: M9 FINAL / Finalisasi Dokumen Sidang

#### Entri Farchan (UX+Backend)
Aktivitas: Finalisasi narasi presentasi dan script.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Finalisasi narasi presentasi dan script sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Draft deck final' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Finalisasi narasi presentasi dan script.
- Outcome harian terukur: Draft deck final.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 19-26: peta dokumentasi final proyek.
- `docs/README.md` baris 5-16: indeks dokumen untuk paket sidang.
- `docs/logbook/logbook.md` baris 350-418, 686-754, 1526-1594: baseline progres implementasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Siapkan visual slide dan video demo FE.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Siapkan visual slide dan video demo FE dalam konteks 'Finalisasi narasi presentasi'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M9 FINAL / Finalisasi Dokumen Sidang. Hasil 'Draft deck final' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Siapkan visual slide dan video demo FE.
- Outcome harian terukur: Draft deck final.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LandingPage.tsx` baris 20-30 dan 75-108: capture final landing flow.
- `src/app/components/CollaborationPage.tsx` baris 58-74 dan 104-168: capture final flow mitra.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 166-206: acuan visual alur untuk deck final.

### Day 94 (Kamis, 4 Jun 2026): Rehearsal presentasi
Status: [RENCANA]
Milestone/Task: M9 FINAL / Finalisasi Dokumen Sidang

#### Entri Farchan (UX+Backend)
Aktivitas: Rehearsal presentasi dan QnA bank.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Rehearsal presentasi dan QnA bank. Pengujian saya lakukan end-to-end pada alur yang kena dampak, termasuk cek transisi status dan integritas data setelah aksi utama dijalankan. Dari hasil uji itu saya rangkum temuan dan konfirmasi stabilitas supaya 'Rehearsal notes' valid secara operasional."
Output Farchan:
- Artefak UX+Backend harian selesai: Rehearsal presentasi dan QnA bank.
- Outcome harian terukur: Rehearsal notes.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 19-26: peta dokumentasi final proyek.
- `docs/README.md` baris 5-16: indeks dokumen untuk paket sidang.
- `docs/logbook/logbook.md` baris 350-418, 686-754, 1526-1594: baseline progres implementasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Rehearsal flow demo di FE.
Uraian Kegiatan (Logbook):
"Hari ini saya fokus ke Rehearsal flow demo di FE dari perspektif pengguna. Saya uji skenario sukses dan gagal, cek konsistensi interaksi lintas role/perangkat, lalu dokumentasikan temuan yang perlu patch. Dengan langkah itu, 'Rehearsal notes' jadi lebih kuat untuk dipakai di fase stabilisasi."
Output Ikram:
- Artefak UI+Frontend harian selesai: Rehearsal flow demo di FE.
- Outcome harian terukur: Rehearsal notes.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LandingPage.tsx` baris 20-30 dan 75-108: capture final landing flow.
- `src/app/components/CollaborationPage.tsx` baris 58-74 dan 104-168: capture final flow mitra.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 166-206: acuan visual alur untuk deck final.

### Day 95 (Jumat, 5 Jun 2026): Revisi paket sidang
Status: [RENCANA]
Milestone/Task: M9 FINAL / Finalisasi Dokumen Sidang

#### Entri Farchan (UX+Backend)
Aktivitas: Revisi final dokumen KP.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Revisi final dokumen KP sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Paket sidang siap' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Revisi final dokumen KP.
- Outcome harian terukur: Paket sidang siap.
Lampiran Farchan (Bukti Screenshot):
- `README.md` baris 19-26: peta dokumentasi final proyek.
- `docs/README.md` baris 5-16: indeks dokumen untuk paket sidang.
- `docs/logbook/logbook.md` baris 350-418, 686-754, 1526-1594: baseline progres implementasi.

#### Entri Ikram (UI+Frontend)
Aktivitas: Revisi final visual dan flow FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Revisi final visual dan flow FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Paket sidang siap' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Revisi final visual dan flow FE.
- Outcome harian terukur: Paket sidang siap.
Lampiran Ikram (Bukti Screenshot):
- `src/app/components/LandingPage.tsx` baris 20-30 dan 75-108: capture final landing flow.
- `src/app/components/CollaborationPage.tsx` baris 58-74 dan 104-168: capture final flow mitra.
- `docs/architecture/SITEMAP_IA_SIMRP.md` baris 166-206: acuan visual alur untuk deck final.

## PEKAN 20 (W20): UAT Final dan Closing

Status Pekan: Proyeksi
Milestone Aktif: M9 FINAL
Task Utama: Closing dan Handover

### Day 96 (Senin, 8 Jun 2026): UAT final mentor
Status: [RENCANA]
Milestone/Task: M9 FINAL / Closing dan Handover

#### Entri Farchan (UX+Backend)
Aktivitas: UAT final dengan mentor dan checklist.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain UAT final dengan mentor dan checklist sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'UAT checklist' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: UAT final dengan mentor dan checklist.
- Outcome harian terukur: UAT checklist.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/logbook.md` baris 1526-1594: referensi kegiatan penutupan Day 96-100.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 52-59: kontrol sinkron akhir tim dua orang.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63 dan 84-87: target akhir dan sign-off.

#### Entri Ikram (UI+Frontend)
Aktivitas: Catat feedback UI/FE final.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Catat feedback UI/FE final sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'UAT checklist' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Catat feedback UI/FE final.
- Outcome harian terukur: UAT checklist.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/LOGBOOK_HARIAN_W06_W20_DUAL_ROLE.md` (line N/A): update status harian ke `[TERLAKSANA]` saat closing.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63: acuan output UAT/closing per pekan.
- `src/app/App.tsx` baris 216-279: bukti routing final lintas halaman saat sign-off.

### Day 97 (Selasa, 9 Jun 2026): Patch minor final
Status: [RENCANA]
Milestone/Task: M9 FINAL / Closing dan Handover

#### Entri Farchan (UX+Backend)
Aktivitas: Implement perubahan minor final backend.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Implement perubahan minor final backend sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Minor patch complete' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Implement perubahan minor final backend.
- Outcome harian terukur: Minor patch complete.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/logbook.md` baris 1526-1594: referensi kegiatan penutupan Day 96-100.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 52-59: kontrol sinkron akhir tim dua orang.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63 dan 84-87: target akhir dan sign-off.

#### Entri Ikram (UI+Frontend)
Aktivitas: Implement patch minor final UI/FE.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Implement patch minor final UI/FE sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Minor patch complete' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Implement patch minor final UI/FE.
- Outcome harian terukur: Minor patch complete.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/LOGBOOK_HARIAN_W06_W20_DUAL_ROLE.md` (line N/A): update status harian ke `[TERLAKSANA]` saat closing.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63: acuan output UAT/closing per pekan.
- `src/app/App.tsx` baris 216-279: bukti routing final lintas halaman saat sign-off.

### Day 98 (Rabu, 10 Jun 2026): Readiness final
Status: [RENCANA]
Milestone/Task: M9 FINAL / Closing dan Handover

#### Entri Farchan (UX+Backend)
Aktivitas: Final readiness note operasional.
Uraian Kegiatan (Logbook):
"Di hari ini saya ngerjain Final readiness note operasional sampai tuntas. Prosesnya saya pakai untuk nutup detail yang masih gantung, nyamain aturan bisnis dengan kebutuhan modul aktif, dan ngecek konsistensi data biar tidak bentrok di integrasi berikutnya. Hasil akhir saya pastikan sudah rapi dan terdokumentasi supaya 'Readiness note' benar-benar siap dipakai."
Output Farchan:
- Artefak UX+Backend harian selesai: Final readiness note operasional.
- Outcome harian terukur: Readiness note.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/logbook.md` baris 1526-1594: referensi kegiatan penutupan Day 96-100.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 52-59: kontrol sinkron akhir tim dua orang.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63 dan 84-87: target akhir dan sign-off.

#### Entri Ikram (UI+Frontend)
Aktivitas: Finalisasi handoff UI/FE note.
Uraian Kegiatan (Logbook):
"Di hari ini fokus saya adalah Finalisasi handoff UI/FE note sampai selesai rapi. Saya benahin detail komponen, konsistensi state, dan perilaku antarmuka supaya sesuai sama kontrak API yang dipakai tim. Sebelum close, saya cek ulang alur dari sisi user agar 'Readiness note' benar-benar siap dipakai tanpa banyak rework."
Output Ikram:
- Artefak UI+Frontend harian selesai: Finalisasi handoff UI/FE note.
- Outcome harian terukur: Readiness note.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/LOGBOOK_HARIAN_W06_W20_DUAL_ROLE.md` (line N/A): update status harian ke `[TERLAKSANA]` saat closing.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63: acuan output UAT/closing per pekan.
- `src/app/App.tsx` baris 216-279: bukti routing final lintas halaman saat sign-off.

### Day 99 (Kamis, 11 Jun 2026): Closing report dan handover
Status: [RENCANA]
Milestone/Task: M9 FINAL / Closing dan Handover

#### Entri Farchan (UX+Backend)
Aktivitas: Susun closing report dan handover teknis.
Uraian Kegiatan (Logbook):
"Untuk hari ini saya ngerjain Susun closing report dan handover teknis dengan pendekatan perumusan teknis. Saya tetapkan aturan, batasan, dan indikator selesai yang bisa diuji, lalu saya sinkronkan dengan prioritas sprint biar eksekusi tim tetap sejalur. Output 'Closing package' saya susun supaya jadi acuan kerja harian yang konkret, bukan cuma catatan umum."
Output Farchan:
- Artefak UX+Backend harian selesai: Susun closing report dan handover teknis.
- Outcome harian terukur: Closing package.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/logbook.md` baris 1526-1594: referensi kegiatan penutupan Day 96-100.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 52-59: kontrol sinkron akhir tim dua orang.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63 dan 84-87: target akhir dan sign-off.

#### Entri Ikram (UI+Frontend)
Aktivitas: Arsip source UI/FE dan dokumentasi.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Arsip source UI/FE dan dokumentasi dalam konteks 'Closing report dan handover'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M9 FINAL / Closing dan Handover. Hasil 'Closing package' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Arsip source UI/FE dan dokumentasi.
- Outcome harian terukur: Closing package.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/LOGBOOK_HARIAN_W06_W20_DUAL_ROLE.md` (line N/A): update status harian ke `[TERLAKSANA]` saat closing.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63: acuan output UAT/closing per pekan.
- `src/app/App.tsx` baris 216-279: bukti routing final lintas halaman saat sign-off.

### Day 100 (Jumat, 12 Jun 2026): Presentasi akhir dan retrospektif
Status: [RENCANA]
Milestone/Task: M9 FINAL / Closing dan Handover

#### Entri Farchan (UX+Backend)
Aktivitas: Presentasi akhir dan retrospektif proyek.
Uraian Kegiatan (Logbook):
"Hari ini saya mengerjakan Presentasi akhir dan retrospektif proyek pada konteks 'Presentasi akhir dan retrospektif'. Pekerjaan saya jalankan bertahap dari perapihan kebutuhan, eksekusi inti, sampai pengecekan hasil agar sesuai milestone M9 FINAL / Closing dan Handover. Setelah selesai, saya pastikan 'Proyek ditutup' sudah siap dipakai tanpa nunggu klarifikasi tambahan."
Output Farchan:
- Artefak UX+Backend harian selesai: Presentasi akhir dan retrospektif proyek.
- Outcome harian terukur: Proyek ditutup.
Lampiran Farchan (Bukti Screenshot):
- `docs/logbook/logbook.md` baris 1526-1594: referensi kegiatan penutupan Day 96-100.
- `docs/logbook/MASTER_LOGBOOK_SYNC_TEAM.md` baris 52-59: kontrol sinkron akhir tim dua orang.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63 dan 84-87: target akhir dan sign-off.

#### Entri Ikram (UI+Frontend)
Aktivitas: Support demo akhir dan sign-off.
Uraian Kegiatan (Logbook):
"Hari ini saya ngerjain Support demo akhir dan sign-off dalam konteks 'Presentasi akhir dan retrospektif'. Pengerjaan saya alirin dari setup komponen, sinkronisasi state, sampai cek akhir integrasi agar tetap sejalan dengan milestone M9 FINAL / Closing dan Handover. Hasil 'Proyek ditutup' saya pastikan bisa langsung dipakai tim tanpa nunggu penjelasan tambahan."
Output Ikram:
- Artefak UI+Frontend harian selesai: Support demo akhir dan sign-off.
- Outcome harian terukur: Proyek ditutup.
Lampiran Ikram (Bukti Screenshot):
- `docs/logbook/LOGBOOK_HARIAN_W06_W20_DUAL_ROLE.md` (line N/A): update status harian ke `[TERLAKSANA]` saat closing.
- `docs/logbook/PROJECT_MANAGEMENT_20_WEEKS_SIMREKAP.md` baris 60-63: acuan output UAT/closing per pekan.
- `src/app/App.tsx` baris 216-279: bukti routing final lintas halaman saat sign-off.

