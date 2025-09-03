tegneseriefigurer = []

tegneseriefigurer.append("Donald Duck")
tegneseriefigurer.append("Obelix")
tegneseriefigurer.append("Pondus")
tegneseriefigurer.append("Pondus")

print(tegneseriefigurer)

# Sjeker om "Pondus" er i listen.
print("Pondus" in tegneseriefigurer)

# Finner første tilfelle av "Pondus".
index = tegneseriefigurer.index("Pondus")
print(index)
# Leter etter neste "Pondus".
ny_index = tegneseriefigurer.index("Pondus",index+1)
print(ny_index)
# Fjerner nøyaktig fra siste tilfelle av "Pondus"
tegneseriefigurer.pop(ny_index)
# Nå er "Pondus-kopien" fjernet.
print(tegneseriefigurer)

# Fjerner første tilfelle av "Pondus"
tegneseriefigurer.remove("Pondus")
# Feilmelding når den ikke finnes lenger.
# Vi må da sjekke om verdien finnes først
if "Pondus" in tegneseriefigurer:
    tegneseriefigurer.remove("Pondus")
else:
    print("Pondus finnes ikke lenger")
    

# Nå er Pondus borte
print(tegneseriefigurer)