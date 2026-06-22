import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('profile.jpeg')
h, w, c = img.shape

img_pixelate = img.copy()

step = 25

for y in range(0, h, step):
    for x in range(0, w, step):
        block_color = img[y, x, :]
        
        img_pixelate[y:y+step, x:x+step] = block_color
        
plt.imshow(img_pixelate)
plt.axis('off')
plt.show()