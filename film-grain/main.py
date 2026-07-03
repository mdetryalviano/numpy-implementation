import matplotlib.pyplot as plt
import numpy as np

# 1. Load gambar asli (Pastikan gambarmu berwarna/3D array)
img = plt.imread('profile.jpeg')
h, w, c = img.shape
print(f"Ukuran gambar asli: {h} x {w} dengan {c} channel warna.")

# Trik Tambahan: Jika gambar dibaca dalam skala 0.0 - 1.0 (float), 
# kita kalikan 255 agar skalanya menjadi 0 - 255 (integer)
if img.max() <= 1.0:
    img = (img * 255).astype(np.uint8)

print("=== 1. GENERATE NOISE GRAIN (Random Numbers) ===")
# Kita buat matriks acak berdistribusi normal (Bell Curve) dengan ukuran yang SAMA dengan gambar (h, w, c)
# Mean (loc) = 0, artinya rata-rata tidak mengubah warna asli
# Standar Deviasi (scale) = 25, menentukan seberapa kasar/kelihatan butiran grain-nya
noise = np.random.normal(loc=0, scale=25, size=(h, w, c))


print("=== 2. GABUNGKAN NOISE KE GAMBAR (Broadcasting Arithmetic) ===")
# BROADCASTING ARITHMETIC: Kita jumlahkan matriks gambar asli dengan matriks noise
# Karena noise berisi angka minus dan plus (misal: -15 sampai +20), 
# sebagian piksel akan menggelap dan sebagian akan menerang secara acak.
img_dengan_noise = img.astype(float) + noise


print("=== 3. AMANKAN RENTANG WARNA (Filtering / Clipping) ===")
# FILTERING: Karena hasil penjumlahan bisa melenceng di bawah 0 atau di atas 255,
# kita potong (clip) nilainya agar tetap berada di rentang warna valid [0, 255].
img_grainy = np.clip(img_dengan_noise, 0, 255).astype(np.uint8)


# === 4. TAMPILKAN PERBANDINGAN HASILNYA ===
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Gambar Asli
axes[0].imshow(img)
axes[0].set_title("Gambar Asli (Clean)")
axes[0].axis('off')

# Gambar dengan Efek Film Grain
axes[1].imshow(img_grainy)
axes[1].set_title("Efek Film Grain (Retro)")
axes[1].axis('off')

plt.tight_layout()
plt.show()