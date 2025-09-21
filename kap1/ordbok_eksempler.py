"""
Noen eksempler på bruk av ordbøker.
"""


# Informasjon om et objekt f.eks. en elev
elev = {
    "id": "S12345",
    "navn": "Sarah Johnson",
    "studieretning": "Realfag",
    "aar": 3,
    "fag": ["IT2", "Fysikk 1", "R1"]
}

# Lagersystem
lager = {
    "laptop": {"pris": 8999.99, "antall": 15, "kategori": "elektronikk"},
    "lærebok": {"pris": 1200.00, "antall": 8, "kategori": "bøker"},
    "mus": {"pris": 259.99, "antall": 50, "kategori": "tilbehør"}
}

# Kontaktliste(!)
kontakter = {
    "mamma": {"telefon": "92345678", "epost": "mamma@epost.com"},
    "bestevenn": {"telefon": "45987654", "epost": "venn@epost.com"},
    "taxi": {"telefon": "0480", "epost": "taxi@oslotaxi.no"}
}

# Restaurantmeny og bestillingssystem
menu = {
    "burger": 8.99,
    "fries": 3.50,
    "soda": 2.25,
    "salad": 6.75
}

order = {"burger": 2, "fries": 1, "soda": 3}

total = 0
for key, value in order.items():
    cost = menu[key] * value
    total += cost
    print(f"{key} x{value}: {cost:.2f} kr")
print("_________________")
print(f"Sum: {total:.2f} kr")


# Konfigurasjon for et spill
spill_innstillinger = {
    "vanskelighetsgrad": "medium",
    "lyd_aktivert": True,
    "oppløsning": "1920x1080",
    "spillernavn": "garbageguy",
    "høyeste_poengsum": 15420
}

# Statistikk
tekst = "hei verden hei python verden"
ord_antall = {}

# .split() deler teksten inn i en liste med alle ordene delt med mellomrom.
ord_liste = tekst.split()   # deler opp tekstvariabel på mellomrommene og lagrer som liste.
for ord in ord_liste:
    if ord in ord_antall:
        ord_antall[ord] += 1
    else:
        ord_antall[ord] = 1

print(ord_antall)  # {'hei': 2, 'verden': 2, 'python': 1}