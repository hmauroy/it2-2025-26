import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**2

xverdier = np.linspace(0, 10, 11)
print(xverdier)
yverdier = f(xverdier)

fig, ax = plt.subplots()

plt.plot(xverdier, yverdier)
plt.show()