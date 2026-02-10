"""
Apememory

tilfeldig antall prikker kommer opp på skjermen.
Svart bakgrunn og gule/lyse prikker på 30px radius.
(Farger kan varieres for høyere vanskelighetsgrad).

Bruker må telle.

Deretter tømmes skjermen og 5 bokser/knapper med et tall i hver kommer frem.

Bruker må trykke på riktig tall som ble vist på forrige skjerm.
"""

import tkinter as tk
import time
from random import randint, random, uniform, sample, shuffle
from prikk import Prikk
from spill import Spill

window = tk.Tk()
window.lift()
window.title("monkey memory")
window.focus_force()
bredde = 1500
hoyde = 1000
canvas_height = hoyde-150
canvas_width = bredde
window.minsize(bredde,hoyde)
vindu_bakgrunn = "#FFFFFF"
tekst_bakgrunn = "#ffffff"
bunn_bakgrunn = "#3e3e3e"
brett_bakgrunn = "#E2DE01"
brett_bakgrunn = "#000000"
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
overskrift["text"] = "Tell antall prikker, trykk på riktig knapp for antallet."
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

# Lager knapper i en rad
button_frame = tk.Frame(window)
button_frame.grid(row=1, column=0, pady=10)

buttons = []
for i in range(5):
    btn = tk.Button(button_frame, text=f"{i}")
    btn.configure(
        command=lambda id=i: handle_knapp(id)
    )
    btn.grid(row=0, column=i, padx=5)
    buttons.append(btn)
# Track visibility state
visible = False
button_frame.grid_remove()

def toggle_buttons():
    global visible
    if visible:
        button_frame.grid_remove()  # Hide the entire frame
    else:
        button_frame.grid()  # Show it again
    visible = not visible

# Lager et canvas der vi kan tegne prikkene.
canvas = tk.Canvas(window)
canvas.configure(
    width=bredde,
    height=canvas_height,
    background=brett_bakgrunn,
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

def handle_knapp(id):
    global antall, isRunning, isWatching, btn_verdier, spill, start_time
    print(f"button ID: {id}")
    print(btn_verdier[id])
    if btn_verdier[id]  == antall:
        print("Riktig")
        spill.poeng += 1
        utskrift["text"] = f"Poeng: {spill.poeng}"
        isWatching = True
        antall = spill.lag_prikker()
        toggle_buttons()
        start_time = time.time()
    else:
        spill.poeng -= 1
        utskrift["text"] = f"Poeng: {spill.poeng}"
        if spill.poeng < 0:
            isRunning = False
            overskrift["text"] = "You Lose!"
        print("Feil knapp")


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
Prikk.canvas = canvas

prikker = []
teller = 0
R = 30
dimensjoner = [xmin,ymin,xmax,ymax]

spill = Spill("henrik",dimensjoner)

antall = spill.lag_prikker()

spill.vis_info_prikker()



isRunning = True
isWatching = True
lastTime = time.time()
start_time = time.time()
slette_indexer = []
dt = 1/30
tidsbegrensning = 0.5

while isRunning:
    if time.time() - lastTime >= dt:
        if isWatching:
            canvas.delete("prikk")
            if time.time() - start_time <= tidsbegrensning:
                spill.tegn_prikker()
            else:
                start_time = time.time()
                isWatching = False
                toggle_buttons()
                riktig = randint(0,4)
                # Lager 5 tilfeldige tall fra en range. Men må ta vekk "antall" først så ikke 
                # samme tall kan forekomme to ganger.
                # Tar vekk antall fra settet med tall fra range-funksjonen.
                populasjon = list(set(range(antall-2,antall+4)) - set([antall]))
                btn_verdier = sample(populasjon, 5)
                shuffle(btn_verdier)
                # Setter inn det ene tallet for nå er det ikke overlapp med de tilfeldige tallene.
                btn_verdier[randint(0,4)] = antall
                teller = 0
                for b in buttons:
                    b["text"] = btn_verdier[teller]
                    print(b["text"])
                    teller += 1
                print(btn_verdier)


        
        

        lastTime = time.time()
    window.update()


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

