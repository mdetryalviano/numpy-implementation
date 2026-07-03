import matplotlib.pyplot as plt
import numpy as np

# Set seed agar hasil simulasi acak bisa diulang dengan hasil yang sama
np.random.seed(42)

print("=== 1. GENERATE PERGERAKAN HARGA (Random Numbers) ===")
# Kita simulasikan pergerakan harga sebuah koin kripto selama 1000 menit ke depan.
menit = 1000
harga_awal = 10000  # Harga awal Rp 10.000

# Generate persentase naik/turun harga secara acak (Random Numbers)
# Kebanyakan menit harganya berubah kecil, berdistribusi normal di sekitar 0% (Rata-rata=0, Standar Deviasi=0.005 atau 0.5%)
persentase_perubahan = np.random.normal(loc=0.0, scale=0.005, size=menit)
print(f"5 Perubahan pertama (persentase): {persentase_perubahan[:5]}\n")


print("=== 2. MEMBENTUK TREN HARGA (Fungsi Agregat Akumulatif) ===")
# FUNGSI AGREGAT AKUMULATIF: np.cumsum()
# Fungsi ini akan menjumlahkan array secara berantai: [a, a+b, a+b+c, ...]
# Kita gunakan ini untuk menghitung akumulasi faktor perubahan harga
faktor_multiplikasi = 1 + persentase_perubahan
tren_harga = harga_awal * np.cumprod(faktor_multiplikasi) # cumprod = cumulative product (perkalian kumulatif)

print(f"Harga menit ke-1: Rp {tren_harga[0]:,.2f}")
print(f"Harga menit ke-2: Rp {tren_harga[1]:,.2f}")
print(f"Harga menit ke-1000: Rp {tren_harga[-1]:,.2f}\n")


print("=== 3. MENGHITUNG STATISTIK (Fungsi Agregat Standar) ===")
harga_tertinggi = tren_harga.max()
harga_terendah = tren_harga.min()
Rata_rata_harga = tren_harga.mean()

print(f"Harga Tertinggi (All-Time High): Rp {harga_tertinggi:,.2f}")
print(f"Harga Terendah (All-Time Low) : Rp {harga_terendah:,.2f}")
print(f"Rata-rata Harga Koin          : Rp {Rata_rata_harga:,.2f}\n")


print("=== 4. MENDETEKSI CRASH / KEPANIKAN PASAR (Filtering) ===")
# Misal, pasar dianggap "Crash" jika harga jatuh di bawah Rp 9.500
batas_crash = 9500

# FILTERING: Cari menit ke berapa saja harga berada di bawah batas crash
crash_mask = tren_harga < batas_crash
jumlah_menit_crash = np.sum(crash_mask)

print(f"Pasar mengalami CRASH selama: {jumlah_menit_crash} menit dari 1000 menit.")

# Menggunakan filtering untuk mengambil semua harga saat terjadi crash
harga_saat_crash = tren_harga[crash_mask]
if jumlah_menit_crash > 0:
    print(f"Harga terparah saat crash: Rp {harga_saat_crash.min():,.2f}")
else:
    print("Pasar aman, tidak menyentuh harga crash.")

# --- BONUS: Visualisasi Grafik ---
plt.figure(figsize=(10, 5))
plt.plot(tren_harga, label='Harga Koin (Simulasi)', color='blue')
plt.axhline(y=harga_awal, color='gray', linestyle='--', label='Harga Awal')
plt.axhline(y=batas_crash, color='red', linestyle=':', label='Batas Crash')
plt.title('Simulasi Pergerakan Harga Koin Kripto (Random Walk)')
plt.xlabel('Waktu (Menit)')
plt.ylabel('Harga (Rp)')
plt.legend()
plt.grid(True)
plt.show()