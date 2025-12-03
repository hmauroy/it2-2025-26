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
# Importerer omstokket_teskt() funksjonen fra filen omstokkeren.py
from omstokkeren import omstokket_tekst

window = tk.Tk()
window.lift()
window.focus_force()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)
window.configure(background="#334467")

# Setter inn en ramme (Frame)
topp = tk.Frame(window,background="#dddddd")
topp.configure(
    height=100,
    width=bredde*0.75,
)
topp.pack_propagate(False) # Skrur av at children kan endre rammen.

topp.pack()

# Lager noe tekst med Label
tekst = tk.Label(topp)
tekst["text"] = "Omstokkeren"
tekst.configure(
    font = ("Aptos", 30),
    foreground="white",
    background="deeppink"
)
tekst.pack()

def lesKnapp():
    global utskrift
    # 1) Les inn teksten.
    # 2) Stokk om
    # 3) Vis teksten
    tekst1 = input1.get(1.0,tk.END)
    omstokket = omstokket_tekst(tekst1)
    # Slett alle tegn fra og med det første tegnet på 0. linje.
    utskrift.delete("1.0", tk.END) # "1.0" refers to the first character of the first line
    utskrift.insert(tk.END, omstokket + "\n")

# Når vi trykker på knappen endres teksten til "Hei IT2!".
knapp = tk.Button(window)
knapp["text"] = "Vis resultat"
knapp.configure(
    command=lambda: lesKnapp()
)
knapp.pack()

# Legger til et inputfelt (Entry)
input1 = tk.Text(window,
                   width=45,
                   height=5, 
                   bg="#93f786", fg="black",
                   selectbackground="deeppink", 
                   selectforeground="black",
                   font=("Comic Sans MS", 14),)
input1.pack()

# Legger til et utskriftsvindu med en ny Entry
utskrift = tk.Text(window,
                   width=45,
                   height=15, 
                   bg="#ff3c3c", fg="black",
                   selectbackground="deeppink", 
                   selectforeground="black",
                   font=("Comic Sans MS", 14),)
utskrift.pack()


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

