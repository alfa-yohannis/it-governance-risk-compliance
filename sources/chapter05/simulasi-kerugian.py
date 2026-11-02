# Kegunaan: simulasi Monte Carlo kerugian tahunan R-01 dan R-03 (Pendalaman Bab 05).
# Cara memakai: python simulasi-kerugian.py, bandingkan dengan kurva-kerugian.csv.
"""Simulasi kerugian tahunan, paling banyak satu kejadian per skenario per tahun.

Model sengaja sederhana supaya hasilnya dapat dicek dengan hitungan tangan.
Seluruh angka pengandaian pembelajaran, bukan kerugian Medikara yang telah diukur.
"""

import random

# Jumlah tahun besar supaya selisih dengan hitungan tangan kecil, tetapi tetap cepat.
JUMLAH_TAHUN_SIMULASI = 200_000

# Benih tetap membuat hasil dapat diulang oleh peninjau lain.
BENIH_ACAK = 2026

# Setiap tingkat berisi pasangan (kerugian dalam juta rupiah, peluang bersyarat).
TINGKAT_KERUGIAN_R01 = ((100, 0.5), (500, 0.3), (1500, 0.2))
TINGKAT_KERUGIAN_R03 = ((50, 0.5), (100, 0.3), (200, 0.2))

PELUANG_R01_AWAL = 0.2
PELUANG_R01_SETELAH_KONTROL = 0.05
PELUANG_R03 = 0.3

# Ambang mengikuti Tabel kurva kerugian pada naskah, dalam juta rupiah.
AMBANG_KERUGIAN_JUTA = (100, 200, 500, 1500)


def tarik_kerugian(pembangkit, peluang_kejadian, tingkat_kerugian):
  """Mengembalikan kerugian satu tahun; nol berarti skenario tidak terjadi tahun itu."""
  if pembangkit.random() >= peluang_kejadian:
    return 0
  nilai_acak = pembangkit.random()
  peluang_kumulatif = 0.0
  for kerugian_juta, peluang_bersyarat in tingkat_kerugian:
    peluang_kumulatif += peluang_bersyarat
    if nilai_acak < peluang_kumulatif:
      return kerugian_juta
  # Galat pembulatan pecahan dapat melewati perulangan; tingkat terakhir dipakai.
  return tingkat_kerugian[-1][0]


def ringkas_hasil(nama_skenario, daftar_kerugian):
  """Mencetak rata-rata dan peluang melampaui ambang supaya mudah dibandingkan."""
  jumlah_tahun = len(daftar_kerugian)
  rata_rata_juta = sum(daftar_kerugian) / jumlah_tahun
  print(f"{nama_skenario}: rata-rata Rp{rata_rata_juta:.1f} juta per tahun")
  for ambang_juta in AMBANG_KERUGIAN_JUTA:
    jumlah_melampaui = sum(1 for kerugian in daftar_kerugian if kerugian >= ambang_juta)
    persen = 100 * jumlah_melampaui / jumlah_tahun
    print(f"  peluang kerugian >= Rp{ambang_juta} juta: {persen:.2f} persen")


def jalankan_simulasi():
  """Menjalankan tiga kumpulan tahun dan mencetak ringkasannya."""
  pembangkit = random.Random(BENIH_ACAK)
  r01_awal = []
  r01_setelah_kontrol = []
  gabungan_awal = []
  for _ in range(JUMLAH_TAHUN_SIMULASI):
    kerugian_awal = tarik_kerugian(pembangkit, PELUANG_R01_AWAL, TINGKAT_KERUGIAN_R01)
    kerugian_kontrol = tarik_kerugian(
      pembangkit, PELUANG_R01_SETELAH_KONTROL, TINGKAT_KERUGIAN_R01
    )
    # R-03 ditarik terpisah karena model mengandaikan kedua skenario tidak terkait.
    kerugian_r03 = tarik_kerugian(pembangkit, PELUANG_R03, TINGKAT_KERUGIAN_R03)
    r01_awal.append(kerugian_awal)
    r01_setelah_kontrol.append(kerugian_kontrol)
    gabungan_awal.append(kerugian_awal + kerugian_r03)
  ringkas_hasil("R-01 awal", r01_awal)
  ringkas_hasil("R-01 setelah AC-01", r01_setelah_kontrol)
  ringkas_hasil("R-01 awal ditambah R-03", gabungan_awal)


if __name__ == "__main__":
  jalankan_simulasi()
