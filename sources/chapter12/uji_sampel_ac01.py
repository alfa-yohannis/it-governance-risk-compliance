"""Uji sampel AC-01 dan batas statistiknya: python uji_sampel_ac01.py dari folder bab.

Skrip menghitung penyimpangan pada data sintetis dan menunjukkan apa yang tidak
dapat dibuktikan sampel. Hasilnya bahan penilaian auditor, bukan vonis.
"""

import argparse
import csv
import json
from datetime import date, timedelta
from math import comb
from pathlib import Path

POPULASI_AKUN = 120
TANGGAL_ACUAN_CONTOH = "2026-03-31"
TINGKAT_RISIKO = 0.05
PENANDA_KOMENTAR = "#"
HARI_SABTU = 5
KOLOM_WAJIB = {"akun", "penugasan_berakhir", "status_akun"}
HASIL_YANG_DIBACA = (6, 2, 0)
AKUN_BERMASALAH_YANG_DIUJI = (24, 12, 6, 2, 1)
UKURAN_SAMPEL_CONTOH = 30


def baca_sampel(lokasi):
  """Tolak kolom hilang dan akun ganda agar kesalahan data tidak terbaca lulus."""
  with lokasi.open(encoding="utf-8-sig", newline="") as berkas:
    baris_data = [
      baris for baris in berkas if not baris.startswith(PENANDA_KOMENTAR)
    ]
  pembaca = csv.DictReader(baris_data)
  if not KOLOM_WAJIB.issubset(pembaca.fieldnames or []):
    raise ValueError("Kolom wajib tidak lengkap")
  catatan_akun = list(pembaca)
  identitas = [catatan["akun"] for catatan in catatan_akun]
  if len(identitas) != len(set(identitas)):
    raise ValueError("Identitas akun ganda")
  return catatan_akun


def hari_kerja_berikutnya(tanggal):
  """Geser ke Senin bila jatuh pada akhir pekan; hari libur belum dihitung."""
  berikutnya = tanggal + timedelta(days=1)
  while berikutnya.weekday() >= HARI_SABTU:
    berikutnya += timedelta(days=1)
  return berikutnya


def akun_menyimpang(catatan, tanggal_acuan):
  """Akun menyimpang bila masih aktif setelah batas 1 hari kerja terlewati."""
  if catatan["status_akun"] != "aktif":
    return False
  penugasan_berakhir = date.fromisoformat(catatan["penugasan_berakhir"])
  return tanggal_acuan > hari_kerja_berikutnya(penugasan_berakhir)


def peluang_nol_temuan(akun_bermasalah, ukuran_sampel, populasi):
  """Hitung peluang sampel acak tidak memuat satu pun akun bermasalah."""
  cara_tanpa_masalah = comb(populasi - akun_bermasalah, ukuran_sampel)
  return cara_tanpa_masalah / comb(populasi, ukuran_sampel)


def peluang_paling_banyak(temuan, akun_bermasalah, ukuran_sampel, populasi):
  """Hitung peluang hipergeometrik karena sampel diambil tanpa pengembalian."""
  jumlah_cara = 0
  for jumlah in range(temuan + 1):
    jumlah_cara += comb(akun_bermasalah, jumlah) * comb(
      populasi - akun_bermasalah, ukuran_sampel - jumlah
    )
  return jumlah_cara / comb(populasi, ukuran_sampel)


def batas_atas(temuan, ukuran_sampel, populasi):
  """Cari jumlah akun bermasalah terbesar yang masih wajar menghasilkan temuan."""
  terbesar = temuan
  for akun_bermasalah in range(temuan, populasi + 1):
    peluang = peluang_paling_banyak(
      temuan, akun_bermasalah, ukuran_sampel, populasi
    )
    if peluang >= TINGKAT_RISIKO:
      terbesar = akun_bermasalah
  return terbesar


def batas_bawah(temuan, ukuran_sampel, populasi):
  """Cari jumlah akun bermasalah terkecil yang masih wajar menghasilkan temuan."""
  if temuan == 0:
    return 0
  for akun_bermasalah in range(populasi + 1):
    peluang = 1 - peluang_paling_banyak(
      temuan - 1, akun_bermasalah, ukuran_sampel, populasi
    )
    if peluang >= TINGKAT_RISIKO:
      return akun_bermasalah
  return populasi


def sampel_minimal(akun_bermasalah, populasi):
  """Cari sampel terkecil yang 95 persen pasti memuat minimal satu akun itu."""
  for ukuran_sampel in range(1, populasi + 1):
    peluang = peluang_nol_temuan(akun_bermasalah, ukuran_sampel, populasi)
    if peluang <= TINGKAT_RISIKO:
      return ukuran_sampel
  return populasi


def ringkas_hasil(catatan_akun, tanggal_acuan, populasi):
  """Satukan hitungan agar setiap angka pada bab dapat diperiksa ulang."""
  menyimpang = [
    catatan["akun"]
    for catatan in catatan_akun
    if akun_menyimpang(catatan, tanggal_acuan)
  ]
  ukuran_sampel = len(catatan_akun)
  bacaan_sampel = []
  for temuan in HASIL_YANG_DIBACA:
    bacaan_sampel.append({
      "temuan": temuan,
      "perkiraan_titik": temuan * populasi // UKURAN_SAMPEL_CONTOH,
      "batas_bawah": batas_bawah(temuan, UKURAN_SAMPEL_CONTOH, populasi),
      "batas_atas": batas_atas(temuan, UKURAN_SAMPEL_CONTOH, populasi),
    })
  daya_deteksi = []
  for akun_bermasalah in AKUN_BERMASALAH_YANG_DIUJI:
    peluang_nol = peluang_nol_temuan(
      akun_bermasalah, UKURAN_SAMPEL_CONTOH, populasi
    )
    daya_deteksi.append({
      "akun_bermasalah": akun_bermasalah,
      "peluang_tertangkap_persen": round((1 - peluang_nol) * 100, 2),
      "sampel_minimal_95_persen": sampel_minimal(akun_bermasalah, populasi),
    })
  return {
    "tanggal_acuan": tanggal_acuan.isoformat(),
    "ukuran_sampel": ukuran_sampel,
    "akun_sesuai": ukuran_sampel - len(menyimpang),
    "akun_menyimpang": len(menyimpang),
    "daftar_menyimpang": menyimpang,
    "persen_menyimpang": round(len(menyimpang) / ukuran_sampel * 100, 2),
    "populasi": populasi,
    "bacaan_sampel_bila_acak": bacaan_sampel,
    "daya_deteksi_sampel_30": daya_deteksi,
    "batas_klaim": "Sampel contoh satu lokasi; batas statistik hanya bila acak",
  }


def main():
  """Baca CSV lokal dan cetak JSON; tidak ada sistem organisasi yang diakses."""
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    "berkas", nargs="?", default="sampel-ac01-30-akun.csv", type=Path
  )
  parser.add_argument("--tanggal", default=TANGGAL_ACUAN_CONTOH)
  parser.add_argument("--populasi", default=POPULASI_AKUN, type=int)
  argumen = parser.parse_args()
  try:
    tanggal_acuan = date.fromisoformat(argumen.tanggal)
    catatan_akun = baca_sampel(argumen.berkas)
    hasil = ringkas_hasil(catatan_akun, tanggal_acuan, argumen.populasi)
  except (ValueError, OSError, csv.Error) as kesalahan:
    parser.error(str(kesalahan))
  print(json.dumps(hasil, ensure_ascii=False, indent=2))


if __name__ == "__main__":
  main()
