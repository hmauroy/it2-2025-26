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
    # Gjør om te
    qr.text_to_bits(input1.get())
    
def handle_klikk(event):
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


# Legger til et inputfelt (Entry)
input1 = tk.Entry(window)
input1.configure(
    width=12,
    font = ("Aptos", 14),
    fg="black",
    bg=tekst_bakgrunn,
    insertbackground = "black")
input1.pack()

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


# Lager utskrift der resultatet skal havne
utskrift = tk.Label()
utskrift["text"] = "Resultat..."
utskrift.configure(
    font = ("Aptos", 14),
    foreground="black",
    background=tekst_bakgrunn
)
utskrift.pack()


# Lager et canvas der vi kan tegne strekkodene som sorte og smale rektangler
canvas = tk.Canvas(window)
canvas.configure(
    width=bredde,
    height=hoyde-50,
    background=tekst_bakgrunn,
)
canvas.pack(expand=True)

            

canvas.bind("<Button-1>", handle_klikk)

qr = QR_generator(text="Henrik Charlsen Mauroy",error_correction=1,mask=0)
qr.drawGrid(canvas)
qr.drawDefaultCode(canvas)
qr.create_format_string()
print(f"format_string error corrected: {qr.mask_format_string()}")
qr.draw_format_string(canvas)
#qr.drawDataRedSquares(canvas,window)
qr.draw_data(canvas,window)
qr.drawMask0(canvas)
print(qr.bitstream)



# Kjører vinduet. Må være nederst i koden.
window.mainloop()
