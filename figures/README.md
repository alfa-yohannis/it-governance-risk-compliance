# Gambar Modul dan Slide

Folder ini menyimpan gambar yang dipakai bersama oleh modul dan slide, supaya kedua
versi menampilkan gambar yang sama.

- Diagram TikZ `chNN-nama.tex` hanya berisi satu `tikzpicture` tanpa preamble. Modul
  memanggil `\input{../figures/chNN-nama.tex}`, slide memanggil
  `\input{../../figures/chNN-nama.tex}`.
- Diagram konsep `chNN-diagram-konsep.png`, dengan versi vektor `chNN-diagram-konsep.svg`,
  dibangkitkan `tools/render-diagrams.py` dari `chapter-diagrams.json`. Ringkasan per bab ada
  di [`ILLUSTRATIONS.md`](ILLUSTRATIONS.md). Bab memasangnya bersyarat dengan `\IfFileExists`.
- Ilustrasi JPG `chNN-nama.jpg` tanpa teks di dalam gambar disimpan sebagai arsip. Prompt
  pembuatannya ada di `illustration-prompts.json`. Keempat belas berkas JPG tidak dipasang
  pada bab atau slide, karena diagram TikZ dan diagram konsep sudah cukup.
- `logo_universitas.png` dan `building.png` adalah berkas asli untuk halaman judul modul
  dan tema slide.

Kolom Isi mengikuti caption gambar di naskah bab. Untuk JPG, kolom Isi meringkas adegan pada
prompt pembuatannya.

