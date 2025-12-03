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
    foreground="black",
    background="peachpuff"
)
tekst.pack()

def lesKnapp(kommando):
    print(kommando)
    tall1 = float(input1.get())
    tall2 = float(input2.get())
    if kommando == "pluss":
        tekst["text"] = tall1 + tall2
    elif kommando == "minus":
        tekst["text"] = tall1 - tall2
    elif kommando == "gange":
        tekst["text"] = tall1 * tall2
    elif kommando == "dele":
        tekst["text"] = tall1 / tall2

# Legger til to inputfelt (Entry)
input1 = tk.Entry(window, width=60)
input1.pack()

input2 = tk.Entry(window, width=60)
input2.pack()

# Lager knappene".
pluss = tk.Button(window)
pluss.configure(
    text = "+",
    command=lambda: lesKnapp("pluss")
)
pluss.pack()
minus = tk.Button(window)
minus.configure(
    text = "-",
    command=lambda: lesKnapp("minus")
)
minus.pack()
gange = tk.Button(window)
gange.configure(
    text = "*",
    command=lambda: lesKnapp("gange")
)
gange.pack()
dele = tk.Button(window)
dele.configure(
    text = "/",
    command=lambda: lesKnapp("dele")
)
dele.pack()


# Kjører vinduet. Må være nederst i koden.
window.mainloop()

