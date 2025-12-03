import tkinter as tk
from skuddAar import skuddaar

window = tk.Tk()
window.lift()
window.title("Skuddårkalkulator")
window.focus_force()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)
window.configure(background="#334467")
tekst_bakgrunn = "#dddddd"

# Setter inn en ramme (Frame)
topp = tk.Frame(window,background=tekst_bakgrunn)
topp.configure(
    height=100,
    width=bredde*0.75,
)
topp.pack_propagate(False) # Skrur av at children kan endre rammen.

topp.pack()

# Lager noe tekst med Label
utskrift = tk.Label(topp)
utskrift["text"] = "Skriv inn et år"
utskrift.configure(
    font = ("Aptos", 20),
    foreground="black",
    background=tekst_bakgrunn
)
utskrift.pack()

def lesKnapp():
    global input1, utskrift
    aar = int(input1.get())
    erDetSkuddaar = skuddaar(aar)
    tekst = "er"
    if erDetSkuddaar == False:
        tekst = "er ikke"
    utskrift["text"] = f"Året {aar} {tekst} et skuddår."


# Legger til et inputfelt (Entry)
input1 = tk.Entry(window)
input1.configure(
    width=30,
    fg="black",
    bg=tekst_bakgrunn,
    insertbackground = "black")
input1.pack()

# Knapp
knapp = tk.Button(window)
knapp.configure(
    text = "Beregn skuddår",
    command=lambda: lesKnapp()
)
knapp.pack()


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

