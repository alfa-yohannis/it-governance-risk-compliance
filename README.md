# IT Governance, Risk & Compliance

IT40813 · Magister Teknologi Informasi, peminatan Digital Enterprise Architecture, Universitas Pradita.

Mata kuliah ini membahas cara organisasi mengarahkan dan mengawasi pemakaian TI (teknologi informasi), mengendalikan risikonya, dan memenuhi kewajiban hukum serta standar yang berlaku. Ketiga hal itu biasa diringkas sebagai GRC (*Governance, Risk, and Compliance*). Setiap topik dibuka dengan masalah organisasi yang nyata. Misalnya, siapa yang berhak menyetujui investasi TI, bagaimana direksi tahu bahwa data pasien aman, atau apa yang harus dilakukan ketika vendor membocorkan data. Setelah masalahnya jelas, barulah kerangka dan istilahnya dipakai: ISO/IEC 38500, COBIT, ITIL, ISO 31000, ISO/IEC 27001, NIST CSF, UU Pelindungan Data Pribadi, ISO 22301, dan ISO/IEC 42001. Pada tingkat magister, menghafal kerangka tidak cukup. Mahasiswa diminta memilih, menimbang *trade-off*, membaca laporan industri dan artikel ilmiah, lalu menuliskan alasan keputusannya.

