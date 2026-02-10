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
tekst["text"] = "tkinter pensum:"
tekst.configure(
    font = ("Aptos", 30),
    foreground="white",
    background="blue"
)
tekst.pack()

lenke = tk.Label(topp)
lenke["text"] = "https://geeksforgeeks.org/python-gui-tkinter"
lenke.configure(
    font = ("Arial", 14),
    foreground="white",
    background="tomato"
)
lenke.pack()

# Kjører vinduet. Må være nederst i koden.
window.mainloop()

