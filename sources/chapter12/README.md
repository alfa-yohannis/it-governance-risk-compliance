<!-- Daftar sumber Bab 12; lakukan pemeriksaan manual sebelum membandingkan hasil skrip. -->
# Sumber Bab 12: Audit TI dan Asurans

| Berkas | Kegunaan |
| --- | --- |
| rencana-asurans.csv | Semesta audit dan rencana dua tahun, dengan skor prioritas dan jam |
| peta-asurans.csv | Siapa memberi keyakinan pada tiap area, serta celah dan pengulangannya |
| program-audit-hak-akses.md | Kriteria AC-01, prosedur, dan batas kesimpulan |
| sampel-ac01-30-akun.csv | Sampel 30 dari 120 akun vendor sintetis, dari satu lokasi |
| uji_sampel_ac01.py | Menghitung 24 dari 30 dan batas statistik sampel, memakai pustaka standar |
| hasil-sampel-ac01.json | Keluaran acuan uji_sampel_ac01.py, tanggal acuan 31 Maret 2026 |
| data-contoh-hak-akses.csv | Delapan akun sintetis satu rumah sakit; tidak memuat data pasien |
| audit_hak_akses.py | Pemeriksaan lokal delapan baris dengan Python pustaka standar |
| hasil-audit-contoh.json | Keluaran acuan audit_hak_akses.py, tanggal acuan 30 Oktober 2026 |
| templat-temuan-audit.md | Kondisi, kriteria, sebab, akibat, tindakan, verifikasi |
| contoh-temuan-ta01.md | Contoh temuan TA-01 yang terisi, sebagai pembanding |

Buka CSV UTF-8 dengan pemisah koma. Baris pertama berawalan # adalah komentar; buang
baris itu bila aplikasi tidak mengenalinya. Periksa manual seluruh baris, kemudian
jalankan dari folder bab bila Python 3 tersedia:

~~~text
python uji_sampel_ac01.py
python audit_hak_akses.py
python audit_hak_akses.py data-contoh-hak-akses.csv --tanggal 2026-10-30
~~~

Hasil acuan sampel: 24 akun sesuai, 6 akun menyimpang (20 persen). Bila sampel itu
acak, perkiraan titiknya 24 dari 120 akun dengan batas 13 sampai 40 akun. Hasil 0 dari
30 masih menyisakan batas atas 9 akun. Satu akun bermasalah hanya tertangkap dengan
peluang 25 persen. Sampel contoh berasal dari satu lokasi, sehingga batas ini
memperlihatkan cara membaca, bukan estimasi Medikara.

Hasil acuan delapan baris: 7 akun aktif, 3 akun berindikasi, 4 indikasi, 5 tinjauan
tepat waktu (71,43 persen). Akun tidak aktif dipisahkan; satu akun dapat memiliki
beberapa indikasi. Tanpa populasi aktif, persentase bernilai null. Kolom hilang,
identitas ganda, dan tanggal tinjau masa depan ditolak. Indikasi bukan temuan final;
persetujuan dan penyebab memerlukan konfirmasi.

Kedua skrip hanya membaca berkas lokal dan tidak mengakses sistem apa pun. Data
organisasi nyata wajib berizin dan dianonimkan. Data pribadi pasien atau karyawan tidak
boleh dipakai. Luaran masuk tonggak C4.
