"""
Animasjon:
Lag en versjon der ballen spretter mellom venstre og høyre "vegg".
"""


import tkinter as tk
import time
from random import randint, random

window = tk.Tk()
window.lift()
window.focus_force()
bredde = 500
hoyde = 550
window.minsize(bredde,hoyde)
farge_tekst_bakgrunn = "#dddddd"
farge_bakgrunn = "#334467"
farge_canvas = "#343434"
window.configure(background=farge_bakgrunn)

# Setter inn en ramme (Frame)
topp = tk.Frame(window,background=farge_tekst_bakgrunn)
topp.configure(
    height=50,
    width=bredde,
)
topp.pack_propagate(False) # Skrur av at children kan endre rammen.

topp.pack()

# Lager noe tekst med Label
tekst = tk.Label(topp)
tekst["text"] = "Fasong-transformers"
tekst.configure(
    font = ("Aptos", 30),
    foreground="white",
    background=farge_bakgrunn,
)
tekst.pack()

# Setter inn et tegnevindu.
canvas_width = 500
canvas_height = 500
canvas = tk.Canvas(window)
canvas.configure(
    height=canvas_height,
    width=canvas_width,
    background=farge_canvas
)
canvas.pack() # Skrur av at children kan endre rammen.

# Setter inn en footer der avslutningsknappen skal være
footer = tk.Frame(window)
footer.configure(
    height=50,
    width=bredde,
    background="#5b5b5b"
)
footer.pack()

def handle_avslutt():
    window.destroy()

# Setter inn en knapp for å avslutte.
avslutt_btn = tk.Button(footer)
avslutt_btn.configure(
    text="Avslutt",
    command=lambda: handle_avslutt()
)
avslutt_btn.pack()

# Kode nedenfor handler om animasjon.

def tegnBall(xpos,ypos,R=25):
    canvas.create_oval(xpos-R,ypos-R,xpos+R,ypos+R,fill="#ff9944", tags="ball")

def tegnKvadrat(xpos, ypos, R=25):
    canvas.create_rectangle(xpos-R, ypos-R, xpos+R, ypos+R, fill="#ff9944", tags="ball")

def tegnTrekant(xpos,ypos,s=30):
    # Tweaket hvor høyt det øverste punktet skal tegnes.
    canvas.create_polygon(xpos-s,ypos+s,xpos,ypos-0.67*s,xpos+s,ypos+s,fill="#ff9944", outline="white", tags="ball")

def slettBall():
    canvas.delete("ball")

def sjekkKollisjon(xpos, ypos, x_step, y_step, dx, dy, R):
    global isRunning, canvas_height, canvas_width
    if xpos + R >= canvas_width:  # Høyre vegg
        dx = -x_step * randint(-5,5) * random() # Lager en tilfeldig fart.
        # Flytter ball til nøyaktig ved siden av veggen.
        xpos = canvas_width - R
    elif xpos - R <= 0:     # Venstre vegg
        dx = x_step * randint(-5,5) * random()  
        xpos = R
    if ypos + R >= canvas_height: # Bunnen
        dy = -y_step * randint(-5,5) * random()
        ypos = canvas_height - R
    elif ypos - R <= 0:     # Toppen
        dy = y_step * randint(-5,5) * random()
        ypos = R
    return dx, dy, xpos, ypos

def settFasong(fasonger, indeks):
    return fasonger[indeks]

xpos = 100
ypos = 100
x_step = 5
y_step = 5
dx = -x_step
dy = y_step
R = 25


canvas.update()


isRunning = True # Bestemmer om animasjon skal skje eller ikke.
last_time = time.time()
teller = 0
fps = 30
delta_t = 1/fps
fasonger = [1,2,3]
fasong_indeks = 0
fasong = settFasong(fasonger, fasong_indeks)
# Animasjonsloop
while isRunning:
    if time.time() - last_time >= delta_t:
        last_time = time.time()
        print(teller)
        # 1) Sletter ballen
        slettBall()
        # 2) Flytter ballen
        xpos += dx
        ypos += dy
        # 3) Sjekk om det er kollisjon.
        """
        - Funksjonen returnerer en tuple som vi pakker ut med dx, dy, x, y = ...
        - Nå har vi den nye retningen for neste frame som skal tegnes opp,
        - samt oppdaterte posisjoner rett ved siden av veggen.
        """
        dx, dy, xpos, ypos = sjekkKollisjon(xpos, ypos, x_step, y_step, dx, dy, R)
        # 4) Tegner ballen
        if teller % 30 == 0:
            # Resetter fasong_indeks hvis det ikke er flere fasonger igjen.
            if fasong_indeks >= len(fasonger):
                fasong_indeks = 0
            fasong = settFasong(fasonger, fasong_indeks)
            fasong_indeks += 1
            dx = x_step * randint(-5,5) * random()
            dy = y_step * randint(-5,5) * random()
        if fasong == 1:
            tegnBall(xpos,ypos,R)
        elif fasong == 2:
            tegnKvadrat(xpos,ypos,R)
        elif fasong == 3:
            tegnTrekant(xpos,ypos,30)
        teller += 1

        # En måte å stoppe ting på hvis det går skjæis.
        if teller > 10000:
            isRunning = False
    
    
    window.update()
        


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

