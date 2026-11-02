<!-- Daftar sumber Bab 13; hitung rasio lalu tulis keputusan yang didukung angka. -->
# Sumber Bab 13: Indikator dan Laporan Direksi

| Berkas | Kegunaan |
| --- | --- |
| katalog-indikator.csv | Dua belas definisi: rumus, sumber, pemilik, ambang, tindakan, dan dasar ambang |
| data-indikator.csv | Tiga periode agregat sintetis, Agustus sampai Oktober 2026 |
| hitung_indikator.py | Menghasilkan dashboard CSV secara lokal dengan pustaka standar |
| dashboard-contoh.csv | Keluaran terhitung untuk ketiga periode |
| templat-laporan-direksi.md | Tiga pesan utama, satu permintaan keputusan, dan contoh terisi |

CSV memakai UTF-8 dan pemisah koma. Baris pertama yang diawali tanda pagar adalah
komentar. Hitung manual, atau jalankan:

~~~text
python hitung_indikator.py
python hitung_indikator.py data-indikator.csv > dashboard-lokal.csv
~~~

Rasio dihitung pembilang/penyebut kali 100. Nilai sebelum pembulatan dipakai untuk
status; nilai tampilan dibulatkan dua desimal. Penyebut nol dengan pembilang nol
menghasilkan TIDAK_BERLAKU. Data kosong menghasilkan DATA_TIDAK_TERSEDIA. Pembilang
melebihi penyebut, jumlah negatif, periode ganda, dan kolom hilang ditolak. Jangan
menyebut data tidak tersedia sebagai hijau.

Ambang KRI mengikuti batas Bab 5. IK-01, IK-02, IK-04, IK-05, dan IK-06 memakai
toleransi nol, sehingga tidak memiliki zona kuning. IK-03 memakai RTO 90 menit dari
Bab 10 dan batas 2 jam per bulan dari Bab 5. IK-07 mengikuti tabel pengantar Bab 5.
IK-08 memakai status terburuk dari rasio gabungan dan rasio rumah sakit. IK-11 tidak
memiliki zona kuning. Ambang lain adalah keputusan skenario, bukan batas universal.

Hasil yang perlu cocok dengan naskah: IK-07 Agustus, September, Oktober = 85, 90, 95
persen dari 120 akun. IK-01 = 3, 2, 1 dan seluruhnya merah. IK-08 tiga bulan = 29 dari
36 uji, dengan rumah sakit 3 dari 5, sama dengan Bab 10. IK-11 September dan Oktober
tidak berlaku karena tidak ada pemberitahuan wajib.

Data tiga periode ini berbeda dari contoh 7 akun aktif pada 30 Oktober 2026 di Bab 12,
karena contoh itu hanya mencakup satu rumah sakit. Skrip sengaja tidak menghitung skor
gabungan. Luaran masuk C4.
