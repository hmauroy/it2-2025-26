import tkinter as tk

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

def handle_button(kommando):
    # Parameter er en tuple med variablene (kodeord,event)
    # Pakker ut
    kodeord,event = kommando
    if kodeord == "Enter":
        event.widget.config(bg="white", fg="tomato")
    elif kodeord== "Leave":
        event.widget.config(bg="tomato", fg="white")


# Legger på events på lenken.
# Hover-effekt
lenke.bind("<Enter>", lambda event: handle_button(("Enter",event)))
lenke.bind("<Leave>", lambda event: handle_button(("Leave",event)))
# Klikk event
lenke.bind("<Button>", lambda event: print(lenke["text"]))
lenke.bind("<Double-Button>", lambda event: print("Dobbeltklikk"))
lenke.pack()

# Kjører vinduet. Må være nederst i koden.
window.mainloop()

