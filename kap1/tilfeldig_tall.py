"""
1) Hardkodet tilfeldig heltall.
2) Bruke biblioteket randint
"""
import math
from random import random, randint

minst = 1
maks = 6

# 1) Hardkodet løsning
tilfeldig = math.floor( random() * (maks-minst + 1) ) + minst
print(tilfeldig)

# 2) randint
print(randint(minst,maks))