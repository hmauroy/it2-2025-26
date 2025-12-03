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
    print(omstokket_tekst("Heisann IT2klassen"))
    vitser = [
    "Hei, pass deg for den den landminen! Pøh, og den tror du jeg går på",

    "Har du hørt om han som ikke klarte å komme på hva støv betød på engelsk? Han følte seg ganske dust",

    "Har du hørt om han som ikke likte kaffe? Han syntes ikke det var noe å trakte etter",

    "Man kan si mye rart om Sveits, men en ting er i hvert fall sikkert. Flagget er et stort pluss",

    "Har du hørt om appelsinen som ble til appelsinjuice? Den følte seg presset til det",

    "Har du hørt om eselet som skrek så høyt at det ble hest?",

    "En far vasker bilen med sønnen. Så spør sønnen Hvorfor kan du ikke bare bruke en svamp?",

    "Hvorfor bør du ikke pusse tennene med venstrehånda? Det er mye bedre å bruke en tannbørste.",

    "Hvorfor fikk ikke eplet komme inn på utestedet? Fordi dørvakta var eplenektar",

    "Eple nekta, de kneip brødet, men sikta hvetemelet",

    "Jeg pleier å be ungene om å stille seg i hjørnet om de klager på at det er kaldt, er jo 90 grader der.",

    "Hva kaller du to soldater som holder hender? Leiesoldater",

    "Hvorfor døde mammutene ut? Det var ingen papputer igjen",

    "Kan du kjøpe en kiste? Nei! Det er det siste jeg skal kjøpe.",

    "Kona fant en edderkopp i boden, og spurte om jeg kunne ta den med ut. Så vi tok et par øl på puben, hyggelig fyr. Han er web designer",

    "Vet du hvem som har ansvaret for melkesalget i Saudi-Arabia? Milksjeiken",

    "Hvorfor har ikke isbiter armer og bein? De er vannskapte",

    "Hvorfor kan man ikke forsove seg som skuespiller? Du må alltid opptre.",

    "Og så var det skredderen som var stoffmisbruker.",

    "En mann kjøpte en klokke. Så ventet han til den ble to, og så solgte han den andre.",

    "Sønn kolon, Pappa, kan du ta på skoene mine? Pappa kolon, Det kan jeg, men jeg tror ikke de vil passe.",

    "Kan være at jeg er innbillsk altså, men jeg er rimelig sikker på at resepsjonisten på hotellet sjekket meg ut.",

    "Hva spiser spøkelser til frokost? Bøskiver.",

    "Det var en gang. Og innafor var det et kjøkken.",

    "Da jeg var liten ble jeg vaksinert mot kopper. Derfor drikker jeg nå alltid rett fra flasken.",

    "Hva heter opplysningskontoret for kuer? Q-tips.",

    "Hva sa den ene snømannen til den andre? Er det bare meg eller lukter det litt gulrot her?",

    "Den ene tørrfisken sa til den andre: Long time. no sea.",

    "Hva slags musikk hører osten på? Ostepop.",

    "Hvilken hunderase drikker mest vann? Olden Retriever.",

    "Hva kaller du en hund som kan trylle? Labrakadabrador!",

    "Hva spiser datamaskinen på julaften? Minnepinnekjøtt",

    "Jammen er seilbåter i vinden om dagen!",

    "Hørt om tyven som stjal en kalender? Han fikk 12 måneder.",

    "Jeg trener nesten hver dag. Som i dag for eksempel, da trente jeg nesten.",

    "Hørt om svensken som drev et datingbyrå for ender? Dessverre var det vanskelig å få endene til å møtes.",

    "Hva heter foreldrene til Tarzan ? Morzan og Farzan",

    "Hva har en svidd pizza og en gravid kvinne til felles? En mann har glemt å ta den ut i tide.",

    "Hvorfor har brannmenn røde bukseseler? For å holde buksene oppe.",

    "Hørt om det narkomane trollet som gikk ut i sola for å bli stein?",

    "Vet dere hvorfor elektrikere leser detektivbøker? Det er fordi de liker spenning!",

    "En skilpadde gikk over gaten og ble ranet av to snegler. Da politiet kom, spurte de ham hva som skjedde. Jeg vet ikke, svarte skilpadden, alt gikk så fort.",

    "Hva er det som er grønt, fluffy, og som dreper deg hvis det faller ned fra et tre? Et biljardbord!",

    "Hvilket dyr i havet er mest opptatt av sikkerheten? Sikkerhetsselen",
    ]
    for vits in vitser:
        print(omstokket_tekst(vits))




if __name__ == "__main__":
    main()