| Berkas | Dipakai di | Isi |
| --- | --- | --- |
| `ch01-alur.tex` | Bab 1; Slide 1 | Siklus tujuan, keputusan, dan bukti untuk pekerjaan GRC |
| `ch01-bahasa-bersama-grc.jpg` | Arsip, tidak dipasang | Klinisi, manajer bisnis, teknisi, dan petugas kepatuhan menghubungkan kemudi, penanda bahaya, dan daftar periksa di sekitar layanan kesehatan mini |
| `ch01-capstone.tex` | Bab 1; Slide 1 | Empat mata kuliah mengisi satu cetak biru lewat empat tonggak |
| `ch01-diagram-konsep.png` | Bab 1; Slide 1 | Dari tujuan layanan ke kontrol dan bukti GRC |
| `ch01-grc-terpadu.tex` | Bab 1; Slide 1 | GRC terpadu: tiga fungsi berbagi satu tujuan, satu register, dan satu dasar peninjauan |
| `ch01-peta-pemangku.tex` | Bab 1; Slide 1 | Peta pemangku kepentingan Medikara untuk pemicu insiden vendor (penilaian contoh) |
| `ch01-tata-kelola-manajemen.tex` | Bab 1; Slide 1 | Pembagian tugas dan arus informasi antara tata kelola dan manajemen |
| `ch02-alur.tex` | Bab 2; Slide 2 | Siklus EDM dengan pelibatan pemangku kepentingan pada keputusan Medikara+ |
| `ch02-arah-dan-tanggung-jawab.jpg` | Arsip, tidak dipasang | Direksi rumah sakit menetapkan arah dengan roda navigasi, lalu tim operasional menjalankan pekerjaan lewat serah terima yang jelas |
| `ch02-diagram-konsep.png` | Bab 2; Slide 2 | *Evaluate, Direct, Monitor* dengan pelibatan pemangku kepentingan |
| `ch02-matriks-arketipe.tex` | Bab 2; Slide 2 | Matriks hak keputusan pengandaian Medikara: lima keputusan dan enam arketipe menurut Weill dan Ross |
| `ch02-mekanisme.tex` | Bab 2; Slide 2 | Tiga mekanisme tata kelola dan akibat bila salah satunya hilang |
| `ch02-organ-perseroan.tex` | Bab 2; Slide 2 | Organ perseroan, forum komite, dan pemilik hasil pada pengandaian Medikara |
| `ch02-rantai-nilai.tex` | Bab 2; Slide 2 | Rantai tata kelola, keselarasan, dan kinerja beserta contoh pengandaian Medikara |
| `ch03-aliran-mitra.tex` | Bab 3; Slide 3 | Aturan yang mengikat langsung dan syarat yang mengalir lewat kontrak |
| `ch03-alur.tex` | Bab 3; Slide 3 | Jejak satu baris register dari pasal sampai status |
| `ch03-diagram-konsep.png` | Bab 3; Slide 3 | Menurunkan sumber hukum menjadi kewajiban yang dapat diuji |
| `ch03-hierarki.tex` | Bab 3; Slide 3 | Kedudukan aturan yang dibaca Medikara menurut Pasal 7 dan Pasal 8 UU 12/2011 |
| `ch03-jam-pelaporan.tex` | Bab 3; Slide 3 | Batas waktu pelaporan yang berbeda pada satu kejadian (angka kontrak adalah pengandaian) |
| `ch03-lokasi-data.tex` | Bab 3; Slide 3 | Pertanyaan desain untuk penyimpanan rekam medis oleh pihak lain (penafsiran bab) |
| `ch03-peta-kewajiban.jpg` | Arsip, tidak dipasang | Tim kepatuhan memetakan kewajiban ke unit klinik dengan map bertab warna dan rak bukti |
| `ch04-alur.tex` | Bab 4; Slide 4 | Desain tata kelola dimulai dari konteks dan diakhiri dengan bukti prioritas |
| `ch04-cakupan-desain.tex` | Bab 4; Slide 4 | Faktor desain dipakai bertahap untuk menyusun cakupan sistem tata kelola |
| `ch04-diagram-konsep.png` | Bab 4; Slide 4 | COBIT 2019: tujuan, faktor desain, dan bukti kapabilitas |
| `ch04-model-inti.tex` | Bab 4; Slide 4 | Lima domain model inti COBIT 2019 dan enam objektif awal pengandaian Medikara |
| `ch04-rantai-tujuan.tex` | Bab 4; Slide 4 | Rantai tujuan dan penyaringan objektif menurut contoh Kadam |
| `ch04-sistem-tata-kelola-yang-sesuai.jpg` | Arsip, tidak dipasang | Tim lintas fungsi memilih komponen yang sesuai dari kotak alat untuk menyusun sistem tata kelola di sekitar rumah sakit mini |
| `ch04-tangga-kapabilitas.tex` | Bab 4; Slide 4 | Tingkat kapabilitas proses COBIT 2019 sebagai tangga |
| `ch05-batas-risiko.tex` | Bab 5; Slide 5 | Kapasitas, *risk appetite*, *risk tolerance*, dan indikator untuk R-01 (misalkan) |
| `ch05-diagram-konsep.png` | Bab 5; Slide 5 | Skenario risiko dinilai terhadap tujuan dan kriteria |
| `ch05-kurva-kerugian.tex` | Bab 5; Slide 5 | *Loss exceedance curve* R-01 sebelum dan sesudah AC-01 (misalkan) |
| `ch05-matriks-risiko.tex` | Bab 5; Slide 5 | Matriks 5 x 5 dengan 12 skenario register contoh (misalkan) |
| `ch05-proses-risiko.tex` | Bab 5; Slide 5 | Proses dari konteks hingga keputusan risiko |
| `ch05-risiko-dan-keputusan.jpg` | Arsip, tidak dipasang | Pimpinan layanan kesehatan menilai bahaya pada rute layanan pasien dan memilih perlindungan yang sepadan |
| `ch05-skenario-r01.tex` | Bab 5; Slide 5 | Skenario R-01: sebab, kejadian, akibat, dan letak kontrol |
| `ch06-diagram-konsep.png` | Bab 6; Slide 6 | ISMS menghubungkan risiko, kontrol, dan hasil keamanan |
| `ch06-enam-fungsi.tex` | Bab 6; Slide 6 | Govern mengarahkan lima fungsi lain yang saling berhubungan |
| `ch06-keamanan-sebagai-sistem.jpg` | Arsip, tidak dipasang | Layanan informasi kesehatan dilindungi beberapa lapisan: kesadaran staf, penyimpanan aman, pemantauan, dan area pemulihan |
| `ch06-keterlacakan-celah.tex` | Bab 6; Slide 6 | Keterlacakan tiga celah prioritas (misalkan) |
| `ch06-langkah-profil.tex` | Bab 6; Slide 6 | Lima langkah membuat dan memakai profil, dengan keluaran Medikara (misalkan) |
| `ch06-rantai-soa.tex` | Bab 6; Slide 6 | Rantai dari risiko ke SoA dan bukti operasi |
| `ch06-sistem-keamanan.tex` | Bab 6; Slide 6 | Klausul 4 sampai 10 sebagai satu sistem kerja |
| `ch07-alur-insiden.tex` | Bab 7; Slide 7 | Alur keputusan ketika kegagalan pelindungan terdeteksi |
| `ch07-data-pribadi-dengan-tujuan.jpg` | Arsip, tidak dipasang | Pasien dan staf berwenang meninjau kartu informasi; hanya kartu yang diperlukan masuk baki aman |
| `ch07-diagram-konsep.png` | Bab 7; Slide 7 | Tujuan dan dasar pemrosesan mengendalikan alur data pribadi |
| `ch07-jam-pertama.tex` | Bab 7; Slide 7 | Jam-jam pertama sesudah Medikara mengetahui kejadian (misalkan; skala tidak proporsional) |
| `ch07-lapis-transfer.tex` | Bab 7; Slide 7 | Pertanyaan berurutan untuk lokasi dan transfer data pasien (penafsiran bab) |
| `ch07-peran-pemrosesan.tex` | Bab 7; Slide 7 | Pengendali, prosesor, dan letak tanggung jawab (penafsiran bab) |
| `ch07-titik-mulai.tex` | Bab 7; Slide 7 | Fakta latihan insiden 2025 dan tiga pembacaan rentang 72 jam (jam adalah pengandaian) |
| `ch08-alur-berbagi-data.tex` | Bab 8; Slide 8 | Alur persetujuan pembukaan data kepada mitra dalam 10 hari kerja (misalkan) |
| `ch08-desain-target.tex` | Bab 8; Slide 8 | Empat tahap panduan desain dan penerapannya pada capstone |
| `ch08-diagram-konsep.png` | Bab 8; Slide 8 | Rancangan tata kelola target berawal dari celah yang terbukti |
| `ch08-hierarki-kebijakan.tex` | Bab 8; Slide 8 | Arsitektur kebijakan dan penyetujunya (misalkan) |
| `ch08-peta-peran.tex` | Bab 8; Slide 8 | Forum dan peran pada Three Lines Model (misalkan) |
| `ch08-target-bertingkat.tex` | Bab 8; Slide 8 | Target kapabilitas bertingkat dibanding usulan tingkat 4 (misalkan) |
| `ch08-tata-kelola-target.jpg` | Arsip, tidak dipasang | Perwakilan operasi, teknologi, risiko, dan pimpinan menata gerbang keputusan, dengan tongkat tanggung jawab berpindah ke pemilik yang tepat |
| `ch09-alur-dpia.tex` | Bab 9; Slide 9 | Alur DPIA untuk berbagi data dengan mitra (penafsiran bab) |
| `ch09-diagram-konsep.png` | Bab 9; Slide 9 | Risiko konsentrasi tersembunyi di balik beberapa vendor |
| `ch09-garis-waktu-kontrak.tex` | Bab 9; Slide 9 | Klausul laporan 12 jam pada garis waktu pemberitahuan (misalkan) |
| `ch09-peta-ketergantungan.tex` | Bab 9; Slide 9 | Peta ketergantungan pihak ketiga dan pihak keempat (misalkan) |
| `ch09-rantai-kepercayaan-mitra.jpg` | Arsip, tidak dipasang | Tim layanan menilai vendor dan fasilitas cloud melintasi jembatan terkendali, dengan titik uji tuntas, serah terima kontrak, pemantauan, dan jalur keluar |
| `ch09-siklus-vendor.tex` | Bab 9; Slide 9 | Siklus kendali pihak ketiga dari klasifikasi sampai keluar |
| `ch09-tanggung-jawab-cloud.tex` | Bab 9; Slide 9 | Pembagian lapisan menurut panduan Microsoft; kontrak layanan tetap menentukan |
| `ch10-alur.tex` | Bab 10; Slide 10 | Alur keputusan kelangsungan bisnis dan ketahanan operasional |
| `ch10-antrean.tex` | Bab 10; Slide 10 | Antrean pendaftaran selama dan sesudah gangguan enam jam di Bekasi (misalkan) |
| `ch10-diagram-konsep.png` | Bab 10; Slide 10 | Kelangsungan layanan memerlukan jalur bisnis dan teknologi |
| `ch10-eskalasi.tex` | Bab 10; Slide 10 | Tiga tingkat eskalasi: insiden, krisis organisasi, dan Krisis Siber |
| `ch10-garis-waktu.tex` | Bab 10; Slide 10 | Letak RPO, RTO, MTPD, dan kapasitas minimum pada satu gangguan farmasi |
| `ch10-ketergantungan.tex` | Bab 10; Slide 10 | Ketergantungan enam layanan pada sistem dan pihak pendukung (rancangan target) |
| `ch10-layanan-esensial-tetap-berjalan.jpg` | Arsip, tidak dipasang | Staf menjaga rute layanan esensial saat satu sayap rumah sakit terganggu, sementara tim pemulihan berlatih memulihkan peralatan dari perangkat cadangan |
| `ch11-alur.tex` | Bab 11; Slide 11 | Alur keputusan tata kelola kecerdasan artifisial |
| `ch11-diagram-konsep.png` | Bab 11; Slide 11 | AI dikelola menurut tujuan, dampak, dan kemampuan pengawasan |
| `ch11-jalur-kebijakan.tex` | Bab 11; Slide 11 | Tiga jalur kebijakan pemakaian AI (misalkan) |
| `ch11-klasifikasi.tex` | Bab 11; Slide 11 | Urutan pertanyaan klasifikasi menurut EU AI Act |
| `ch11-lapis-acuan.tex` | Bab 11; Slide 11 | Lapis acuan yang masuk ke kebijakan pemakaian AI |
| `ch11-pengawasan-ai.jpg` | Arsip, tidak dipasang | Asisten AI mengajukan rekomendasi kepada panel peninjau manusia, dengan ruang kerja terbatas dan tuas henti di tangan manusia |
| `ch11-waktu-bersih.tex` | Bab 11; Slide 11 | Waktu per ringkasan: klaim, hasil uji, dan pemeriksaan yang diperpanjang (misalkan) |
| `ch12-alur.tex` | Bab 12; Slide 12 | Siklus asurans dari mandat sampai tindak lanjut terverifikasi |
| `ch12-bukti-dan-asurans.jpg` | Arsip, tidak dipasang | Peninjau independen memeriksa sampel bukti operasional dan menelusuri satu butir daftar periksa ke proses nyata |
| `ch12-diagram-konsep.png` | Bab 12; Slide 12 | Pengelolaan risiko dan asurans independen mempunyai peran berbeda |
| `ch12-populasi-sampel.tex` | Bab 12; Slide 12 | Tiga pemeriksaan dari populasi 120 akun vendor |
| `ch12-rancangan-operasi.tex` | Bab 12; Slide 12 | Empat keadaan kontrol menurut hasil uji rancangan dan uji operasi |
| `ch12-tiga-lini.tex` | Bab 12; Slide 12 | Three Lines Model pada kontrol AC-01 (misalkan) |
| `ch12-unsur-temuan.tex` | Bab 12; Slide 12 | Hubungan unsur temuan pada TA-01 (misalkan) |
| `ch13-alur.tex` | Bab 13; Slide 13 | Alur dari tujuan dan risiko sampai keputusan |
| `ch13-ambang-pendaftaran.tex` | Bab 13; Slide 13 | Zona ambang IK-03 dari RTO Bab 10 dan batas Bab 5 (misalkan) |
| `ch13-dashboard-oktober.tex` | Bab 13; Slide 13 | *Dashboard* GRC Medikara, Oktober 2026 (misalkan) |
| `ch13-diagram-konsep.png` | Bab 13; Slide 13 | Indikator yang berbeda memicu keputusan yang berbeda |
| `ch13-laporan-satu-halaman.tex` | Bab 13; Slide 13 | Susunan laporan GRC satu halaman (misalkan) |
| `ch13-rantai-r01.tex` | Bab 13; Slide 13 | Rantai kejadian R-01 dan indikator pada tiap titik (misalkan) |
| `ch13-sinyal-untuk-direksi.jpg` | Arsip, tidak dipasang | Direksi membaca sedikit indikator visual yang terhubung ke kegiatan klinik, termasuk satu ambang yang memicu tindakan |
| `ch14-alat-grc.tex` | Bab 14; Slide 14 | Urutan memilih alat GRC pada Medikara (misalkan) |
| `ch14-alur.tex` | Bab 14; Slide 14 | Alur keputusan alat GRC dan peta jalan tata kelola terpadu |
| `ch14-anggaran.tex` | Bab 14; Slide 14 | Uang baru peta jalan dibandingkan anggaran modernisasi (misalkan) |
| `ch14-diagram-konsep.png` | Bab 14; Slide 14 | Satu kontrol terhubung ke risiko, kewajiban, dan bukti |
| `ch14-lintas-bab.tex` | Bab 14; Slide 14 | Asal angka peta jalan dari tonggak C1 sampai C4 (misalkan) |
| `ch14-peta-jalan.tex` | Bab 14; Slide 14 | Peta jalan GRC tiga tahun Medikara (misalkan) |
| `ch14-peta-jalan-grc-terpadu.jpg` | Arsip, tidak dipasang | Tim tata kelola menyatukan map bukti dan alat proses pada satu meja kerja, lalu jalur bertahap menuju tiga stasiun layanan |
