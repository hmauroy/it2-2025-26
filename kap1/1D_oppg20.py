"""
Skriv en kode som bytter plass på verdiene i lista tall = [3, 4, 1, 2, 5] 
slik at den blir sortert. Du skal altså sortere lista manuelt.

Implementerer boblesortering
"""

tall = [3, 4, 1, 2, 5] 

# Søker gjennom n^2 ganger.
for i in range(len(tall)):
    for j in range(len(tall)):
        if tall[i] < tall[j]:
            # Bytter om
            buf = tall[i]
            tall[i] = tall[j]
            tall[j] = buf



# Nytt forsøk
tall = [21, 99, 3, 4, 1, 2, 5, 9, 7, 6]
print(tall)
for i in range(1,len(tall)):
    for j in range(len(tall)-1):
        if tall[j] > tall[j+1]:
            # Bytter om
            buf = tall[j+1]
            tall[j+1] = tall[j]
            tall[j] = buf
            print(tall)

print(tall)