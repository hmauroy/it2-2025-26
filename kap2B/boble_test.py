"""Klassedefinisjon for Boble"""
from ring import Ring
from random import random, randint
import math

class Boble(Ring):
    def __init__(self,r,x,y,fart,id):
        super().__init__(r,x,y)
        self.type = "boble"
        self.dy = random() * fart
        if self.dy == 0:
            self.dy = 0.1
        self.dx = 0
        self.id = id
        self.levende = True
        self.merge = False
        self.mergeTeller = 0

    def kollisjon(self,objekt2):
        """
        Ved kollisjon med en annen boble skal den største boblen spise den lille. 
        Ny posisjon blir gjennomsnitet av x,y-pos for begge.
        Hvis kollisjon med hindring skal boblen sprekke.
        Hva slags objekt det kollideres mot må sjekkes før kollisjon. Hvis hindring må hindring.kollisjon() benyttes.
        """
        # Tilfeldig tall 1% om det skal sjekkes for kollisjon.
        testKollisjon = randint(1,100) == 42
        if self.type == "helt":
            testKollisjon = True
        if not self == objekt2 and testKollisjon == True:
            # Sjekk avstand mellom senter av boblene.
            dx = self.x - objekt2.x
            dy = self.y - objekt2.y
            d = math.sqrt(dx**2 + dy**2)
            if d <= self.R + objekt2.R:
                # Kollisjon.
                #print(f"kollisjon: {self.x},{self.y}")
                self.merge = True
                self.mergeTeller += 1
                if self.mergeTeller >= len(Boble.farger)-1:
                    self.mergeTeller = len(Boble.farger)-1
                #self.outline = Boble.farger[self.mergeTeller-1]
                #self.outline = "chartreuse"
                objekt2.merge = True
                if self.R >= objekt2.R:
                    # Spiser mindre boble.
                    #print("self spiser mindre boble")
                    objekt2.levende = False
                    self.ny_radius(objekt2)
                    #self.beregn_ny_posisjon(objekt2)
                    #self.dy = 0.1
                    self.beregn_ny_fart(objekt2)
                else:
                    self.levende = False
                    objekt2.ny_radius(self)
                    #objekt2.beregn_ny_posisjon(self)
                    #objekt2.dy = 0.1
                    objekt2.beregn_ny_fart(self)
                    #objekt2.outline = "red"
            else:
                self.merge = False

    def oppdater(self):
        # Reseter merge flagget
        self.merge = False
        """Wrapper-funksjon som gjør ulike oppgaver."""
        self.oppdater_helper()

    def oppdater_helper(self):
        "Oppdater fart, posisjon, sjekk kollisjon, tegn"
        self.y -= self.dy
        if self.y + self.R < 0:
            self.levende = False

    def ny_radius(self,objekt2):
        areal = self.areal() + objekt2.areal()
        self.R = math.sqrt(areal / math.pi)
        if self.R >= 100:
            self.levende = False

    def beregn_ny_posisjon(self,objekt2):
        """Ny posisjon er vektet gjennomsnitt av posisjonene."""
        self.x = (self.x + objekt2.x )/2
        self.y = (self.y + objekt2.y )/2

    def beregn_ny_fart(self,objekt2):
        """Ny fart er vektet gjennomsnitt av fartene. Omtrent som bevegelsesmengde."""
        faktor = self.R / objekt2.R
        self.dx = (self.dx + objekt2.dx/faktor)/2
        self.dy = (self.dy + objekt2.dy/faktor)/2

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