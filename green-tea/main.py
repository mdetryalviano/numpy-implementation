import matplotlib.pyplot as plt
import numpy as np

# 1. Load gambar objek dengan green screen
img_main = plt.imread('profile.png')

# Pastikan skala gambar berada di rentang 0-255 (Integer)
if img_main.max() <= 1.0:
    img_main = (img_main * 255).astype(np.uint8)

# SOLUSI DI SINI:
# Jika gambar memiliki 4 channel (RGBA), kita buang channel terakhirnya pakai slicing
# Kita cuma ambil baris (:), kolom (:), dan channel index 0 sampai 2 (0:3)
if img_main.shape[2] == 4:
    img_main = img_main[:, :, 0:3]

# 2. Definisikan warna baru dari kode heksadesimal #a5aa44 (RGB)
warna_baru = np.array([165, 170, 68], dtype=np.uint8)

# 3. Deteksi area hijau (Filtering / Masking)
is_green = (img_main[:, :, 1] > 100) & (img_main[:, :, 0] < 100)

# 4. Buat kanvas baru untuk hasil akhir
img_result = img_main.copy()

# Aksi A: Ubah background (yang berwarna hijau) menjadi warna #a5aa44
img_result[is_green] = warna_baru

# Aksi B: Ubah objek utamanya (yang BUKAN hijau) menjadi HITAM pekat
img_result[~is_green] = [0, 0, 0]

# 5. Tampilkan Hasil Siluet
plt.figure(figsize=(8, 8))
plt.imshow(img_result)
plt.axis('off')
plt.show()