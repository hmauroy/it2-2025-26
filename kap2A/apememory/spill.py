from random import randint
from math import sqrt
from prikk import Prikk

class Spill:
    """
    dimensions = [xmin,ymin,xmaks,ymaks]
    """
    def __init__(self,username,dimensions):
        self.poeng = 0
        self.prikker = []
        self.R = 30
        self.padding = int(self.R*1.1)
        self.player = username
        self.xmin = dimensions[0] + self.padding
        self.xmaks = dimensions[2] - self.padding
        self.ymin = dimensions[1] + self.padding
        self.ymaks = dimensions[3] - self.padding
    
    def avstand(self,p1,p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        return sqrt(dx**2 + dy**2)

    def lag_prikker(self):
        N = randint(3,10)
        self.prikker = []
        teller = 0
        # 1) Lager N antall prikker som ikke overlapper
        while len(self.prikker) < N:
            overlapp = True
            while overlapp == True:
                # 2) Lag en ny prikk
                x = randint(self.xmin,self.xmaks)
                y = randint(self.ymin,self.ymaks)
                ny_prikk = Prikk(self.R,x,y)
                teller += 1
                if teller >= 1000000:
                    print("For mange prikker til å unngå overlapp!")
                    exit()
                # 3) Sjekk overlapp
                overlapp = False
                for p2 in self.prikker:
                    if not ny_prikk == p2:
                        if self.avstand(ny_prikk,p2) <= 2*self.R + self.padding:
                            overlapp = True
                            break
                if overlapp == False:
                    self.prikker.append(ny_prikk)
        return N
    
    def vis_info_prikker(self):
        print(f"{len(self.prikker)} prikker:")
        print("--------------------------")
        for p in self.prikker:
            print(p)
        print("--------------------------")
    

    def tegn_prikker(self):
        for prikk in self.prikker:
            prikk.tegn()