Peserta mata kuliah ini berasal dari latar belakang yang beragam. Sebagian berlatar bisnis, manajemen, akuntansi, hukum, atau kesehatan. Sebagian lagi berlatar ilmu komputer, rekayasa perangkat lunak, atau TI. Seluruh materi inti dapat diikuti tanpa kemampuan memprogram. Mahasiswa berlatar teknis mendapat pendalaman teknis opsional di setiap pertemuan. Mata kuliah ini dijalankan bersama [IT40513 Enterprise Architecture & Digital Blueprint](https://github.com/alfa-yohannis/enterprise-architecture-digital-blueprint), [IT40613 Digital Platform & API Economy](https://github.com/alfa-yohannis/digital-platform-api-economy), dan [IT40713 Cloud-Native & Microservices Architecture](https://github.com/alfa-yohannis/cloud-native-microservices-architecture) sebagai satu proyek capstone. Tiap tim menyusun "Cetak Biru Transformasi Digital" untuk satu organisasi, dan mata kuliah ini menyumbang sisi tata kelola, risiko, dan kepatuhannya. Tatap muka hanya berlangsung pada hari Sabtu untuk membahas progres proyek. Karena itu modul dan slide disusun agar dapat dipelajari mandiri.

## Peta Pertemuan

Urutan pertemuan mengikuti empat tonggak capstone. Pertemuan 1 sampai 3 membangun konteks: siapa yang memutuskan dan aturan apa yang mengikat. Pertemuan 4 sampai 7 memotret kondisi saat ini, lalu hasilnya ditinjau menjelang UTS (Ujian Tengah Semester). Pertemuan 8 sampai 11 merancang kondisi target. Pertemuan 12 sampai 14 menutup dengan asurans, pengukuran, dan peta jalan yang dipresentasikan menjelang UAS (Ujian Akhir Semester). Kolom terakhir menunjukkan luaran yang disumbangkan ke tiap tonggak.

| # | Pertemuan | Aktivitas | Luaran Capstone |
| --- | --- | --- | --- |
| 1 | **Orientasi Mata Kuliah dan Dasar-Dasar GRC** | Membentuk tim, memilih organisasi, lalu memetakan pemicu GRC dan pemangku kepentingan | C1: profil organisasi dan peta pemangku kepentingan |
| 2 | Prinsip Tata Kelola TI dan Peran Direksi | Menyusun matriks hak keputusan TI dan rancangan piagam komite pengarah TI | C1: matriks hak keputusan dan piagam komite |
| 3 | Lanskap Regulasi dan Kewajiban Kepatuhan | Menurunkan pasal UU PDP, aturan rekam medis, PSTE, dan BSSN menjadi kewajiban yang dapat diperiksa | C1: register kewajiban kepatuhan |
| 4 | COBIT 2019: Sistem Tata Kelola dan Faktor Desain | Menerapkan faktor desain dan *goals cascade*, lalu menilai cepat kapabilitas saat ini | C2: objektif prioritas dan potret kapabilitas |
| 5 | Manajemen Risiko Enterprise dan Risiko TI | Merumuskan *risk appetite* dan mengisi *risk register* kondisi saat ini | C2: pernyataan *risk appetite* dan *risk register* |
| 6 | Keamanan Informasi: ISO/IEC 27001 dan NIST CSF 2.0 | Menyusun profil saat ini NIST CSF dan daftar celah kontrol ISO/IEC 27001 | C2: profil keamanan saat ini dan daftar celah |
| 7 | Pelindungan Data Pribadi dalam Praktik | Mencatat kegiatan pemrosesan data pribadi dan menganalisis insiden kebocoran lewat vendor | C2: catatan pemrosesan data dan analisis celah PDP |
| 8 | Merancang Sistem Tata Kelola Target | Merancang struktur, RACI, target kapabilitas, dan profil target keamanan | C3: model tata kelola target |
| 9 | Risiko Pihak Ketiga dan Cloud | Mengklasifikasi vendor, mengisi matriks tanggung jawab cloud, dan menyusun DPIA berbagi data mitra | C3: kerangka risiko pihak ketiga dan DPIA |
| 10 | Kelangsungan Bisnis dan Ketahanan Operasional | Melakukan BIA, menetapkan RTO dan RPO, lalu memilih strategi kelangsungan | C3: BIA dan strategi kelangsungan layanan |
| 11 | Tata Kelola Kecerdasan Artifisial | Menginventaris kasus pemakaian AI, mengklasifikasi risikonya, dan merumuskan kebijakan AI | C3: inventaris AI dan kebijakan pemakaian AI |
| 12 | Audit TI dan Asurans | Menyusun rencana asurans berbasis risiko dan menguji satu kontrol dengan bukti | C4: rencana asurans dan contoh pengujian kontrol |
| 13 | KPI, KRI, dan Pelaporan ke Direksi | Merancang *dashboard* indikator dan laporan satu halaman untuk direksi | C4: *dashboard* GRC dan laporan direksi |
| 14 | Alat GRC dan Peta Jalan Tata Kelola Terpadu | Memadukan luaran semester menjadi peta jalan GRC, memilih alat GRC, dan berlatih presentasi | C4: peta jalan GRC dan presentasi akhir |

Keempat Bagian di bawah sejajar dengan tonggak capstone. Bagian I (1 sampai 3) menjawab dua pertanyaan dasar: siapa yang memutuskan dan aturan apa yang mengikat. Bagian II (4 sampai 7) memotret kondisi saat ini lewat empat lensa, yaitu tata kelola, risiko, keamanan, dan data pribadi. Bagian III (8 sampai 11) merancang kontrol untuk kondisi target. Bagian IV (12 sampai 14) memastikan rancangan itu dapat diperiksa, diukur, dan dijalankan bertahap.

**Mengapa Bagian III diletakkan setelah C2.** Kontrol yang tepat bergantung pada sistem yang akan dikendalikan. Risiko cloud baru dapat dinilai setelah tim memilih strategi migrasi di IT40713. Penilaian dampak berbagi data baru bermakna setelah tim merancang alur data mitra di IT40613. Susunan ini punya satu konsekuensi. Selama Pertemuan 8 sampai 11, rancangan arsitektur dan rancangan kontrol harus diperbarui bersama. Bila arsitektur berubah, daftar kontrol ikut ditinjau ulang.

---

## Rencana Pertemuan

### Bagian I. Fondasi dan Konteks Tata Kelola (1 sampai 3)

#### Pertemuan 01 · Orientasi Mata Kuliah dan Dasar-Dasar GRC

**Tujuan.**
1. Membedakan tata kelola, manajemen, risiko, kontrol, kepatuhan, dan asurans dengan contoh dari organisasi tempat bekerja.
2. Menjelaskan peran mata kuliah ini dalam capstone bersama dan luaran yang disumbangkan ke tiap tonggak.
3. Memetakan pemangku kepentingan dan pemicu GRC pada organisasi yang dipilih tim.

**Topik.** Alasan organisasi membutuhkan tata kelola TI: proyek gagal, data bocor, dan temuan audit. Beda tata kelola dan manajemen. Istilah dasar: risiko, kontrol, kepatuhan, asurans, kebijakan, standar, dan prosedur. GRC sebagai satu kesatuan, bukan tiga unit yang terpisah. Peta kerangka dan regulasi yang dipakai sepanjang semester. Pengantar capstone, tonggak C1 sampai C4, dan kasus fiktif Medikara Health. Cara belajar mandiri dengan modul, slide, dan berkas di folder `sources`.

**Aktivitas.** Tim campuran dibentuk, lalu memilih organisasi: tempat kerja salah satu anggota (dengan izin dan data yang dianonimkan) atau Medikara Health. Untuk mata kuliah ini, tiap anggota memegang satu peran. Pemilik konteks adalah anggota yang paling mengenal organisasi. Analis regulasi membaca aturan, analis risiko menilai dampak, dan analis teknologi memahami sistem. Peran ini dipakai sepanjang semester. Tim menulis profil organisasi satu halaman dan mendaftar tiga sampai lima pemicu GRC, misalnya insiden, temuan audit, atau aturan baru. Tim juga menggambar peta pemangku kepentingan yang menunjukkan siapa berkepentingan, siapa memutuskan, dan siapa terdampak. Luarannya masuk C1. *Pendalaman teknis (opsional):* menyiapkan register GRC yang akan dipakai sepanjang semester dalam bentuk berkas terstruktur, misalnya CSV (*Comma-Separated Values*) atau YAML, di bawah kendali versi. Dilanjutkan pengenalan OSCAL (*Open Security Controls Assessment Language*) sebagai format terbuka untuk katalog kontrol.

**Latihan.**
1. Ambil satu keputusan TI yang baru terjadi di tempat kerja. Tentukan bagian mana yang termasuk tata kelola dan bagian mana yang termasuk manajemen, beserta alasannya.
2. Jelaskan dengan contoh mengapa organisasi yang patuh pada regulasi belum tentu risikonya terkendali.
3. Pilih satu pemicu GRC pada Medikara Health. Sebutkan pemangku kepentingan yang paling dirugikan bila pemicu itu diabaikan, lalu jelaskan alasannya.

#### Pertemuan 02 · Prinsip Tata Kelola TI dan Peran Direksi

**Tujuan.**
1. Menerapkan model *Evaluate, Direct, Monitor* dan prinsip ISO/IEC 38500:2024 untuk menilai praktik tata kelola sebuah organisasi.
2. Menyusun matriks hak keputusan TI yang memisahkan pihak yang memberi masukan dari pihak yang memutuskan.
3. Mengkritisi pilihan struktur tata kelola, misalnya komite pengarah TI, berdasarkan ukuran dan konteks organisasi.

**Topik.** Masalah pembuka: investasi TI besar yang tidak jelas pemiliknya. Tata kelola korporat dan posisi TI di dalamnya. Peran direksi dan dewan komisaris. ISO/IEC 38500:2024: prinsip dan model *Evaluate, Direct, Monitor*. Hak keputusan TI dan arketipe tata kelola menurut Weill dan Ross. Struktur, proses, dan mekanisme relasional. Komite pengarah TI dan piagamnya. Keselarasan bisnis dan TI. Penciptaan nilai. Bukti empiris tentang kaitan tata kelola TI dengan kinerja organisasi.

**Aktivitas.** Tim memetakan keputusan TI penting di organisasinya, misalnya pemilihan vendor SIMRS (Sistem Informasi Manajemen Rumah Sakit), anggaran keamanan, atau pembukaan data ke mitra. Untuk tiap keputusan, tim menentukan siapa memberi masukan, siapa memutuskan, dan siapa mengawasi. Hasilnya dibandingkan dengan arketipe Weill dan Ross. Dari situ tim menulis rancangan piagam komite pengarah TI: tujuan, anggota, wewenang, frekuensi rapat, dan laporan ke direksi. Pemilik konteks memastikan matriks mencerminkan kenyataan, bukan sekadar bagan organisasi. Analis regulasi memeriksa kesesuaiannya dengan anggaran dasar dan aturan tata kelola perusahaan. Luarannya masuk C1. *Pendalaman teknis (opsional):* menelusuri jejak keputusan TI di alat kerja sehari-hari, misalnya persetujuan perubahan di sistem tiket atau aturan persetujuan *merge* di repositori kode. Jejak ini menjadi bukti bahwa hak keputusan benar-benar dijalankan.

**Latihan.**
1. Sebuah rumah sakit membentuk komite pengarah TI, tetapi rapatnya hanya membahas laporan kemajuan proyek. Bagian mana dari model *Evaluate, Direct, Monitor* yang belum dijalankan? Jelaskan.
2. Bandingkan dua arketipe hak keputusan untuk investasi aplikasi pasien Medikara+. Mana yang lebih tepat, dan apa *trade-off*-nya?
3. Ringkas temuan Wu, Straub, dan Liang (2015) tentang peran keselarasan strategis. Nilai apakah temuan itu berlaku untuk organisasi tempat bekerja.

#### Pertemuan 03 · Lanskap Regulasi dan Kewajiban Kepatuhan

**Tujuan.**
1. Mengidentifikasi regulasi dan standar yang mengikat sebuah organisasi berdasarkan sektor, jenis data, dan model bisnisnya.
2. Menurunkan pasal regulasi menjadi kewajiban yang dapat diperiksa, lengkap dengan pemilik dan buktinya.
3. Membedakan kewajiban hukum, kewajiban kontrak, dan standar sukarela beserta akibat pelanggarannya.

**Topik.** Masalah pembuka: aturan baru terbit, tetapi tidak ada yang tahu siapa yang harus bertindak. Hierarki peraturan perundang-undangan. Cara memeriksa status peraturan di JDIH (Jaringan Dokumentasi dan Informasi Hukum). UU 27/2022 tentang PDP (Pelindungan Data Pribadi) dan PP 33/2026 sebagai peraturan pelaksananya, dalam garis besar. UU ITE (Informasi dan Transaksi Elektronik) beserta perubahannya dan PP 71/2019 tentang PSTE (Penyelenggaraan Sistem dan Transaksi Elektronik). UU 17/2023 tentang Kesehatan, PP 28/2024, dan Permenkes 24/2022 tentang Rekam Medis. Peraturan BSSN (Badan Siber dan Sandi Negara) dan Perpres 82/2022 tentang Pelindungan Infrastruktur Informasi Vital. Regulasi OJK (Otoritas Jasa Keuangan) yang mengikat mitra asuransi. Evaluasi SPBE (Sistem Pemerintahan Berbasis Elektronik) bagi mitra sektor publik. Register kewajiban kepatuhan dan prinsip ISO 37301.

**Aktivitas.** Tim menyusun register kewajiban kepatuhan untuk organisasinya. Analis regulasi memimpin pembacaan pasal, dan anggota berlatar hukum sangat membantu pada tahap ini. Tiap baris register berisi sumber aturan, pasal, kewajiban dalam kalimat sederhana, unit pemilik, bukti kepatuhan, dan status awal. Untuk Medikara Health, register minimal mencakup UU PDP, aturan rekam medis elektronik, PSTE, integrasi SATUSEHAT, dan pelaporan insiden siber. Analis teknologi menandai kewajiban yang berdampak pada sistem, misalnya masa simpan rekam medis atau notifikasi kegagalan pelindungan data pribadi. Luarannya masuk C1 dan dipakai ulang pada Pertemuan 5, 7, dan 12. *Pendalaman teknis (opsional):* menurunkan tiga kewajiban menjadi persyaratan sistem yang dapat diuji, misalnya kebutuhan *logging*, enkripsi, dan masa simpan data. Persyaratan itu lalu ditautkan ke *backlog* tim pengembang.

**Latihan.**
1. Sebuah klinik mitra menyimpan rekam medis di layanan cloud luar negeri. Kewajiban apa saja yang perlu diperiksa, dan pada peraturan mana?
2. Tulis ulang satu pasal UU PDP menjadi kewajiban yang dapat diperiksa auditor: siapa melakukan apa, kapan, dan apa buktinya.
3. Jelaskan mengapa sertifikat ISO/IEC 27001 tidak otomatis membuktikan kepatuhan pada UU PDP.

### Bagian II. Menilai Kondisi Saat Ini (4 sampai 7)

#### Pertemuan 04 · COBIT 2019: Sistem Tata Kelola dan Faktor Desain

**Tujuan.**
1. Menjelaskan komponen sistem tata kelola dan 40 objektif tata kelola dan manajemen dalam COBIT 2019.
2. Menerapkan faktor desain dan *goals cascade* untuk memilih objektif yang paling penting bagi sebuah organisasi.
3. Menilai tingkat kapabilitas saat ini untuk objektif prioritas berdasarkan bukti, bukan pengakuan.

**Topik.** Masalah pembuka: organisasi ingin "menerapkan COBIT", tetapi tidak tahu harus mulai dari mana. Prinsip sistem tata kelola. Model inti dengan 40 objektif dalam lima domain: EDM, APO, BAI, DSS, dan MEA. Tujuh komponen sistem tata kelola. Sebelas faktor desain dan *focus area*. *Goals cascade* dari kebutuhan pemangku kepentingan ke tujuan organisasi, tujuan keselarasan, lalu objektif. Tingkat kapabilitas proses 0 sampai 5 dan cara menilainya. Kaitan COBIT dengan ITIL 4 (dirinci di Pertemuan 8) dan dengan tata kelola arsitektur (dibahas rinci di mata kuliah IT40513). Status COBIT 7 yang diumumkan ISACA pada Oktober 2026.

**Aktivitas.** Tim menerapkan sebelas faktor desain COBIT 2019 pada organisasinya dengan lembar kerja di `sources/chapter04`. Faktor itu antara lain strategi, profil risiko, isu TI, *threat landscape*, kebutuhan kepatuhan, peran TI, dan model *sourcing*. Hasilnya dipadukan dengan *goals cascade* untuk mendapatkan lima sampai tujuh objektif prioritas. Untuk tiap objektif prioritas, tim menilai cepat kapabilitas saat ini dengan meminta bukti nyata, misalnya notulen, prosedur, atau laporan. Pemilik konteks mengumpulkan bukti, sedangkan analis risiko dan analis teknologi menilainya. Luarannya masuk C2. *Pendalaman teknis (opsional):* memakai COBIT Design Toolkit resmi dan menelusuri bagaimana bobot faktor desain menggeser prioritas. Mahasiswa berlatar rekayasa perangkat lunak dapat membandingkan hasilnya dengan *focus area* DevOps.

**Latihan.**
1. Dua rumah sakit memiliki strategi yang sama, tetapi satu mengembangkan sistem sendiri dan satu bergantung pada vendor. Bagaimana perbedaan model *sourcing* itu menggeser objektif prioritas?
2. Seorang manajer menyatakan proses manajemen perubahan sudah berada di tingkat kapabilitas 3. Bukti apa yang perlu diminta untuk menguji klaim itu?
3. Jelaskan mengapa COBIT tidak dimaksudkan untuk diterapkan seluruhnya sekaligus.

#### Pertemuan 05 · Manajemen Risiko Enterprise dan Risiko TI

**Tujuan.**
1. Menerapkan proses ISO 31000 untuk mengidentifikasi, menganalisis, dan mengevaluasi risiko terkait TI.
2. Merumuskan pernyataan *risk appetite* yang dapat dipakai untuk mengambil keputusan.
3. Membandingkan penilaian risiko kualitatif dan kuantitatif beserta keterbatasan masing-masing.

**Topik.** Masalah pembuka: daftar risiko yang panjang, tetapi tidak pernah mengubah keputusan apa pun. Prinsip, kerangka, dan proses ISO 31000:2018. COSO ERM (*Enterprise Risk Management*) 2017 dan kaitan risiko dengan strategi serta kinerja. *Risk appetite*, *risk tolerance*, dan kapasitas risiko. Risiko keamanan informasi menurut ISO/IEC 27005:2022, termasuk pendekatan berbasis peristiwa dan berbasis aset. *Risk register*: skenario, pemilik, dampak, kemungkinan, kontrol, dan rencana penanganan. Opsi penanganan risiko. Matriks risiko dan kelemahannya. Gambaran pengukuran risiko secara kuantitatif. Pengantar KRI (*Key Risk Indicator*), yang dirinci di Pertemuan 13.

**Aktivitas.** Tim merumuskan pernyataan *risk appetite* untuk tiga sampai empat kategori, misalnya keselamatan pasien, kerahasiaan data, kelangsungan layanan, dan kepatuhan. Bahasanya dipilih agar dapat langsung dipakai direksi. Setelah itu tim mengisi *risk register* kondisi saat ini berisi 10 sampai 15 skenario risiko. Untuk Medikara Health, skenario wajib mencakup kebocoran data lewat vendor, kontrol akses yang lemah, gangguan integrasi BPJS Kesehatan, dan laporan manajemen yang bergantung pada spreadsheet. Analis risiko memimpin. Anggota berlatar akuntansi atau keuangan menilai dampak finansial. Analis teknologi menilai kemungkinan kejadian dan kontrol yang sudah ada. Luarannya masuk C2. *Pendalaman teknis (opsional):* mengkuantifikasi dua skenario dengan simulasi Monte Carlo sederhana di spreadsheet, mengikuti pendekatan Hubbard dan Seiersen, lalu menggambar *loss exceedance curve*.

**Latihan.**
1. Ubah pernyataan "Medikara tidak menoleransi kebocoran data" menjadi pernyataan *risk appetite* yang realistis dan dapat diukur.
2. Dua risiko sama-sama mendapat skor 12 pada matriks 5 x 5, tetapi hanya satu yang berdampak pada keselamatan pasien. Jelaskan kelemahan matriks risiko dari contoh ini.
3. Tentukan opsi penanganan yang paling tepat untuk risiko ketergantungan pada vendor aplikasi Medikara+, beserta alasan dan risiko sisanya.

#### Pertemuan 06 · Keamanan Informasi: ISO/IEC 27001 dan NIST CSF 2.0

**Tujuan.**
1. Menjelaskan struktur ISMS (*Information Security Management System*) menurut ISO/IEC 27001:2022 serta peran kontrol Annex A dan ISO/IEC 27002.
2. Menyusun profil saat ini NIST CSF 2.0 untuk sebuah organisasi.
3. Menganalisis celah kontrol keamanan dan mengaitkannya dengan skenario di *risk register*.

**Topik.** Masalah pembuka: audit menemukan kontrol akses yang lemah, padahal kebijakan keamanan sudah ada. Kerahasiaan, integritas, dan ketersediaan. ISO/IEC 27001:2022 beserta Amandemen 1:2024: klausul 4 sampai 10 dan perbaikan berkelanjutan. Kontrol Annex A dalam empat tema dan SoA (*Statement of Applicability*). ISO/IEC 27002:2022 sebagai panduan penerapan kontrol. ISO 27799:2025 untuk organisasi kesehatan. NIST CSF (*Cybersecurity Framework*) 2.0: enam fungsi termasuk fungsi Govern yang baru, profil, dan *tier*. Pemetaan antara ISO/IEC 27001 dan NIST CSF. Keamanan API (*Application Programming Interface*) dan keamanan cloud cukup disinggung, karena dibahas rinci di mata kuliah IT40613 dan IT40713.

**Aktivitas.** Tim menyusun profil saat ini NIST CSF 2.0. Subkategori yang relevan dipilih pada keenam fungsi, lalu dinilai berdasarkan bukti. Untuk Medikara Health, fokusnya kontrol akses SIMRS lintas rumah sakit, pengelolaan akun vendor, pencatatan *log*, dan cadangan data. Hasilnya diterjemahkan menjadi daftar celah terhadap kontrol Annex A ISO/IEC 27001, lalu dihubungkan ke skenario risiko dari Pertemuan 5. Analis teknologi memimpin penilaian. Analis regulasi menandai kontrol yang juga diwajibkan regulasi. Pemilik konteks memastikan buktinya benar ada. Luarannya masuk C2. *Pendalaman teknis (opsional):* memeriksa satu kontrol teknis secara langsung, misalnya cakupan MFA (*Multi-Factor Authentication*) atau konfigurasi *logging* terhadap CIS Benchmarks. Pemetaan antarkerangka dapat memakai NIST OLIR (*Online Informative References*).

**Latihan.**
1. Jelaskan mengapa organisasi dapat disertifikasi terhadap ISO/IEC 27001, tetapi tidak terhadap ISO/IEC 27002.
2. Fungsi Govern ditambahkan pada NIST CSF 2.0. Masalah organisasi apa yang ingin diselesaikan dengan penambahan itu?
3. Sebuah rumah sakit memutuskan tidak menerapkan satu kontrol Annex A. Apa yang harus ditulis di SoA agar keputusan itu dapat dipertanggungjawabkan?

#### Pertemuan 07 · Pelindungan Data Pribadi dalam Praktik

**Tujuan.**
1. Menjelaskan kewajiban pengendali dan prosesor data pribadi menurut UU 27/2022 dan PP 33/2026.
2. Menyusun catatan kegiatan pemrosesan data pribadi untuk satu proses layanan.
3. Menganalisis insiden kebocoran data dan menilai apakah penanganannya memenuhi kewajiban notifikasi.

**Topik.** Masalah pembuka: data pasien bocor lewat vendor, lalu muncul pertanyaan siapa yang bertanggung jawab. Data pribadi umum dan data pribadi yang bersifat spesifik, termasuk data kesehatan. Prinsip dan dasar pemrosesan. Hak subjek data. Pengendali, prosesor, dan pengendali bersama. Pejabat pelindungan data pribadi. Penilaian dampak pelindungan data pribadi. Notifikasi kegagalan pelindungan data pribadi. Transfer data ke luar wilayah hukum Indonesia. Sanksi administratif dan pidana. PP 33/2026 yang berlaku mulai 16 Januari 2027 beserta rincian teknisnya. Status lembaga pengawas pelindungan data pribadi. ISO/IEC 27701:2025 sebagai sistem manajemen privasi yang kini dapat berdiri sendiri.

**Aktivitas.** Tim memilih satu proses layanan, misalnya pendaftaran pasien dan telekonsultasi di Medikara+. Untuk proses itu, tim menyusun catatan kegiatan pemrosesan: jenis data, tujuan, dasar pemrosesan, pihak penerima, lokasi penyimpanan, masa simpan, dan kontrol. Tim kemudian menyusun garis waktu insiden kebocoran lewat vendor pada 2025, lalu menilai celahnya terhadap UU PDP dan PP 33/2026. Analis regulasi memimpin. Pemilik konteks memetakan alur data yang sebenarnya. Analis teknologi menelusuri sistem yang terlibat. Seluruh luaran Bagian II dirangkum menjadi C2 dan ditinjau menjelang UTS. *Pendalaman teknis (opsional):* merancang teknik pengurangan risiko privasi seperti pseudonimisasi, tokenisasi, dan klasifikasi data otomatis. Dilanjutkan dengan mempelajari cara persetujuan pasien direpresentasikan dalam sumber daya Consent pada HL7 FHIR (*Health Level Seven Fast Healthcare Interoperability Resources*), yang dibahas rinci di mata kuliah IT40613.

**Latihan.**
1. Medikara memakai vendor untuk aplikasi Medikara+. Dalam hubungan ini, siapa pengendali dan siapa prosesor? Apa akibatnya terhadap tanggung jawab saat terjadi kebocoran?
2. Tentukan dasar pemrosesan yang paling tepat untuk data rekam medis dalam layanan pengobatan. Jelaskan mengapa persetujuan belum tentu menjadi dasar yang terbaik.
3. Susun garis waktu notifikasi yang memenuhi UU PDP untuk insiden yang ditemukan pada Jumat malam.

### Bagian III. Merancang Kondisi Target (8 sampai 11)

#### Pertemuan 08 · Merancang Sistem Tata Kelola Target

**Tujuan.**
1. Merancang struktur tata kelola target, termasuk forum keputusan, peran kunci, dan matriks RACI.
2. Menetapkan target kapabilitas COBIT dan profil target NIST CSF yang selaras dengan *risk appetite*.
3. Mengaitkan praktik ITIL 4 dengan objektif manajemen COBIT untuk menjalankan layanan TI sehari-hari.

**Topik.** Masalah pembuka: semua orang setuju arah transformasi, tetapi tidak jelas siapa menyetujui apa. Langkah desain COBIT: menyempurnakan cakupan dan menyimpulkan rancangan. Penetapan target kapabilitas. Struktur organisasi tata kelola: komite pengarah TI, komite risiko, CISO (*Chief Information Security Officer*), pejabat pelindungan data pribadi, dan pemilik data. Matriks RACI (*Responsible, Accountable, Consulted, Informed*). Arsitektur kebijakan: kebijakan, standar, prosedur, dan pedoman. ITIL 4: sistem nilai layanan dan praktik seperti *change enablement*, *incident management*, dan *service level management*. Catatan tentang ITIL (Version 5) yang diterbitkan PeopleCert pada 2026. Profil target NIST CSF. Kaitan dengan *architecture board* dan prinsip arsitektur (dibahas rinci di mata kuliah IT40513).

**Aktivitas.** Berdasarkan kondisi target yang dirancang di tiga mata kuliah lain, tim merancang model tata kelola target. Isinya forum keputusan dan perannya, matriks RACI untuk 8 sampai 10 keputusan atau proses kunci, target kapabilitas untuk objektif prioritas, profil target NIST CSF, dan daftar kebijakan yang perlu dibuat atau direvisi. Untuk Medikara Health, model ini harus menjawab dua pertanyaan: siapa menyetujui pembukaan data ke mitra, dan siapa memegang akuntabilitas atas rekam medis terpadu. Pemilik konteks dan analis regulasi merancang struktur. Analis risiko menyelaraskan target dengan *risk appetite*. Analis teknologi memetakan praktik ITIL. Luarannya masuk C3. *Pendalaman teknis (opsional):* mengenal *policy as code*, misalnya Open Policy Agent, untuk menegakkan sebagian kebijakan secara otomatis. Dilanjutkan dengan merancang alur persetujuan perubahan yang menyatu dengan *pipeline* CI/CD (*Continuous Integration / Continuous Delivery*), yang dibahas rinci di mata kuliah IT40713.

**Latihan.**
1. Mengapa dalam matriks RACI satu aktivitas hanya boleh memiliki satu pihak *Accountable*? Berikan contoh masalah bila aturan ini dilanggar.
2. Jelaskan perbedaan peran COBIT dan ITIL 4 dengan contoh proses manajemen perubahan di rumah sakit.
3. Sebuah tim menetapkan target kapabilitas tingkat 4 untuk semua objektif. Kritisi keputusan ini dari sisi biaya dan *risk appetite*.

#### Pertemuan 09 · Risiko Pihak Ketiga dan Cloud

**Tujuan.**
1. Menyusun siklus hidup manajemen risiko pihak ketiga, mulai dari uji tuntas sampai pemutusan kontrak.
2. Memetakan pembagian tanggung jawab keamanan antara organisasi dan penyedia cloud.
3. Menyusun penilaian dampak pelindungan data pribadi untuk alur berbagi data dengan mitra.

**Topik.** Masalah pembuka: kebocoran terjadi di vendor, tetapi kerugian reputasi ditanggung organisasi. Rantai pasok digital dan pihak keempat. Siklus hidup risiko pihak ketiga: klasifikasi vendor, uji tuntas, klausul kontrak, pemantauan, dan strategi keluar. ISO/IEC 27036 tentang hubungan dengan pemasok. Model tanggung jawab bersama di cloud. CSA CCM (*Cloud Controls Matrix*) dan kuesioner CAIQ (*Consensus Assessments Initiative Questionnaire*). Lokasi data dan kewajiban PSE (Penyelenggara Sistem Elektronik) lingkup privat. Kewajiban prosesor menurut UU PDP. Risiko ekosistem mitra. DPIA (*Data Protection Impact Assessment*), yang dalam UU PDP disebut penilaian dampak pelindungan data pribadi, untuk berbagi data. Strategi migrasi cloud dan keamanan teknis API cukup disinggung, karena dibahas rinci di mata kuliah IT40713 dan IT40613.

**Aktivitas.** Tim mengklasifikasi vendor dan mitra dalam rancangan target berdasarkan akses data dan kekritisan layanan. Contohnya penyedia cloud, vendor Medikara+, laboratorium mitra, asuransi, dan apotek daring. Untuk dua vendor paling kritis, tim menyusun daftar pertanyaan uji tuntas, klausul kontrak minimum, dan indikator pemantauan. Tim juga mengisi matriks tanggung jawab bersama untuk layanan cloud yang dipilih di IT40713. Terakhir, tim menyusun DPIA untuk satu alur berbagi data dengan mitra asuransi. Analis regulasi memimpin penyusunan klausul kontrak. Anggota berlatar bisnis menilai kekritisan vendor. Analis teknologi mengisi matriks cloud. Luarannya masuk C3. *Pendalaman teknis (opsional):* menilai kontrol vendor dengan CSA CCM v4, mempelajari SBOM (*Software Bill of Materials*) untuk risiko rantai pasok perangkat lunak, dan membaca bukti teknis seperti laporan uji penetrasi.

**Latihan.**
1. Jelaskan mengapa sertifikat ISO/IEC 27001 milik penyedia cloud tidak memindahkan seluruh tanggung jawab keamanan kepada penyedia.
2. Susun tiga klausul kontrak yang dapat mencegah atau membatasi dampak insiden seperti kebocoran data lewat vendor yang dialami Medikara pada 2025.
3. Kapan alur berbagi data dengan mitra wajib didahului DPIA? Jelaskan dengan contoh.

#### Pertemuan 10 · Kelangsungan Bisnis dan Ketahanan Operasional

**Tujuan.**
1. Melakukan BIA (*Business Impact Analysis*) untuk menentukan layanan kritis beserta RTO dan RPO-nya.
2. Memilih strategi kelangsungan yang sepadan dengan dampak dan biaya.
3. Merancang skenario latihan krisis yang menguji keputusan, bukan hanya teknologi.

**Topik.** Masalah pembuka: SIMRS mati selama enam jam dan antrean pasien mengular. Beda manajemen insiden, kelangsungan bisnis, dan pemulihan bencana. Sistem manajemen kelangsungan bisnis menurut ISO 22301:2019 beserta Amandemen 1:2024. BIA. MTPD (*Maximum Tolerable Period of Disruption*), RTO (*Recovery Time Objective*), dan RPO (*Recovery Point Objective*). Strategi kelangsungan, termasuk prosedur manual pengganti. Pengelolaan insiden siber menurut Peraturan BSSN 1/2024 dan manajemen krisis siber. Ketahanan operasional sebagai tanggung jawab direksi. Latihan *tabletop*. *Disaster recovery* secara teknis cukup disinggung, karena dibahas rinci di mata kuliah IT40713.

**Aktivitas.** Tim melakukan BIA untuk lima sampai tujuh layanan, misalnya pendaftaran pasien, IGD (Instalasi Gawat Darurat), farmasi, laboratorium, klaim BPJS Kesehatan, dan telekonsultasi. Untuk tiap layanan, tim menetapkan dampak menurut waktu, MTPD, RTO, dan RPO, serta ketergantungan pada sistem dan vendor. Tim lalu memilih strategi kelangsungan untuk dua layanan paling kritis. Tim juga menyusun skenario latihan *tabletop* singkat, misalnya serangan *ransomware* pada SIMRS di satu rumah sakit. Anggota berlatar kesehatan atau operasional memimpin penilaian dampak. Analis teknologi menilai apakah RTO dan RPO dapat dicapai oleh arsitektur target. Analis risiko menautkan hasilnya ke *risk register*. Luarannya masuk C3. *Pendalaman teknis (opsional):* menguji apakah RTO dan RPO yang diminta bisnis dapat dipenuhi oleh rancangan replikasi dan cadangan di IT40713. Selisihnya dicatat sebagai risiko yang harus diterima atau ditangani.

**Latihan.**
1. Jelaskan perbedaan RTO dan RPO dengan contoh layanan farmasi rumah sakit.
2. Mengapa RTO untuk semua layanan tidak boleh ditetapkan nol? Kaitkan dengan biaya dan *risk appetite*.
3. Rancang tiga pertanyaan keputusan yang harus dijawab direksi dalam latihan *tabletop* serangan *ransomware*.

#### Pertemuan 11 · Tata Kelola Kecerdasan Artifisial

**Tujuan.**
1. Mengidentifikasi kasus pemakaian AI (*Artificial Intelligence*) di organisasi dan mengklasifikasi risikonya.
2. Menjelaskan persyaratan sistem manajemen AI menurut ISO/IEC 42001:2023 dan pendekatan berbasis risiko dalam EU AI Act.
3. Merumuskan kebijakan pemakaian AI yang dapat dijalankan dan diawasi.

**Topik.** Masalah pembuka: staf memakai *chatbot* AI umum untuk merangkum catatan pasien tanpa izin. Peluang dan risiko AI di layanan kesehatan. *Shadow AI*. ISO/IEC 42001:2023 tentang sistem manajemen AI dan ISO/IEC 42005:2025 tentang penilaian dampak sistem AI. NIST AI RMF (*Risk Management Framework*) 1.0. EU AI Act, yaitu Regulation (EU) 2024/1689, beserta perubahan jadwal penerapannya melalui Regulation (EU) 2026/1744. Kategori risiko: terlarang, risiko tinggi, kewajiban transparansi, dan minimal. Posisi Indonesia: Surat Edaran Menkominfo 9/2023 tentang etika AI, rancangan Perpres tentang AI, dan aturan keputusan otomatis dalam UU PDP. Inventaris AI, pengawasan oleh manusia, dan akuntabilitas. EA (*Enterprise Architecture*) untuk AI dan API untuk agen AI cukup disinggung, karena dibahas rinci di mata kuliah IT40513 dan IT40613.

**Aktivitas.** Tim menyusun inventaris kasus pemakaian AI yang sudah ada dan yang mungkin muncul dalam kondisi target. Contohnya triase gejala di Medikara+, ringkasan rekam medis, prediksi ketersediaan tempat tidur, dan deteksi kecurangan klaim. Tiap kasus diklasifikasi tingkat risikonya dengan EU AI Act sebagai pembanding, karena per Oktober 2026 aturan AI di Indonesia masih berupa surat edaran dan rancangan Perpres. Tim lalu merumuskan kebijakan pemakaian AI: pemakaian yang dilarang, pemakaian yang perlu persetujuan, bentuk pengawasan oleh manusia, dan pelaporan insiden AI. Anggota berlatar kesehatan atau hukum menilai dampak pada pasien. Analis teknologi menilai data dan model. Analis regulasi menautkan kebijakan ke UU PDP. Luarannya masuk C3. *Pendalaman teknis (opsional):* menilai satu kasus berbasis LLM (*Large Language Model*) dengan OWASP Top 10 for LLM Applications, lalu merancang uji evaluasi sederhana untuk halusinasi dan kebocoran data.

**Latihan.**
1. Klasifikasikan fitur triase gejala Medikara+ menurut kategori risiko EU AI Act. Jelaskan alasannya dan kewajiban yang muncul.
2. Jelaskan mengapa larangan total memakai AI generatif sering justru memperbanyak *shadow AI*.
3. Bandingkan ISO/IEC 42001 dan ISO/IEC 27001 dari sisi tujuan dan jenis risiko yang dikelola.

### Bagian IV. Asurans, Pengukuran, dan Peta Jalan (12 sampai 14)

#### Pertemuan 12 · Audit TI dan Asurans

**Tujuan.**
1. Menjelaskan pembagian peran dalam Three Lines Model dan posisi audit internal yang independen.
2. Menyusun rencana asurans berbasis risiko untuk program transformasi digital.
3. Menguji rancangan dan efektivitas satu kontrol dengan bukti yang memadai.

**Topik.** Masalah pembuka: direksi menerima laporan "semua aman" dari unit TI, padahal audit menemukan sebaliknya. Konsep asurans dan bedanya dengan konsultasi. Three Lines Model dan *Statement of Position* IIA tahun 2026. Global Internal Audit Standards yang berlaku sejak 9 Januari 2025. Audit berbasis risiko dan rencana audit tahunan. Program audit: tujuan, kriteria, prosedur, dan sampel. Uji rancangan dan uji efektivitas kontrol. Kualitas bukti audit. Penulisan temuan: kondisi, kriteria, sebab, akibat, dan rekomendasi. Audit eksternal, sertifikasi, dan laporan asurans pihak ketiga seperti SOC 2 (*System and Organization Controls 2*). ITAF (*IT Audit Framework*) dari ISACA.

**Aktivitas.** Tim memetakan siapa menjalankan lini pertama, kedua, dan ketiga di organisasinya. Setelah itu tim menyusun rencana asurans berbasis risiko untuk dua tahun pertama peta jalan. Tim memilih satu kontrol penting, misalnya peninjauan hak akses SIMRS, lalu menyusun program audit singkat dan mengujinya dengan data contoh di `sources/chapter12`. Temuan ditulis dalam format kondisi, kriteria, sebab, akibat, dan rekomendasi. Anggota berlatar akuntansi atau audit memimpin. Analis teknologi menyiapkan dan menganalisis data. Pemilik konteks menilai apakah rekomendasinya dapat dijalankan. Luarannya masuk C4. *Pendalaman teknis (opsional):* menerapkan teknik audit berbantuan komputer pada *log* akses, misalnya mencari akun tanpa pemilik, akun bersama, dan akses di luar jam kerja. Dilanjutkan pengenalan konsep *continuous control monitoring*.

**Latihan.**
1. Unit manajemen risiko di sebuah rumah sakit melapor kepada direktur TI. Apa masalahnya menurut Three Lines Model, dan bagaimana memperbaikinya?
2. Jelaskan perbedaan uji rancangan dan uji efektivitas dengan contoh kontrol peninjauan hak akses.
3. Tulis satu temuan audit lengkap untuk kasus kebocoran data lewat vendor Medikara pada 2025.

#### Pertemuan 13 · KPI, KRI, dan Pelaporan ke Direksi

**Tujuan.**
1. Membedakan KPI, KRI, dan KCI, lalu memilih indikator yang memicu tindakan.
2. Menetapkan ambang batas KRI yang selaras dengan *risk appetite*.
3. Menyusun laporan GRC satu halaman yang dapat dipakai direksi untuk mengambil keputusan.

**Topik.** Masalah pembuka: laporan bulanan TI setebal 40 halaman yang tidak pernah dibaca direksi. KPI (*Key Performance Indicator*), KRI, dan KCI (*Key Control Indicator*). Indikator yang mendahului kejadian dan indikator yang tertinggal. Ambang batas dan jalur eskalasi yang diturunkan dari *risk appetite*. Sumber data indikator dan mutu datanya. Metrik tata kelola dari COBIT dan metrik keamanan dari NIST CSF. Risiko indikator yang dimanipulasi. *Dashboard* GRC dan prinsip visualisasi yang sederhana. Struktur laporan ke direksi: pesan utama, tren, dan keputusan yang diminta. Metrik platform dan SLO (*Service Level Objective*) cukup disinggung, karena dibahas rinci di mata kuliah IT40613 dan IT40713.

**Aktivitas.** Tim memilih 8 sampai 12 indikator yang mencakup tata kelola, risiko, keamanan, privasi, dan kelangsungan layanan. Tiap indikator diberi definisi, rumus, sumber data, frekuensi, pemilik, serta ambang hijau, kuning, dan merah. Tim lalu membuat *dashboard* sederhana dengan spreadsheet. Tim juga menulis laporan satu halaman untuk direksi Medikara Health atau organisasinya, berisi tiga pesan utama dan satu keputusan yang diminta. Analis risiko memimpin penetapan ambang. Anggota berlatar bisnis menyusun narasi untuk direksi. Analis teknologi memeriksa ketersediaan data. Luarannya masuk C4. *Pendalaman teknis (opsional):* mengotomasi pengambilan dua indikator dari sumber data nyata, misalnya sistem tiket atau *log*, ke alat *dashboard* sumber terbuka seperti Metabase atau Grafana.

**Latihan.**
1. "Jumlah pelatihan keamanan yang diselenggarakan" diusulkan sebagai KRI. Kritisi usulan ini dan tawarkan indikator yang lebih baik.
2. Turunkan ambang KRI untuk risiko kontrol akses dari pernyataan *risk appetite* yang dibuat pada Pertemuan 5.
3. Jelaskan apa yang membuat sebuah laporan direksi berujung pada keputusan, bukan sekadar dibaca.

#### Pertemuan 14 · Alat GRC dan Peta Jalan Tata Kelola Terpadu

**Tujuan.**
1. Membandingkan pilihan alat GRC, dari spreadsheet sampai platform terintegrasi, berdasarkan kebutuhan dan kematangan organisasi.
2. Menyusun peta jalan GRC bertahap yang selaras dengan peta jalan transformasi digital.
3. Mempertahankan rekomendasi tata kelola, risiko, dan kepatuhan di depan pemangku kepentingan.

**Topik.** Masalah pembuka: register risiko, kepatuhan, dan audit tersebar di puluhan spreadsheet yang isinya saling bertentangan. GRC terpadu: satu kontrol untuk banyak kewajiban. Fungsi alat GRC: register, alur kerja, pengelolaan bukti, dan pelaporan. Pilihan alat: spreadsheet terstruktur, alat sumber terbuka, dan platform komersial. Kriteria pemilihan dan biaya total kepemilikan. Penyusunan peta jalan GRC: gelombang inisiatif, ketergantungan, *quick win*, dan anggaran. Manajemen perubahan dan budaya organisasi. Penyelarasan dengan peta jalan dan portofolio inisiatif (dibahas rinci di mata kuliah IT40513). Persiapan presentasi C4.

**Aktivitas.** Tim memadukan seluruh luaran semester menjadi peta jalan GRC tiga tahun yang menempel pada peta jalan transformasi di IT40513. Peta jalan memuat gelombang inisiatif, ketergantungan, pemilik, perkiraan biaya, dan indikator keberhasilan. Tim juga memilih pendekatan alat GRC yang sesuai, misalnya tetap memakai spreadsheet terstruktur atau beralih ke alat sumber terbuka, disertai alasan dan *trade-off*-nya. Terakhir, tim berlatih presentasi C4 dengan format rapat direksi: masalah, rekomendasi, biaya, risiko bila rekomendasi tidak dijalankan, dan keputusan yang diminta. Semua peran terlibat. Pemilik konteks memastikan rekomendasi realistis bagi organisasinya. Luarannya masuk C4. *Pendalaman teknis (opsional):* memasang alat GRC sumber terbuka seperti CISO Assistant atau eramba, memuat kerangka ISO/IEC 27001 dan NIST CSF, lalu mengimpor register yang disusun selama semester.

**Latihan.**
1. Organisasi dengan 300 karyawan ingin membeli platform GRC yang mahal. Argumen apa yang mendukung dan menolak keputusan itu?
2. Jelaskan gagasan "satu kontrol untuk banyak kewajiban" dengan contoh kontrol peninjauan hak akses yang sekaligus memenuhi UU PDP, ISO/IEC 27001, dan NIST CSF.
3. Susun tiga inisiatif *quick win* GRC untuk Medikara Health pada enam bulan pertama, lalu jelaskan alasan urutannya.

---

## Kaitan dengan Capstone

| Tonggak | Pertemuan | Luaran dari mata kuliah ini |
| --- | --- | --- |
| C1 Konteks dan Strategi | 1 sampai 3 | Profil organisasi dan daftar pemicu GRC. Peta pemangku kepentingan. Matriks hak keputusan TI dan rancangan piagam komite pengarah TI. Register kewajiban kepatuhan. |
| C2 Kondisi Saat Ini, ditinjau menjelang UTS | 4 sampai 7 | Hasil faktor desain, objektif prioritas COBIT, dan potret kapabilitas. Pernyataan *risk appetite* dan *risk register*. Profil saat ini NIST CSF dan daftar celah kontrol. Catatan kegiatan pemrosesan data pribadi dan analisis celah PDP. |
| C3 Kondisi Target | 8 sampai 11 | Model tata kelola target dengan RACI, target kapabilitas, dan profil target NIST CSF. Kerangka risiko pihak ketiga, matriks tanggung jawab cloud, dan DPIA. BIA dan strategi kelangsungan layanan. Inventaris AI dan kebijakan pemakaian AI. |
| C4 Peta Jalan dan Tata Kelola, dipresentasikan menjelang UAS | 12 sampai 14 | Rencana asurans dan contoh pengujian kontrol. *Dashboard* KPI dan KRI serta laporan satu halaman untuk direksi. Peta jalan GRC terpadu dan pilihan alat GRC. |

Luaran ini saling terkait dengan luaran tiga mata kuliah lain. Register kewajiban dari C1 menjadi syarat bagi rancangan berbagi data mitra di IT40613. Profil target keamanan dan BIA dari C3 menjadi masukan bagi rancangan cloud dan pemulihan di IT40713. Peta jalan GRC dari C4 dilebur ke peta jalan dan portofolio inisiatif di IT40513, sehingga direksi menerima satu cetak biru, bukan empat dokumen terpisah.

## Kasus Berjalan: Medikara Health

PT Medikara Nusa Sehat ("Medikara Health") adalah **organisasi fiktif** yang dipakai bersama oleh keempat mata kuliah. Medikara mengelola 5 rumah sakit (Jakarta, Bekasi, Depok, Bogor, dan Bandung), 18 klinik pratama, 1 laboratorium rujukan, dan 12 apotek. Karyawannya sekitar 4.800 orang, dengan sekitar 1,2 juta kunjungan pasien per tahun.

Kondisi saat ini cukup khas untuk organisasi yang tumbuh lewat akuisisi. Tiap rumah sakit menjalankan SIMRS monolitik *on-premise* dengan versi yang berbeda. Keuangan sudah memakai ERP (*Enterprise Resource Planning*) terpusat. Aplikasi pasien Medikara+ untuk janji temu dan telekonsultasi dibuat oleh vendor. Integrasi ke BPJS Kesehatan dan SATUSEHAT (Kementerian Kesehatan, berbasis HL7 FHIR) masih *point-to-point*. Data pasien tersebar, dan banyak laporan manajemen masih disusun dengan spreadsheet. Strategi 2026 sampai 2030 berjudul "Satu Pasien, Satu Rekam Medis": layanan terintegrasi lintas fasilitas, ekosistem mitra (klinik mitra, asuransi, laboratorium, apotek daring, dan layanan kesehatan karyawan perusahaan), modernisasi ke cloud, serta kepatuhan pada UU PDP dan aturan rekam medis elektronik. Pemicu tambahannya adalah insiden kebocoran data pasien skala kecil lewat vendor pada 2025, temuan audit internal tentang kontrol akses yang lemah, antrean layanan yang panjang, dan biaya integrasi yang tinggi.

Mata kuliah ini memakai kasus tersebut dari sisi GRC:

- **Insiden kebocoran lewat vendor (2025)** menjadi bahan analisis notifikasi di Pertemuan 7, kontrak dan uji tuntas vendor di Pertemuan 9, dan penulisan temuan audit di Pertemuan 12.
- **Temuan audit kontrol akses** menjadi titik awal penilaian keamanan di Pertemuan 6 dan pengujian kontrol di Pertemuan 12.
- **Kewajiban UU PDP, rekam medis elektronik, dan SATUSEHAT** menjadi isi register kepatuhan di Pertemuan 3 dan catatan pemrosesan data di Pertemuan 7.
- **Ekosistem mitra dan modernisasi cloud** menjadi bahan risiko pihak ketiga dan DPIA di Pertemuan 9 serta BIA di Pertemuan 10.
- **Antrean layanan dan laporan berbasis spreadsheet** menjadi bahan *risk register* di Pertemuan 5 dan indikator di Pertemuan 13.
- **Kemungkinan pemakaian AI** dalam kondisi target, misalnya triase gejala di Medikara+, diangkat sebagai skenario di Pertemuan 11.

Tim yang memakai organisasi tempat kerja tetap dapat memakai Medikara sebagai pembanding. Seluruh data organisasi nyata wajib dianonimkan dan dipakai dengan izin.

## Struktur Repositori

| Folder | Isi |
| --- | --- |
| `figures/` | Gambar untuk modul dan slide. `logo_universitas.png` dan `building.png` adalah symlink. |
| `module/` | Naskah modul LaTeX: berkas utama `it-governance-risk-compliance.tex`, `titlepage.tex`, `chapter01.tex` sampai `chapter14.tex`, `references.bib` untuk rujukan inti, dan `bib/chapterNN.bib` untuk rujukan khusus tiap bab. `fonts/` adalah symlink. |
| `slides/` | `preamble.tex` bersama, `theme/` (symlink), dan satu folder `sessionNN/` untuk tiap pertemuan. |
| `sources/` | Berkas pendukung tiap bab di `chapter01/` sampai `chapter14/`: lembar kerja, templat, data kasus, dan berkas teknis opsional. |

Modul dan slide dikompilasi dengan XeLaTeX. Modul dikompilasi dengan perintah berikut di folder `module`:

```
xelatex it-governance-risk-compliance
bibtex it-governance-risk-compliance
xelatex it-governance-risk-compliance
xelatex it-governance-risk-compliance
```

Slide dikompilasi dengan menjalankan `xelatex` dua kali di folder `slides/sessionNN`, misalnya `xelatex session01` sebanyak dua kali di `slides/session01`.

`module/fonts`, `slides/theme`, `figures/logo_universitas.png`, dan `figures/building.png` adalah symlink ke repo advanced-software-engineering. Repo itu perlu tersedia di lokasi yang dituju symlink. Di Windows, symlink sering muncul sebagai berkas teks biasa, sehingga aset aslinya perlu disalin ke lokasi tersebut sebelum kompilasi.

## Rujukan Utama

Daftar berikut adalah hasil penelusuran per 30 Oktober 2026. Versi dicantumkan karena beberapa kerangka berubah pada 2024 sampai 2026.

**Tata kelola TI**
- ISO/IEC 38500:2024 (edisi ketiga), *Information technology: Governance of IT for the organization*. [iso.org](https://www.iso.org/standard/81684.html)
- ISACA, *COBIT 2019 Framework: Introduction and Methodology* dan *COBIT 2019 Design Guide* (2018). [isaca.org/resources/cobit](https://www.isaca.org/resources/cobit)
- ISACA, informasi transisi dari COBIT 2019 ke COBIT 7. [isaca.org](https://www.isaca.org/credentialing/cobit-foundation)
- AXELOS, *ITIL Foundation: ITIL 4 Edition* (2019), dan PeopleCert, ITIL (Version 5) (2026). [peoplecert.org](https://www.peoplecert.org/news-and-announcements/itil-version-5-foundation-whats-new-guide)

**Manajemen risiko**
- ISO 31000:2018, *Risk management: Guidelines*. [iso.org](https://www.iso.org/standard/31000)
- COSO, *Enterprise Risk Management: Integrating with Strategy and Performance* (2017). [coso.org](https://www.coso.org/erm-framework)
- ISO/IEC 27005:2022, *Guidance on managing information security risks*. [iso.org](https://www.iso.org/standard/80585.html)

**Keamanan informasi dan privasi**
- ISO/IEC 27001:2022 beserta Amd 1:2024 (*Climate action changes*). [iso.org](https://www.iso.org/standard/27001), [amandemen](https://www.iso.org/standard/88435.html)
- ISO/IEC 27002:2022, *Information security controls*. [iso.org](https://www.iso.org/standard/75652.html)
- ISO 27799:2025 (edisi ketiga), kontrol keamanan informasi untuk organisasi kesehatan berbasis ISO/IEC 27002. [iso.org](https://www.iso.org/standard/84647.html)
- ISO/IEC 27701:2025, *Privacy information management systems*, kini standar mandiri. [iso.org](https://www.iso.org/standard/27701)
- NIST CSWP 29, *The NIST Cybersecurity Framework (CSF) 2.0* (26 Februari 2024). [doi.org](https://doi.org/10.6028/NIST.CSWP.29)

**Kelangsungan bisnis**
- ISO 22301:2019 beserta Amd 1:2024, *Business continuity management systems: Requirements*. [iso.org](https://www.iso.org/standard/75106.html)

**Tata kelola AI**
- ISO/IEC 42001:2023, *Artificial intelligence: Management system*. [iso.org](https://www.iso.org/standard/42001)
- NIST AI 100-1, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* (2023). [doi.org](https://doi.org/10.6028/NIST.AI.100-1)
- Regulation (EU) 2024/1689 (*Artificial Intelligence Act*), diubah dengan Regulation (EU) 2026/1744. [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

**Audit dan asurans**
- The IIA, *Global Internal Audit Standards* (terbit 2024, berlaku 9 Januari 2025). [theiia.org](https://www.theiia.org/en/standards/2024-standards/global-internal-audit-standards/)
- The IIA, *Three Lines Model: Assurance and Advice in Support of Effective Governance*, *Statement of Position* (8 Juli 2026). [theiia.org](https://www.theiia.org/globalassets/site/resources/statements-of-position/tlm_assurance_advice_support_effective_gov_en.pdf)

**Regulasi Indonesia**
- UU 27/2022 tentang Pelindungan Data Pribadi. [JDIH BPK](https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022)
- PP 33/2026 tentang Peraturan Pelaksanaan UU 27/2022, ditetapkan 16 Juli 2026 dan berlaku 16 Januari 2027. [ringkasan Katadata](https://katadata.co.id/finansial/makro/6a9979b7c5745/pp-pelindungan-data-pribadi-berlaku-januari-2027-ini-aturan-baru-data-anak)
- PP 71/2019 tentang Penyelenggaraan Sistem dan Transaksi Elektronik (berlaku). [JDIH BPK](https://peraturan.bpk.go.id/Details/122030/pp-no-71-tahun-2019)
- PP 28/2024 tentang Peraturan Pelaksanaan UU 17/2023 tentang Kesehatan. [JDIH BPK](https://peraturan.bpk.go.id/Details/294077)
- Permenkes 24/2022 tentang Rekam Medis (berlaku). [JDIH BPK](https://peraturan.bpk.go.id/Details/245544)
- Peraturan BSSN 1/2024 tentang Pengelolaan Insiden Siber. [peraturan.go.id](https://www.peraturan.go.id/files/peraturan-bssn-no-1-tahun-2024.pdf)
- Perpres 82/2022 tentang Pelindungan Infrastruktur Informasi Vital. [peraturan.go.id](https://peraturan.go.id/files/ps82-2022.pdf)
- POJK 4/POJK.05/2021 tentang Penerapan Manajemen Risiko dalam Penggunaan Teknologi Informasi oleh Lembaga Jasa Keuangan Nonbank. [ojk.go.id](https://ojk.go.id/id/regulasi/Pages/Penerapan-Manajemen-Risiko-dalam-Penggunaan-Teknologi-Informasi-oleh-Lembaga-Jasa-Keuangan-Nonbank.aspx)
- Perpres 95/2018 tentang Sistem Pemerintahan Berbasis Elektronik. [JDIH BPK](https://peraturan.bpk.go.id/Details/96913)

**Buku dan artikel**
- De Haes, S., Van Grembergen, W., Joshi, A., dan Huygh, T. (2020). *Enterprise Governance of Information Technology: Achieving Alignment and Value in Digital Organizations* (edisi ketiga). Springer. [doi.org](https://doi.org/10.1007/978-3-030-25918-1)
- Weill, P. dan Ross, J. W. (2004). *IT Governance: How Top Performers Manage IT Decision Rights for Superior Results*. Harvard Business School Press.
- Wu, S. P.-J., Straub, D. W., dan Liang, T.-P. (2015). How IT Governance and Strategic Alignment Influence Organizational Performance. *MIS Quarterly*, 39(2), 497 sampai 518. [aisel.aisnet.org](https://aisel.aisnet.org/misq/vol39/iss2/12)
- Hubbard, D. W. dan Seiersen, R. (2023). *How to Measure Anything in Cybersecurity Risk* (edisi kedua). Wiley. [oreilly.com](https://www.oreilly.com/library/view/-/9781119892304/)

**Laporan industri**
- IBM, *Cost of a Data Breach Report 2026* (Juli 2026). [newsroom.ibm.com](https://newsroom.ibm.com/2026-07-29-ibm-study-one-in-four-malicious-breaches-are-ai-enabled,-costing-companies-6-million-on-average)
- World Economic Forum, *Global Cybersecurity Outlook 2026* (Januari 2026). [weforum.org](https://www.weforum.org/publications/global-cybersecurity-outlook-2026/)
- Verizon, *Data Breach Investigations Report 2026*. [verizon.com](https://www.verizon.com/business/resources/reports/dbir/)

**Silabus pembanding**
- Carnegie Mellon University, Heinz College, 95-744 *Cybersecurity Policy and Governance I*. [cylab.cmu.edu](https://cylab.cmu.edu/education/course-list/cybersecurity-policy-governance-1.html)
- University of Melbourne, ISYS90038 *IS Strategy and Governance*, Master of Information Systems. [handbook.unimelb.edu.au](https://handbook.unimelb.edu.au/2025/subjects/isys90038)
- Antwerp Management School bersama Maastricht University, *Executive Master in IT Governance & Assurance*. [antwerpmanagementschool.be](https://antwerpmanagementschool.be/en/program/executive-master-it-governance-assurance)

**Catatan status per 30 Oktober 2026.** ISACA telah mengumumkan COBIT 7 dalam bentuk platform digital. Sertifikat COBIT 7 Foundation dijadwalkan menggantikan sertifikat COBIT 2019, tetapi halaman kerangka resmi ISACA masih menampilkan COBIT 2019. Karena itu modul memakai COBIT 2019 sebagai dasar dan mencatat perubahan COBIT 7. PeopleCert menerbitkan ITIL (Version 5) pada awal 2026, sementara ITIL 4 masih berlaku berdampingan. ISO/IEC 27001 belum terbit dalam edisi baru, sehingga acuannya tetap edisi 2022 beserta amandemen 2024. ISO 31000 dan ISO 22301 sedang direvisi. Jadwal kewajiban risiko tinggi dalam EU AI Act diundur oleh Regulation (EU) 2026/1744: sistem Annex III menjadi 2 Desember 2027, dan sistem dalam produk Annex I menjadi 2 Agustus 2028. Naskah PP 33/2026 dilaporkan media dan firma hukum, tetapi belum tampil di JDIH BPK saat penelusuran, sehingga naskah resminya perlu diperiksa ulang sebelum isi bab ditulis. RUU Keamanan dan Ketahanan Siber serta Perpres tentang AI masih dalam pembahasan menurut berita terakhir yang ditemukan.

## Daftar Singkatan

| Singkatan | Kepanjangan |
| --- | --- |
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| APO | Align, Plan and Organize (domain COBIT) |
| BAI | Build, Acquire and Implement (domain COBIT) |
| BIA | Business Impact Analysis |
| BPJS | Badan Penyelenggara Jaminan Sosial |
| BPK | Badan Pemeriksa Keuangan |
| BSSN | Badan Siber dan Sandi Negara |
| CAIQ | Consensus Assessments Initiative Questionnaire |
| CCM | Cloud Controls Matrix |
| CI/CD | Continuous Integration / Continuous Delivery |
| CIS | Center for Internet Security |
| CISO | Chief Information Security Officer |
| COBIT | Control Objectives for Information and Related Technologies |
| COSO | Committee of Sponsoring Organizations of the Treadway Commission |
| CSA | Cloud Security Alliance |
| CSF | Cybersecurity Framework |
| CSV | Comma-Separated Values |
| DPIA | Data Protection Impact Assessment |
| DSS | Deliver, Service and Support (domain COBIT) |
| EA | Enterprise Architecture |
| EDM | Evaluate, Direct and Monitor (domain COBIT) |
| ERM | Enterprise Risk Management |
| ERP | Enterprise Resource Planning |
| EU | European Union |
| FHIR | Fast Healthcare Interoperability Resources |
| GRC | Governance, Risk, and Compliance |
| HL7 | Health Level Seven |
| IEC | International Electrotechnical Commission |
| IGD | Instalasi Gawat Darurat |
| IIA | The Institute of Internal Auditors |
| ISMS | Information Security Management System |
| ISO | International Organization for Standardization |
| ITAF | IT Audit Framework |
| ITE | Informasi dan Transaksi Elektronik |
| ITIL | Information Technology Infrastructure Library |
| JDIH | Jaringan Dokumentasi dan Informasi Hukum |
| KCI | Key Control Indicator |
| KPI | Key Performance Indicator |
| KRI | Key Risk Indicator |
| LLM | Large Language Model |
| MEA | Monitor, Evaluate and Assess (domain COBIT) |
| MFA | Multi-Factor Authentication |
| MTPD | Maximum Tolerable Period of Disruption |
| NIST | National Institute of Standards and Technology |
| OJK | Otoritas Jasa Keuangan |
| OLIR | Online Informative References |
| OSCAL | Open Security Controls Assessment Language |
| OWASP | Open Worldwide Application Security Project |
| PDP | Pelindungan Data Pribadi |
| Permenkes | Peraturan Menteri Kesehatan |
| Perpres | Peraturan Presiden |
| POJK | Peraturan Otoritas Jasa Keuangan |
| PP | Peraturan Pemerintah |
| PSE | Penyelenggara Sistem Elektronik |
| PSTE | Penyelenggaraan Sistem dan Transaksi Elektronik |
| RACI | Responsible, Accountable, Consulted, Informed |
| RMF | Risk Management Framework |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| SBOM | Software Bill of Materials |
| SIMRS | Sistem Informasi Manajemen Rumah Sakit |
| SLO | Service Level Objective |
| SoA | Statement of Applicability |
| SOC 2 | System and Organization Controls 2 |
| SPBE | Sistem Pemerintahan Berbasis Elektronik |
| TI | Teknologi Informasi |
| UAS | Ujian Akhir Semester |
| UTS | Ujian Tengah Semester |
| UU | Undang-Undang |
| YAML | YAML Ain't Markup Language |
