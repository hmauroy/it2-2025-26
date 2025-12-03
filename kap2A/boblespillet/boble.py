"""
Klassedefinisjoner for bobler og underklassene av disse.
"""

class Ring:
    """Default klasse for å tegne en ring."""
    def __init__(self,r,x,y):
        pass

    def tegn(self):
        """Tegn ringen i canvas."""
        pass

class Boble(Ring):
    def __init__(self,r,x,y):
        super().__init__(r,x,y)
        pass

    def kollisjon(self,objekt2):
        """
        Ved kollisjon med en annen boble skal den største boblen spise den lille. 
        Ny posisjon blir gjennomsnitet av x,y-pos for begge.
        Hvis kollisjon med hindring skal boblen sprekke.
        """
        pass

    def oppdater(self):
        "Oppdater fart, posisjon, sjekk kollisjon, tegn"
        pass

    def sprekk_boble(self):
        """
        En form for animasjon viser at boblen sprekker.
        Kanskje blåses opp som flere konsentriske ringer som blir større og større radius 
        mens de første innerste ringene fader ut.
        Kan animeres ved å la ringene vises i x antall frames og for hver y frame opprettes en ny ring.
        """
        pass

class Helt(Boble):
    def __init__(self, r, x, y):
        super().__init__(r, x, y)
        self.poeng = 0
    
    def sett_ny_fart(self,dx,dy):
        pass

    def kollisjon(self, objekt2):
        """
        Hvis helten treffer en annen boble skal den spise den andre hvis mindre.
        Ellers dør helten.
        """
        pass
    


class Fiende(Boble):
    def __init__(self, r, x, y):
        super().__init__(r, x, y)
    
    def oppdater(self):
        """
        Delvis overstyring av superklassens oppdater().
        Skal generere tilfeldig fart og bevegelse.
        Deretter kjøre super().oppdater()
        """
        pass

class Hindring:
    """Det finnes hindringer i vannet som dukker opp"""
    def __init__(self):
        pass
    

