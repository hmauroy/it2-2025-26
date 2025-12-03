import tkinter as tk
from PIL import Image, ImageTk



window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde, hoyde)
window.configure(background="#0F0F64")

bilde = Image.open("kirkulator.jpg")
bilde = bilde.resize((700, 150))
tk_bilde = ImageTk.PhotoImage(bilde)
label = tk.Label(window, image=tk_bilde, bg="gold", bd = 12, relief="ridge")
label.pack()

topp = tk.Frame(window, bg="darkgreen", bd = 12, relief="flat")
topp.configure(
    height = 50,
    width = bredde
)
topp.pack()

overskrift = tk.Label(topp)
overskrift["text"] = "KIRKULATOR"
overskrift.configure(
    font = ("Algerian", 40),
    background = "brown"
    )
overskrift.pack()

midt = tk.Frame(window, background="#3115B0")
midt.configure(
    height = 60,
    width = 100
)
midt.pack()

hoved = tk.Frame(window, background="#59154C")
hoved.configure(
    height = 300,
    width = bredde
)
hoved.pack_propagate(False)
hoved.pack()


input1 = tk.Text(midt)
input1.configure(
    font = ("Times new roman", 32),
    height=1,
    width=20,
    background="silver"
)
input1.pack()

input1a = 0
regneart = ""

def lesKnapp(tall):
    global input1
    for i in range(10):
        if int(tall) == i:
            input1.insert(tk.END, tall)
    
    
    return input1

def lesArt(kommando):
    global input1a, regneart, input1
    regneart = kommando
    
    input1a = float(input1.get(1.0,tk.END))
    
    input1.delete(1.0, tk.END)
    
    return input1a, regneart

def rens():
    input1.delete(1.0, tk.END)

def regnUt(kommando):
    global regneart, input1
    input1b = float(input1.get(1.0, tk.END))
    input1.delete(1.0, tk.END)
    if kommando == "erlik":
        if regneart == "pluss":
            input1.insert(tk.END, (input1a + input1b))
        elif regneart == "minus":
            input1.insert(tk.END, (input1a - input1b))
        elif regneart == "gange":
            input1.insert(tk.END, (input1a * input1b))
        elif regneart == "dele":
            input1.insert(tk.END, (input1a / input1b))

knapp1 = tk.Button(hoved, text="1", height="3", width="6")
knapp1.configure(command = lambda: lesKnapp("1"))
knapp2 = tk.Button(hoved, text="2", height="3", width="6")
knapp2.configure(command = lambda: lesKnapp("2"))
knapp3 = tk.Button(hoved, text="3", height="3", width="6")
knapp3.configure(command = lambda: lesKnapp("3"))
knapp4 = tk.Button(hoved, text="4", height="3", width="6")
knapp4.configure(command = lambda: lesKnapp("4"))
knapp5 = tk.Button(hoved, text="5", height="3", width="6")
knapp5.configure(command = lambda: lesKnapp("5"))
knapp6 = tk.Button(hoved, text="6", height="3", width="6")
knapp6.configure(command = lambda: lesKnapp("6"))
knapp7 = tk.Button(hoved, text="7", height="3", width="6")
knapp7.configure(command = lambda: lesKnapp("7"))
knapp8 = tk.Button(hoved, text="8", height="3", width="6")
knapp8.configure(command = lambda: lesKnapp("8"))
knapp9 = tk.Button(hoved, text="9", height="3", width="6")
knapp9.configure(command = lambda: lesKnapp("9"))
knapp0 = tk.Button(hoved, text="0", height="3", width="6")
knapp0.configure(command = lambda: lesKnapp("0"))

pluss = tk.Button(hoved)
pluss["text"] = " + "
pluss.configure(
    command = lambda: lesArt("pluss"),
    height = 3,
    width = 6
)
pluss.pack()

minus = tk.Button(hoved)
minus["text"] = " - "
minus.configure(
    command = lambda: lesArt("minus"),
    height = 3,
    width = 6
)
minus.pack()

gange = tk.Button(hoved)
gange["text"] = " * "
gange.configure(
    command = lambda: lesArt("gange"),
    height = 3,
    width = 6
)
gange.pack()

dele = tk.Button(hoved)
dele["text"] = " / "
dele.configure(
    command = lambda: lesArt("dele"),
    height = 3,
    width = 6
)
dele.pack()

erlik = tk.Button(hoved)
erlik["text"] = " = "
erlik.configure(
    command = lambda: regnUt("erlik"),
    height = 3,
    width = 6
)
erlik.pack()

clear = tk.Button(hoved)
clear["text"] = " AC "
clear.configure(
    command = lambda: rens(),
    height = 3,
    width = 6
)
clear.pack()

knapp1.grid(row=0, column=0)
knapp2.grid(row=0, column=1)
knapp3.grid(row=0, column=2)
knapp4.grid(row=1, column=0)
knapp5.grid(row=1, column=1)
knapp6.grid(row=1, column=2)
knapp7.grid(row=2, column=0)
knapp8.grid(row=2, column=1)
knapp9.grid(row=2, column=2)
knapp0.grid(row=3, column=0)
pluss.grid(row=0, column=3)
minus.grid(row=1, column=3)
gange.grid(row=2, column=3)
dele.grid(row=3, column=3)
erlik.grid(row=3, column=2)
clear.grid(row=3, column=1)




window.mainloop()