"""
Newtons metode for å finne nullpunktene til ethvert polynom opptil grad 8

F.eks: Skal løse f(x) = -0.1x^5 + 5x^4 - 10x^3 - 5x^2 - 5x - 2 = 0

Finner tangenter og deres skjæring med x-aksen

f'(x) = -0.5x^4 + 20x^3 - 30x^2 - 10x - 5

Tangent har stigningstall a = f'(x)

Må finne likningen for tangenten for å finne skjæring med x-aksen.
"""

def f(koeffs, x):
    """Beregner funksjonsverdi for f(x)"""
    # f(x) = koeffs[i]*x^i + ... + koeffs[n]*x^1 + k
    sum_verdi = 0
    grad = len(koeffs) - 1
    
    for i in range(grad):  # Stopper før siste plass i array pga det er konstant-leddet
        sum_verdi += koeffs[i] * (x ** (grad - i))
    
    sum_verdi += koeffs[-1]  # Legger til konstantleddet
    return sum_verdi


def df(koeffs, x):
    """Beregner funksjonsverdi for den deriverte for å finne stigningstallet"""
    # f'(x) = (grad-i) * koeffs[i] * x^(grad-i-1)
    sum_verdi = 0
    grad = len(koeffs) - 1
    
    for i in range(grad):  # Stopper før siste plass i array pga det deriveres bort
        sum_verdi += (grad - i) * koeffs[i] * (x ** (grad - i - 1))
    
    return sum_verdi


def finn_x(koeffs, x_test):
    """Finner nullpunkt for funksjonen. Nullpunktet for en tangent er -b/a"""
    return -(f(koeffs, x_test) - df(koeffs, x_test) * x_test) / df(koeffs, x_test)


def finn_nullpunkt(koeffs, nullpunkt):
    """Finner et nullpunkt ved hjelp av Newtons metode"""
    forrige_svar = 0
    delta_x = 1
    teller = 0
    
    # Kjører en loop inntil vi har konvergens: forrige_svar - nullpunkt = delta_x = 0.0000001
    for i in range(100):
        teller += 1
        nullpunkt = finn_x(koeffs, nullpunkt)
        delta_x = (forrige_svar - nullpunkt) ** 2  # Finner kvadratavviket
        print(f"Iterasjon {teller}: x = {nullpunkt}")
        forrige_svar = nullpunkt
        
        if delta_x < 0.0000001:  # Vi har konvergens!
            break
    
    print(f"Antall iterasjoner: {teller}")
    print(f"Nullpunkt: {nullpunkt}")
    return nullpunkt


def finn_neste_nullpunkt(koeffs, nullpunkt, grad):
    """Finner neste startpunkt for søk etter nullpunkt"""
    # Først må vi sjekke om polynomet er av 2. grad
    if grad == 2:
        # Hvis f(x) = x^2 - 2, så er f'(x) = 2x som er en rett linje med b = 0
        # a = 2, x = -b / a = -0/2 = 0
        # (0,f(0)) er bunnpunktet
        print("Andregradsfunksjon gjør det enkelt å finne ekstremalpunkt.")
        return 0  # 0 for en symmetrisk funksjon som x^2 - 2
    elif grad < 2:
        print("For lav grad!")
        return 0
    else:
        # Finner neste nullpunkt ved å se når fortegnet til f(x) bytter. Søker litt grovt pga vi trenger
        # kun å gå rett forbi nullpunktet for å kunne bruke Newtons metode.
        dx = 0.1
        fortegn = f(koeffs, nullpunkt + dx)  # beregner fortegnet til funksjonen litt til høyre for nullpunktet
        print(f"Fortegn: {fortegn}")
        nullpunkt += 2 * dx  # flytter oss ett hakk lenger bort fra der vi beregner fortegnet
        
        for i in range(1000000):
            nullpunkt += dx
            produkt = f(koeffs, nullpunkt) * fortegn
            
            if produkt > 0:
                # Derivert har samme fortegn pga (-*-) > 0 og (+*+) > 0
                pass
            elif produkt < 0:
                # Derivert har byttet fortegn! Vi har gått forbi ekstremalpunktet!
                print(f"i={i}")
                print(f"Derivert byttet fortegn! x={nullpunkt}: Fortegn * f(x): {produkt}")
                break
            else:
                # Ekstremalpunkt er funnet (lite sannsynlig)
                pass
    
    return nullpunkt


def finn_alle_nullpunkter(koeffs, x_start, grad):
    """Finner alle nullpunkter for polynomet"""
    nullpunkter = []
    x_test = x_start
    
    # Looper gjennom hvert nullpunkt vi ønsker å finne. Starter på en svært negativ x-verdi
    for i in range(grad):
        # Finner neste nullpunkt
        print(f"\nStartverdi for søk: {x_test}")  # Dette er startverdi for x for søket etter nullpunkt
        x = finn_nullpunkt(koeffs, x_test)  # finner nullpunktet
        
        # Sjekker om vi allerede har funnet nullpunktet
        if i > 0:
            if round(x, 6) == round(nullpunkter[i-1], 6):  # Runder av til 6 desimaler for å sjekke likhet
                print("Alle nullpunkter funnet!")
                return nullpunkter
        
        nullpunkter.append(x)  # legger nullpunktet inn i array
        
        if i >= grad - 1:  # Hvis vi er på siste loopen skal vi avbryte pga neste ekstremalpunkt ikke finnes
            break
        
        # Finner neste x_start ved å finne neste ekstremalpunkt (til høyre).
        x_test = finn_neste_nullpunkt(koeffs, x, grad)  # Finner neste nullpunkt i nærheten av x
        print(f"Neste nullpunktstart: {x_test}")
    
    return nullpunkter


def les_koeffisienter():
    """Leser inn polynom-grad og koeffisienter fra bruker"""
    grad = int(input("\nHvor mange grader har polynomet? (1-8): "))
    
    if grad < 1 or grad > 8:
        print("Grad må være mellom 1 og 8!")
        return None, None
    
    koeffs = []
    print(f"\nSkriv inn koeffisientene for polynomet av grad {grad}:")
    print("(Start med høyeste grad)")
    
    for i in range(grad, -1, -1):
        if i == 0:
            koeff = float(input(f"Konstantledd: "))
        elif i == 1:
            koeff = float(input(f"Koeffisient for x: "))
        else:
            koeff = float(input(f"Koeffisient for x^{i}: "))
        koeffs.append(koeff)
    
    return koeffs, grad


def main():
    """Hovedfunksjon som starter programmet"""
    print("=" * 50)
    print("Henriks nullpunktsniffer")
    print("=" * 50)
    print("Finner alle nullpunkter ved hjelp av Newtons metode")
    
    koeffs, grad = les_koeffisienter()
    
    if koeffs is None:
        return
    
    print(f"\nKoeffisienter: {koeffs}")
    print(f"Grad: {grad}")
    
    x_start = -10  # Startverdi for søk etter første nullpunkt
    nullpunkter = finn_alle_nullpunkter(koeffs, x_start, grad)
    
    print("\n" + "=" * 50)
    print("NULLPUNKTER:")
    print("=" * 50)
    for i, nullpunkt in enumerate(nullpunkter, 1):
        print(f"{i}. x = {nullpunkt:.5f}")
    print("=" * 50)


if __name__ == "__main__":
    main()