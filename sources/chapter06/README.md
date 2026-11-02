<!-- Kegunaan: indeks berkas Aktivitas Bab 06. Cara pakai: salin templat ke folder tim, baca petunjuk, dan pisahkan contoh pengandaian dari bukti organisasi. -->

# Sumber Bab 06

| Berkas | Kegunaan |
| --- | --- |
| `profil-csf-saat-ini.csv` | Templat profil dengan 14 subkategori pada enam fungsi sebagai titik awal. |
| `contoh-profil-medikara.csv` | Contoh status dan batas bukti untuk 14 subkategori dalam skenario pembelajaran. |
| `celah-kontrol.csv` | Enam contoh celah dan baris isian: hasil yang belum tercapai, nomor Annex A, kontrol, risiko, kewajiban, pemilik, dan bukti penerimaan. |
| `pemetaan-csf-annex-a.csv` | Nomor klausul dan Annex A untuk 14 subkategori, disalin dari berkas CSF 2.0 Reference Tool NIST. |
| `panduan-bukti.md` | Cara mencatat cakupan, populasi, sampel, izin, dan batas kesimpulan. |
| `catatan-soa.md` | Lembar alasan pemilihan dan pengecualian kontrol. |

## Cara memakai

1. Baca tujuan dan Aktivitas pada bab, lalu tetapkan ruang lingkup serta peran tim.
2. Salin berkas isian; pertahankan berkas contoh sebagai pembanding.
3. Isi sumber bukti, pemilik, keputusan, dan hal yang belum diketahui.
4. Tautkan setiap celah ke risiko Bab 5 dan kewajiban Bab 3.
5. Tinjau bersama anggota berlatar nonteknis dan teknis sebelum pengumpulan.

Berkas CSV memakai UTF-8 dan pemisah koma. Baris pertama berisi komentar kegunaan,
dan nama kolom ada pada baris kedua. Hapus baris komentar bila aplikasi spreadsheet
atau alat impor tidak menerimanya. Buka melalui menu impor bila pemisah lokal berbeda.
Seluruh angka tambahan pada contoh adalah pengandaian pembelajaran.
Data organisasi nyata harus berizin dan anonim; jangan menyalin data pasien,
rahasia akses, atau dokumen asli organisasi ke folder tugas.

## Status profil

Gunakan terbukti, sebagian, belum ada bukti, atau tidak relevan sebagai status
lokal tim. Status ini bukan tier atau sertifikat resmi NIST. Jangan menyimpulkan
keamanan seluruh organisasi dari satu sampel, satu lokasi, atau keberhasilan cadangan.

## Dua kolom pemilik

`pemilik_risiko` mengikuti register Bab 5, misalnya pemilik SIMRS untuk R-02.
`pemilik_hasil` dan `pemilik_tindakan` menunjuk penanggung jawab hasil, bukti, atau
tindakan, misalnya kepala TI untuk inventaris sistem. Kedua peran itu tidak boleh
dianggap sama.

## Membaca pemetaan

Nomor pada `pemetaan-csf-annex-a.csv` menunjukkan kaitan, bukan kesetaraan. NIST tidak
menguji kebenaran pemetaan dari pihak lain. Dua daftar untuk satu subkategori dapat
berbeda, seperti pada PR.AA-05. Cocokkan nomor ke naskah berlisensi sebelum dipakai
sebagai temuan audit.
