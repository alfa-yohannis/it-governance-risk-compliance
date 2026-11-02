<!-- Daftar sumber Bab 14; satukan identitas kontrol lalu susun peta jalan yang dapat diputuskan. -->
# Sumber Bab 14: GRC Terpadu dan Peta Jalan

| Berkas | Kegunaan |
| --- | --- |
| pemetaan-kontrol.csv | Kontribusi AC-01 pada acuan, yang dijawab dan yang belum |
| peta-jalan-grc.csv | Sebelas inisiatif tiga tahun dengan ketergantungan, pemilik, biaya per tahun, dan gerbang |
| beban-jam-peta-jalan.csv | Tiga belas baris jam beserta objektif dan kelompoknya |
| periksa_peta_jalan.py | Menghitung ulang biaya, jam, dan uang baru dari kedua CSV |
| kriteria-alat-grc.csv | Syarat wajib dan lima kriteria berbobot |
| catatan-perpanjangan-ta01.md | Contoh catatan perpanjangan tenggat temuan |
| templat-presentasi-c4.md | Agenda, pertanyaan direksi, lima keputusan contoh, dan catatan keputusan |

Buka CSV sebagai UTF-8 dengan pemisah koma. Baris pertama CSV adalah komentar.
Semua biaya dan skor adalah asumsi pembelajaran, bukan harga atau penilaian produk.

Biaya penuh per tahun Rp1.912,76 juta, Rp1.561,92 juta, dan Rp1.501,92 juta, atau
Rp4.976,60 juta. Jam per tahun 6.873, 3.299, dan 3.299, atau 13.471 jam senilai
Rp808,26 juta pada tarif Rp60.000. Uang baru Rp4.168,34 juta. Jam di dalam GRC-01
tidak ditambahkan lagi ke rupiah. Rencana asurans dan laporan satu halaman memakai
kapasitas yang sudah ada.

Syarat wajib lulus dahulu. Skor berbobot = jumlah bobot x skor / 100 pada skala 1
sampai 5; contoh spreadsheet 3,70, sumber terbuka 3,35, platform 3,55. Skor sementara
tidak memilih pemenang sebelum syarat akses dan ekspor diuji. CSV ini bukan format
OSCAL. Luaran menutup C4 dan dilebur ke peta jalan transformasi di IT40513.
