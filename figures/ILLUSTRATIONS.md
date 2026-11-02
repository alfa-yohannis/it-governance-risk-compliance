# Diagram Bab

Gambar aktif pada modul dan slide adalah diagram PNG berlabel. Setiap panah menyatakan alur atau relasi yang tertulis pada labelnya. Diagram disusun dari konsep, batasan, dan kasus pada naskah masing-masing bab, bukan hanya dari judul bab. Seluruh diagram ini dibuat tanpa TikZ.

PNG dipakai oleh LaTeX; SVG menyimpan versi vektor. Spesifikasi komponen, hubungan, catatan batas, dan dasar pemilihan terdapat pada [chapter-diagrams.json](chapter-diagrams.json). Kotak memakai notasi generik, bukan klaim konformansi ArchiMate atau reproduksi gambar standar.

| Bab | Isi diagram | PNG | SVG |
| --- | --- | --- | --- |
| 01 | Dari tujuan layanan ke kontrol dan bukti GRC | [gambar](ch01-diagram-konsep.png) | [vektor](ch01-diagram-konsep.svg) |
| 02 | Evaluate, Direct, Monitor dengan pelibatan pemangku kepentingan | [gambar](ch02-diagram-konsep.png) | [vektor](ch02-diagram-konsep.svg) |
| 03 | Menurunkan sumber hukum menjadi kewajiban yang dapat diuji | [gambar](ch03-diagram-konsep.png) | [vektor](ch03-diagram-konsep.svg) |
| 04 | COBIT 2019: tujuan, faktor desain, dan bukti kapabilitas | [gambar](ch04-diagram-konsep.png) | [vektor](ch04-diagram-konsep.svg) |
| 05 | Skenario risiko dinilai terhadap tujuan dan kriteria | [gambar](ch05-diagram-konsep.png) | [vektor](ch05-diagram-konsep.svg) |
| 06 | ISMS menghubungkan risiko, kontrol, dan hasil keamanan | [gambar](ch06-diagram-konsep.png) | [vektor](ch06-diagram-konsep.svg) |
| 07 | Tujuan dan dasar pemrosesan mengendalikan alur data pribadi | [gambar](ch07-diagram-konsep.png) | [vektor](ch07-diagram-konsep.svg) |
| 08 | Rancangan tata kelola target berawal dari celah yang terbukti | [gambar](ch08-diagram-konsep.png) | [vektor](ch08-diagram-konsep.svg) |
| 09 | Risiko konsentrasi tersembunyi di balik beberapa vendor | [gambar](ch09-diagram-konsep.png) | [vektor](ch09-diagram-konsep.svg) |
| 10 | Kelangsungan layanan memerlukan jalur bisnis dan teknologi | [gambar](ch10-diagram-konsep.png) | [vektor](ch10-diagram-konsep.svg) |
| 11 | AI dikelola menurut tujuan, dampak, dan kemampuan pengawasan | [gambar](ch11-diagram-konsep.png) | [vektor](ch11-diagram-konsep.svg) |
| 12 | Pengelolaan risiko dan asurans independen mempunyai peran berbeda | [gambar](ch12-diagram-konsep.png) | [vektor](ch12-diagram-konsep.svg) |
| 13 | Indikator yang berbeda memicu keputusan yang berbeda | [gambar](ch13-diagram-konsep.png) | [vektor](ch13-diagram-konsep.svg) |
| 14 | Satu kontrol terhubung ke risiko, kewajiban, dan bukti | [gambar](ch14-diagram-konsep.png) | [vektor](ch14-diagram-konsep.svg) |

## Membuat ulang

Jalankan dari akar repositori dengan Python, Matplotlib, dan Pillow:

```powershell
python tools/render-diagrams.py
python tools/render-diagrams.py --chapter 1 5
```

Font Titillium Web dibaca dari `module/fonts/`. PNG RGB maksimum 500 KiB; SVG menyimpan huruf sebagai path agar tampilannya tetap sama. Ubah `chapter-diagrams.json` untuk mengubah komponen atau relasi.

JPG ilustrasi terdahulu disimpan sebagai arsip dan tidak lagi dirujuk pada gambar bab aktif. Diagram TikZ pendukung yang sudah ada tetap menjadi bagian materi.
