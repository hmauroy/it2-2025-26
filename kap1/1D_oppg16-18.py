"""
16) 
Lag et program med en løkke som samtidig finner største og minste verdi i en liste. 
Test programmet og kontroller det ved å bruke min() og max() i tillegg.
17)
Lag et program som finner den korteste og den lengste teksten i en liste, 
altså teksten med færrest tegn og teksten med flest tegn.
18)
Skriv et program som beregner summen og gjennomsnittet av tallene i lista 
tall = [2, 3, 4, 5, -5, 8, 4, -7, 2, 9, 7, -9, 5, 3, 8, 5, -3, 3, 3, 2, 0, 1, 9, 1]. 
Du skal ikke bruke innebygde funksjoner.
"""
from random import randint
# 16)
liste = [11, 99, 94, 82, 46, 18, 42, 66, 43, 55]
minst = liste[0]
storst = liste[0]

for tall in liste:
    if tall < minst:
        minst = tall
    if tall > storst:
        storst = tall
print(liste)
print(f"Størst: {storst}, minst: {minst}")
print(f"Størst: {max(liste)}, minst: {min(liste)}")

# 17)
tekster = ["Ja", "vi", "elsker", "dette", "landet"]
kortest = tekster[0]
lengst = tekster[0]
for ord in tekster:
    if len(ord) < len(kortest):
        kortest = ord
    if len(ord) > len(lengst):
        lengst = ord

print(f"Kortest: {kortest}, er {len(kortest)} tegn langt.")
print(f"Kortest: {lengst}, er {len(lengst)} tegn langt.")

# 18)
tall = [2, 3, 4, 5, -5, 8, 4, -7, 2, 9, 7, -9, 5, 3, 8, 5, -3, 3, 3, 2, 0, 1, 9, 1]
sum = 0
for x in tall:
    sum += x

snitt = sum / len(tall)
print(f"Sum er {sum}")
print(f"Gjennomsnitt er {snitt}")
