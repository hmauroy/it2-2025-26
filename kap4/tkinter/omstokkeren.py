"""
Stokker om de midterste bokstavene i hvert ord i en tekst.

Eksempel på bruk:
tekst = omstokket_tekst("Heisann IT2klassen!)
print(tekst) gir svaret "Hnieasn IlsaT2kesn"
"""
from random import randint

def omstokket(ordet):
    spesialtegn = list(".,:;!-_%&/()=?+^*")
    output = ""
    # 1) Plukk ut første og siste bokstav.
    output += ordet[0]
    slutten = ordet[-1]
    # 2) Plukk ut midten hvis lengre enn 3 tegn
    if len(ordet) > 3:
        # Dersom spesialtegn på slutten av ordet.
        if str(ordet[-1]) in spesialtegn:
            midt = list(ordet[1:-2])
            slutten = ordet[-2:]
        else:
            midt = list(ordet[1:-1])
        # a) Hvis midt == 2, reverser de to midterste bokstavene.
        if len(midt) == 2:
           output += str(midt[1]) + str(midt[0])
        # b) Stokk om midten ved bruk av random.shuffle()
        else:
            midt = random_henrik(midt)
            # Bygger opp en tekst igjen.
            for c in midt:
                output += str(c)
        # X) Sett på siste bokstav
        output += slutten
    else:
        return ordet
    return output

def omstokket_baklengs(ordet):
    spesialtegn = list(".,:;!-_%&/()=?+^*")
    output = ""
    # 1) Plukk ut første bokstav
    output += ordet[0]
    slutten = ordet[-1]
    # 2) Plukk ut midten hvis lengre enn 3 tegn
    if len(ordet) > 3:
        # Dersom spesialtegn på slutten av ordet.
        if str(ordet[-1]) in spesialtegn:
            midt = list(ordet[1:-2])
            slutten = ordet[-2:]
        else:
            midt = list(ordet[1:-1])
        # a) Hvis midt == 2, reverser de to midterste bokstavene.
        midt = random_henrik(midt)
        # Reverserer midten
        midt.reverse()
        # Bygger opp en tekst igjen.
        for c in midt:
            output += str(c)
        # X) Sett på siste bokstav
        output += slutten
    else:
        return ordet
    return output


def random_henrik(liste):
    """
        Shuffle av en liste.
        Output er en liste
    """
    output = []
    while len(liste) > 0:
        # Plukker ut en tilfeldig index.
        indeks = randint(0,len(liste)-1)
        # Tar ut verdi med pop() for indeksen valgt og legger til output.
        output.append(liste.pop(indeks))    
    return output


def omstokket_tekst(tekst):
    liste = tekst.split()
    ulesbar_tekst = ""
    for ord in liste:
        ulesbar_tekst += omstokket(ord) + " "

    return ulesbar_tekst


def main():
    tekst = "En lengre tekst som er vanskelig! hmauroy@gmail.com å lese hvis den er omstokket."
    print(tekst)
    print(omstokket_tekst(tekst))
    print(omstokket_tekst("Heisann IT2 klassen"))



if __name__ == "__main__":
    main()

