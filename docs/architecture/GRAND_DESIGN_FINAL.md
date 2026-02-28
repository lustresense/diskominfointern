# GRAND DESIGN DOKUMENTASI
## Sistem Informasi Manajemen RElawan KAmpung Pancasila (SIMREKAP)
**"The Pillar-Balance & Maturity Engine"**

Project Owner: Dinas Komunikasi dan Informatika Kota Surabaya  
Tim Pengembang: Mahasiswa Kerja Praktik PENS  
Status: Proposal Operasional (Pitch Version)  
Versi: 2.4 (Kampung-Centric, revisi struktur aktor dan kolaborasi)

## EXECUTIVE SUMMARY
SIMREKAP adalah sistem operasional digital untuk Program Kampung Pancasila Surabaya. Fokus SIMREKAP adalah memastikan aktivitas kampung tidak berhenti sebagai kegiatan lapangan saja, tetapi berubah menjadi data kinerja kampung yang terstruktur, tervalidasi, dan berguna untuk evaluasi kebijakan.

Inti konsep SIMREKAP adalah **Gamifikasi Kampung-Centric**: yang dinilai adalah kampung (kelurahan), bukan kompetisi individu. Sistem mengarahkan kampung agar berkembang seimbang di empat pilar melalui Pillar-Balance Engine.

## 1. LANDASAN PROGRAM: KAMPUNG PANCASILA
Kampung Pancasila Surabaya merupakan gerakan berbasis kampung/RW yang menekankan gotong royong, penyelesaian masalah sosial, dan penguatan kapasitas wilayah melalui satgas lintas aktor.

Gerakan ini berjalan melalui empat bidang utama:
- Lingkungan
- Ekonomi
- Sosial Budaya
- Kemasyarakatan

Karena keberhasilan kota ditopang oleh keberhasilan kampung, dibutuhkan sistem yang mampu membaca progres kampung secara konsisten, adil, dan terdokumentasi.

## 2. PERMASALAHAN YANG DISASAR
Permasalahan operasional utama di lapangan:
- Aktivitas kampung berjalan, tetapi data dampak belum seragam.
- Jejak verifikasi kegiatan dan laporan belum tertata optimal.
- Pilar tertentu cenderung dominan, pilar lain tertinggal.
- Kontribusi relawan belum selalu kuat menjadi basis data kebijakan.

SIMREKAP dirancang untuk menutup gap tersebut dengan alur terintegrasi dari kegiatan, verifikasi, pelaporan, hingga pembacaan performa kampung.

## 3. SOLUSI INTI: GAMIFIKASI KAMPUNG-CENTRIC
### 3.1 Prinsip Dasar
Gamifikasi dipakai sebagai alat tata kelola dan pengarah perilaku kolektif kampung, bukan alat kompetisi personal.

### 3.2 Pillar-Balance Engine
Engine memantau distribusi progres empat pilar. Jika ada ketimpangan, sistem mendorong kampung menyeimbangkan inisiasi kegiatan pada pilar yang tertinggal.

### 3.3 XP Kampung dan Leaderboard Kampung
- XP utama milik kampung (kelurahan).
- XP pilar menunjukkan kekuatan relatif per pilar.
- Leaderboard dipakai untuk pemetaan performa antar kampung.

## 4. DEFINISI AKTOR DAN PERAN (REVISI FINAL)
### 4.1 Relawan (Warga Tinggal di Surabaya)
Relawan adalah warga yang tinggal di Surabaya, termasuk mahasiswa/perantau yang berdomisili atau beraktivitas di Surabaya.

Peran relawan:
- registrasi akun,
- mengikuti kegiatan,
- mengirim laporan kegiatan yang diikuti,
- menerima poin kontribusi dan sertifikat kegiatan.

### 4.2 KSH (Entitas Terpisah dari Relawan Umum)
KSH adalah pengguna khusus operasional lapangan (kepanitiaan kegiatan kampung).

Peran KSH:
- mengelola jalannya kegiatan kampung di lapangan,
- menandai kegiatan selesai,
- mengisi output/ringkasan dampak kegiatan,
- memastikan kelengkapan administrasi kegiatan.

