"""
Funksjonell programmering av "klassen Bil".
"""

from typing import Dict

# Rene funksjoner - ingen tilstandsendring
def opprett_bil(merke: str, modell: str) -> Dict:
    return {
        "merke": merke,
        "modell": modell,
        "hastighet": 0
    }

def aksellerer(bil: Dict, økning: int) -> Dict:
    # Returnerer ny bil, endrer ikke original
    return {**bil, "hastighet": bil["hastighet"] + økning}

def info(bil: Dict) -> str:
    return f"{bil['merke']} {bil['modell']}"

# Høyere-ordens funksjon
def kjør_operasjoner(bil: Dict, operasjoner: list) -> Dict:
    result = bil
    for op in operasjoner:
        result = op(result)
    return result

# Bruk
bil = opprett_bil("Tesla", "Model 3")
ny_bil = aksellerer(bil, 50)  # Uforanderlighet
print(info(ny_bil))
print(f"Hastighet: {ny_bil['hastighet']}")