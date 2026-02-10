"""
Lage histogram av alle lysstyrkene i bildet.
1) Ta intensitet som summen av fargene i hver pixel.
2) Legg intensitetene inn i ordbok.
3) Legg på frekvensen for hver intensitet.

Max antall bins blir 256*3 = 768 pga. hver pixel kan være fra 0-255.
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load the image with pixel values [0-1] 
#img = mpimg.imread('blomst.png')
#img = mpimg.imread('minions.jpg')
img = mpimg.imread('enchanted_sky_fire.jpg')

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

statistikk = {}
# Fyller alle klassene med pixelverdiene fra 0 til 255*3 for å håndtere alle mulige intensiteter.
for i in range(255*3 + 1):
    statistikk[i] = 0
    if i == 765:
        print(i)

w = img.shape[1]
h = img.shape[0]
for y in range(h):
    for x in range(w):
        # Tar summen av RGB-verdiene
        intensity = int(sum(img[y][x][0:3]))
        # Oppdaterer antallet for denne intensiteten.
        statistikk[intensity] += 1


# Lager lister for x-verdier og y-verdier
xverdier = []
yverdier = []
for key, value in statistikk.items():
    xverdier.append(key)
    yverdier.append(value)

# Viser "histogram"
plt.bar(xverdier,yverdier)
plt.axis('on')
plt.xlabel("Intensity")
plt.ylabel("Counts")
plt.show()