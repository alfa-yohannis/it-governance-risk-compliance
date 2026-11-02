<!-- Kegunaan: indeks berkas Aktivitas Bab 05. Cara pakai: salin templat ke folder tim, baca petunjuk, dan pisahkan contoh pengandaian dari bukti organisasi. -->

# Sumber Bab 05

| Berkas | Kegunaan |
| --- | --- |
| `risk-appetite.md` | Templat dan contoh arah risiko, ukuran, tindakan, kapasitas, serta empat pertanyaan uji. |
| `kriteria-risiko.md` | Skala pembelajaran, kelompok skor, dan batas penggunaan skor. |
| `risk-register.csv` | Register kosong untuk 10 sampai 15 skenario. |
| `contoh-risk-register-medikara.csv` | Dua belas skenario terisi; seluruh detail tambahan adalah pengandaian. |
| `analisis-sensitivitas.csv` | Tiga asumsi peluang dan tiga uji tambahan untuk menghitung harapan kerugian dan manfaat bersih. |
| `kurva-kerugian.csv` | Hitungan tangan peluang kerugian R-01 melampaui ambang, sebelum dan sesudah AC-01. |
| `simulasi-kerugian.py` | Simulasi Monte Carlo opsional untuk R-01 dan R-03, dengan benih tetap. |

## Cara memakai

1. Baca tujuan dan Aktivitas pada bab, lalu tetapkan ruang lingkup serta peran tim.
2. Salin berkas isian; pertahankan berkas contoh sebagai pembanding.
3. Sepakati skala di `kriteria-risiko.md` sebelum menilai skenario apa pun.
4. Isi sumber bukti, pemilik, keputusan, dan hal yang belum diketahui.
5. Tinjau bersama anggota berlatar nonteknis dan teknis sebelum pengumpulan.

Berkas CSV memakai UTF-8 dan pemisah koma. Baris pertama berisi komentar kegunaan,
dan nama kolom ada pada baris kedua. Hapus baris komentar bila aplikasi spreadsheet
atau alat impor tidak menerimanya. Buka melalui menu impor bila pemisah lokal berbeda.
Seluruh angka tambahan pada contoh adalah pengandaian pembelajaran.
Data organisasi nyata harus berizin dan anonim; jangan menyalin data pasien,
rahasia akses, atau dokumen asli organisasi ke folder tugas.

## Menghitung sensitivitas

Kerugian harapan = peluang kejadian per tahun dikali kerugian bersyarat.
Manfaat bersih = harapan awal dikurangi harapan sisa dikurangi biaya kontrol.
Model mengasumsikan paling banyak satu kejadian per tahun dan tidak mengubah
kewajiban keselamatan atau hukum. Bandingkan seluruh baris, bukan hanya angka tengah.

## Menjalankan simulasi (opsional)

Jalankan `python simulasi-kerugian.py`. Skrip hanya memakai pustaka standar Python
dan tidak membaca atau menulis berkas. Dengan 200.000 tahun simulasi dan benih 2026,
hasilnya dekat dengan hitungan tangan pada `kurva-kerugian.csv`.
