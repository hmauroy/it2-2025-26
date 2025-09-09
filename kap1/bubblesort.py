"""
Bubble sort algoritmen optimalisert.
"""

liste = [99, 1, 5, 7, 4, 1, 2, 1, 5, 6, 7, 8]

liste = [3,4,5,20,33]

for i in range(len(liste)):
    print(f"***** i: {i} **********")
    swapped = False
    for j in range(len(liste)-1-i):
        print("j: ",j)
        if liste[j] > liste[j+1]:
            swapped = True
            # Bytt verdier
            buf = liste[j+1]
            liste[j+1] = liste[j]
            liste[j] = buf
            print(liste)
    if not swapped:
        print("Ingen swaps => Ferdig sortert.")
        break

