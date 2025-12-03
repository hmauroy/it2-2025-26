
"""
Klasse for en Person
"""


class Person:
    # Klassevariabel
    personnummer = 1
    def __init__(self,fornavn,etternavn):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.personnummer = Person.personnummer
        Person.personnummer += 1
    
    def __str__(self):
        return f"{self.fornavn} {self.etternavn}, personnummer: {self.personnummer}"

def finnPerson(personnummer,liste):
    """
    Returnerer objektet med riktig personnummer, eller None hvis ikke det eksisterer.
    Eks: finnPerson(8,klasse3C) vil returnere objektet med fornavn 56b og etternavn 392c
    """
    for p in liste:
        if p.personnummer == personnummer:
            return p
    return None

def finnPersonVedFornavn(fornavn,liste):
    """Returnerer en liste over objekter med foravn man søker etter."""
    funn = []
    for p in liste:
        if p.fornavn == fornavn:
            funn.append(p)
    return funn


klasse3C = []
tekst = "abcdefghijklmno"
for i in range(22):
    fornavn = f"{i*Person.personnummer}{tekst[i%3]}" # Genererer et unikt fornavn basert på i
    etternavn = f"{i**2*Person.personnummer}{tekst[5*i%3]}" # Unikt etternavn basert på i
    person = Person(fornavn,etternavn) # lager et Person-objekt.
    klasse3C.append(person) # Legger objektet inn i listen vår.
print(finnPerson(13,klasse3C))
mineFunn = finnPersonVedFornavn("56b",klasse3C)
for p in mineFunn:
    print(p)

