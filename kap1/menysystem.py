"""
Enkelt menysystem for terminalen.
"""
isRunning = True

while isRunning:
    print("1. Meny 1")
    print("2. Meny 2")
    print("3. Meny 3")
    print("4. Meny 4")
    print("0. Avslutt")
    valg = input("Velg meny: ")
    valg = int(valg)
    if valg == 1:
        print("Du valgte meny 1")
    elif valg == 2:
        print("Du valgte meny 2")
    elif valg == 3:
        print("Du valgte meny 3")
    elif valg == 4:
        print("Du valgte meny 4")
    elif valg == 0:
        print("Ha det bra!")
        isRunning = False
