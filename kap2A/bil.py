"""
Klassen Bil.
"""

class Bil:
    def __init__(self, merke, modell):
        self.merke = merke      # Innkapsling
        self.modell = modell
        self.hastighet = 0

    def aksellerer(self, økning):
        self.hastighet += økning  # Endrer tilstand
        return self.hastighet

    def info(self):
        return f"{self.merke} {self.modell}"

class Elbil(Bil):  # Arv
    def __init__(self, merke, modell, batterikap):
        super().__init__(merke, modell)
        self.batterikap = batterikap

    def lad(self):
        return f"Lader {self.batterikap}kWh batteri"

# Bruk
min_bil = Elbil("Tesla", "Model 3", 75)
print(min_bil.info())  # Polymorfisme
print(min_bil.aksellerer(50))
print(min_bil.lad())