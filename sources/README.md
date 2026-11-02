# Sumber Modul

Direktori ini memuat berkas pendukung tiap bab: lembar kerja, templat, data
studi kasus, dan berkas teknis opsional yang dirujuk dari naskah modul.

Susunannya satu subdirektori per bab, dari `chapter01` sampai `chapter14`.
Naskah bab merujuk berkas di sini dengan penulisan seperti
`sources/chapter02/matriks-hak-keputusan.csv`, sehingga mahasiswa dapat memakai
templat yang sama tanpa menyalin ulang dari halaman cetak. Setiap subdirektori
punya `README.md` berisi daftar berkas dan cara memakainya.

| Bab | Isi | Tonggak |
| --- | --- | --- |
| [01](chapter01/README.md) | Templat profil organisasi, peta pemangku kepentingan, register GRC awal, panduan izin dan anonimisasi | C1 |
| [02](chapter02/README.md) | Matriks hak keputusan, templat piagam komite pengarah TI, lembar telaah penelitian | C1 |
| [03](chapter03/README.md) | Register kewajiban, daftar regulasi Medikara, panduan menurunkan pasal, skrip pemeriksa register | C1 |
| [04](chapter04/README.md) | Lembar faktor desain, *goals cascade*, katalog 40 objektif, skor prioritas lokal, lembar bukti kapabilitas | C2 |
| [05](chapter05/README.md) | Pernyataan *risk appetite*, kriteria risiko, templat dan contoh *risk register*, analisis sensitivitas, kurva kerugian, skrip simulasi kerugian | C2 |
| [06](chapter06/README.md) | Profil CSF saat ini beserta contohnya, pemetaan CSF ke Annex A, daftar celah kontrol, catatan SoA, panduan bukti | C2 |
| [07](chapter07/README.md) | Catatan pemrosesan beserta contohnya, penyaringan penilaian dampak, kronologi insiden vendor 2025, templat notifikasi, analisis celah PDP, skrip hitung tenggat | C2 |
| [08](chapter08/README.md) | Model tata kelola target, RACI beserta contohnya, target kapabilitas dan profil target CSF, daftar kebijakan | C3 |
| [09](chapter09/README.md) | Klasifikasi vendor, kuesioner uji tuntas, klausul kontrak, peta ketergantungan, matriks cloud, templat dan contoh DPIA | C3 |
| [10](chapter10/README.md) | Templat dan contoh BIA, perbandingan strategi, praktik DSS04, rencana uji pemulihan, skenario *tabletop ransomware* | C3 |
| [11](chapter11/README.md) | Inventaris AI beserta contohnya, rencana evaluasi dan contoh hasil uji, daftar cek OWASP LLM, templat kebijakan AI | C3 |
| [12](chapter12/README.md) | Peta dan rencana asurans, program audit hak akses, data contoh dan sampel 30 akun, templat dan contoh temuan, skrip audit dan uji sampel | C4 |
| [13](chapter13/README.md) | Katalog indikator, data indikator, *dashboard* contoh, templat laporan direksi, skrip hitung indikator | C4 |
| [14](chapter14/README.md) | Peta jalan GRC, beban jam, pemetaan kontrol, kriteria alat GRC, catatan perpanjangan TA-01, templat presentasi C4, skrip pemeriksa peta jalan | C4 |

Berkas Markdown memuat petunjuk, contoh Medikara yang ditandai sebagai skenario,
ruang isian, dan kriteria pemeriksaan. CSV memakai baris pertama sebagai komentar
kegunaan dan baris kedua sebagai nama kolom; buang baris komentar bila aplikasi
spreadsheet tidak mengenalinya.

Panduan penggabungan luaran dan batas data ada di
[panduan-capstone.md](panduan-capstone.md). Seluruh angka dan kejadian di dalam
berkas contoh rekaan, mengikuti kasus Medikara Health. Data pribadi pasien atau
karyawan tidak boleh dimasukkan ke templat. Skrip teknis bersifat opsional;
aktivitas utama tetap dapat dikerjakan tanpa pemrograman.
