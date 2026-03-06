# User Journey Map — SIMRP
## Sistem Informasi Manajemen Relawan Kampung Pancasila
### Farchan Ramadhan | 4 Maret 2026

---

## JOURNEY 1 — Relawan Mengikuti Event dan Mendapat Reward

**Persona**: Rizky Aditya Pratama (`user`)  
**Skenario**: Rizky mengetahui ada event kebersihan lingkungan, mendaftar, hadir, lalu mendapat sertifikat dan poin  
**Goal**: Mendapat bukti kontribusi dan reward nyata

---

### Tahap 1 — Awareness (Tau ada event)

| | Detail |
|---|---|
| **Aktivitas** | Rizky buka aplikasi SIMRP, lihat halaman beranda |
| **Touchpoint** | Halaman Home / Feed Event |
| **Pikiran** | *"Ada event kebersihan di RW gue minggu depan, lumayan."* |
| **Emosi** | 😐 Netral → 🙂 Sedikit tertarik |
| **Pain Point** | Kalau notifikasi tidak ada, Rizky mungkin tidak buka aplikasi sama sekali |
| **Opportunity** | Tambah push notification saat ada event baru di wilayah user |

---

### Tahap 2 — Consideration (Pertimbangkan ikut)

| | Detail |
|---|---|
| **Aktivitas** | Rizky buka detail event, lihat deskripsi, lokasi, poin yang bisa didapat |
| **Touchpoint** | Halaman Event Detail |
| **Pikiran** | *"Poinnya 150 XP, lumayan buat naikin ranking kampung. Kuota masih ada."* |
| **Emosi** | 🙂 Tertarik → 😊 Termotivasi |
| **Pain Point** | Kalau informasi event tidak lengkap, Rizky tidak yakin mau daftar |
| **Opportunity** | Tampilkan preview reward yang bisa didapat dari poin event ini |

---

### Tahap 3 — Registration (Daftar event)

| | Detail |
|---|---|
| **Aktivitas** | Rizky tap tombol "Ikut Kegiatan", sistem validasi kuota, status berubah jadi terdaftar |
| **Touchpoint** | Tombol Join Event, notifikasi konfirmasi |
| **Pikiran** | *"Oke, sudah terdaftar. Semoga tidak lupa."* |
| **Emosi** | 😊 Senang → 😌 Lega |
| **Pain Point** | Tidak ada reminder H-1 sebelum event, Rizky bisa lupa |
| **Opportunity** | Kirim reminder notifikasi H-1 dan H-0 (pagi hari event) |

---

### Tahap 4 — Participation (Hadir di event)

| | Detail |
|---|---|
| **Aktivitas** | Rizky hadir di lokasi, Pak Hendra (KSH) centang kehadiran Rizky di aplikasi |
| **Touchpoint** | Fitur Attendance Checklist (sisi KSH) |
| **Pikiran** | *"Semoga kehadiran gue tercatat. Kalau nggak, percuma datang."* |
| **Emosi** | 😊 Antusias → 😰 Sedikit khawatir |
| **Pain Point** | Rizky tidak bisa self-checkin, bergantung pada KSH yang mungkin lupa |
| **Opportunity** | Tambah konfirmasi kehadiran dari sisi user setelah KSH checkin |

---

### Tahap 5 — Reporting (Laporan kegiatan)

| | Detail |
|---|---|
| **Aktivitas** | Setelah event selesai, Rizky submit laporan via wizard 2 langkah (deskripsi + foto bukti) |
| **Touchpoint** | Halaman Submit Laporan (wizard step 1 & 2) |
| **Pikiran** | *"Upload foto dulu. Semoga cepat diverifikasi."* |
| **Emosi** | 😌 Tenang → 🤔 Menunggu |
| **Pain Point** | Tidak tau kapan laporan akan diverifikasi, tidak ada estimasi waktu |
| **Opportunity** | Tampilkan SLA verifikasi ("Biasanya diverifikasi dalam 1x24 jam") |

---

### Tahap 6 — Verification (Laporan diverifikasi)

