# Kegunaan: memeriksa kelengkapan register kewajiban dan menghitung sebaran status.
# Cara pakai: python periksa-register.py register-kewajiban.csv

"""Pemeriksa register kewajiban Bab 3.

Register hanya berguna bila tiap baris dapat diuji. Skrip ini menolak baris tanpa
pemilik, bukti, atau status yang dikenal, supaya kekosongan terlihat sebelum register
masuk C1. Skrip tidak menilai kebenaran hukum; penilaian itu tetap tugas tim.
"""

import csv
import sys
from collections import Counter

PENANDA_KOMENTAR = "#"
PENANDA_BARIS_ISIAN = "..."
KOLOM_WAJIB = ("id", "sumber", "kewajiban_ringkas", "pemilik", "bukti", "status_awal")
STATUS_DIKENAL = (
  "Terverifikasi memenuhi",
  "Memenuhi sebagian",
  "Tidak memenuhi",
  "Belum diverifikasi",
  "Tidak berlaku",
)
ARGUMEN_DIPERLUKAN = 2
KODE_KELUAR_MASALAH = 1


def baca_baris_register(jalur_berkas):
  """Membaca baris data dan melewati komentar, supaya templat dapat diberi catatan."""
  with open(jalur_berkas, encoding="utf-8", newline="") as berkas:
    baris_tanpa_komentar = [
      baris for baris in berkas if not baris.startswith(PENANDA_KOMENTAR)
    ]
  return list(csv.DictReader(baris_tanpa_komentar))


def cari_masalah_baris(baris):
  """Mengembalikan masalah satu baris, agar semua kekurangan terlihat sekaligus."""
  masalah = []
  for kolom in KOLOM_WAJIB:
    if not (baris.get(kolom) or "").strip():
      masalah.append(f"kolom {kolom} kosong")
  if baris.get("status_awal") not in STATUS_DIKENAL:
    masalah.append(f"status tidak dikenal: {baris.get('status_awal')}")
  return masalah


def main():
  """Mencetak sebaran status dan masalah; kode keluar 1 menandai ada masalah."""
  if len(sys.argv) != ARGUMEN_DIPERLUKAN:
    print("Cara pakai: python periksa-register.py register-kewajiban.csv")
    return KODE_KELUAR_MASALAH

  semua_baris = baca_baris_register(sys.argv[1])
  # Baris bertanda titik-titik adalah ruang isian mahasiswa, bukan data contoh.
  baris_terisi = [
    baris for baris in semua_baris if baris["jenis"] != PENANDA_BARIS_ISIAN
  ]
  sebaran_status = Counter(baris["status_awal"] for baris in baris_terisi)

  print(f"Jumlah kewajiban: {len(baris_terisi)}")
  for status in STATUS_DIKENAL:
    print(f"  {status}: {sebaran_status[status]}")

  jumlah_masalah = 0
  for baris in baris_terisi:
    for masalah in cari_masalah_baris(baris):
      print(f"Masalah pada {baris['id']}: {masalah}")
      jumlah_masalah += 1

  print(f"Jumlah masalah: {jumlah_masalah}")
  return KODE_KELUAR_MASALAH if jumlah_masalah else 0


if __name__ == "__main__":
  sys.exit(main())
