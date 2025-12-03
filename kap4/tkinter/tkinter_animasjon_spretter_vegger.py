"""
Animasjon:
Lag en versjon der ballen spretter mellom venstre og høyre "vegg".
"""


import tkinter as tk
import time

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
tekst["text"] = "Animasjon med Canvas"
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

def tegnBall(xpos,ypos,R=50):
    canvas.create_oval(xpos-R,ypos-R,xpos+R,ypos+R,fill="#ff9944", tags="ball")

def slettBall():
    canvas.delete("ball")

def sjekkKollisjon(xpos, ypos, x_step, y_step, dx, dy, R):
    global isRunning, canvas_height, canvas_width
    if xpos + R >= canvas_width:  # Høyre vegg
        dx = -x_step
        # Flytter ball til nøyaktig ved siden av veggen.
        xpos = canvas_width - R
    elif xpos - R <= 0:     # Venstre vegg
        dx = x_step
        xpos = R
    if ypos + R >= canvas_height: # Bunnen
        dy = -y_step
        ypos = canvas_height - R
    elif ypos - R <= 0:     # Toppen
        dy = y_step
        ypos = R
    return dx, dy, xpos, ypos


xpos = 100
ypos = 100
x_step = 10
y_step = 0
dx = -x_step
dy = y_step
R = 25


canvas.update()

isRunning = True # Bestemmer om animasjon skal skje eller ikke.
last_time = time.time()
teller = 0
fps = 30
delta_t = 1/fps
# Animasjonsloop
while isRunning:
    if time.time() - last_time >= delta_t:
        last_time = time.time()
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
        tegnBall(xpos,ypos,R)
        teller += 1

        # En måte å stoppe ting på hvis det går skjæis.
        if teller > 10000:
            isRunning = False
    
    
    window.update()
        


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