Batasan KSH:
- **tidak membuat draft kegiatan**,
- **tidak mengajukan approval kegiatan**.

### 4.3 Moderator Tier 1 - ASN Pendamping
Peran:
- inisiasi draft kegiatan,
- monitoring kampung binaan yang menjadi tanggung jawabnya.

Catatan:
- Tier 1 tidak melakukan approval akhir.

### 4.4 Moderator Tier 2 - Verifikator Wilayah (Dengan Badge)
Tier 2 dibedakan oleh badge agar cakupan kewenangannya jelas:
- **Badge A: Kelurahan** -> menangani satu kelurahan.
- **Badge B: Kecamatan** -> menangani satu kecamatan (berisi banyak kelurahan).

Peran Tier 2:
- approval kegiatan,
- verifikasi laporan,
- review permintaan kolaborasi mitra sesuai skala kontribusi.

### 4.5 Moderator Tier 3 - OPD
Tier 3 merepresentasikan OPD tematik (contoh: DLH, OPD ekonomi/ketenagakerjaan, dan OPD terkait lain) untuk:
- monitoring agregat lintas wilayah,
- analisis tren per pilar,
- masukan kebijakan tingkat kota.

### 4.6 Admin (Back-Office Sistem)
Admin diposisikan sebagai pengelola aplikasi/sistem di balik layar:
- menjaga stabilitas sistem,
- mengelola konfigurasi teknis,
- memastikan data dan alur berjalan.

Batasan desain operasional:
- admin **bukan pengampu operasional kampung**,
- admin **bukan pihak utama review kolaborasi kampung**.

## 5. PIHAK EKSTERNAL: MITRA (NON-LOGIN)
Mitra adalah pihak eksternal (komunitas/perusahaan/institusi) yang **tidak perlu login**.

Alur mitra:
- mengisi form kolaborasi publik,
- request masuk ke antrian moderator,
- diproses oleh moderator sesuai skala kontribusi.

Skala kontribusi yang ditetapkan:
- skala kelurahan,
- skala kecamatan,
- skala kota.

Catatan desain:
- form kolaborasi perlu memuat pilihan skala kontribusi secara eksplisit agar routing request tepat sasaran.

## 6. FITUR OPERASIONAL DAN STATUS
### 6.1 Fitur Operasional Saat Ini (Live)
- Landing publik + About + FAQ.
- Form kolaborasi mitra publik.
- Registrasi/login multi peran.
- Alur kegiatan: draft -> approval -> published -> completed.
- Laporan kegiatan peserta dan verifikasi moderator.
- Dashboard per peran (user, moderator, admin).
- Leaderboard kampung + ringkasan progres kampung.

### 6.2 Fitur Penguatan (Dalam Kajian / Penyempurnaan)
- popup peringatan ketimpangan pilar saat awal login ASN pendamping/Tier 2,
- CTA otomatis untuk inisiasi program pada pilar yang kosong/tertinggal,
- routing mitra berbasis skala kontribusi (kelurahan/kecamatan/kota) yang lebih ketat,
- otomatisasi sertifikat 1 kegiatan 1 sertifikat secara end-to-end.

## 7. ALUR BISNIS END-TO-END (RINGKAS)
1. ASN Tier 1 inisiasi draft kegiatan kampung.  
2. Tier 2 (badge kelurahan/kecamatan) melakukan review dan approval.  
3. Kegiatan dipublikasikan, relawan mendaftar sesuai kuota.  
4. KSH mengelola pelaksanaan, menandai kegiatan selesai, dan mengisi output.  
5. Relawan peserta mengirim laporan kegiatan.  
6. Tier 2 memverifikasi laporan.  
7. Progres pilar dan XP kampung diperbarui.

## 8. APRESIASI RELAWAN: SERTIFIKAT DAN POIN
Prinsip apresiasi relawan:
- **1 kegiatan = 1 sertifikat kontribusi**.
- Relawan menerima poin kontribusi pada dashboard.
- Poin dapat ditukar menjadi voucher/manfaat layanan di Surabaya.

Skema penukaran (konsep operasional):
- poin ditukar menjadi voucher (misalnya transportasi publik Surabaya),
- setelah ditukar, poin berkurang/habis sesuai nilai penukaran,
- mekanisme katalog reward disesuaikan dengan kerja sama layanan kota.

