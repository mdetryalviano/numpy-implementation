import matplotlib.pyplot as plt
import numpy as np

# 1. Load dua gambar berbeda
img_a = plt.imread('gambar_a.jpeg')
img_b = plt.imread('gambar_b.jpeg')

# Pastikan keduanya dalam format RGB 3-channel standar (buang alpha channel jika ada)
if img_a.shape[2] == 4: img_a = img_a[:, :, 0:3]
if img_b.shape[2] == 4: img_b = img_b[:, :, 0:3]

# Ambil ukuran gambar A sebagai patokan standar
h, w, c = img_a.shape

print("=== 1. MENYAMAKAN UKURAN DENGAN SLICING ===")
# Ingat aturan Emas hstack: Jumlah baris (tinggi) HARUS sama persis.
# Kita potong gambar B agar ukurannya sama dengan gambar A demi keselamatan stacking.
img_b_ready = img_b[0:h, 0:w, :]


print("\n=== 2. IMPLEMENTASI HSTACK (Cinematic Split Screen) ===")
# Kita gabungkan gambar A dan gambar B ke samping secara horizontal
# Hasilnya akan menjadi satu kanvas lebar berisi kedua gambar berdampingan
split_screen = np.hstack((img_a, img_b_ready))
print("Ukuran Matriks Split Screen:", split_screen.shape) # Lebarnya (width) akan berlipat ganda


print("\n=== 3. IMPLEMENTASI RESHAPE & FLATTEN (Eksperimen Dimensi) ===")
# Mari kita ambil satu baris piksel paling tengah dari gambar A
baris_tengah = img_a[h // 2, :, :] # Mengambil baris tengah, semua kolom, semua channel RGB
print("Ukuran baris tengah asli:", baris_tengah.shape) # Hasilnya (Width, 3)

# Kita ratakan (Flatten) data baris tersebut menjadi 1D lurus panjang
baris_flat = baris_tengah.flatten()
print("Ukuran setelah di-Flatten menjadi 1D:", baris_flat.shape)

# Sekarang kita Reshape balik array 1D tersebut menjadi bentuk matriks vertikal baru (Width * 3, 1)
# Ini sering dipakai untuk memanipulasi susunan warna sebelum dilempar ke algoritma Machine Learning
baris_reshaped = baris_flat.reshape(-1, 1)
print("Ukuran setelah di-Reshape ulang:", baris_reshaped.shape)


# === 4. TAMPILKAN HASIL SPLIT SCREEN ===
plt.figure(figsize=(12, 6))
plt.imshow(split_screen)
plt.title("Hasil Efek Cinematic Split-Screen (np.hstack)")
plt.axis('off')
plt.show()