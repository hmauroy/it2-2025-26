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
from tkinter import PhotoImage

window = tk.Tk()
window.lift()
window.focus_force()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)
farge_tekst_bakgrunn = "#dddddd"
farge_bakgrunn = "#334467"
window.configure(background=farge_bakgrunn)

# Setter inn en ramme (Frame)
topp = tk.Frame(window,background=farge_tekst_bakgrunn)
topp.configure(
    height=100,
    width=bredde*0.75,
)
topp.pack_propagate(False) # Skrur av at children kan endre rammen.

topp.pack()

# Lager noe tekst med Label
tekst = tk.Label(topp)
tekst["text"] = "Bilder med Canvas"
tekst.configure(
    font = ("Aptos", 20),
    foreground="white",
    background=farge_bakgrunn,
)
tekst.pack()

# Setter inn et tegnevindu.
canvas = tk.Canvas(window,background=farge_tekst_bakgrunn)
canvas.configure(
    height=hoyde-100,
    width=bredde*0.9,
)
canvas.pack() # Skrur av at children kan endre rammen.



bilde_sol = PhotoImage(file="sol_100px.png")
bilde_siluett = PhotoImage(file="siluett_bak_skyer_100px.png")


canvas.create_image(110,110, image=bilde_sol, tags="mittBilde")


def handle_hover(kommando):
    global canvas
    # Parameter er en tuple med variablene (kodeord,event)
    # Pakker ut
    kodeord,evt = kommando
    if kodeord == "Enter":
        #bilde_siluett = PhotoImage(file="siluett.png")
        canvas.delete("mittBilde")
        canvas.create_image(110,110, image=bilde_siluett, tags="mittBilde")
    elif kodeord== "Leave":
        #bilde_sol = PhotoImage(file="sol.png")
        canvas.delete("mittBilde")
        canvas.create_image(110,110, image=bilde_sol, tags="mittBilde")
    print("Hover!")
    


# Hover-effekt ved mus
canvas.bind("<Enter>", lambda event: handle_hover(("Enter",event)))
canvas.bind("<Leave>", lambda event: handle_hover(("Leave",event)))


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

