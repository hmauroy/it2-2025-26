import tkinter as tk
from gs1_codes import lookup_gs1_code
from barcode_generator import generateBarcode

window = tk.Tk()
window.lift()
window.title("Barcode-generatoren")
window.focus_force()
bredde = 500
hoyde = 500
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
overskrift["text"] = "Skriv inn barcode-sifre."
overskrift.configure(
    font = ("Aptos", 20),
    foreground="black",
    background=tekst_bakgrunn
)
overskrift.pack()

def lesKnapp():
    """ 8711253001202 """
    global input1, utskrift, canvas, bredde
    canvas.delete("bar")
    tall_streng = str(input1.get())
    if len(tall_streng) == 0:
        tall_streng = "8711253001202"
    elif len(tall_streng) < 12:
        utskrift["text"] = "Skriv inn 12 eller 13 siffer strekkode!"
        return False
    # Plukker ut kun de 12 første sifre pga. siste blir kalkulert.
    tall_streng = tall_streng[0:12]
    binary_seq, checksum = generateBarcode(tall_streng)
    #print(binary_seq)
    x = 50
    y = 80
    dx = 3
    drawBarcode(binary_seq, checksum, tall_streng, x, y, dx)
    lag_barcode_text(tall_streng, checksum, x, y+155, dx)

def drawBarcode(binary_seq, checksum, tall_streng, x=50, y=100, dx=3):
    barcode_width = len(binary_seq) * dx
    x = int( (bredde / 2) - (barcode_width / 2) )
    teller = 0
    for code in binary_seq:
        # Sjekker om det er star, center eller end strekene som skal telles ut ifra indexene.
        if teller in [0,1,2] or teller in [44,45,46,47,48] or teller in [92,93,94]:
            dy = 155
        else:
            dy = 140
        if code == 1:
            lag_bar(x,y,dx,dy)
        else:
            lag_bar(x,y,dx,dy,"white")
        x += dx
        teller += 1
    land = lookup_gs1_code(int(tall_streng[:3]))
    if len(tall_streng) == 12:
        tall_streng += str(checksum)
    utskrift["text"] = f"Produksjonsland: {land}, {tall_streng}"
    

def lag_bar(x,y,width=3,height=140,fill="black"):
    global canvas
    #canvas.create_rectangle(x,y,x+width,y+height, fill=fill, outline="", tags="bar")
    canvas.create_polygon(
        x,y,
        x,y+height, 
        x+width,y+height, 
        x+width,y, 
        fill=fill, tags="bar")

def lag_barcode_text(tall_streng, check, x, y, dx):
    global canvas, bredde
    canvas.delete("barcode_text")
    if len(tall_streng) == 12:
        tall_streng += str(check)
    barcode_width = 95 * dx
    myFont = "Futura"
    myFont = "Helvetica"
    myFont = "Monospace"
    fontSize = 20
    x = int( (bredde / 2) - (barcode_width / 2) ) - (dx * 4)
    # Skriver teksten hvert siffer av gangen
    # Første siffer
    canvas.create_text(x,y,text=tall_streng[0],font=(myFont, fontSize), fill="black", tags="barcode_text")
    x += dx*9 + 2
    for char in tall_streng[1:7]:
        canvas.create_text(x,y,text=char,font=(myFont, fontSize), fill="black", tags="barcode_text")
        x += dx*7
    x += dx*5
    for char in tall_streng[7:]:
        canvas.create_text(x,y,text=char,font=(myFont, fontSize), fill="black", tags="barcode_text")
        x += dx*7

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

barcode_text_exist = None

"""
# Tester bar-lageren
xpos = 100
ypos = 150
for i in range(47):
    if i % 300 == 0:
        lag_bar(xpos,ypos)
        lag_bar(xpos+4,ypos)
        lag_bar(xpos+6,ypos)
        continue
    lag_bar(xpos,ypos)
    xpos += 4
"""

# Kjører vinduet. Må være nederst i koden.
window.mainloop()
