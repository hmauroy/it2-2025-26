import tkinter as tk
from qr import *

window = tk.Tk()
window.lift()
window.title("QR-generatoren")
window.focus_force()
bredde = 500
hoyde = 600
window.minsize(bredde,hoyde)
vindu_bakgrunn = "#FFFFFF"
tekst_bakgrunn = "#ffffff"
window.configure(background=vindu_bakgrunn)
window.pack_propagate(False) # Skrur av at children kan endre størrelsen til window.


# Setter inn en ramme (Frame)
topp = tk.Frame(window)
topp.configure(
    height=50,
    width=bredde*0.75,
    background=vindu_bakgrunn,
)
topp.pack_propagate(False) # Skrur av at children kan endre rammen.
topp.pack()

# Lager noe tekst med Label
overskrift = tk.Label(topp)
overskrift["text"] = "Skriv inn tekst"
overskrift.configure(
    font = ("Aptos", 20),
    foreground="black",
    background=tekst_bakgrunn
)
overskrift.pack()

def lesKnapp():
    global input1, utskrift, canvas, bredde
    text = input1.get()
    print("Ny tekst:")
    print(f"'{text}'")
    qr.update_text(text,canvas)
    
    
    
def handle_klikk(event):
    global qr
    #print("klikket")
    x = event.x
    y = event.y
    for rad in qr.grid:
        for rute in rad:
            id = rute.isPressed(x,y,canvas)
            if id:
                l = id.split(",")
                i = int(l[0])
                j = int(l[1])
                print(f"({i},{j}),")
                #canvas.delete(rute.id)
                #rute.tegn(canvas)

def on_entry_change(*args):
    # This function is called whenever the Entry content changes
    current_value = entry_var.get()
    print(f"Entry changed to: {current_value}")
    if len(current_value) > 32:
        qr.update_text(current_value[:32],canvas)
        utskrift["text"] = f"Antall tegn igjen: 0"
    else:
        utskrift["text"] = f"Antall tegn igjen: {32-len(current_value)}"
        qr.update_text(current_value,canvas)
    

# Legger til et inputfelt (Entry)
# Lager en StringVar for å tracke inputfeltets verdi.
entry_var = tk.StringVar()
# Fester en callback-funksjon på variabelen.
entry_var.trace_add("write", on_entry_change)
# Legger til selve feltet.
input1 = tk.Entry(window,textvariable=entry_var)
input1.configure(
    width=32,
    font = ("Aptos", 14),
    fg="black",
    bg=tekst_bakgrunn,
    insertbackground = "black")
input1.pack()

# Lager utskrift der resultatet skal havne
utskrift = tk.Label()
utskrift["text"] = f"Antall tegn igjen: 0"
utskrift.configure(
    font = ("Aptos", 8),
    foreground="black",
    background=tekst_bakgrunn
)
utskrift.pack()

# Knapp
knapp = tk.Button(window)
knapp.configure(
    text = "Generer",
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


# Lager et canvas der vi kan tegne strekkodene som sorte og smale rektangler
canvas = tk.Canvas(window)
canvas.configure(
    width=bredde,
    height=hoyde-50,
    background=tekst_bakgrunn,
)
canvas.pack(expand=True)

            

canvas.bind("<Button-1>", handle_klikk)


# Here we start the program.
qr = QR_generator(text="HEI IT2!",error_correction=1,mask=0)
qr.update_code(canvas)


# Kjører vinduet. Må være nederst i koden.
window.mainloop()
