# Kegunaan: menghitung ulang biaya dan jam peta jalan Bab 14 dari baris CSV.
# Cara memakai: python periksa_peta_jalan.py (jalankan di folder berkas ini).
"""Menghitung ulang jumlah peta jalan supaya tabel tidak berbeda dari barisnya.

Jumlah pada presentasi direksi mudah bergeser ketika satu baris berubah. Skrip ini
menurunkan semua jumlah dari CSV, sehingga selisih dengan naskah terlihat langsung.
"""
import csv
from decimal import Decimal
from pathlib import Path

FOLDER = Path(__file__).resolve().parent
BERKAS_BIAYA = FOLDER / "peta-jalan-grc.csv"
BERKAS_JAM = FOLDER / "beban-jam-peta-jalan.csv"
# Tarif mengikuti Bab 7; mengubahnya mengubah nilai jam dan uang baru sekaligus.
TARIF_JUTA_PER_JAM = Decimal("0.06")
# Anggaran mengikuti Bab 1 dan Bab 2, dalam juta rupiah.
ANGGARAN_MODERNISASI = Decimal("10000")
MEDIKARA_PLUS = Decimal("8400")
RUANG_TOLERANSI = Decimal("400")
# Batas Bab 2: di atasnya keputusan memerlukan dewan komisaris.
BATAS_DIREKSI = Decimal("5000")
KOLOM_BIAYA = ("biaya_t1_juta", "biaya_t2_juta", "biaya_t3_juta")
KOLOM_JAM = ("jam_t1", "jam_t2", "jam_t3")


def baca_csv(jalur):
  """Membaca CSV dan melewati baris komentar agar berkas tetap dapat dibuka tim."""
  with open(jalur, encoding="utf-8", newline="") as berkas:
    baris_data = [baris for baris in berkas if not baris.startswith("#")]
  return list(csv.DictReader(baris_data))


def jumlah_kolom(daftar_baris, kolom):
  """Menjumlahkan per tahun; Decimal mencegah galat pembulatan pada rupiah."""
  return [sum(Decimal(baris[nama]) for baris in daftar_baris) for nama in kolom]


def jumlah_jam_grup(daftar_baris, kelompok):
  """Memisahkan jam di dalam GRC-01, karena jam itu tidak menambah rupiah."""
  terpilih = [baris for baris in daftar_baris if baris["kelompok"] == kelompok]
  return jumlah_kolom(terpilih, KOLOM_JAM)


def cetak_baris(label, nilai):
  """Mencetak nilai per tahun dan jumlahnya dalam susunan yang sama dengan tabel."""
  teks = "  ".join(f"{angka:>9}" for angka in nilai)
  print(f"{label:<24}{teks}  jumlah {sum(nilai):>9}")


def main():
  """Mencetak biaya penuh, jam, uang baru, dan pembacaan terhadap anggaran."""
  biaya = jumlah_kolom(baca_csv(BERKAS_BIAYA), KOLOM_BIAYA)
  baris_jam = baca_csv(BERKAS_JAM)
  jam = jumlah_kolom(baris_jam, KOLOM_JAM)
  nilai_jam = [angka * TARIF_JUTA_PER_JAM for angka in jam]
  uang_baru = [penuh - staf for penuh, staf in zip(biaya, nilai_jam)]
  cetak_baris("Biaya penuh, juta", biaya)
  cetak_baris("Jam di dalam GRC-01", jumlah_jam_grup(baris_jam, "di dalam GRC-01"))
  cetak_baris("Jumlah jam", jam)
  cetak_baris("Nilai jam, juta", nilai_jam)
  cetak_baris("Uang baru, juta", uang_baru)
  sisa = ANGGARAN_MODERNISASI - MEDIKARA_PLUS
  tersedia = sisa - RUANG_TOLERANSI
  print(f"Sisa modernisasi {sisa}; tersedia {tersedia}")
  print(f"Kurang pada Tahun 1 {uang_baru[0] - tersedia}")
  print(f"Jarak ke batas direksi {BATAS_DIREKSI - sum(biaya)}")


if __name__ == "__main__":
  main()
