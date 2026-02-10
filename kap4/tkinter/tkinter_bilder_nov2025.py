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
    height=50,
    width=bredde,
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


# Lager noen bilder
bilde = PhotoImage(file="sol.png")
bilde2 = PhotoImage(file="siluett.png")
bilde3 = PhotoImage(file="siluett_bak_skyer.png")

# Setter inn et tegnevindu.
bildevindu = tk.Label(window,
                      background=farge_tekst_bakgrunn,
                      image=bilde2,
                      text="bildet mitt")
bildevindu.configure(
    height=hoyde-50,
    width=bredde*0.9,
)
bildevindu.pack()





# Kjører vinduet. Må være nederst i koden.
window.mainloop()

