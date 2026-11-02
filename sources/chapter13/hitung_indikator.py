"""Hitung 12 indikator Bab 13: jalankan python hitung_indikator.py di folder ini.

Perhitungan lokal menjaga definisi, penyebut nol, dan status tetap terlihat.
Skrip tidak membuat skor gabungan, karena skor gabungan menyembunyikan status merah.
"""

import argparse
import csv
import sys
from operator import itemgetter
from pathlib import Path

HIJAU = "HIJAU"
KUNING = "KUNING"
MERAH = "MERAH"
TIDAK_BERLAKU = "TIDAK_BERLAKU"
DATA_TIDAK_TERSEDIA = "DATA_TIDAK_TERSEDIA"

# Urutan ini dipakai bila dua angka harus dibaca bersama: yang terburuk menang.
TINGKAT_KEPARAHAN = {HIJAU: 0, KUNING: 1, MERAH: 2}

KOMENTAR_KELUARAN = (
  "# Kegunaan: keluaran hitung_indikator.py untuk tiga periode Bab 13. "
  "Cara memakai: bandingkan dengan hitungan manual; jangan disalin sebagai bukti."
)

# Toleransi nol dari Bab 5: tidak ada zona kuning agar pelanggaran tidak dilunakkan.
TOLERANSI_NOL = (
  ("IK-01", "akun_tanpa_pemilik", "akun"),
  ("IK-02", "akun_lewat_masa", "akun"),
  ("IK-04", "skenario_lewat_batas", "skenario"),
  ("IK-05", "kewajiban_lewat_tenggat", "baris"),
  ("IK-06", "cedera_lewat_tinjauan", "laporan"),
)

# Makin kecil makin baik: kolom, batas hijau, batas merah, dan apakah batas merah
# sudah termasuk merah. IK-03 merah sesudah 120 menit; IK-12 merah mulai 30 menit.
MAKIN_KECIL_MAKIN_BAIK = (
  ("IK-03", "KRI", "menit_gangguan_pendaftaran", 90, 120, False),
  ("IK-12", "KPI", "menit_tunggu_pendaftaran", 25, 30, True),
)

# Rasio: jenis, pembilang, penyebut, batas hijau, dan batas kuning dalam persen.
RASIO = (
  ("IK-07", "KCI", "akun_ditinjau", "akun_aktif", 95, 90),
  ("IK-09", "KCI", "dpia_selesai", "dpia_wajib", 100, 80),
  ("IK-10", "KPI", "temuan_tertutup", "temuan_jatuh_tempo", 90, 80),
  ("IK-11", "KPI", "pemberitahuan_tepat", "pemberitahuan_wajib", 100, 100),
)

# IK-08 memakai dua rasio dengan ambang yang sama, sehingga 5 uji SIMRS rumah sakit
# tidak tenggelam di antara uji fasilitas lain.
UJI_PEMULIHAN_HIJAU = 100
UJI_PEMULIHAN_KUNING = 75
KOLOM_UJI = ("uji_total", "uji_lulus", "uji_rumah_sakit", "uji_rumah_sakit_lulus")

DESIMAL_TAMPILAN = 2
KOLOM_KELUARAN = ("periode", "id", "jenis", "nilai", "satuan", "status", "catatan")


def kolom_wajib():
  """Kumpulkan kolom dari definisi agar data yang kurang langsung ditolak."""
  kolom = {"periode", "cedera_dilaporkan", *KOLOM_UJI}
  kolom.update(definisi[1] for definisi in TOLERANSI_NOL)
  kolom.update(definisi[2] for definisi in MAKIN_KECIL_MAKIN_BAIK)
  for definisi in RASIO:
    kolom.update(definisi[2:4])
  return kolom


def angka_opsional(teks):
  """Bedakan data kosong dari nol sah agar mutu data tidak disembunyikan."""
  if teks is None:
    raise ValueError("Baris tidak memiliki seluruh kolom")
  if not teks.strip():
    return None
  nilai = int(teks)
  if nilai < 0:
    raise ValueError("Jumlah tidak boleh negatif")
  return nilai


def status_rasio(pembilang, penyebut, batas_hijau, batas_kuning):
  """Bandingkan nilai penuh sebelum pembulatan agar ambang tidak bergeser."""
  if pembilang is None or penyebut is None:
    return None, DATA_TIDAK_TERSEDIA
  if pembilang > penyebut:
    raise ValueError("Pembilang melebihi penyebut")
  if penyebut == 0:
    return None, TIDAK_BERLAKU
  nilai = pembilang / penyebut * 100
  if nilai >= batas_hijau:
    return nilai, HIJAU
  if nilai >= batas_kuning:
    return nilai, KUNING
  return nilai, MERAH


def status_toleransi_nol(nilai):
  """Nol hijau dan lebih dari nol merah, tanpa zona kuning buatan."""
  if nilai is None:
    return DATA_TIDAK_TERSEDIA
  return HIJAU if nilai == 0 else MERAH