| | Detail |
|---|---|
| **Aktivitas** | Bu Sari (Moderator) mereview laporan Rizky, klik approve, sistem otomatis tambah XP |
| **Touchpoint** | Notifikasi push + update status di halaman "Laporan Saya" |
| **Pikiran** | *"Laporan disetujui! XP nambah 150 poin."* |
| **Emosi** | 😄 Senang → 🤩 Excited |
| **Pain Point** | Kalau ditolak tanpa alasan jelas, Rizky frustrasi |
| **Opportunity** | Notifikasi approval harus include berapa XP yang didapat |

---

### Tahap 7 — Reward (Tukar poin)

| | Detail |
|---|---|
| **Aktivitas** | Rizky buka halaman reward, pilih voucher, konfirmasi redeem, dapat kode voucher |
| **Touchpoint** | Halaman Katalog Reward, Modal Redeem, Halaman Sertifikat |
| **Pikiran** | *"Akhirnya bisa ditukar. Ada juga sertifikat yang bisa didownload buat portofolio."* |
| **Emosi** | 😄 Puas → 🤩 Bangga |
| **Pain Point** | Kalau reward tidak menarik atau XP yang dibutuhkan terlalu tinggi, motivasi turun |
| **Opportunity** | Tampilkan progress bar "Kamu butuh X XP lagi untuk reward berikutnya" |

---

### Emotional Journey — Rizky

```
Awareness  → Consideration → Registration → Participation → Reporting → Verification → Reward
   😐              🙂              😊              😊/😰          🤔            😄            🤩
                                                                              
Netral      Tertarik       Terdaftar      Hadir tapi     Nunggu      Approved    Puas & Bangga
                                          khawatir                              
                                          tercatat
```

---

## JOURNEY 2 — KSH Membuat dan Menyelesaikan Event

**Persona**: Pak Hendra Kusuma (`ksh`)  
**Skenario**: Pak Hendra buat event kerja bakti, tunggu approval, jalankan event, tandai selesai  
**Goal**: Event tercatat resmi dan laporan masuk ke sistem tanpa proses manual

---

### Tahap 1 — Create Event (Buat draft event)

| | Detail |
|---|---|
| **Aktivitas** | Pak Hendra buka halaman buat event, isi form (judul, tanggal, lokasi, kuota, pilar) |
| **Touchpoint** | Halaman Form Create Event |
| **Pikiran** | *"Semoga form-nya tidak terlalu panjang dan ribet."* |
| **Emosi** | 😐 Netral → 🤔 Fokus |
| **Pain Point** | Form terlalu banyak field, membingungkan bagi user yang kurang tech-savvy |
| **Opportunity** | Progressive form dengan tooltip penjelasan setiap field |

---

### Tahap 2 — Waiting Approval (Menunggu persetujuan)

| | Detail |
|---|---|
| **Aktivitas** | Draft event tersubmit, menunggu Bu Sari (Moderator) approve |
| **Touchpoint** | Status badge "Menunggu Persetujuan" di dashboard |
| **Pikiran** | *"Kapan ini disetujui? Nggak ada kabarnya."* |
| **Emosi** | 😌 Menunggu → 😤 Tidak sabar |
| **Pain Point** | Tidak ada notifikasi saat status event berubah |
| **Opportunity** | Push notification saat event diapprove atau ditolak beserta alasannya |

---

### Tahap 3 — Event Berlangsung (Hari-H)

| | Detail |
|---|---|
| **Aktivitas** | Event sudah published, relawan datang, Pak Hendra buka aplikasi untuk absensi |
| **Touchpoint** | Halaman Detail Event → Fitur Checklist Kehadiran |
| **Pikiran** | *"Lebih mudah dari absen manual. Tinggal centang satu-satu."* |
| **Emosi** | 🙂 Terbantu → 😊 Puas |
| **Pain Point** | Kalau sinyal jelek di lokasi event, checkin bisa gagal |
| **Opportunity** | Mode offline untuk attendance, sync saat online kembali |

---

### Tahap 4 — Complete Event (Tandai selesai)

