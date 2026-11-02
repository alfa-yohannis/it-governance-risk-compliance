<!-- Panduan penggabungan luaran GRC. Pakai sebagai daftar periksa sebelum tinjauan setiap tonggak. -->

# Penggabungan Luaran GRC ke Capstone

Keempat mata kuliah memakai satu organisasi dan satu Cetak Biru Transformasi
Digital. Tim tidak perlu membuat empat profil organisasi yang berbeda.
Setiap luaran GRC harus menunjuk nama proses, sistem, dan data yang sama
dengan dokumen arsitektur, platform API, serta cloud.

| Tonggak | Pemeriksaan sebelum tinjauan | Masukan dari mata kuliah lain |
| --- | --- | --- |
| C1, pertemuan 1 sampai 3 | Lingkup dan pemilik keputusan jelas; setiap kewajiban punya sumber resmi serta alasan keberlakuan | Profil dan prinsip arsitektur; calon mitra; kendala lokasi data |
| C2, pertemuan 4 sampai 7 | Kondisi saat ini didukung bukti; asumsi dan ketiadaan bukti dinyatakan; risiko dan celah saling tertaut | Katalog aplikasi/data, inventaris integrasi, diagnosis kesiapan cloud |
| C3, pertemuan 8 sampai 11 | Target menjawab celah C2; tanggung jawab vendor, privasi, AI, dan kelangsungan dapat dijalankan | Arsitektur target, kontrak API, pilihan layanan cloud dan rancangan pemulihan |
| C4, pertemuan 12 sampai 14 | Inisiatif punya pemilik, biaya, dependensi, tenggat, indikator, dan bukti penerimaan | Peta jalan transformasi, nilai platform, rencana operasi serta modernisasi |

## Menjaga jejak keputusan

1. Beri ID tetap untuk kewajiban, risiko, kontrol, bukti, dan inisiatif.
   Contoh lintas bab: risiko `R-01` kebocoran melalui vendor dan kontrol
   `AC-01` peninjauan hak akses. ID tetap sama ketika judul diperbaiki.
2. Pisahkan kondisi yang sudah diamati, skenario latihan, dan target yang
   belum diterapkan. Rencana kontrol tidak membuktikan risiko sudah turun.
3. Tautkan risiko ke proses atau layanan, lalu ke kontrol dan pemiliknya.
   Bukti kontrol menyebut periode, populasi, sumber, dan hasil pemeriksaan.
4. Catat perubahan keputusan: alasan, pihak yang menyetujui, tanggal,
   pengaruh pada biaya, serta artefak mata kuliah lain yang ikut berubah.
5. Tulis keputusan yang diminta pada tinjauan Sabtu. Tim membawa satu atau
   dua persoalan yang memerlukan pilihan, disertai bukti dan alternatif.

## Bukti dan penilaian

Luaran yang kuat menjelaskan masalah organisasi, membandingkan pilihan,
menyebut keterbatasan bukti, dan mempertahankan alasan keputusan. Banyaknya
baris register atau banyaknya diagram tidak otomatis menunjukkan mutu.
Rubrik singkat pada tiap bab membantu pemeriksaan sejawat; bobot penilaian
resmi mata kuliah tetap mengikuti ketentuan dosen.

Untuk Medikara, seluruh angka selain fakta dasar kasus merupakan skenario
latihan. Tim menulis kata "Misalkan" atau "data sintetis" sebelum memakai
angka itu. Hasil simulasi tidak diperlakukan sebagai pengukuran nyata.

## Izin dan batas data

Organisasi nyata harus memberi izin atas informasi yang dipakai. Dokumen tim
hanya berisi metadata, jumlah, persentase, dan bukti yang sudah dianonimkan.
Nama pasien, nomor rekam medis, isi diagnosis, identitas karyawan, kata sandi,
token, dan berkas produksi tidak disalin ke repositori atau layanan AI umum.
Jika suatu bukti tidak boleh dibagikan, catat jenis dan pemilik buktinya,
kemudian gunakan contoh sintetis untuk pembahasan kelas.