def status_makin_kecil(nilai, batas_hijau, batas_merah, batas_termasuk_merah):
  """Tentukan status ukuran yang membaik ketika angkanya mengecil."""
  if nilai is None:
    return DATA_TIDAK_TERSEDIA
  if nilai <= batas_hijau:
    return HIJAU
  melewati_batas = nilai >= batas_merah if batas_termasuk_merah else nilai > batas_merah
  return MERAH if melewati_batas else KUNING


def status_terburuk(status_pertama, status_kedua):
  """Pilih status terburuk; status tanpa nilai mengalah pada yang dapat dinilai."""
  if status_pertama not in TINGKAT_KEPARAHAN:
    return status_kedua
  if status_kedua not in TINGKAT_KEPARAHAN:
    return status_pertama
  return max(status_pertama, status_kedua, key=TINGKAT_KEPARAHAN.get)


def bulatkan(nilai):
  """Bulatkan hanya untuk tampilan, sesudah status ditentukan."""
  return None if nilai is None else round(nilai, DESIMAL_TAMPILAN)


def hitung_uji_pemulihan(angka):
  """Baca rasio gabungan dan rasio rumah sakit bersama, lalu pakai yang terburuk."""
  nilai, status_gabungan = status_rasio(
    angka["uji_lulus"], angka["uji_total"], UJI_PEMULIHAN_HIJAU, UJI_PEMULIHAN_KUNING
  )
  hasil_rumah_sakit = status_rasio(
    angka["uji_rumah_sakit_lulus"], angka["uji_rumah_sakit"],
    UJI_PEMULIHAN_HIJAU, UJI_PEMULIHAN_KUNING,
  )
  catatan = (
    f"rumah sakit {angka['uji_rumah_sakit_lulus']}/{angka['uji_rumah_sakit']}"
  )
  return nilai, status_terburuk(status_gabungan, hasil_rumah_sakit[1]), catatan


def hitung_periode(catatan_periode):
  """Keluarkan 12 indikator tanpa merata-ratakan risiko yang berbeda."""
  periode = catatan_periode["periode"]
  angka = {
    kolom: angka_opsional(catatan_periode[kolom])
    for kolom in kolom_wajib() if kolom != "periode"
  }
  hasil = []
  for identitas, kolom, satuan in TOLERANSI_NOL:
    hasil.append({
      "periode": periode, "id": identitas, "jenis": "KRI", "nilai": angka[kolom],
      "satuan": satuan, "status": status_toleransi_nol(angka[kolom]), "catatan": "",
    })
  for definisi in MAKIN_KECIL_MAKIN_BAIK:
    identitas, jenis, kolom, batas_hijau, batas_merah, termasuk = definisi
    hasil.append({
      "periode": periode, "id": identitas, "jenis": jenis, "nilai": angka[kolom],
      "satuan": "menit", "catatan": "",
      "status": status_makin_kecil(angka[kolom], batas_hijau, batas_merah, termasuk),
    })
  for identitas, jenis, pembilang, penyebut, batas_hijau, batas_kuning in RASIO:
    nilai, status = status_rasio(
      angka[pembilang], angka[penyebut], batas_hijau, batas_kuning
    )
    hasil.append({
      "periode": periode, "id": identitas, "jenis": jenis, "nilai": bulatkan(nilai),
      "satuan": "persen", "status": status, "catatan": "",
    })
  nilai, status, catatan = hitung_uji_pemulihan(angka)
  hasil.append({
    "periode": periode, "id": "IK-08", "jenis": "KCI", "nilai": bulatkan(nilai),
    "satuan": "persen", "status": status, "catatan": catatan,
  })
  return sorted(hasil, key=itemgetter("id"))


def baca_dan_hitung(lokasi):
  """Tolak struktur rusak dan periode ganda sebelum menerbitkan dashboard."""
  hasil = []
  periode_terbaca = set()
  with lokasi.open(encoding="utf-8-sig", newline="") as berkas:
    pembaca = csv.DictReader(baris for baris in berkas if not baris.startswith("#"))
    if not kolom_wajib().issubset(pembaca.fieldnames or []):
      raise ValueError("Kolom wajib tidak lengkap")
    for catatan_periode in pembaca:
      if None in catatan_periode:
        raise ValueError("Baris memiliki kolom tambahan tanpa nama")
      periode = catatan_periode["periode"]
      if not periode or periode in periode_terbaca:
        raise ValueError("Periode kosong atau ganda")
      periode_terbaca.add(periode)
      hasil.extend(hitung_periode(catatan_periode))
  return hasil


def main():
  """Cetak CSV agar hasil dapat dibuka tanpa aplikasi dashboard khusus."""
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument("berkas", nargs="?", default="data-indikator.csv", type=Path)
  argumen = parser.parse_args()
  try:
    hasil = baca_dan_hitung(argumen.berkas)
  except (ValueError, OSError, csv.Error) as kesalahan:
    parser.error(str(kesalahan))
  print(KOMENTAR_KELUARAN)
  penulis = csv.DictWriter(
    sys.stdout, fieldnames=KOLOM_KELUARAN, lineterminator="\n",
  )
  penulis.writeheader()
  penulis.writerows(hasil)


if __name__ == "__main__":
  main()
