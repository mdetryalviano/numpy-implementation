import matplotlib.pyplot as plt

img = plt.imread('profile.jpeg')
img_negatif = 255 - img

plt.imshow(img_negatif)
plt.axis('off')
plt.show()