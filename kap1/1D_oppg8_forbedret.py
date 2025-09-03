"""
Lag et program som bruker en løkke for å fjerne alle forekomster av tallet 3 fra denne lista:
[1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
"""

liste = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]

for tall in liste:
    if tall == 3:
        liste.remove(tall)
print("Har ikke klart å fjerne alle 3-tallene så noen er igjen.")
print(liste)

print("Forsøker med en bedre løsning med for i in range() loop.")
# Bruker indekser, sparer på dem, sorterer i synkende rekkefølge og bruker pop().
indekser = []
for i in range(len(liste)):
    if liste[i] == 3:
        indekser.append(i)


# [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]
# Indeksene er forlengs, reverserer dem:
indekser.reverse()
for j in range(len(indekser)):
    liste.pop(indekser[j])

print(liste)
