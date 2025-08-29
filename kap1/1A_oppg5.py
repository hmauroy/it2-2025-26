tall = input("Skriv inn et tall ")
tall = float(tall)

if tall > 0:
    if tall > 100:
        print("større enn 100")
else:
    if tall < -100:
        print("mindre enn -100")