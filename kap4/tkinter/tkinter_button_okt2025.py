import tkinter as tk

window = tk.Tk()
window.lift()
window.title("Knapp")
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
tekst["text"] = "Resultat..."
tekst.configure(
    font = ("Aptos", 30),
    foreground="white",
    background="blue"
)
tekst.pack()

def lesKnapp(knapp):
    tekst["text"] = "Hei IT2!"
    tekst.configure(
        foreground="blue",
        background="white"
    )
    knapp["text"] = "Trykket!"
    

# Når vi trykker på knappen endres teksten til "Hei IT2!".
knapp = tk.Button(window)
knapp["text"] = "Click Me Plz!"
knapp.configure(
    command=lambda: lesKnapp(knapp)
)
knapp.pack()

# Kjører vinduet. Må være nederst i koden.
window.mainloop()

