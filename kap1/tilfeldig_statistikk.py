"""
Sjekker om en tilfeldig desimaltall-generator virker.
ytterverdiene skal kunne velges |m desimaltall.
"""

from random import random

n = 100000
statistikk = {}

minst = -7
maks = 13
for i in range(n):
    tilfeldig = random()*(maks - minst) + minst
    if tilfeldig in statistikk:
        statistikk[tilfeldig] += 1
    else:
        statistikk[tilfeldig] = 1

sorted_dict = dict(sorted(statistikk.items()))
for key, val in sorted_dict.items():
    if key > -6.9:
        break
    print(key,val)