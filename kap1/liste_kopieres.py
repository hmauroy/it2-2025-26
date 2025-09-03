"""
Hvordan kopiere en liste.
Forskjellen på grunn kopi og dyp kopi
"""

liste = [[5,5,5],3,2,1]

liste_kopiA = list(liste)
liste_kopiB = liste.copy()

# Dyp kopi
import copy
liste_kopiDeep = copy.deepcopy(liste)


# Legge til en verdi påvirker ikke
liste.append(10)
print(liste_kopiA)
print(liste_kopiB)
print(liste_kopiDeep)

# Legge til en verdi i listen lagret i ytre liste påvirker.
liste[0].append(492)

print(liste_kopiA)
print(liste_kopiB)
print(liste_kopiDeep)


