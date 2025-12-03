"""
Hensikt: 
Finne ut av hvordan list-klassen skriver ut lister.
"""

liste = [1,2,3,4,5,6,7,8,9]

for tall in liste:
    print(f"Tallet er: {tall}")

print(liste)
# Oppretter en tekst-utskrift fra metoden til liste-objektet.
tekst = liste.__format__("")
# Printer typen til variabelen tekst: <class 'str'>
print(type(tekst))
# Printer typen til tallet 42: <class 'int'>
print(type(42))
# Printer typen til tallet 2.718281828: <class 'float'>
print(type(2.718281828))
# Printer typen til listen ovenfor: <class 'list'>
print(type(liste))
# Printer typen til ordboken: <class 'dict'>
print(type({"klasse": "IT2"}))
# Printer typen til True: <class 'bool'>
print(type(True))
# Printer typen til False: <class 'bool'>
print(type(False))

# Printer ut dokumentasjonen for klassen "list"
#print(help(str))
"""
Etter lesing av dokumentasjonen på nett: https://docs.python.org/3/library/stdtypes.html#str
Ser det ut til at kildekoden for __str__() for list-klassen ikke er så lett å finne.
Etter prat med Claude 4.5 Sonnet ser det ut til at python kaller på __repr__() metoden for listen som deretter
går gjennom hvert element og kaller på deres egen repr() metode.
"""
# Pythons implementering av utskrift av en liste
tekst = "["
for i in range(len(liste)-1):
    element = liste[i]
    tekst += element.__repr__() + ","
# Siste elementet blir så lagt til uten komma bak, men en klammeparentes.
element = liste[-1]
tekst += element.__repr__() + "]"

print(tekst)