| | Detail |
|---|---|
| **Aktivitas** | Setelah selesai, Pak Hendra tap "Tandai Selesai", isi output summary |
| **Touchpoint** | Tombol Complete Event + Modal Output Summary |
| **Pikiran** | *"Sekarang relawan bisa langsung laporan sendiri. Tidak perlu kirim ke saya dulu."* |
| **Emosi** | 😊 Lega → 😄 Puas |
| **Pain Point** | Tidak ada konfirmasi bahwa relawan sudah ternotifikasi untuk laporan |
| **Opportunity** | Auto-notif ke semua peserta terdaftar bahwa event selesai dan bisa laporan |

---

### Emotional Journey — Pak Hendra

```
Create Event → Waiting Approval → Event Day → Complete Event
    🤔               😤               😊            😄

  Fokus isi       Tidak sabar      Terbantu        Lega & Puas
    form           nunggu          absensi         sistem jalan
```

---

## JOURNEY 3 — Moderator Memverifikasi Laporan

**Persona**: Ibu Sari Dewi Lestari (`moderator_t1`)  
**Skenario**: Bu Sari buka dashboard, review laporan masuk, approve yang valid, reject yang tidak  
**Goal**: Semua laporan terverifikasi akurat dan tepat waktu

---

### Tahap 1 — Dashboard Review

| | Detail |
|---|---|
| **Aktivitas** | Bu Sari login, buka panel moderasi, lihat daftar laporan pending |
| **Touchpoint** | Halaman Admin/Moderator Dashboard |
| **Pikiran** | *"Ada 12 laporan pending hari ini. Harus diselesaikan sebelum COB."* |
| **Emosi** | 😐 Fokus → 🤔 Prioritasi |
| **Pain Point** | Tidak ada urutan prioritas, laporan lama dan baru tercampur |
| **Opportunity** | Sort by tanggal, filter by kampung, highlight laporan yang sudah > 24 jam |

---

### Tahap 2 — Review Detail Laporan

| | Detail |
|---|---|
| **Aktivitas** | Klik salah satu laporan, lihat detail: deskripsi, jumlah peserta, foto bukti |
| **Touchpoint** | Halaman Detail Laporan |
| **Pikiran** | *"Foto buktinya jelas, jumlah peserta masuk akal. Ini bisa diapprove."* |
| **Emosi** | 🔍 Teliti → ✅ Yakin |
| **Pain Point** | Foto terlalu kecil, tidak bisa zoom untuk verifikasi |
| **Opportunity** | Fitur zoom foto bukti + metadata foto (waktu, ukuran file) |

---

### Tahap 3 — Approve / Reject

| | Detail |
|---|---|
| **Aktivitas** | Klik "Setujui", konfirmasi, sistem update XP otomatis. Atau klik "Tolak" + isi alasan |
| **Touchpoint** | Tombol Approve/Reject + Konfirmasi Modal |
| **Pikiran** | *"Kalau approved, XP langsung masuk. Kalau rejected, relawan harus tau alasannya."* |
| **Emosi** | 😊 Efisien → 😌 Puas prosesnya jelas |
| **Pain Point** | Tidak ada template alasan penolakan, ketik dari nol setiap kali |
| **Opportunity** | Template alasan penolakan yang bisa dipilih (foto tidak jelas, jumlah tidak sesuai, dll) |

---

### Tahap 4 — Audit & Monitoring

| | Detail |
|---|---|
| **Aktivitas** | Bu Sari cek riwayat verifikasi, lihat statistik laporan per kampung bulan ini |
| **Touchpoint** | Halaman Audit Log + Chart Progress Pilar |
| **Pikiran** | *"Kampung A sudah 3 kegiatan bulan ini, Kampung B masih 0. Perlu didorong."* |
| **Emosi** | 📊 Analitis → 💡 Insightful |
| **Pain Point** | Data statistik tidak ada, harus hitung manual dari list laporan |
| **Opportunity** | Dashboard summary: total laporan, total XP didistribusi, kampung paling aktif |

---

### Emotional Journey — Bu Sari

```
Dashboard → Review Detail → Approve/Reject → Audit
   🤔           🔍               😊             💡

Prioritasi    Teliti          Efisien       Dapat insight
  tugas        bukti          & jelas       buat laporan
```

