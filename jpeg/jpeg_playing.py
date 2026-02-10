import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load the image with pixel values [0-1] 
img = mpimg.imread('blomst.png')

print(f"Shape: {img.shape}")
print(f"Data type: {img.dtype}")

# Sjekker først om bildet har en tredje indeks for dimensjonen til hver pixel, svart-hvitt har ikke en tredje.
if img.shape[2]:
    if img.shape[2] == 4:
        print("alfakanal registrert. Tar vekk alfakanalen.")
    # Tar ut kun RGB-kanalene fra png-bildet hvis det har en gjennomsiktigkanal på 4. indeksen.
        img = img[:,:, 0:3]
    elif img.shape[2] == 3:
        print("RGB-bilde registrert.")

# Display the image
plt.imshow(img)
plt.axis('off')
plt.show()

# Normaliserer alle verdiene 0-1 så de oppfører seg som RGB-verdier.
img = img * 255

# Klipper alle verdier så de er i intervallet [0,255]
np.clip(img, 0, 255)
# Gjør om til heltall
img.astype(np.uint8)


w = img.shape[1]
h = img.shape[0]
for y in range(h):
    for x in range(w):
        img[y][x][0] = 200

# Endrer en hel slice av 2D-arrayet. Setter G-kanalen til 255 og blå til 0.
img[100:130,30:60,1] = 255
img[100:130,30:60,2] = 0

# Plukker ut en bit av bildet. Lager først et tomt 2D-array som så peker på et utsnitt.
crop = np.zeros((h, w), dtype=np.float32)
crop = img[60:200,0:200]

print(crop)

# Før vi kan plotte bildet igjen må pixel-verdiene være i intervallet 0-1 igjen.
crop = crop / 255
# klipper data for å passe i intervall 0-1
np.clip(crop, 0, 1)


# Display the image
plt.imshow(crop)
plt.axis('off')
plt.show()