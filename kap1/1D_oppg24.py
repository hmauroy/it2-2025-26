"""
En 5 x 5-liste fylt med 0-er.
En 8 x 8-liste der annenhver verdi er "H" for hvit og "S" for svart (som i et sjakkbrett).
En 5 x 5-liste der alle verdier er 0, men verdiene i første og siste rad er 1.
En 5 x 5-liste der alle verdier er 0, men verdiene i første og siste kolonne er 1.
Skriv ut listene du har laget ovenfor, slik at de vises som tabeller.
"""
liste1 = []
for i in range(5):
    liste1.append([])   # legger tom liste inn i ytre liste.
    for j in range(5): # lager 5 nye plasser i den tomme listen.
        liste1[i].append(5) # legger inn verdien 5 på hver nye plass.
        print(liste1[i])

for rad in liste1:
    print(rad)

liste2 = []
for i in range(8):
    liste2.append([])   # legger tom liste inn i ytre liste.
    for j in range(8): # lager 5 nye plasser i den tomme listen.
        if i % 2 == 0:
            if j % 2 == 0:
                liste2[i].append("S") # legger inn verdien
            else:
                liste2[i].append("H") # legger inn verdien
        else:
            if j % 2 == 0:
                liste2[i].append("H") # legger inn verdien
            else:
                liste2[i].append("S") # legger inn verdien

for rad in liste2:
    print(rad)     
