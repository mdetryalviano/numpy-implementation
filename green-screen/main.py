import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import resize

img_main = plt.imread('profile.png')
img_background = plt.imread('folklore.png')

h, w, c = img_main.shape

if img_background.ndim == 2:
    img_background = np.stack([img_background] * 3, axis=-1)

bg_c = img_background.shape[2]
if bg_c < c:
    alpha = np.ones((*img_background.shape[:2], c - bg_c), dtype=img_background.dtype)
    img_background = np.concatenate([img_background, alpha], axis=-1)
elif bg_c > c:
    img_background = img_background[:, :, :c]

img_bg_resized = resize(img_background, (h, w), anti_aliasing=True)
img_bg_resized = img_bg_resized.astype(img_main.dtype)

is_green = (img_main[:, :, 1] > 0.4) & (img_main[:, :, 0] < 0.4) & (img_main[:, :, 2] < 0.4)

img_result = img_main.copy()
img_result[is_green] = img_bg_resized[is_green]

plt.imshow(img_result)
plt.axis('off')
plt.show()