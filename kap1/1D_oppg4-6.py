# 4)
kvadrattall = [x**2 for x in range(1,21)]
print(len(kvadrattall))
print(kvadrattall)

# 5)
kubikktall = [x**3 for x in range(1,16)]
print(len(kubikktall))
print(kubikktall)

# 6)
# min() finner minste verdi i en liste
print(f"Minste kubikktall: {min(kubikktall)}")

# max() finner størst verdi i en liste
print(f"Største kubikktall: {max(kubikktall)}")

# sum() finner summen av alle elementene i en liste
print(f"Sum kubikktall: {sum(kubikktall)}")