"""
Lag lister som inneholder verdiene nedenfor 
(én liste for hver deloppgave). Kan du lage listene på forskjellige måter og kun ved hjelp av programmering?
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
"""

partall = [x for x in range(0,21,2)]

print(partall)

print([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] == partall)

null_liste = []

for i in range(10):
    null_liste.append(0)

print(null_liste)

print([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]==null_liste)
