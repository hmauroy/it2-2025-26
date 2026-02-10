"""
Kopiere liste

Sette sammen lister

Sortere lister

Tilfeldige tall

Hente ut innhold fra liste

"""
liste = [5,4,3,2,1]
kopi = liste.copy()

for verdi in kopi:
    liste.append(verdi)
print(liste)

liste.sort()
liste.reverse()

import random
tilfeldig = [random.random() for x in range(100)]
tilfeldig_heltall = [random.randint(0,100) for x in range(100)]
tilfeldige_uniform = [random.uniform(0,100) for x in range(100)]
print(tilfeldig)
print(tilfeldig_heltall)
print(tilfeldige_uniform)

heltall = [x for x in range(10)]
liste_midt = heltall[5:10]
liste_start = heltall[:5] # frem til og med index 4
liste_slutt = heltall[5:] # fra og med index 5

print(liste_start)
print(liste_midt)
print(liste_slutt)