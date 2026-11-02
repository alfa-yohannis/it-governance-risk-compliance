"""Audit data sintetis: jalankan python audit_hak_akses.py dari folder bab.

Skrip memberi indikasi untuk pemeriksaan lanjutan, bukan vonis penyalahgunaan.
"""

import argparse
import csv
import json
from datetime import date
from pathlib import Path

BATAS_TINJAU_HARI = 90
TANGGAL_ACUAN_CONTOH = "2026-10-30"
PENANDA_KOMENTAR = "#"
KOLOM_WAJIB = {
  "akun", "aktif", "pemilik", "jenis", "terakhir_ditinjau", "persetujuan"
}
JENIS_AKUN = {"individual", "bersama", "layanan"}


def baca_data(lokasi):
  """Validasi bentuk masukan agar kolom hilang tidak dianggap kontrol lulus."""
  with lokasi.open(encoding="utf-8-sig", newline="") as berkas:
    baris_data = [
      teks for teks in berkas if not teks.startswith(PENANDA_KOMENTAR)
    ]
  pembaca = csv.DictReader(baris_data)
  if not KOLOM_WAJIB.issubset(pembaca.fieldnames or []):
    raise ValueError("Kolom wajib tidak lengkap")
  baris = list(pembaca)
  identitas = set()
  for catatan in baris:
    if not catatan["akun"] or catatan["akun"] in identitas:
      raise ValueError("Identitas akun kosong atau ganda")
    identitas.add(catatan["akun"])
    if catatan["aktif"] not in {"ya", "tidak"}:
      raise ValueError("Status aktif harus ya atau tidak")
    if catatan["jenis"] not in JENIS_AKUN:
      raise ValueError("Jenis akun tidak dikenal")
  return baris


def nilai_akun(catatan, tanggal_acuan):
  """Pisahkan indikasi per akun agar satu akun tidak dihitung berulang."""
  indikasi = []
  if not catatan["pemilik"].strip():
    indikasi.append("pemilik_kosong")
  if catatan["jenis"] == "bersama":
    indikasi.append("akun_bersama")
  tanggal_teks = catatan["terakhir_ditinjau"].strip()
  tepat_waktu = False
  if tanggal_teks:
    tanggal_tinjau = date.fromisoformat(tanggal_teks)
    umur_hari = (tanggal_acuan - tanggal_tinjau).days
    if umur_hari < 0:
      raise ValueError("Tanggal tinjau berada setelah tanggal acuan")
    tepat_waktu = umur_hari <= BATAS_TINJAU_HARI
  if not tepat_waktu:
    indikasi.append("tinjauan_terlambat_atau_kosong")
  return indikasi, tepat_waktu


def ringkas_data(catatan_akun, tanggal_acuan):
  """Hitung populasi aktif, cakupan tinjauan, dan indikasi yang dapat ditelusuri."""
  aktif = [catatan for catatan in catatan_akun if catatan["aktif"] == "ya"]
  pengecualian = []
  jumlah_tepat_waktu = 0
  jumlah_indikasi = 0
  for catatan in aktif:
    indikasi, tepat_waktu = nilai_akun(catatan, tanggal_acuan)
    jumlah_tepat_waktu += int(tepat_waktu)
    jumlah_indikasi += len(indikasi)
    if indikasi:
      pengecualian.append({"akun": catatan["akun"], "indikasi": indikasi})
  cakupan = None
  if aktif:
    cakupan = round(jumlah_tepat_waktu / len(aktif) * 100, 2)
  return {
    "tanggal_acuan": tanggal_acuan.isoformat(),
    "batas_tinjau_hari": BATAS_TINJAU_HARI,
    "jumlah_baris": len(catatan_akun),
    "akun_aktif": len(aktif),
    "akun_dikecualikan_tidak_aktif": len(catatan_akun) - len(aktif),
    "akun_dengan_indikasi": len(pengecualian),
    "jumlah_indikasi": jumlah_indikasi,
    "tinjauan_tepat_waktu": jumlah_tepat_waktu,
    "cakupan_tinjauan_persen": cakupan,
    "pengecualian": pengecualian,
    "batas_klaim": "Indikasi snapshot sintetis; perlu validasi bukti auditor",
  }


def main():
  """Baca CSV lokal dan cetak JSON agar hitungan dapat diperiksa ulang."""
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument(
    "berkas", nargs="?", default="data-contoh-hak-akses.csv", type=Path
  )
  parser.add_argument("--tanggal", default=TANGGAL_ACUAN_CONTOH)
  argumen = parser.parse_args()
  try:
    tanggal_acuan = date.fromisoformat(argumen.tanggal)
    hasil = ringkas_data(baca_data(argumen.berkas), tanggal_acuan)
  except (ValueError, OSError, csv.Error) as kesalahan:
    parser.error(str(kesalahan))
  print(json.dumps(hasil, ensure_ascii=False, indent=2))


if __name__ == "__main__":
  main()
