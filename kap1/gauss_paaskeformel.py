"""
Gauss sin påskeformel som gir deg langfredag i påskeuka.
https://www.math.ntnu.no/emner/MA1301/2008h/paaske.pdf

Sjekk "svaret" her: https://www.timeanddate.no/kalender/
"""




def gauss_paskedag(aar):
    """
    Beregner datoen for Første påskedag i et gitt år ved hjelp av Gauss sin formel.
    Returnerer måned og dag som en tuple.
    """
    # Gauss sin formel for Første påskedag
    a = aar % 19
    b = aar // 100
    c = aar % 100
    d = b // 4
    e = b % 4
    f = (b+8) // 25
    g = (b - f + 1) // 3
    h = (19*a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2*e + 2*i - h - k) % 7
    m = (a + 11*h + 22*l) // 451
    mnd = (h + l - 7*m + 114) // 31
    p = (h + l - 7*m + 114) % 31

    # Påsken faller på den p + 1te dagen i den nte måneden. (3 = mars, 4 = april)
    dag = p - 1

    return mnd, dag



if __name__ == "__main__":
    aar = 2026
    print(f"Når er langfredag i år {aar} er {gauss_paskedag(aar)}")


