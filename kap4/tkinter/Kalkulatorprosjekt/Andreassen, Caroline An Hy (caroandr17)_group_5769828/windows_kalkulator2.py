import tkinter as tk

window = tk.Tk()
window.lift()
window.focus_force()
bredde = 500 # størrelse i pixler
hoyde = 500
window.minsize(bredde, hoyde)
window.configure(background="#FFFFFF") # Bruke web colors, white, black, peachpuff, maroon...
 
# 1) Lage en header boks
header = tk.Frame(window,
    width = bredde,
    height=100,
    background="#ADADAD"
)
header.pack_propagate(False) # Skrur av at children kan endre rammen.
header.pack() # Legger rammen til vinduet.

overskrift = tk.Label(
    header,
    text="Kalkulator",
    font=("Arial",25),
    background="#95C3EF",
    foreground="black", 
    pady = 5, 
    width= 50
)
overskrift.pack()
 
# Lager noe tekst med Label
tekst = tk.Label(header)
tekst["text"] = ""
tekst.configure(
    font = ("Aptos", 30),
    foreground="black",
    background="white", 
    width= 15
)
tekst.pack()
 
# 2) Lage en hovedramme der innhold skal ligge
hovedramme = tk.Frame(window,
    width=bredde,
    height=350,
    background="#ADADAD"
)
# Skrur innstillinger så både størrelse og bakgrunnsfarger til rammen ikke påvirkes av barna sine.
hovedramme.pack_propagate(False)
hovedramme.pack(fill=tk.BOTH, expand=True)
 
# 3) Lage en buffer ramme mellom pack og grid for å beholde midtstillingen
buffer_ramme = tk.Frame(hovedramme)
buffer_ramme.pack()
 
# 4) Indre ramme som legger ut med grid.
indre_ramme = tk.Frame(buffer_ramme, background="#ADADAD")
indre_ramme.grid(row=0,column=0)
 
 
# 5) Knapper og tall i grid
 
null = tk.Button(indre_ramme, text="0", width=5, height=3, command=lambda: lesKnapp("0"))
en = tk.Button(indre_ramme, text="1", width=5, height=3, command=lambda: lesKnapp("1"))
to = tk.Button(indre_ramme, text="2", width=5, height=3, command=lambda: lesKnapp("2"))
tre = tk.Button(indre_ramme, text="3", width=5, height=3, command=lambda: lesKnapp("3"))
fire = tk.Button(indre_ramme, text="4", width=5, height=3, command=lambda: lesKnapp("4"))
fem = tk.Button(indre_ramme, text="5", width=5, height=3, command=lambda: lesKnapp("5"))
seks = tk.Button(indre_ramme, text="6", width=5, height=3, command=lambda: lesKnapp("6"))
syv = tk.Button(indre_ramme, text="7", width=5, height=3, command=lambda: lesKnapp("7"))
atte = tk.Button(indre_ramme, text="8", width=5, height=3, command=lambda: lesKnapp("8"))
ni = tk.Button(indre_ramme, text="9", width=5, height=3, command=lambda: lesKnapp("9"))
 
btn1 = tk.Button(indre_ramme, text="*", width=5, height=3, command=lambda: lesKnapp("gange"))
btn2 = tk.Button(indre_ramme, text="/", width=5, height=3, command=lambda: lesKnapp("dele"))
btn3 = tk.Button(indre_ramme, text="+", width=5, height=3, command=lambda: lesKnapp("pluss"))
btn4 = tk.Button(indre_ramme, text="-", width=5, height=3, command=lambda: lesKnapp("minus"))
btn6 = tk.Button(indre_ramme, text="**", width=5, height=3, command=lambda: lesKnapp("**"))
btn9 = tk.Button(indre_ramme, text="sqrt", width=5, height=3, command=lambda: lesKnapp("sqrt"))

lik = tk.Button(indre_ramme, text="=", width=5, height=3, command=lambda: lesKnapp("="))

btn5 = tk.Button(indre_ramme, text="c", width=5, height=3, command=lambda: lesKnapp("C"))
btn8 = tk.Button(indre_ramme, text="erase", width=5, height=3, command=lambda: lesKnapp("erase"))


btn7 = tk.Button(indre_ramme, text=".", width=5, height=3, command=lambda: lesKnapp("."))
 
 
null.grid(row=3, column=1)
en.grid(row=2, column=0)
fire.grid(row=1, column=0)
syv.grid(row=0, column=0)
 
to.grid(row=2, column=1)
fem.grid(row=1, column=1)
atte.grid(row=0,column=1)
 
tre.grid(row=2, column=2)
seks.grid(row=1, column=2)
ni.grid(row=0, column=2)
 
btn1.grid(row=1, column=3)
btn2.grid(row=0, column=3)
btn3.grid(row=3, column=3)
btn4.grid(row=2, column=3)
btn5.grid(row=4, column=3)
btn6.grid(row=4, column=2)
btn7.grid(row=3, column=0)
btn8.grid(row=4, column=1)
btn9.grid(row=4, column=0)
 
lik.grid(row=3, column=2)
 
tall1 = ""
tegn = ""
 
def lesKnapp(kommando):
    global tall1, tegn
    print(kommando)
    if kommando == "C":
        tekst["text"] = ""
        tall1 = ""
        tegn = ""
        return 

    elif kommando == "pluss":
        tall1 = tekst["text"]
        print(f"Nå er tall1 lagret som '{tall1}' ")
        tekst["text"] = ""
        tegn = "+"
    elif kommando == "minus":
        tall1 = tekst["text"]
        tekst["text"] = ""
        tegn = "-"
    elif kommando == "gange":
        tall1 = tekst["text"]
        tekst["text"] = ""
        tegn = "*"
    elif kommando == "dele":
        tall1 = tekst["text"]
        tekst["text"] = ""
        tegn = "/"
    elif kommando == "**":
        tall1 = tekst["text"]
        tekst["text"] = ""
        tegn = "**"
    elif kommando == "sqrt":
        tekst["text"] != ""
        tekst["text"] = str(round(float(tekst["text"]) ** 0.5, 2))
    elif kommando == "." and "." not in tekst["text"]:
        if tekst["text"] == "":
            tekst["text"] = "0."
        else:
            tekst["text"] += "."
    elif kommando == "erase":
        tekst["text"] = tekst["text"][:-1]  
    elif kommando == "0":
        tekst["text"] += "0"
    elif kommando == "1":
        tekst["text"] += "1"
    elif kommando == "2":
        tekst["text"] += "2"
    elif kommando == "3":
        tekst["text"] += "3"
    elif kommando == "4":
        tekst["text"] += "4"
    elif kommando == "5":
        tekst["text"] += "5"
    elif kommando == "6":
        tekst["text"] += "6"
    elif kommando == "7":
        tekst["text"] += "7"
    elif kommando == "8":
        tekst["text"] += "8"
    elif kommando == "9":
        tekst["text"] += "9"
    elif kommando == "=":
        print("hei")
        print(tall1)
        tall2 = tekst["text"]
        if tegn == "+":
            tekst["text"] = float(tall1) + float(tall2)
        elif tegn == "-":
            tekst["text"] = float(tall1) - float(tall2)
        elif tegn == "/":
            tekst["text"] = float(tall1) / float(tall2)
        elif tegn == "*":
            tekst["text"] = float(tall1) * float(tall2)
        elif tegn == "**":
            tekst["text"] = float(tall1) ** float(tall2)
        elif tegn == "C":
            tekst["text"] = float(tall1) * float(tall2)
       
window.mainloop()