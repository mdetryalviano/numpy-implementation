import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('profile.jpeg')
h, w, c = img.shape

canvas = np.zeros((h * 2, w * 2, c), dtype=np.uint8)

img_bright = np.clip(img.astype(int) + 60, 0, 255).astype(np.uint8)
img_dark = np.clip(img.astype(int) - 60, 0, 255).astype(np.uint8)
img_no_red = img.copy()
img_no_red[:, :, 0] = 0

canvas[0:h, 0:w] = img
canvas[0:h, w:w*2] = img_bright
canvas[h:h*2, 0:w] = img_dark
canvas[h:h*2, w:w*2] = img_no_red

plt.imshow(canvas)
plt.axis('off')
plt.show()