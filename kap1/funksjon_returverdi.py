"""
Når benyttes return av en f-string?

Hvordan oppfører parametre seg i programmet?
"""
# Globale variabler er tilgjengelig for alle funksjoner i programmet.
# Globale variabler blir oversett av funksjoner hvis de har parameter med samme navn.
minTekst = "IT2 rocker!"
globalt_tall = 42

def tekst(minTekst):
    # minTekst-parameteren er en PRIVAT variabel inni funksjonen.
    # Valgfritt om du printer tekst eller returnerer en tekst. Kommer an på bruksområdet.
    print(f"Hei jeg fikk en tekst: {minTekst} som var {len(minTekst)} tegn lang. Tallet er {globalt_tall}")
    return f"Hei jeg fikk en tekst: {minTekst} som var {len(minTekst)} tegn lang. Tallet er {globalt_tall}"

lagring = tekst("hei")