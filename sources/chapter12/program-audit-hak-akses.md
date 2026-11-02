<!-- Program uji AC-01; tentukan kriteria sebelum memeriksa CSV sintetis. -->
# Program Audit AC-01

Tujuan: menilai rancangan serta pelaksanaan peninjauan akses dalam lingkup
contoh. Risiko terkait: R-01 kebocoran melalui vendor. Semua akun, pemilik, dan
bukti merupakan identitas fiktif.

## Kriteria

- Akun vendor dicabut paling lambat 1 hari kerja setelah penugasan berakhir (Bab 2).
- Nol akun vendor aktif tanpa pemilik (Bab 5).
- Peninjauan bulanan berjalan pada 5 rumah sakit, atau 60 catatan per tahun (Bab 6).
- Akun bersama manusia tidak digunakan; peninjau berwenang dan persetujuannya
  terdokumentasi.
- Khusus latihan delapan baris: setiap akun aktif ditinjau paling lama 90 hari. Batas
  90 hari adalah aturan skenario, bukan kewajiban standar. Akun layanan boleh memiliki
  pemilik unit yang jelas dan penilaian tersendiri.

## Prosedur

| Langkah | Prosedur | Bukti dan batas |
| --- | --- | --- |
| 1 | Baca rancangan dan kewenangan peninjau | CSV tidak membuktikan rancangan memadai |
| 2 | Cocokkan daftar peninjau dengan daftar penugasan | 108 dari 120 akun; populasi dari sumber lain |
| 3 | Periksa catatan bulanan per rumah sakit | 12 dari 60 catatan; pisahkan per lokasi |
| 4 | Uji sampel 30 akun | 24 sesuai, 6 menyimpang; satu lokasi, tidak diproyeksikan |
| 5 | Cari pemilik kosong dan akun bersama | Indikasi perlu konfirmasi, bukan bukti penyalahgunaan |
| 6 | Hitung selisih hari dari tanggal acuan | Tanggal acuan dan batas ditetapkan sebelum melihat data |
| 7 | Validasi referensi persetujuan | Kode EV saja belum membuktikan dokumen tersedia |
| 8 | Konfirmasikan pengecualian dengan pemilik | Jangan mengarang sebab yang belum terbukti |
| 9 | Tulis temuan dan rencana pengujian ulang | Nyatakan periode dan ruang lingkup kesimpulan |

## Hasil acuan sampel 30 akun (tanggal acuan 31 Maret 2026)

24 akun sesuai dan 6 akun menyimpang: VND003, VND007, VND011, VND015, VND019, dan
VND023. VND017 tidak dihitung menyimpang, karena penugasannya berakhir 30 Maret 2026
dan batas 1 hari kerja baru habis pada tanggal acuan. Sampel berasal dari satu lokasi.

## Hasil acuan delapan baris (tanggal acuan 30 Oktober 2026)

8 baris, 7 aktif, 1 tidak aktif dikecualikan. USR002 tanpa pemilik, USR003 akun
bersama dan terlambat, USR005 terlambat. Total 3 akun berindikasi dan 4 indikasi.
Tinjauan tepat waktu 5/7 = 71,43 persen. Dengan batas 31 hari, yang sesuai dengan
siklus bulanan, hasilnya turun menjadi 3/7 = 42,86 persen. USR006 tidak dihitung
sebagai pengecualian aktif. Tidak ada data akses di luar jam kerja pada CSV ini;
kesimpulan seperti itu memerlukan log tambahan.

Uji rancangan memerlukan kebijakan serta kewenangan. Uji operasi memerlukan
bukti tinjau dan tindak lanjut. Potret satu tanggal tidak membuktikan efektivitas
setahun penuh. Simpan kertas kerja dan jelaskan pemilihan populasi.
