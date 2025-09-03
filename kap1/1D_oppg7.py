"""
Lag en tom liste. Fyll opp lista med heltallene fra 1 til 20. 
Deretter fjerner du alle partallene fra lista, slik at du sitter 
igjen med oddetallene.
"""
liste = [x for x in range(21)]

# Må gå baklengs pga vi forkorter listen og får indeksfeil når i er større enn lengden.
for i in range(len(liste)-1,-1,-1):
    if liste[i] % 2 == 0:
        liste.pop(i)

print(liste)

# Kan la Python håndtere at listen forkortes med "for..in" loop.
# Dette står det om i læreboka "1C for-løkker"
liste2 = [x for x in range(21)]
for verdi in liste2:
    if verdi % 2 == 0:
        liste2.remove(verdi)

print(liste2)