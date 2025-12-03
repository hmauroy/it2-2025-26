"""
Lag appen "Omstokkeren" der du bruker omstokkingsfunksjonen fra Uke 43 Man- Funksjoner og algoritmer. 
	• Et inputfelt der bruker kan skrive inn teksten
	• en knapp som bruker kan trykke på
	• en label kalt 'tekst_input', der inputteksten skal vises med blå bakgrunn.
	• en label kalt 'tekst_output' der inputteksten med omstokkede ord skal vises. Denne skal ha rød bakgrunn.
	• Tekstens font settes med disse innstillingene:
tekst.configure(
    text="Her er en osmtokekt tkset",
    font = ("Comic sans MS", 12),
    foreground="white",
    background="blue"
)
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
canvas = tk.Canvas(window)
canvas.configure(
    height=hoyde-50,
    width=bredde,
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

def tegnBall(xpos,ypos,r=50):
    canvas.create_oval(xpos,ypos,xpos+r,ypos+r,fill="#ff9944", tags="ball")

def slettBall():
    canvas.delete("ball")

xpos = 100
ypos = 100
x_step = 2
y_step = 2
dx = x_step
dy = 0


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
        print(teller)
        # 1) Sletter ballen
        slettBall()
        # 2) Flytter ballen
        xpos += dx
        ypos += dy
        # 3) Tegner ballen
        tegnBall(xpos,ypos,r=50)
        teller += 1
        # Bytter retning
        if teller == 150:
            dx = 0
            dy = y_step
        # En måte å stoppe ting på hvis det går skjæis.
        if teller > 300:
            isRunning = False
    
    
    window.update()
        


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

