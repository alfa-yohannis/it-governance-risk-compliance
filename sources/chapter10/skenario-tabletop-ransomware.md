<!-- Panduan latihan krisis; baca skenario bertahap dan catat keputusan tanpa menyentuh sistem nyata. -->
# Tabletop: SIMRS terenkripsi di rumah sakit Bekasi

Semua rincian tambahan berikut adalah skenario fiktif. Tidak ada malware,
pemindaian, pemutusan jaringan, atau data pasien nyata yang dipakai.
Durasi diskusi 45 menit, evaluasi 15 menit. Waktu skenario dapat berbeda dari
waktu diskusi; pengamat mencatat keduanya.

| Peran | Tugas |
| --- | --- |
| Direktur rumah sakit | Mengaktifkan operasi manual dan menjaga kapasitas aman |
| Direktur pelayanan | Memilih strategi lintas fasilitas dan memutuskan pengalihan |
| Kepala operasi TI | Memimpin tanggap insiden, memvalidasi cakupan, menilai isolasi |
| Fungsi hukum dan petugas pelindungan data | Menilai kewajiban serta menyiapkan pemberitahuan |
| Direktur utama | Menyampaikan fakta terverifikasi dan jadwal pembaruan |
| Penanggung jawab klinis | Menentukan layanan minimum dan batas aman |
| Pengamat | Mencatat keputusan, waktu, dasar bukti, serta informasi yang hilang |

| Waktu skenario | Informasi baru | Keputusan yang diuji | Pemilik | Target (menit) |
| --- | --- | --- | --- | --- |
| 08.00 | SIMRS tidak dapat dibuka | Siapa memimpin dan memvalidasi dampak? | Kepala operasi TI | 10 |
| 08.15 | Berkas tampak terenkripsi; tiga unit terpengaruh | Apa yang diisolasi? | Kepala operasi TI | 15 |
| 08.15 | Layanan terganggu | Kapan operasi manual aktif? | Direktur rumah sakit | 20 |
| 08.30 | Cadangan terakhir belum tervalidasi | Strategi apa dipilih dan siapa menerima risiko? | Direktur pelayanan | 30 |
| 08.45 | Vendor tidak dapat dihubungi | Kapan jalur alternatif diaktifkan? | Kepala operasi TI | 15 |
| 09.00 | Media menanyakan kebocoran | Apa fakta yang dapat diumumkan dan kapan diperbarui? | Direktur utama | 60 |
| 09.15 | Ada indikasi data keluar; belum pasti jumlahnya | Kapan proses keputusan pemberitahuan dimulai? | Fungsi hukum | 30 |

Target keputusan merupakan asumsi pendidikan, bukan kewajiban hukum.
Gunakan target RTO dan RPO BIA, bukan angka baru yang dipilih saat latihan.
Bila indikasi data keluar muncul Selasa 09.15, cara hitung Bab 7 memberi batas
internal jam ke-60 pada Kamis 21.15 dan batas terluar 3 kali 24 jam pada Jumat
09.15. Bila vendor terlibat, laporan 12 jam pada K-05 jatuh pada Selasa 21.15.

## Lembar catatan

| Keputusan | Waktu target | Waktu aktual | Pemilik | Dasar bukti | Konsekuensi |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |

## Contoh hasil (misalkan)

| Keputusan | Target | Aktual | Selisih | Penyebab | Tindakan | Tenggat |
| --- | --- | --- | --- | --- | --- | --- |
| Memimpin | 10 | 8 | Tepat waktu | | | |
| Isolasi | 15 | 15 | Tepat waktu | | | |
| Operasi manual | 20 | 35 | Terlambat 15 | Kewenangan: daftar tidak tersedia pada malam dan akhir pekan | Daftar pengganti oleh direktur rumah sakit | 14 hari |
| Strategi | 30 | 25 | Tepat waktu, dasar bukti lemah | Memakai cadangan yang belum tervalidasi | Temuan mutu keputusan | Uji ulang |
| Jalur vendor | 15 | 40 | Terlambat 25 | Teknis dan kontrak: satu nomor kontak | Kontak cadangan masuk kontrak | 30 hari |
| Pernyataan publik | 60 | 50 | Tepat waktu | | | |
| Pemberitahuan | 30 | 45 | Terlambat 15 | Komunikasi: fungsi hukum baru diundang pukul 09.15 | Masuk daftar panggilan awal | 14 hari |

Empat dari tujuh keputusan tepat waktu, atau sekitar 57 persen. Total keterlambatan
55 menit. Ketiga temuan diuji ulang dalam 60 hari.

## Evaluasi

Keputusan mana terlambat, informasi apa kurang, dan apakah kapasitas manual aman?
Setiap celah memiliki tindakan, pemilik, tenggat, dan tanggal uji ulang. Pisahkan
penyebab teknis, kewenangan, komunikasi, dan kapasitas layanan.
