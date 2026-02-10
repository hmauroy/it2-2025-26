import tkinter as tk

window = tk.Tk()
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
tekst["text"] = "Resultat..."
tekst.configure(
    font = ("Aptos", 30),
    foreground="white",
    background="blue"
)
tekst.pack()

def lesKnapp(kommando):
    global tall1, tekst
    tall1 = input1.get()
    if kommando == "hilsen":
        tekst["text"] = "Hei IT2!"

# Når vi trykker på knappen endres teksten til "Hei IT2!".
pluss = tk.Button(window)
pluss.configure(
    text = "Trykk her!",
    command=lambda: lesKnapp("hilsen")
)
pluss.pack()


# Legger til et inputfelt (Entry)
input1 = tk.Entry(window, width=60)
input1.pack()


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

