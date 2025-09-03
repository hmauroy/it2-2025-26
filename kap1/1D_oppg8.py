"""
Lag et program som bruker en løkke for å fjerne alle forekomster av tallet 3 fra denne lista:
[1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
"""

liste = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]

for tall in liste:
    if tall == 3:
        liste.remove(tall)

print(liste)

# Bruker indekser, sparer på dem og bruker pop() baklengs.
indekser = []
for i in range(len(liste)):
    if liste[i] == 3:
        indekser.append(i)


# [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
# Må gå baklengs gjennom indeksene [2,5,9,10,11...]
for j in range(len(indekser)-1, -1, -1):
    liste.pop(indekser[j])

print(liste)
