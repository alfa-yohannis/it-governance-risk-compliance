# Diagram Bab

Gambar aktif pada modul dan slide adalah diagram konsep TikZ berlabel. Setiap panah menyatakan alur atau relasi yang tertulis pada labelnya. Diagram disusun dari konsep, batasan, dan kasus pada naskah masing-masing bab, bukan hanya dari judul bab.

Setiap berkas `chNN-diagram-konsep.tex` berisi satu `tikzpicture` tanpa preamble. Modul memanggilnya dengan `\input{../figures/chNN-diagram-konsep.tex}`, slide dengan `\input{../../figures/chNN-diagram-konsep.tex}`. Spesifikasi komponen, hubungan, catatan batas, dan dasar pemilihan terdapat pada [chapter-diagrams.json](chapter-diagrams.json). Kotak memakai notasi generik, bukan klaim konformansi ArchiMate atau reproduksi gambar standar.

| Bab | Isi diagram | TikZ |
| --- | --- | --- |
| 01 | Dari tujuan layanan ke kontrol dan bukti GRC | [ch01-diagram-konsep.tex](ch01-diagram-konsep.tex) |
| 02 | Evaluate, Direct, Monitor dengan pelibatan pemangku kepentingan | [ch02-diagram-konsep.tex](ch02-diagram-konsep.tex) |
| 03 | Menurunkan sumber hukum menjadi kewajiban yang dapat diuji | [ch03-diagram-konsep.tex](ch03-diagram-konsep.tex) |
| 04 | COBIT 2019: tujuan, faktor desain, dan bukti kapabilitas | [ch04-diagram-konsep.tex](ch04-diagram-konsep.tex) |
| 05 | Skenario risiko dinilai terhadap tujuan dan kriteria | [ch05-diagram-konsep.tex](ch05-diagram-konsep.tex) |
| 06 | ISMS menghubungkan risiko, kontrol, dan hasil keamanan | [ch06-diagram-konsep.tex](ch06-diagram-konsep.tex) |
| 07 | Tujuan dan dasar pemrosesan mengendalikan alur data pribadi | [ch07-diagram-konsep.tex](ch07-diagram-konsep.tex) |
| 08 | Rancangan tata kelola target berawal dari celah yang terbukti | [ch08-diagram-konsep.tex](ch08-diagram-konsep.tex) |
| 09 | Risiko konsentrasi tersembunyi di balik beberapa vendor | [ch09-diagram-konsep.tex](ch09-diagram-konsep.tex) |
| 10 | Kelangsungan layanan memerlukan jalur bisnis dan teknologi | [ch10-diagram-konsep.tex](ch10-diagram-konsep.tex) |
| 11 | AI dikelola menurut tujuan, dampak, dan kemampuan pengawasan | [ch11-diagram-konsep.tex](ch11-diagram-konsep.tex) |
| 12 | Pengelolaan risiko dan asurans independen mempunyai peran berbeda | [ch12-diagram-konsep.tex](ch12-diagram-konsep.tex) |
| 13 | Indikator yang berbeda memicu keputusan yang berbeda | [ch13-diagram-konsep.tex](ch13-diagram-konsep.tex) |
| 14 | Satu kontrol terhubung ke risiko, kewajiban, dan bukti | [ch14-diagram-konsep.tex](ch14-diagram-konsep.tex) |

## Membuat ulang

Jalankan dari akar repositori dengan Python 3. Skrip hanya memakai pustaka standar:

```powershell
python tools/render-diagrams.py
python tools/render-diagrams.py --chapter 1 5
```

Metrik font Titillium Web dibaca dari `module/fonts/` untuk membungkus teks dan menempatkan label. Jalur panah dicari pada grid agar tidak menembus kotak, dan label tidak menutup ujung panah. Skrip berhenti dengan pesan galat bila teks tidak muat di kotak atau label menimpa kotak. Ubah `chapter-diagrams.json` untuk mengubah komponen atau relasi, lalu jalankan ulang skrip. Berkas `.tex` hasilnya tidak disunting langsung.

JPG ilustrasi terdahulu disimpan sebagai arsip dan tidak lagi dirujuk pada gambar bab aktif. Diagram TikZ pendukung yang sudah ada tetap menjadi bagian materi.
