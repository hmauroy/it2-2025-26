import tkinter as tk
import time
from random import randint, random, uniform
from boble_utvikling import Ring, Boble

window = tk.Tk()
window.lift()
window.title("Boblespillet")
window.focus_force()
bredde = 800
hoyde = 700
canvas_height = hoyde-150
canvas_width = bredde
window.minsize(bredde,hoyde)
vindu_bakgrunn = "#FFFFFF"
tekst_bakgrunn = "#ffffff"
bunn_bakgrunn = "#3e3e3e"
vann_bakgrunn = "#292b52"
window.configure(background=vindu_bakgrunn)
window.pack_propagate(False) # Skrur av at children kan endre størrelsen til window.


# Setter inn en ramme (Frame)
topp = tk.Frame(window)
topp.configure(
    height=50,
    width=bredde*0.75,
    background=vindu_bakgrunn,
)
topp.pack_propagate(False) # Skrur av at children kan endre rammen.
topp.pack()

# Lager noe tekst med Label
overskrift = tk.Label(topp)
overskrift["text"] = "Spis mindre bobler, pass deg for de store!"
overskrift.configure(
    font = ("Aptos", 20),
    foreground="black",
    background=tekst_bakgrunn
)
overskrift.pack()


# Lager et mellomrom
mellomrom = tk.Label()
mellomrom.configure(
    height=1,
    width=1,
    bg=vindu_bakgrunn
)
mellomrom.pack()


# Lager utskrift der resultatet skal havne
utskrift = tk.Label()
utskrift["text"] = "Poeng: 0"
utskrift.configure(
    font = ("Aptos", 14),
    foreground="black",
    background=tekst_bakgrunn
)
utskrift.pack()


# Lager et canvas der vi kan tegne strekkodene som sorte og smale rektangler
canvas = tk.Canvas(window)
canvas.configure(
    width=bredde,
    height=canvas_height,
    background=vann_bakgrunn,
)
canvas.pack(expand=True)


# Lager en ramme nederst til avsluttknappen.
bunn = tk.Frame(window)
bunn.configure(
    width=bredde,
    height=50,
    background=bunn_bakgrunn,
)
bunn.pack()
bunn.pack_propagate(False)

def handle_avslutt():
    global isRunning
    isRunning = False
    window.update()
    window.destroy()

# Knapp
avslutt = tk.Button(bunn)
avslutt.configure(
    text = "Avslutt",
    command=lambda: handle_avslutt()
)
avslutt.pack()


# -------------- Spillogikk ligger under her --------------

xmin = 0
xmax = canvas_width
ymin = 0
ymax = canvas_height

# Lager en referanse til canvas inni Ring-klassen.
Ring.canvas = canvas

bobler = []
teller = 0
R_MIN = 5
R_MAX = 20


isRunning = True
lastTime = time.time()
start_time = time.time()
slette_indexer = []

while isRunning:
    if time.time() - lastTime >= 0.01:

        lastTime = time.time()
    window.update()


# Kjører vinduet. Må være nederst i koden.
window.mainloop()
