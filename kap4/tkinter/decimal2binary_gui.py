import tkinter as tk
from decimal2Binary import decimalToBinary

window = tk.Tk()
window.lift()
window.title("Desimal til binær")
window.focus_force()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)
vindu_bakgrunn = "#673357"
tekst_bakgrunn = "#ffaeae"
window.configure(background=vindu_bakgrunn)

# Setter inn en ramme (Frame)
topp = tk.Frame(window,background=tekst_bakgrunn)
topp.configure(
    height=50,
    width=bredde*0.75,
)
topp.pack_propagate(False) # Skrur av at children kan endre rammen.

topp.pack()

# Lager noe tekst med Label
overskrift = tk.Label(topp)
overskrift["text"] = "Skriv inn et heltall"
overskrift.configure(
    font = ("Aptos", 20),
    foreground="black",
    background=tekst_bakgrunn
)
overskrift.pack()

def lesKnapp():
    global input1, utskrift
    tall = int(input1.get())
    binary = decimalToBinary(tall)
    utskrift["text"] = f"{tall} = {binary}"


# Legger til et inputfelt (Entry)
input1 = tk.Entry(window)
input1.configure(
    width=30,
    font = ("Aptos", 14),
    fg="black",
    bg=tekst_bakgrunn,
    insertbackground = "black")
input1.pack()

# Knapp
knapp = tk.Button(window)
knapp.configure(
    text = "Konverter",
    command=lambda: lesKnapp()
)
knapp.pack()

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
utskrift["text"] = "Resultat..."
utskrift.configure(
    font = ("Aptos", 14),
    foreground="black",
    background=tekst_bakgrunn
)
utskrift.pack()


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

