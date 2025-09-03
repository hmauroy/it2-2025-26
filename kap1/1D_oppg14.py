"""
14) 
Lag en liste med 1000 tilfeldige heltall mellom 1 og 100. Sorter lista, 
og bruk den sorterte lista for å finne det minste og det største tallet. 
Kontroller svaret ved å bruke metodene min() og max().
15)
Ta utgangspunkt i lista du laget i forrige oppgave. Legg til verdiene 
17, 42 og 81 på riktige posisjoner slik at lista forblir sortert.
"""
from random import randint

#liste = [randint(1,100) for x in range(1000)]
liste = [x for x in range(15,90)]

liste.sort()

minst = liste[0]
størst = liste[-1]

print(f"minst: {minst}, størst: {størst}")
print(f"min(): {min(liste)}, max: {max(liste)}")

# 15) Finner ut av hvor tallene 17, 42, 81 skal havne.
# Siden listen er sortert vil de minste verdiene settes inn i starten av listen og forskyve indekser.
# Velger å gå baklengs gjennom listen. Passer på å ikke bruke første og siste indeks pga. måten
# vi sjekker plassering av tallet som skal settes inn.
nye_tall = [17, 42, 81]
# Starter med det største tallet først og når det er satt inn endrer vi "indeks" til én mindre.
nye_tall.reverse()
for nytt_tall in nye_tall:
    for i in range(len(liste)-2, 0, -1):
        # Sjekker om tallet ligger mellom i-1 og i+1.
        if liste[i-1] <= nytt_tall and nytt_tall <= liste[i+1]:
            liste.insert(i,nytt_tall)
            break


print(liste)
