# Sumber Bab 03: Lanskap Regulasi dan Kewajiban Kepatuhan

| Berkas | Kegunaan |
| --- | --- |
| `register-kewajiban.csv` | Contoh enam belas kewajiban hukum, kontrak, dan standar dengan pemilik, bukti, serta status. Baris pertama berisi komentar kegunaan; baris kedua berisi nama kolom. Sama dengan tabel register pada Bab 03. |
| `daftar-regulasi-medikara.md` | Daftar sumber resmi, pasal yang dibaca bab, cakupan, dan pemantauan PP 33/2026. |
| `panduan-menurunkan-pasal.md` | Langkah penurunan pasal, contoh Pasal 46 UU PDP dan Pasal 20 Permenkes 24/2022, lembar isian, lima status, dan kendali mutu. |
| `periksa-register.py` | Skrip Python opsional untuk memeriksa kelengkapan kolom register dan menghitung sebaran status. Tidak menilai kebenaran hukum. |

## Cara memakai

1. Salin berkas ke folder kerja tim; simpan versi contoh untuk pembanding.
2. Baca panduan Markdown sebelum mengisi CSV. CSV memakai UTF-8 dan pemisah koma. Buang baris komentar bila aplikasi tidak mengenalinya, sehingga baris pertama berisi nama kolom.
3. Pilih contoh fiktif Medikara atau ganti dengan informasi organisasi yang telah memberi izin.
4. Isi bagian bertanda `...` dan tambahkan baris sesuai kebutuhan. Tanda ini adalah ruang kerja mahasiswa, bukan data contoh.
5. Tulis sumber, tanggal, pemilik, serta alasan keputusan. Jangan mengubah dugaan menjadi fakta.
6. Tinjau silang oleh anggota lain sebelum artefak digabung ke C1.
7. Jalankan `python periksa-register.py register-kewajiban.csv` bila ingin memeriksa kelengkapan. Langkah ini opsional.

Semua angka tambahan dalam contoh merupakan pengandaian untuk pembelajaran, termasuk batas kontrak 12 jam dan 1 jam serta status tiap baris. Isi hukum pada contoh sudah dicocokkan dengan naskah resmi pada 31 Oktober 2026, tetapi tim tetap memeriksa ulang status aturan pada tanggal kerjanya. Berkas ini bahan belajar, bukan nasihat hukum, dan tidak memuat data pribadi pasien atau karyawan. Tim menyimpan bukti asli pada tempat yang diizinkan organisasi dan hanya mencatat rujukan serta data agregat pada capstone.

## Hasil dan penilaian

Register dan daftar regulasi masuk C1. Kewajiban hukum, kontrak, serta standar sukarela diberi kategori terpisah dan dipakai ulang pada Bab 5, Bab 7, dan Bab 12. Baris kontrak vendor juga berguna pada Bab 9.

Ketepatan cakupan serta sumber 30 persen; kewajiban yang dapat diuji 30 persen; pemilik dan bukti 25 persen; konsistensi status dan keterkaitan kontrol 15 persen.

Tidak diperlukan pemrograman. CSV dapat dibuka dengan aplikasi spreadsheet atau editor teks. Pilih UTF-8 dan pemisah koma jika aplikasi tidak mengenali kolom secara otomatis.
