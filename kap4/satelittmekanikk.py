"""
Jeg tok en gammel banesimulering jeg lagde for fysikk 2 fra 2023 og la til kontroll av
- fart ved hjelp av rakettmotor
- retning forover eller bakover
ved hjelp av taster
Piltaster = forover/bakover endre 180 grader
Spacebar = Rakettmotor på så lenge den holdes inne.

Utvidelser:
- Drivstoffmengde (har lite å si for ekte satelitter tror jeg)

Akselerasjon for sirkelbane er a = v^2/r.
Når denne er akkurat lik gravitasjonskraften F_G får vi
v^2/r = F_G/m.
Løser med hensyn på v:
v = sqrt( (F_G*r)/m )



Henrik Mauroy
Okt 2025
hmauroy@gmail.com

"""
import tkinter as tk
import os
import time
from random import randint
from pylab import *
import math

window = tk.Tk()
window.lift()
window.focus_force()
window.title('Satelittbane')
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 800
windowHeight = 700
window.minsize(windowWidth,windowHeight)    # Setter størrelsen.


# 1) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

# 2) Lager en header med knapper
header = tk.Frame(canvas_frame)
header.pack()
# En boks til knappene
knappBoks = tk.Frame(header,height = 100)
knappBoks.pack()
btnRaskere = tk.Button(knappBoks,text="Øk fart")
btnRaskere.grid(column=2,row=1)
btnTregere = tk.Button(knappBoks,text="Senk fart")
btnTregere.grid(column=1,row=1)
btnRestart = tk.Button(knappBoks,text="Restart")
btnRestart.grid(column=3,row=1)
labelFart = tk.Label(knappBoks, text="______Fart oppdateres____")
labelFart.grid(column=4,row=1)
# Knapper for avstand også
btnIncreaseDistance = tk.Button(knappBoks,text="Øk avstand")
btnIncreaseDistance.grid(column=1, row=2)
btnDecreaseDistance = tk.Button(knappBoks,text="Mindre avstand")
btnDecreaseDistance.grid(column=2, row=2)
labelAvstand = tk.Label(knappBoks, text="___Avstand oppdateres____")
labelAvstand.grid(column=4,row=2)

# Lager en NY ramme som selve spill-canvas kan ligge inni.
frame2 = tk.Frame(window)
frame2.pack()
canvas = tk.Canvas(frame2,width=windowWidth,height=windowHeight,background="black")
canvas.pack()

def handle_raskere(evt):
    print("Raskere fart!")
    global satelitt, labelFart
    satelitt.v = satelitt.v * 1.05

def handle_tregere(evt):
    print("Bremser fart!")
    global satelitt, labelFart
    satelitt.v = satelitt.v * 0.9

def handle_restart(evt):
    print("Restarter simulering med hastighetene som er valgt")
    global satelitt, labelFart, forrige_tid
    satelitt.r = array([4e7, 0])
    satelitt.v = array([0, -2.4e3]) 
    forrige_tid = time.time()

def handle_IncreaseDistance(evt):
    global satelitt, labelAvstand
    satelitt.r = satelitt.r * 1.05

def handle_DecreaseDistance(evt):
    global satelitt, labelAvstand
    satelitt.r = satelitt.r * 0.95

def processKeypress(evt):
    global satelitt, isRunning, isPaused, lasTime_keypress
    key = evt.keysym
    if time.time() - lasTime_keypress > 0.500:
        lasTime_keypress = time.time()
        # Må få simulering til å settes på pause idet knappen trykkes.
        #isPaused = True
        print(f'key: {key}')
        if key == "Left":
            print("Left")
            satelitt.motorAv()
        elif key == "Right":
            print("Right")
            satelitt.motorPaa()
        elif key == "space":
            print("Space")
            if satelitt.thrust == True:
                satelitt.motorAv()
            else:
                satelitt.motorPaa()
        

window.bind("<Key>",processKeypress)

import numpy as np

def angle_between_vectors(v1, v2):
    """
    Calculate the angle in degrees between two numpy vectors.
    
    Args:
        v1 (numpy.ndarray): First vector
        v2 (numpy.ndarray): Second vector
    
    Returns:
        float: Angle in degrees between the vectors (0 to 180)
    """
    # Normalize the vectors
    v1_norm = v1 / np.linalg.norm(v1)
    v2_norm = v2 / np.linalg.norm(v2)
    
    # Calculate dot product and clamp to [-1, 1] to avoid numerical errors
    dot_product = np.clip(np.dot(v1_norm, v2_norm), -1.0, 1.0)
    
    # Calculate angle in radians, then convert to degrees
    angle_radians = np.arccos(dot_product)
    angle_degrees = np.degrees(angle_radians)
    
    return angle_degrees


