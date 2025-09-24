"""
Enkel funksjon.
"""

def hello(navn):
    print(f"Hello {navn}!")

def square(n):
    # Kan kun returnere én verdi. Kommer tilbake som en tuple.
    return n**2

import math
def rot(n):
    """Returnerer kvadratroten til n."""
    return math.sqrt(n)


def frem_og_tilbake(n):
    """Tar kvadratroten av n og kvadrerer etterpå. Returnerer verdien til slutt."""
    tall = rot(n)
    return square(tall)

hello("IT2")
kvadrat = square(5)
print(kvadrat)
sluttall = frem_og_tilbake(5)
print(sluttall)
