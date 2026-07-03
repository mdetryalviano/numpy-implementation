import numpy as np

# Set seed agar angka acak yang dihasilkan selalu sama setiap kali di-run (opsional)
np.random.seed(42)

print("=== 1. GENERATE DATA (Random Numbers) ===")
# Anggap ada 5 produk: [Kopi, Teh, Roti, Kue, Air Mineral]
# Kita generate jumlah produk terjual per hari selama 365 hari (Range: 0 - 50 item)
penjualan = np.random.randint(0, 50, size=(365, 5))
print(f"Bentuk matriks penjualan (Hari x Produk): {penjualan.shape}\n")


print("=== 2. MENGHITUNG PENDAPATAN KOTOR (Broadcasting) ===")
# Array 1D berisi harga masing-masing dari 5 produk tersebut
harga_produk = np.array([25000, 15000, 12000, 20000, 5000]) # Ukuran: (5,)

# BROADCASTING: Matriks (365, 5) dikalikan Array (5,)
# NumPy otomatis mengalikan setiap kolom dengan harga yang sesuai
pendapatan_per_hari_per_produk = penjualan * harga_produk

# FUNGSI AGREGAT: Jumlahkan pendapatan 5 produk ke samping (axis=1) untuk tahu total harian
total_pendapatan_harian = pendapatan_per_hari_per_produk.sum(axis=1)
print(f"Total pendapatan hari ke-1: Rp {total_pendapatan_harian[0]:,}")
print(f"Total pendapatan hari ke-2: Rp {total_pendapatan_harian[1]:,}\n")


print("=== 3. ANALISIS PERFORMA BISNIS (Fungsi Agregat) ===")
# Total pendapatan setahun penuh
total_setahun = total_pendapatan_harian.sum()
# Rata-rata pendapatan per hari
rata_rata_harian = total_pendapatan_harian.mean()
# Pendapatan tertinggi dalam satu hari
pendapatan_maksimal = total_pendapatan_harian.max()

# Produk mana yang paling laris (total kuantitas terjual setahun paling banyak)?
# Kita jumlahkan ke bawah (axis=0) untuk tahu total item per produk
total_terjual_per_produk = penjualan.sum(axis=0)
nama_produk = ["Kopi", "Teh", "Roti", "Kue", "Air Mineral"]
produk_terlaris_idx = total_terjual_per_produk.argmax() # Mencari indeks dengan nilai tertinggi

print(f"Total Pendapatan Setahun: Rp {total_setahun:,}")
print(f"Rata-rata Pendapatan Harian: Rp {rata_rata_harian:,.2f}")
print(f"Pendapatan Tertinggi dalam Sehari: Rp {pendapatan_maksimal:,}")
print(f"Produk Paling Laris: {nama_produk[produk_terlaris_idx]} (Terjual {total_terjual_per_produk[produk_terlaris_idx]} item)\n")


print("=== 4. MENCARI HARI BURUK & HARI EMAS (Filtering) ===")
# Misal, target pendapatan harian toko adalah Rp 1.500.000
target = 1500000

# FILTERING: Cari hari-hari di mana pendapatan di bawah target (Hari Buruk)
hari_buruk_mask = total_pendapatan_harian < target
jumlah_hari_buruk = np.sum(hari_buruk_mask) # Menghitung berapa banyak nilai True

# Ambil data pendapatan di hari-hari buruk saja
pendapatan_hari_buruk = total_pendapatan_harian[hari_buruk_mask]

print(f"Jumlah hari di bawah target: {jumlah_hari_buruk} hari dari 365 hari")
print(f"Rata-rata pendapatan di hari buruk tersebut: Rp {pendapatan_hari_buruk.mean():,.2f}")