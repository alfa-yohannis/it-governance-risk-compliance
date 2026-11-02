# Kegunaan: menghitung batas 72 jam Bab 7 dari beberapa titik mulai.
# Cara pakai: python hitung-tenggat-notifikasi.py
"""Menghitung batas pemberitahuan pengandaian insiden vendor 2025.

Skrip ini tidak menetapkan batas hukum. Pasal 46 ayat (1) UU PDP tidak menulis titik
mulai, sehingga tim perlu melihat akibat tiap pilihan sebelum fungsi hukum memutuskan.
"""

from datetime import datetime, timedelta

# Rentang ditulis sebagai jam kalender, karena pasal menulis jam, bukan hari kerja.
JAM_RENTANG = 72

# Tanggal hanya penanda supaya hari jatuh sesuai pengandaian: hari ke-1 adalah Selasa.
# Tahun 2025 mengikuti fakta kasus; tanggal bulannya bukan fakta kasus.
HARI_KE_1 = datetime(2025, 3, 4, 20, 0)

# Nomor hari mengikuti data latihan; jam dokumentasi adalah pengandaian Bab 7.
HARI_PANGGILAN_PERTAMA = 1
HARI_PANGGILAN_TERAKHIR = 8
HARI_DIKETAHUI = 11
HARI_DOKUMENTASI = 12
JAM_DOKUMENTASI = 14

# Angka kontrak dan keterlambatan vendor mengikuti pengandaian Bab 3.
JAM_LAPOR_KONTRAK = 12
JAM_LAPOR_VENDOR = 30

NAMA_HARI = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")


def waktu_hari_ke(nomor_hari, jam=HARI_KE_1.hour):
  """Mengubah nomor hari kronologi menjadi waktu, agar tabel memakai satu acuan."""
  hari = HARI_KE_1 + timedelta(days=nomor_hari - 1)
  return hari.replace(hour=jam)


def nomor_hari_dari(waktu):
  """Mengembalikan nomor hari kronologi, agar keluaran sama dengan tabel pada bab."""
  return (waktu.date() - HARI_KE_1.date()).days + 1


def tulis_waktu(waktu):
  """Menulis waktu seperti pada bab, agar pembaca dapat mencocokkannya langsung."""
  nama = NAMA_HARI[waktu.weekday()]
  return f"Hari {nomor_hari_dari(waktu)}, {nama} {waktu:%H.%M}"


def jam_selisih(awal, akhir):
  """Menghitung selisih jam; nilai negatif berarti batas lewat sebelum diketahui."""
  return (akhir - awal).total_seconds() / 3600


def cetak_titik_mulai(nama_titik, titik_mulai, saat_diketahui):
  """Mencetak satu baris, supaya tiap pilihan dibaca terhadap saat diketahui."""
  batas = titik_mulai + timedelta(hours=JAM_RENTANG)
  sisa = jam_selisih(saat_diketahui, batas)
  print(f"{nama_titik}: mulai {tulis_waktu(titik_mulai)}; "
        f"batas {tulis_waktu(batas)}; sisa terhadap saat diketahui {sisa:.0f} jam")


def main():
  """Mencetak titik mulai pada tabel bab dan varian Bab 3."""
  saat_diketahui = waktu_hari_ke(HARI_DIKETAHUI)
  cetak_titik_mulai(
    "Panggilan pertama", waktu_hari_ke(HARI_PANGGILAN_PERTAMA), saat_diketahui)
  cetak_titik_mulai(
    "Panggilan terakhir", waktu_hari_ke(HARI_PANGGILAN_TERAKHIR), saat_diketahui)
  cetak_titik_mulai("Saat diketahui", saat_diketahui, saat_diketahui)
  cetak_titik_mulai(
    "Kesimpulan dokumentasi",
    waktu_hari_ke(HARI_DOKUMENTASI, JAM_DOKUMENTASI),
    saat_diketahui)

  # Varian Bab 3: vendor tahu lebih dulu, lalu melapor setelah 30 jam.
  terlewat_kontrak = JAM_LAPOR_VENDOR - JAM_LAPOR_KONTRAK
  sisa_rentang = JAM_RENTANG - JAM_LAPOR_VENDOR
  print(f"Varian Bab 3: kontrak terlewat {terlewat_kontrak} jam; "
        f"sisa rentang {sisa_rentang} jam")


if __name__ == "__main__":
  main()
