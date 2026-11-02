<!-- Templat laporan direksi; isi tiga pesan, satu keputusan, dan bukti pada satu halaman. -->
# Laporan GRC kepada Direksi

Periode: ...; penyusun/pemilik: ...; tanggal data: ...; cakupan: ...

**Keputusan yang diminta:** setujui/ubah/tolak ... paling lambat ...

**Pesan 1:** kondisi terpenting, angka, tren, dan risiko terkait.

**Pesan 2:** pengecualian penting atau kesenjangan kontrol.

**Pesan 3:** tindakan yang sudah berjalan dan risiko sisanya.

| Pilihan | Biaya serta asumsi | Akibat pada risiko | Pemilik | Ukuran keberhasilan |
| --- | --- | --- | --- | --- |
| Rekomendasi | ... | ... | ... | ... |
| Pembanding | ... | ... | ... | ... |

**Batas data:** kelengkapan, periode yang tidak sebanding, perubahan definisi,
atau indikator yang tidak berlaku.

**Tindak lanjut keputusan:** catat keputusan, penolakan, dan risiko sisa.

Sebelum menulis permintaan, periksa batas delegasi Bab 2. Biaya sampai Rp100 juta
cukup dilaporkan, karena keputusannya berada pada kepala TI.

## Contoh skenario triwulan Agustus sampai Oktober 2026

**Keputusan yang diminta:** setujui pilihan 1 paling lambat akhir November 2026.

**Pesan 1:** pemulihan belum memenuhi syarat. Sebanyak 29 dari 36 uji lulus, tetapi
hanya 3 dari 5 rumah sakit. Dua kegagalan data berasal dari 9 uji akun terpisah.
R-05 masih 10 persen, batasnya 2 persen.

**Pesan 2:** akses vendor membaik, tetapi belum selesai. Cakupan AC-01 85, 90, dan
95 persen. Satu akun tanpa pemilik sudah dibekukan, dan IK-01 tetap merah pada
tanggal data. TA-01 belum lolos uji ulang.

**Pesan 3:** layanan membaik, dan masih di bawah target. Waktu tunggu 34, 31, dan 28
menit, dengan target 25 menit. Gangguan pendaftaran Oktober 100 menit, di dalam
batas 120 menit, tetapi di atas RTO 90 menit.

| Pilihan | Biaya serta asumsi | Akibat pada risiko | Pemilik | Ukuran keberhasilan |
| --- | --- | --- | --- | --- |
| 1. Tahan tahap kedua; uji ulang 2 rumah sakit dan 9 uji akun terpisah | Rp0 tambahan saat ini | Peluang tetap 0,1; sekitar Rp40 juta lebih tinggi per triwulan | Kepala operasi TI | 5 dari 5 rumah sakit; 9 dari 9 uji; akhir Januari 2027 |
| 2. Cairkan Rp180 juta sekarang | Rp180 juta | Peluang tetap dicatat 0,1 sampai uji lulus | Kepala operasi TI | Sama, tetapi uang keluar sebelum bukti |
| 3. Hentikan opsi B, kembali ke opsi A | Hemat Rp180 juta | SIMRS pulih 480 menit; batas 2 persen dilanggar | Tidak disarankan | Sudah ditolak pada Bab 10 |

**Batas data:** tingkat lulus uji bukan peluang R-05. Lima uji rumah sakit tergolong
sedikit. Definisi tepat waktu pada IK-07 diperketat sejak Agustus.

Jangan merata-ratakan dua status menjadi satu warna yang menyembunyikan risiko.
