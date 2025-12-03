 
import tkinter as tk

window = tk.Tk()
window.lift()
window.focus_force()
bredde = 300  # størrelse i pixler
hoyde = 300
window.minsize(bredde, hoyde)
window.configure(background="#FFFFFF")  # Bruke web colors, white, black, peachpuff, maroon...

# Lage en hovedramme der innhold skal ligge
hovedramme = tk.Frame(window, width=bredde, height=350, background="grey")
hovedramme.pack_propagate(False)
hovedramme.pack(fill=tk.BOTH, expand=True)

overskrift = tk.Label(
    hovedramme,
    text="Kalkulator",
    font=("Arial", 30),
    background="grey",
    foreground="#3E3D3D",
)
overskrift.pack()

utskrift = tk.Text(hovedramme)
utskrift.configure(height=2, background="white", width=29)
utskrift.pack()

# Lage en buffer ramme mellom pack og grid for å beholde midtstillingen
buffer_ramme = tk.Frame(hovedramme)
buffer_ramme.pack()

# Indre ramme som legger ut med grid.
indre_ramme = tk.Frame(buffer_ramme, background="peachpuff")
indre_ramme.grid(row=0, column=0)

# Knapper i grid
btn0 = tk.Button(indre_ramme, text="0", width=7, height=3, command=lambda: lesKnapp(0, "tall"))
btn1 = tk.Button(indre_ramme, text="1", width=7, height=3, command=lambda: lesKnapp(1, "tall"))
btn2 = tk.Button(indre_ramme, text="2", width=7, height=3, command=lambda: lesKnapp(2, "tall"))
btn3 = tk.Button(indre_ramme, text="3", width=7, height=3, command=lambda: lesKnapp(3, "tall"))
btn4 = tk.Button(indre_ramme, text="4", width=7, height=3, command=lambda: lesKnapp(4, "tall"))
btn5 = tk.Button(indre_ramme, text="5", width=7, height=3, command=lambda: lesKnapp(5, "tall"))
btn6 = tk.Button(indre_ramme, text="6", width=7, height=3, command=lambda: lesKnapp(6, "tall"))
btn7 = tk.Button(indre_ramme, text="7", width=7, height=3, command=lambda: lesKnapp(7, "tall"))
btn8 = tk.Button(indre_ramme, text="8", width=7, height=3, command=lambda: lesKnapp(8, "tall"))
btn9 = tk.Button(indre_ramme, text="9", width=7, height=3, command=lambda: lesKnapp(9, "tall"))
btnlik = tk.Button(indre_ramme, text="=", width=7, height=3, command=lambda: lesKnapp("", "resultat"))
btnc = tk.Button(indre_ramme, text="C", width=7, height=3, command=lambda: lesKnapp("", "slett"))
btnmult = tk.Button(indre_ramme, text="*", width=7, height=3, command=lambda: lesKnapp("*", "operator"))
btnpluss = tk.Button(indre_ramme, text="+", width=7, height=3, command=lambda: lesKnapp("+", "operator"))
btnminus = tk.Button(indre_ramme, text="-", width=7, height=3, command=lambda: lesKnapp("-", "operator"))
btndele = tk.Button(indre_ramme, text="/", width=7, height=3, command=lambda: lesKnapp("/", "operator"))

# Plassere knappene i grid
btn0.grid(row=4, column=2)
btn1.grid(row=1, column=1)
btn2.grid(row=1, column=2)
btn3.grid(row=1, column=3)
btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btn7.grid(row=3, column=1)
btn8.grid(row=3, column=2)
btn9.grid(row=3, column=3)
btnc.grid(row=4, column=1)
btnlik.grid(row=4, column=3)
btnpluss.grid(row=1, column=4)
btnminus.grid(row=2, column=4)
btnmult.grid(row=3, column=4)
btndele.grid(row=4, column=4)

# Variabler
tall1_str = ""
tall2_str = ""
tall1 = 0
tall2 = 0
modus = True
operator = ""

def lesKnapp(tall, knapptype):
    global tall1_str, tall2_str, tall1, tall2, modus, operator

    if knapptype == "tall":
        if modus:  #sjekker om if modus==true
            tall1_str += str(tall)
            tall1 = float(tall1_str)
        else:  
            tall2_str += str(tall)
            tall2 = float(tall2_str)

        utskrift.delete(1.0, tk.END)  
        if modus:
            utskrift.insert(tk.END, tall1_str)  
        else:
            utskrift.insert(tk.END, tall2_str)  

    elif knapptype == "operator":
        operator = tall  
        modus = False  

    elif knapptype == "resultat":
        resultat = beregn()  
        utskrift.delete(1.0, tk.END)  
        utskrift.insert(tk.END, resultat)  
        tall1_str = ""
        tall2_str = ""
        modus = True
        operator = ""

    elif knapptype == "slett":
        
        tall1 = 0
        tall2 = 0
        modus = True
        tall1_str = ""
        tall2_str = ""
        operator = ""
        utskrift.delete(1.0, tk.END)  

def beregn():
    global tall1, tall2, operator
    if operator == "+":
        return tall1 + tall2
    elif operator == "-":
        return tall1 - tall2
    elif operator == "*":
        return tall1 * tall2
    elif operator == "/":
        if tall2 != 0:
            return tall1 / tall2
        else:
            return "Uendelig"  # Håndter deling med 0
    return "Feil"

window.mainloop()
