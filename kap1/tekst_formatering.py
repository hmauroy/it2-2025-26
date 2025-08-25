"""Noe tekst"""

a = 7
b = 42
c = a + b

# print med linjeskift (default)
print(a)

# endrer a
a = a + 1

# print uten linjeskift
print("a er nå endret til ", end="")
# printer med linjeskift
print(a)

# print c
print("c: ", end="")
print(c)

# tekst og tall sammen
print("Vi glemte nesten b: " + str(b))