Catatan:
- detail SLA penerbitan sertifikat otomatis masih dalam kajian operasional bersama KSH/moderator.

## 9. ALUR KOLABORASI MITRA
1. Mitra isi form kolaborasi publik (tanpa login).  
2. Mitra memilih skala kontribusi: kelurahan/kecamatan/kota.  
3. Request masuk ke antrian moderator yang relevan.  
4. Moderator Tier 2/Tier 3 memproses sesuai scope.  
5. Status akhir: approved/rejected, lalu ditindaklanjuti operasional.

## 10. ARSITEKTUR KONSEPTUAL (VISUAL & LOGICAL)
```text
+----------------------------------------------------------------+
| USER & ACTOR LAYER                                              |
| Relawan / KSH / Moderator Tier 1-3 / Admin (Back-Office) /     |
| Mitra Eksternal (Non-Login)                                    |
+------------------------------+---------------------------------+
                               |
+------------------------------v---------------------------------+
| PRESENTATION LAYER (WEB)                                       |
| Landing + Informasi Program + Form Mitra + Dashboard Per Peran |
+------------------------------+---------------------------------+
                               |
+------------------------------v---------------------------------+
| APPLICATION / SERVICE LAYER                                    |
| Role Governance, Event Flow, Verifikasi,                        |
| Pillar-Balance Engine, Reward Logic, Monitoring                |
+------------------------------+---------------------------------+
                               |
+------------------------------v---------------------------------+
| DATA LAYER                                                      |
| Data Pengguna, Kegiatan, Laporan, XP Kampung,                  |
| Leaderboard Kampung, Kolaborasi Mitra, Histori Review          |
+----------------------------------------------------------------+
```

## 11. NILAI MANFAAT PER PEMANGKU KEPENTINGAN
- **Relawan**: kontribusi terdata, dapat sertifikat, dapat poin apresiasi.
- **KSH**: operasional kegiatan lebih tertata dan terdokumentasi.
- **ASN Pendamping**: inisiasi program lebih terarah per kampung binaan.
- **Kelurahan/Kecamatan**: verifikasi dan pengendalian mutu data lebih jelas.
- **OPD**: insight agregat per pilar sebagai basis kebijakan.
- **Mitra**: kanal kontribusi formal, transparan, dan terukur.

## 12. PENEGASAN PROPOSAL
SIMREKAP adalah proposal sistem operasional untuk menguatkan Kampung Pancasila agar:
- pembangunan empat pilar lebih seimbang,
- peran lintas aktor lebih tegas dan konsisten,
- kontribusi relawan, KSH, moderator, dan mitra terkonversi menjadi data kebijakan yang kredibel.

Dokumen ini menjadi baseline resmi untuk komunikasi pitch, demonstrasi sistem, dan pengembangan tahap berikutnya.

## 13. RUJUKAN KONSEP PROGRAM (RINGKAS)
Rujukan konteks Kampung Pancasila Surabaya yang dipakai dalam framing dokumen ini:
- Pemkot Surabaya - pembentukan Satgas Kampung Pancasila dan 4 bidang utama: https://www.surabaya.go.id/id/berita/87338/wali-kota-eri-cahyadi-pastikan-pembentukan-satgas-kampung-pancasila-tuntas-agustus-2025
- Pemkot Surabaya - penjelasan makna Kampung Pancasila dan fokus 4 pilar per RW: https://www.surabaya.go.id/id/berita/87676/wali-kota-eri-cahyadi-kampung-pancasila-adalah-fondasi-kekuatan-kota-surabaya
- Pemkot Surabaya - penguatan SOP, pelibatan ASN pendamping, dan pendekatan kampung sebagai fondasi kota: https://www.surabaya.go.id/id/berita/86803/pastikan-program-kampung-pancasila-jalan-konsisten-pemkot-surabaya-aktifkan-forum-4-pilar
- ANTARA Jatim - ringkasan penguatan implementasi Kampung Pancasila tingkat kota: https://www.antaranews.com/berita/4944573/wali-kota-surabaya-bentuk-satgas-kampung-pancasila-inisiatif-tingkat-rw

