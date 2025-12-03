class Maybe:
    def __init__(self, value):
        self._value = value

    def bind(self, func):  # Monadisk operasjon
        if self._value is None:
            return Maybe(None)
        return Maybe(func(self._value))

    def get_or_else(self, default):
        return self._value if self._value else default

# Uten monad - risiko for feil
def finn_bruker(id):
    return None if id < 0 else {"navn": "Ola", "alder": 30}

def hent_alder(bruker):
    return bruker["alder"]  # Krasjer hvis bruker er None!

# Med monad - trygt
bruker = Maybe(finn_bruker(-1))
alder = bruker.bind(hent_alder).get_or_else(0)
print(f"Alder: {alder}")  # 0, ingen feil

# Kjeding av operasjoner
resultat = (Maybe(finn_bruker(1))
    .bind(hent_alder)
    .bind(lambda a: a * 2)
    .get_or_else(0))