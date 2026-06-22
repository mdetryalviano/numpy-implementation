import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('profile.jpeg')
print('Ukuran matriks gambar: ', img.shape)

cropped_img = img[100:400, 200:500, :]

img_bright1 = np.clip(img.astype(int) + 50, 0, 255).astype(np.uint8)
img_bright2 = np.clip(img.astype(int) - 20, 0, 255).astype(np.uint8)

blue_filter = img.copy()
blue_filter[:, :, 0:2] = 0

plt.imshow(blue_filter)
plt.axis('off')
plt.show()
