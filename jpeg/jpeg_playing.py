import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load the image
img = mpimg.imread('image.png')

print(f"Shape: {img.shape}")
print(f"Data type: {img.dtype}")

# Display the image
plt.imshow(img)
plt.axis('off')
plt.show()


w = img.shape[1]
h = img.shape[0]
for y in range(h):
    for x in range(w):
        img[y][x][0] = 255

crop = np.zeros((h, w), dtype=np.float32)

# Endrer en hel slice av 2D-arrayet. Setter R-kanalen til 0.
img[70:100,30:60,0] = 0
img[100:130,30:60,1] = 0
img[0:50,0:60,3] = 0

print(crop)

# Display the image
plt.imshow(img)
plt.axis('off')
plt.show()