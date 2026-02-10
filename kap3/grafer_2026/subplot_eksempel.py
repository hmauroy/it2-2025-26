"""
Eksempel på større figur som bruker subplot og autoskalering.
"""

from matplotlib import pyplot as plt
import numpy as np

xverdier = np.linspace(0,10,11)
yverdier = []
for x in xverdier:
    yverdier.append(2*x)

print(xverdier)
print(yverdier)

plt.figure(figsize=(12, 8))  # Plot images
plt.suptitle(f"Grafer")
plt.subplot(221)
plt.title(f"y=2x"), plt.scatter(xverdier,yverdier)
plt.subplot(222)
plt.title(f"y=2x"), plt.plot(xverdier,yverdier)
yverdier = []
for x in xverdier:
    yverdier.append(10*x)
plt.subplot(223)
plt.title(f"y=10x"), plt.scatter(xverdier,yverdier)
plt.subplot(224), plt.xticks([]), plt.yticks([]) # Fjerner xticks og yticks i figuren
plt.title(f"y=10x"), plt.scatter(xverdier,yverdier)

plt.show()  