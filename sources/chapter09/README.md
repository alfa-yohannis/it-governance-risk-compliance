<!-- Kegunaan: indeks berkas Aktivitas Bab 09. Cara pakai: salin templat ke folder tim, baca petunjuk, dan pisahkan contoh pengandaian dari bukti organisasi. -->

# Sumber Bab 09

| Berkas | Kegunaan |
| --- | --- |
| `klasifikasi-vendor.csv` | Contoh pengandaian enam hubungan dengan skor, tingkat pemeriksaan, pemilik, dan pemicu tinjau ulang. |
| `peta-ketergantungan.csv` | Contoh pengandaian pihak keempat per hubungan untuk menemukan titik kegagalan bersama. |
| `kuesioner-uji-tuntas.md` | Sepuluh pertanyaan yang meminta bukti, cakupan, dan pengecualian. |
| `klausul-kontrak.md` | Sembilan pokok klausul, lima pokok tawar ulang, dan simulasi laporan 12 jam. |
| `matriks-cloud.csv` | Pembagian kendali untuk dikonfirmasi terhadap kontrak layanan. |
| `templat-dpia.md` | Penilaian tujuan, alur, dampak, kontrol, dan risiko sisa. |
| `contoh-dpia-medikara.md` | Contoh pengandaian berbagi data asuransi dan pengurangan data. |

## Cara memakai

1. Baca tujuan dan Aktivitas pada bab, lalu tetapkan ruang lingkup serta peran tim.
2. Salin berkas isian; pertahankan berkas contoh sebagai pembanding.
3. Isi sumber bukti, pemilik, keputusan, dan hal yang belum diketahui.
4. Tinjau bersama anggota berlatar nonteknis dan teknis sebelum pengumpulan.

Berkas CSV memakai UTF-8 dan pemisah koma. Baris pertama adalah komentar berawalan `#`, dan nama
kolom ada pada baris kedua. Buang baris komentar bila aplikasi tidak mengenalinya, dan buka melalui
menu impor spreadsheet bila pemisah lokal berbeda. Seluruh angka tambahan pada contoh adalah
pengandaian pembelajaran. Data organisasi nyata harus berizin dan anonim. Data pasien, rahasia
akses, dan dokumen asli organisasi tidak boleh disalin ke folder tugas.

## Kode yang dipakai

| Kode | Arti | Asal |
| --- | --- | --- |
| V-01 sampai V-06 | Baris hubungan pemasok | Bab 09 |
| R-01, R-08, R-10 | Skenario risiko akses vendor, satu subpenyedia, dan keluar | Bab 05 |
| K-05, K-07, K-12, K-13 | Kewajiban laporan vendor, kerja sama penyimpanan, laporan ke mitra, lokasi data | Bab 03 |
| CP-01, CP-03, CP-07 | Celah perjanjian vendor, DPIA asuransi, lokasi cadangan | Bab 07 |
| T-02, T-11, KB-05 | Target APO10, target GV.SC-07, kebijakan berbagi data | Bab 08 |

## Versi dan asurans

Catat versi CCM dan CAIQ yang diunduh, tanggal bukti, dan cakupan layanan. Halaman resmi CSA saat
bab ini ditulis menyajikan versi 4.1. Jawaban kuesioner dan sertifikat adalah masukan pemeriksaan,
bukan kesimpulan bahwa konfigurasi pelanggan aman. Angka 12 jam pada klausul mengikuti K-05 di Bab
03 dan merupakan syarat kontrak pengandaian, bukan tenggat UU PDP.