def rotate_points_list(points, center, angle_degrees):
    """
    Rotate a list of points around a center.
    
    Args:
        points (list of tuples): Points to rotate [(x1,y1), (x2,y2), ...]
        center (tuple): Center of rotation (cx, cy)
        angle_degrees (float): Rotation angle in degrees
    
    Returns:
        list of tuples: Rotated points
    """
    angle_radians = np.radians(angle_degrees)
    cos_a = np.cos(angle_radians)
    sin_a = np.sin(angle_radians)
    cx, cy = center
    
    rotated = []
    for x, y in points:
        x_shifted = x - cx
        y_shifted = y - cy
        x_rot = x_shifted * cos_a - y_shifted * sin_a
        y_rot = x_shifted * sin_a + y_shifted * cos_a
        rotated.append((x_rot + cx, y_rot + cy))
    
    return rotated



class Satelitt:
    gamma = 6.67e-11  # gravitasjonskonstanten, Nm^2/kg^2
    def __init__(self,windowWidth,windowHeight) -> None:
        self.m = 200
        self.window = [windowWidth, windowHeight]
        self.pixel_norm_faktor = 25e3 # Normalisering av ekte avstander mot pixelverdier: 62.5 m/px.
        self.R = windowWidth/50 # Radius
        self.farge = "#ffee33"
        self.xpos = windowWidth/2 + 150
        self.ypos = windowHeight/2
        self.r = array([6.578e6, 0])    # posisjonen til satelitten, m
                                    # Må normalisere mot pixelverdier i canvas...
                                    # r = 6.578e6 m
                                    # 2e7 = windowWidth (Omtrent 150 % av diameter til banen)
                                    # 2e7 m / 800px = 25e3 m/px
        self.v = array([0, -7781.72505])  # farten til satellitten, m/s
        self.aks = 0
        self.forrige_r = self.r
        self.bane_r = self.r
        self.thrust = False
        self.orientering = 1
        self.vector_up = array([0, -1])
    
    # Variable krefter, beregning av kraftsum og akselerasjon
    def akselerasjon(self,earth):
        G_abs = Satelitt.gamma*self.m*earth.M/norm(self.r)**2  # absoluttverdi gravitasjon, N
        e_r = -self.r/norm(self.r)              # enhetsvektor mot sentrum av sola
        G = G_abs*e_r                 # gravitasjonskraft med riktig retning
        aks = G/self.m                     # akselerasjon, m/s^2
        self.aks = aks
        return aks

    def tegnSatelitt(self,canvas):
        # Calculate the 4 corners of the rectangle
        upper_left = (self.xpos - self.R, self.ypos - 1.5 * self.R)
        upper_right = (self.xpos + self.R, self.ypos - 1.5 * self.R)
        lower_right = (self.xpos + self.R, self.ypos + 1.5 * self.R)
        lower_left = (self.xpos - self.R, self.ypos + 1.5 * self.R)

        # Rotate all 4 corners
        vinkel = angle_between_vectors(self.r, self.vector_up)
        if self.xpos < windowWidth/2:
            vinkel = -vinkel
        #print(vinkel)

        corners = [upper_left, upper_right, lower_right, lower_left]
        rotated_corners = rotate_points_list(corners, (self.xpos, self.ypos), vinkel)

        # Flatten for polygon
        coords = [coord for point in rotated_corners for coord in point]

        canvas.create_polygon(coords, fill=self.farge, outline=self.farge, tags="satelitt")
    
    def tegnBane(self,canvas, windowWidth, windowHeight):
        """Tegne banen med venstre hjørne en radius unna sentrum i x- og y-retning."""
        #print(f"r-vektor (px) = {self.r/self.pixel_norm_faktor}")
        # Beregner baneradius fra posisjonsvektoren fra forrige radius
        R = norm(self.bane_r/self.pixel_norm_faktor)
        x1 = windowWidth/2 - R
        y1 = windowHeight/2 - R
        x2 = windowWidth/2 + R
        y2 = windowHeight/2 + R
        canvas.create_oval(x1,y1,x2,y2,
            outline="white",tags="bane")
    
    def motorPaa(self):
        self.thrust = True
        self.v = self.v * 1.05

    def motorAv(self):
        self.thrust = False
        self.v = self.v / 1.05

    

