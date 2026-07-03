import numpy as np

# Set seed agar nilainya konsisten saat dicoba
np.random.seed(10)

print("=== 1. GENERATE NILAI UJIAN (Random Numbers) ===")
# Kita generate nilai ujian untuk 100 siswa.
# Anggap saja rata-rata asli kelasnya 65 dengan standar deviasi 12 (distribusi normal)
nilai_mentah = np.random.normal(loc=65, scale=12, size=100)

# Karena distribusi normal bisa menghasilkan angka desimal bebas, kita bulatkan dan batasi max 100
nilai_mentah = np.clip(np.round(nilai_mentah), 0, 100)
print(f"5 Nilai Mentah Siswa Pertama: {nilai_mentah[:5]}\n")


print("=== 2. HITUNG STATISTIK KELAS (Fungsi Agregat) ===")
rata_rata_kelas = nilai_mentah.mean()
standar_deviasi = nilai_mentah.std()

print(f"Rata-rata Kelas Asli  : {rata_rata_kelas:.2f}")
print(f"Standar Deviasi Kelas : {standar_deviasi:.2f}\n")


print("=== 3. NORMALISASI Z-SCORE (Broadcasting) ===")
# BROADCASTING: array (100,) dikurangi skalar (nilai tunggal), lalu dibagi skalar.
# NumPy otomatis mengurangkan dan membagi ke 100 siswa sekaligus tanpa loop!
z_scores = (nilai_mentah - rata_rata_kelas) / standar_deviasi
print(f"5 Z-Score Siswa Pertama: {z_scores[:5]}\n")


print("=== 4. PENGELOMPOKAN GRADE (Filtering) ===")
# Kita filter siswa berdasarkan performa relatif mereka di kelas
# Grade A: Z-Score > 1.2 (Jauh di atas rata-rata kelas)
# Grade E (Gagal): Z-Score < -1.2 (Jauh di bawah rata-rata kelas)

siswa_A_mask = z_scores > 1.2
siswa_E_mask = z_scores < -1.2

# Ambil nilai asli dari siswa yang mendapat grade tersebut
nilai_siswa_A = nilai_mentah[siswa_A_mask]
nilai_siswa_E = nilai_mentah[siswa_E_mask]

print(f"Jumlah siswa yang dapat Grade A : {np.sum(siswa_A_mask)} siswa")
print(f"Nilai terendah untuk dapat A   : {nilai_siswa_A.min() if len(nilai_siswa_A) > 0 else 'N/A'}")
print(f"-> Daftar nilai siswa Grade A  : {nilai_siswa_A}\n")

print(f"Jumlah siswa yang dapat Grade E : {np.sum(siswa_E_mask)} siswa")
print(f"Nilai tertinggi di kelompok E   : {nilai_siswa_E.max() if len(nilai_siswa_E) > 0 else 'N/A'}")
print(f"-> Daftar nilai siswa Grade E  : {nilai_siswa_E}")