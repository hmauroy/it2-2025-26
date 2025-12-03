"""
Noen enkle klasser for å vise hva OOP er.

Dyr
Type dyr
Vekt
Lengde
Alder
Dø
Spise
Sove
Formere

Kanin
Art
Pelsfarge
rovdyr
Løpe

Rev
Art
Pelsfarge
rovdyr
Jage

"""
from random import randint

class Dyr:
    def __init__(self,type_dyr,vekt,lengde,alder=0):
        self.type_dyr = type_dyr
        self.vekt = vekt
        self.lengde = lengde
        self.alder = alder
        self.levende = True
        self.antall_barn = 0

    def __str__(self):
        return f"type_dyr: {self.type_dyr}, alder: {self.alder}"
    
    def sove(self):
        """Alder øker med ca. 8 timer dvs 1/3*1/365 år"""
        self.alder += 1/3 * 1/365
        return self.alder
    
    def die(self):
        self.levende = False
        return False
    
    def formere_seg(self):
        self.alder += 1/10 * 1/365
        self.vekt -= 0.5
        self.antall_barn += 4
        # Kan hende dyret dør underveis pga blir angrepet av rovdyr.
        if randint(1,100) == 13:
            print("Dyret dør under formering!")
            self.die()
            return False
        return True

    def spise(self):
        if randint(0,10) != 0:
            self.vekt += 0.5
            return True
        return False

class Kanin(Dyr):
    """Klassen kanin \n
    løpe():bool er en metode for å løpe fra fiender.
    """
    def __init__(self, vekt, lengde, alder, pelsfarge):
        super().__init__("pattedyr", vekt, lengde, alder)
        self.Art = "Kanin"
        self.pelsfarge = pelsfarge
        self.rovdyr = False
    
    def løpe(self):
        # En viss tilfeldighet at haren ikke løper fort nok.
        if randint(0,50) == 42:
            print("Kanin ble fanget :(")
            self.die()
        else:
            self.vekt -= 0.05
            print("Kanin slapp unna.")
        return self.levende
    
class Rev(Dyr):
    def __init__(self, vekt, lengde, alder, pelsfarge):
        super().__init__("pattedyr", vekt, lengde, alder)
        self.Art = "Rev"
        self.pelsfarge = pelsfarge
        self.rovdyr = True
    
    def jage(self):
        fangst = randint(0,3)
        for i in range(fangst):
            spist = self.spise()
            if spist:
                print("Rev spiser.")
        # En viss tilfeldighet at reven dør under jakten.
        if randint(1,200) == 13:
            print("Rev dør under jakten.")
            self.die()
        # Vekt minker alltid etter jaging pga bruker tid på å ikke spise.
        self.vekt -= 0.3
        return self.levende


if __name__ == "__main__":
    """ 
    Denne delen av koden kjører kun hvis vi kjører klassefilen. Ikke hvis vi importerer den i et annet program.
    """
    # Oppretter et Dyr-objekt.
    henrik = Dyr("pattedyr",72,180,42)

    # Oppretter en kanin
    kalle = Kanin(2,35,2,"grå")

    # Oppretter en rev
    mikkel = Rev(11,120,5,"rødbrun")

    print(kalle)
    print(mikkel)

    print("-------------------------")
    dager = 0
    # Vi lar kalle og mikkel leve litt i skogen. Hver loop er én dag.
    while kalle.levende and mikkel.levende:
        dager += 1
        if dager >= 1000000:
            print("Early exit")
            break
        # Lar kalle prøve å få tak i litt mat et tilfeldig antall ganger.
        ant_mat = randint(1,3)
        for i in range(ant_mat):
            kalle.spise()
            # Kanskje må kalle løpe litt mens han spiser:
            if randint(0,1) == 1:
                kalle.løpe()
        # mikkel kommer for å jage!
        ant_jakt = randint(0,3)
        for j in range(ant_jakt):
            mikkel.jage()
        # Kalle er jo kanin så må jo formere seg litt også.
        # Skjer hver 5. dag
        if dager % 5 == 0:
            kalle.formere_seg()
        # Sjekker om kalle er sykelig tynn.
        if kalle.vekt <= 0.5:
            print("kalle dør pga undervekt.")
            kalle.die()
        elif kalle.vekt >= 10:
            print("kalle dør pga undervekt.")
            kalle.die()
        # Sjekker vekten til mikkel om han er undervektig eller overvektig.
        if mikkel.vekt <= 4:
            print("mikkel dør pga undervekt.")
            mikkel.die()
        elif mikkel.vekt >= 20:
            print("mikkel dør av overvekt.")
            mikkel.die()
        # Begge dyrene må sove etter en dag.
        kalle.sove()
        mikkel.sove()

    print(f"Simulering stoppet etter {dager} dager")

    print(f"Kalle lever: {kalle.levende}, vekt: {kalle.vekt:.1f}, alder: {kalle.alder:.3f} år, antall barn: {kalle.antall_barn}.")
    print(f"Mikkel lever: {mikkel.levende}, vekt: {mikkel.vekt:.1f}, alder: {mikkel.alder:.3f} år")