class Jord:
    def __init__(self,windowWidth,windowHeight) -> None:
        self.M = 5.972e24
        self.radius = 6378e3
        self.R = windowWidth/10
        self.xpos = windowWidth/2
        self.ypos = windowHeight/2
        self.farge = "#1199ff"
        self.faktor = 10
    
    def tegnJord(self,canvas):
        canvas.create_oval(self.xpos-self.R,self.ypos-self.R,
        self.xpos+self.R,self.ypos+self.R,
            fill=self.farge,tags="earth")
    

# Lager objektene som skal holde på all informasjon
satelitt = Satelitt(windowWidth,windowHeight)
jord = Jord(windowWidth,windowHeight)
jord.tegnJord(canvas)

btnRaskere.bind("<Button-1>",handle_raskere)
btnTregere.bind("<Button-1>",handle_tregere)
btnRestart.bind("<Button-1>",handle_restart)
btnIncreaseDistance.bind("<Button-1>",handle_IncreaseDistance)
btnDecreaseDistance.bind("<Button-1>",handle_DecreaseDistance)

# Setter opp simuleringen
dt = 1         # sek, For en smooth simulering som går litt sakte sett til 1 sek maks 10 sek.
t = 0           # starttiden
sim_speed = 1000 # Antall ganger raskere simulering enn virkeligheten.
forrige_tid = time.time()   # Brukes til animasjon.
forrige_tegne_tid = forrige_tid
lasTime_keypress = forrige_tid
isRunning = True
teller = 0
isPaused = False

while isRunning:
    # Utfører kun beregning der hvert sekund i simuleringstid er x ms i realtime for at ikke CPU skal beregne for fort.
    if time.time() - forrige_tid >= 1/(dt*sim_speed):
        forrige_tid = time.time()

        # Testing
        if t == 0:
            satelitt.tegnBane(canvas, windowWidth, windowHeight)
            #isRunning = False
        
        if not isPaused:
            # For hver loop går det 1 sekund simuleringstid
            # Flytt litt i tidsrom dt
            a = satelitt.akselerasjon(jord)  # beregner akselerasjon
            #print(f"a = {a}")
            satelitt.v = satelitt.v + a*dt         # beregner ny fart
            #print(f"v = {satelitt.v}")
            satelitt.r = satelitt.r + satelitt.v*dt         # beregner ny posisjon
            t = t + dt           # ny tid

            d = np.sqrt(satelitt.xpos**2 + satelitt.ypos**2)
            print(f"d:{d}")
            if d < jord.R:
                # Krasjet i overflaten
                print("Krasjet i overflaten.")
                print(f"Høyde = {norm(satelitt.r) - jord.radius} m")
                isRunning = False
                canvas.delete("satelitt")
                satelitt.tegnSatelitt(canvas)

            
            # oppdaterer grafikken med den nye r-vektoren.
            satelitt.xpos = windowWidth/2 + satelitt.r[0]/satelitt.pixel_norm_faktor
            satelitt.ypos = windowHeight/2 + satelitt.r[1]/satelitt.pixel_norm_faktor

            #isPaused = True

            # Roterer satelitt så den er parallell med tangent til banen.

            #canvas.delete("satelitt")
            #satelitt.tegnSatelitt(canvas)
        
        # Oppdatering av tegning skjer ved faste tidsintervall.
        if time.time() - forrige_tegne_tid >= 0.04:   # 0.04 gir ca. 25 fps (CPU gjør mye utregning)
            teller += 1
            forrige_tegne_tid = time.time()
            # 1) slett satelitt fra canvas før man tegner opp med oppdaterte posisjoner.
            canvas.delete("satelitt")
            #canvas.delete("bane")
            # 2) tegn
            satelitt.tegnSatelitt(canvas)
            # Oppdater fart og avstand hver 10. frame
            if teller == 10:
                labelAvstand["text"] = f"{(norm(satelitt.r) - jord.radius):.5e} m"
                labelFart["text"] = f"{norm(satelitt.v):.1f} m/s"
                teller = 0
        
    
    window.update()





window.mainloop()