---

## JOURNEY 4 — Mitra Submit Kemitraan

**Persona**: Dina Marlina (Publik, tanpa akun)  
**Skenario**: Dina temukan SIMRP, isi form kemitraan, tunggu konfirmasi  
**Goal**: Pengajuan kemitraan diterima dan ada tindak lanjut resmi

---

### Tahap 1 — Discovery

| | Detail |
|---|---|
| **Aktivitas** | Dina buka website SIMRP dari referral kolega, lihat landing page mitra |
| **Touchpoint** | Halaman Landing Page / Halaman Mitra |
| **Pikiran** | *"Programnya bagus. Ada form untuk perusahaan yang mau support."* |
| **Emosi** | 🔍 Penasaran → 🙂 Tertarik |

---

### Tahap 2 — Form Submission

| | Detail |
|---|---|
| **Aktivitas** | Isi form: nama organisasi, PIC, email, jenis dukungan, scope wilayah, deskripsi |
| **Touchpoint** | Halaman Form Kemitraan (publik, tanpa login) |
| **Pikiran** | *"Form-nya cukup singkat. Bisa pilih scope kecamatan atau kelurahan, bagus."* |
| **Emosi** | 😊 Terbantu → 😌 Submitted |
| **Pain Point** | Tidak ada konfirmasi email otomatis setelah submit |
| **Opportunity** | Auto-reply email konfirmasi dengan nomor tracking pengajuan |

---

### Tahap 3 — Waiting & Follow Up

| | Detail |
|---|---|
| **Aktivitas** | Dina menunggu kabar, tidak ada jalur untuk cek status pengajuan |
| **Touchpoint** | — (gap, tidak ada touchpoint) |
| **Pikiran** | *"Sudah 3 hari belum ada kabar. Jangan-jangan tidak masuk."* |
| **Emosi** | 🤔 Menunggu → 😟 Khawatir |
| **Pain Point** | Tidak ada halaman atau link untuk track status pengajuan |
| **Opportunity** | Halaman cek status dengan nomor tracking atau email |

---

### Tahap 4 — Konfirmasi dari Moderator

| | Detail |
|---|---|
| **Aktivitas** | Moderator approve request, Dina terima email konfirmasi resmi |
| **Touchpoint** | Email notifikasi approval |
| **Pikiran** | *"Akhirnya ada konfirmasi. Bisa dilanjutkan ke proses internal perusahaan."* |
| **Emosi** | 😄 Lega → 🤝 Siap kolaborasi |

---

### Emotional Journey — Dina

```
Discovery → Form Submit → Waiting → Konfirmasi
   🙂           😌          😟         😄

 Tertarik     Submitted   Khawatir    Lega &
                          tidak ada   Siap
                          kabar       Kolaborasi
```

---

## RINGKASAN OPPORTUNITY PER JOURNEY

| Journey | Opportunity Utama | Prioritas |
|---------|------------------|-----------|
| Rizky — Relawan | Push notification event baru di wilayah | 🔴 Tinggi |
| Rizky — Relawan | Reminder H-1 sebelum event | 🟡 Sedang |
| Rizky — Relawan | Progress bar "X XP lagi untuk reward" | 🟡 Sedang |
| Pak Hendra — KSH | Notifikasi saat event diapprove/ditolak | 🔴 Tinggi |
| Pak Hendra — KSH | Auto-notif peserta saat event selesai | 🔴 Tinggi |
| Bu Sari — Moderator | Filter & sort laporan pending | 🔴 Tinggi |
| Bu Sari — Moderator | Template alasan penolakan | 🟡 Sedang |
| Bu Sari — Moderator | Dashboard summary per kampung | 🟡 Sedang |
| Dina — Mitra | Auto-reply email konfirmasi | 🟡 Sedang |
| Dina — Mitra | Halaman tracking status pengajuan | 🟢 Rendah |

---

*Dokumen ini dibuat sebagai bagian dari UX Research SIMRP Sprint 1.*  
*Author: Farchan Ramadhan | 4 Maret 2026 | SIMRP Internship*