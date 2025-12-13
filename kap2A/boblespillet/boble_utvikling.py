"""
Klassedefinisjoner for bobler og underklassene av disse.
"""
from random import random
import math

class Ring:
    canvas = None
    """Default klasse for å tegne en ring."""
    def __init__(self,r,x,y):
        self.R = r
        self.x = x
        self.y = y
        self.canvas = Ring.canvas
        self.tag = "ring"
        self.outline = "white"

    def tegn(self):
        """Tegn ringen i canvas."""
        self.canvas.create_oval(self.x-self.R,self.y-self.R,
        self.x+self.R,self.y+self.R, outline=self.outline,tags=self.tag)

class Boble(Ring):
    def __init__(self,r,x,y,fart,id):
        super().__init__(r,x,y)
        self.type = "boble"
        self.dx = random() * fart
        if self.dx == 0:
            self.dx = 0.1
        self.dy = 0
        self.id = id
        self.levende = True
        self.merge = False

    def kollisjon(self,objekt2):
        """
        Ved kollisjon med en annen boble skal den største boblen spise den lille. 
        Ny posisjon blir gjennomsnitet av x,y-pos for begge.
        Hvis kollisjon med hindring skal boblen sprekke.
        Hva slags objekt det kollideres mot må sjekkes før kollisjon. Hvis hindring må hindring.kollisjon() benyttes.
        """
        if not self == objekt2:
            # Sjekk avstand mellom senter av boblene.
            dx = self.x - objekt2.x
            dy = self.y - objekt2.y
            d = math.sqrt(dx**2 + dy**2)
            if d <= self.R + objekt2.R:
                # Kollisjon.
                print(f"kollisjon: {self.x},{self.y}")
                self.merge = True
                objekt2.merge = True
                if self.R >= objekt2.R:
                    # Spiser mindre boble.
                    print("self spiser mindre boble")
                    objekt2.levende = False
                    self.ny_radius(objekt2)
                    self.beregn_ny_posisjon(objekt2)
                    self.beregn_ny_fart(objekt2)
                else:
                    self.levende = False
                    objekt2.ny_radius(self)
                    objekt2.beregn_ny_posisjon(self)
                    objekt2.beregn_ny_fart(self)
            else:
                self.merge = False
        

    def oppdater(self):
        "Oppdater fart, posisjon, sjekk kollisjon, tegn"
        self.x -= self.dx
        if self.x + self.R < 0:
            self.levende = False

    def ny_radius(self,objekt2):
        areal = self.areal() + objekt2.areal()
        self.r = math.sqrt(areal / math.pi)
    
    def beregn_ny_posisjon(self,objekt2):
        self.x = (self.x + objekt2.x )/2
        self.y = (self.y + objekt2.y )/2
    
    def beregn_ny_fart(self,objekt2):
        self.dx = (self.dx + objekt2.dx)/2
        self.dy = (self.dy + objekt2.dy)/2

    def areal(self):
        return math.pi*self.R**2

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
        self.type = "helt"
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
        self.type = "fiende"
    
    def oppdater(self):
        """
        Delvis overstyring av superklassens oppdater().
        Skal generere tilfeldig fart og bevegelse.
        Deretter kjøre super().oppdater()
        """
        pass

class Hindring:
    """
    Det finnes hindringer i vannet som dukker opp. 
    Disse er kvadratiske for enkelthets skyld.
    Kan være mangekanter hvis ønskelig.
    """
    def __init__(self,a):
        self.type = "hindring"
        pass

    def kollisjon(self,objekt2):
        """
        Hindringer har en annen algorite for å sjekke for kollisjon som ikke 
        benytter Pythagoras som gjelder for kollisjon mellom sirkler (boblene).

        """
    

