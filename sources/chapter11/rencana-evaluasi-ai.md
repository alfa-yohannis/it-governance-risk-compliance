<!-- Panduan evaluasi AI; gunakan hanya kasus sintetis dan tetapkan kriteria sebelum pengujian. -->
# Rencana Evaluasi AI

Misalkan AI merangkum 100 catatan sintetis. Tidak ada identitas, rekam medis,
atau teks pasien nyata yang dikirim ke penyedia model. Seluruh angka mengikuti
Bab 11 dan merupakan pengandaian.

| Unsur | Contoh rencana | Isian tim |
| --- | --- | --- |
| Tujuan | Mengurangi waktu dokumentasi tanpa menghilangkan informasi penting | ... |
| Ukuran awal (*baseline*) | Manual 12 menit per catatan; 1 kesalahan kritis dari 100 | ... |
| Pembanding | Draf 2 menit dan pemeriksaan 8 menit; bersih hemat 2 menit | ... |
| Kesalahan kritis | Alergi atau obat penting terlewat | ... |
| Kriteria lulus | Keseluruhan tidak melebihi 1 persen; tidak ada kelompok di atas 3 persen | ... |
| Sampel | 100 kasus sintetis: 60 di bawah 60 tahun, 40 berusia 60 tahun ke atas | ... |
| Penilai | Dua penilai kompeten, 15 menit per kasus; selisih dinilai ulang | ... |
| Uji pemeriksa | 150 ringkasan memuat 20 kesalahan sisipan; hitung temuan per waktu periksa | ... |
| Penghentian | Kesalahan kritis di atas kriteria memicu penghentian uji dan analisis sebab | ... |
| Batas klaim | Sampel kecil tidak membuktikan keselamatan produksi | ... |

Catat versi, tanggal, konfigurasi, pertanyaan, keluaran, dan penilaian. Uji
instruksi menyesatkan hanya melalui dokumen tiruan. Bandingkan hasil per
kelompok dan catat ketidakpastian. Jika 4 dari 100 ringkasan menghilangkan
alergi, laporkan 4 kejadian tersebut; rerata kemiripan teks tidak menutupnya.

## Hitungan yang dapat dicek ulang

- Beban satu putaran: 100 kasus kali 15 menit kali 2 penilai sama dengan 50 jam.
- Volume 60.000 ringkasan dengan tingkat 4 persen menghasilkan 2.400 ringkasan
  bermasalah sebelum pemeriksaan.
- Pemeriksa yang menemukan 70 persen menyisakan 720. Pemeriksa yang menemukan
  90 persen menyisakan 240, tetapi waktunya 14 menit, lebih lama daripada manual.
- Tingkat 1 persen menghasilkan 600, dan pemeriksa 70 persen menyisakan 180.
- Pembanding manual 1 persen setara 600 ringkasan per tahun.

Contoh bentuk laporan per kelompok ada di `contoh-hasil-uji-ai.csv`.
