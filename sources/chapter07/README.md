<!-- Kegunaan: indeks berkas Aktivitas Bab 07. Cara pakai: salin templat ke folder tim, baca petunjuk, dan pisahkan contoh pengandaian dari bukti organisasi. -->

# Sumber Bab 07

| Berkas | Kegunaan |
| --- | --- |
| `catatan-pemrosesan.csv` | Templat catatan pemrosesan: tujuan, data, dasar, peran, penerima, lokasi, retensi, kontrol, dan bukti. |
| `contoh-pemrosesan-medikara.csv` | Contoh pengandaian lima proses: pendaftaran, telekonsultasi, rekam medis, promosi, dan dukungan vendor. Baris P-01, P-02, dan P-05 sama dengan tabel catatan pemrosesan pada bab. |
| `penyaringan-penilaian-dampak.csv` | Penyaringan usulan terhadap tujuh keadaan Pasal 34 ayat (2) UU PDP. Tiga usulan contoh sama dengan tabel pada bab. |
| `kronologi-insiden-vendor-2025.md` | Kronologi insiden 2025, selaras dengan data latihan Bab 1 dan IT40613 Bab 6, ditambah pengandaian jam untuk latihan tenggat. |
| `analisis-celah-pdp.md` | Lembar pembandingan kewajiban dengan bukti, serta contoh celah CP-01 sampai CP-07. |
| `templat-notifikasi.md` | Rancangan latihan; tidak dikirim kepada pihak nyata. |
| `hitung-tenggat-notifikasi.py` | Skrip opsional untuk menghitung batas 72 jam dari beberapa titik mulai. Tanpa data pribadi dan tanpa jaringan. |

## Cara memakai

1. Baca tujuan dan Aktivitas pada bab, lalu tetapkan ruang lingkup serta peran tim.
2. Salin berkas isian; pertahankan berkas contoh sebagai pembanding.
3. Isi sumber bukti, pemilik, keputusan, dan hal yang belum diketahui.
4. Tinjau bersama anggota berlatar nonteknis dan teknis sebelum pengumpulan.

Berkas CSV memakai UTF-8 dan pemisah koma. Baris pertama berisi komentar kegunaan, dan
baris kedua berisi nama kolom. Buang baris komentar bila aplikasi tidak mengenalinya.
Buka melalui menu impor aplikasi spreadsheet bila pemisah lokal berbeda.

Seluruh angka tambahan pada contoh adalah pengandaian pembelajaran. Data organisasi nyata
harus berizin dan anonim. Data pasien, rahasia akses, atau dokumen asli organisasi tidak
boleh disalin ke folder tugas.

Skrip dijalankan dengan `python hitung-tenggat-notifikasi.py`. Keluaran dipakai untuk
memeriksa tabel titik mulai, bukan untuk menetapkan batas hukum.

## Catatan sumber hukum, diperiksa 1 November 2026

Bab ini bukan nasihat hukum. Kolom dasar pemrosesan dan urutan pertanyaan adalah penafsiran bab.

- UU 27/2022: teks dibaca dari salinan resmi. Pasal 46 ayat (1) menulis paling lambat
  3 x 24 jam tanpa frasa titik mulai. Pasal 30, 32, 40, dan 41 memakai frasa "terhitung sejak".
- Putusan MK 151/PUU-XXII/2024: amar menyatakan kata "dan" pada Pasal 53 ayat (1) huruf b
  tidak mengikat secara bersyarat sepanjang tidak dimaknai "dan/atau".
- PP 28/2024 Pasal 966, 971, dan 972 dibaca dari naskah resmi. Lokasi dan transfer data
  kesehatan dinilai lebih dahulu dengan pasal itu, lalu bersama Pasal 56 UU PDP.
- PP 33/2026: naskah resmi belum diperoleh. Pasal yang disebut bab berasal dari salinan pihak
  ketiga (Meridian Hukum, yang menyebut JDIH Setneg) dan ringkasan RSM Indonesia, sehingga
  statusnya pemantauan. Mulai berlaku menurut sumber itu 16 Januari 2027.
- Lembaga pelindungan data pribadi dan Perpresnya: berita Juli sampai September 2026 masih
  menyebut proses, dan naskah Perpres belum ditemukan. Kanal pemberitahuan kepada lembaga
  harus diperiksa ulang pada tanggal kerja tim.
