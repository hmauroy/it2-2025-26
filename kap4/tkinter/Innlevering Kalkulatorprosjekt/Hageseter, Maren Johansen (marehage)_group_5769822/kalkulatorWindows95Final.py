import tkinter as tk
from math import sqrt

window = tk.Tk()
window.lift()
window.focus_force()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)
window.configure(background = "#808080")

topp = tk.Frame(window,background = "#3d90de")
topp.configure(
    height = 50,
    width = bredde
)
topp.pack_propagate(False)
topp.pack()

tekst = tk.Label(topp)
tekst["text"] = "Calculator"
tekst.configure(
    font = ("Aptos", 15),
    foreground = "white",
    background = "#3d90de",
)
tekst.pack(anchor = "w")

hovedramme = tk.Frame(window,
    width=bredde,
    height=350,
    background="#808080"
)

input = tk.Entry(window, width=35)
input.configure(
    font=("Aptos", 15)
)
input.pack()

hovedramme.pack_propagate(False)
hovedramme.pack(fill=tk.BOTH, expand=True)

buffer_ramme = tk.Frame(hovedramme)
buffer_ramme.pack()
 
indre_ramme = tk.Frame(buffer_ramme, background="#808080")
indre_ramme.grid(row=0,column=0)

# -------------------------
# Funksjonene fra første kode
# -------------------------

stykke = ""

def regnUt():
    """Regner ut stykket når = blir trykket"""
    global stykke
    try:
        resultat = eval(stykke.replace("sqrt", "sqrt"))
        input.delete(0, tk.END)
        input.insert(0, str(resultat))
        print(f"Utregning: {stykke} = {resultat}")
        stykke = str(resultat)
    except Exception as e:
        input.delete(0, tk.END)
        input.insert(0, "Error")
        print("Feil i utregning:", e)

def lesKnapp(kommando):
    """Leser knappetrykk og oppdaterer input-feltet"""
    global stykke
    stykke = str(stykke)

    if kommando in [0,1,2,3,4,5,6,7,8,9,".", "+", "-", "*", "/", "(", ")", "sqrt"]:
        stykke += str(kommando)
        input.delete(0, tk.END)
        input.insert(0, stykke)
    elif kommando == "C":  # Clear all
        stykke = ""
        input.delete(0, tk.END)
    elif kommando == "erase":  # Backspace
        stykke = stykke[:-1]
        input.delete(0, tk.END)
        input.insert(0, stykke)
    else:
        pass

# -------------------------
# Knapper fra utseendekoden
# -------------------------

btn = tk.Button(indre_ramme, text="C", width=3, height=2, command=lambda: lesKnapp("C"))
btn1 = tk.Button(indre_ramme, text="7", width=3, height=2, command=lambda: lesKnapp(7))
btn2 = tk.Button(indre_ramme, text="8", width=3, height=2, command=lambda: lesKnapp(8))
btn3 = tk.Button(indre_ramme, text="9", width=3, height=2, command=lambda: lesKnapp(9))
btn4 = tk.Button(indre_ramme, text="4", width=3, height=2, command=lambda: lesKnapp(4))
btn5 = tk.Button(indre_ramme, text="5", width=3, height=2, command=lambda: lesKnapp(5))
btn6 = tk.Button(indre_ramme, text="6", width=3, height=2, command=lambda: lesKnapp(6))
btn7 = tk.Button(indre_ramme, text="1", width=3, height=2, command=lambda: lesKnapp(1))
btn8 = tk.Button(indre_ramme, text="2", width=3, height=2, command=lambda: lesKnapp(2))
btn9 = tk.Button(indre_ramme, text="3", width=3, height=2, command=lambda: lesKnapp(3))
btn10 = tk.Button(indre_ramme, text="0", width=3, height=2, command=lambda: lesKnapp(0))

btn11 = tk.Button(indre_ramme, text="/", width=3, height=2, command=lambda: lesKnapp("/"))
btn12 = tk.Button(indre_ramme, text="*", width=3, height=2, command=lambda: lesKnapp("*"))
btn13 = tk.Button(indre_ramme, text="-", width=3, height=2, command=lambda: lesKnapp("-"))
btn14 = tk.Button(indre_ramme, text="+", width=3, height=2, command=lambda: lesKnapp("+"))
btn15 = tk.Button(indre_ramme, text="=", width=3, height=2, command=lambda: regnUt())
btn16 = tk.Button(indre_ramme, text="sqrt", width=3, height=2, command=lambda: lesKnapp("sqrt"))
btn17 = tk.Button(indre_ramme, text="erase", width=3, height=2, command=lambda: lesKnapp("erase"))
btn18 = tk.Button(indre_ramme, text="(", width=3, height=2, command=lambda: lesKnapp("("))
btn19 = tk.Button(indre_ramme, text=")", width=3, height=2, command=lambda: lesKnapp(")"))
btn20 = tk.Button(indre_ramme, text=".", width=3, height=2, command=lambda: lesKnapp("."))

 
btn.grid(row=2, column=1)
btn1.grid(row=3, column=1)
btn2.grid(row=3, column=2)
btn3.grid(row=3, column=3)
btn4.grid(row=4, column=1)
btn5.grid(row=4, column=2)
btn6.grid(row=4, column=3)
btn7.grid(row=5, column=1)
btn8.grid(row=5, column=2)
btn9.grid(row=5, column=3)
btn10.grid(row=6, column=1)

btn11.grid(row=3, column=4)
btn12.grid(row=4, column=4)
btn13.grid(row=5, column=4)
btn14.grid(row=6, column=4)
btn15.grid(row=6, column=5)
btn16.grid(row=2, column=4)
btn17.grid(row=2, column=3)
btn18.grid(row=6, column=2)
btn19.grid(row=6, column=3)
btn20.grid(row=2, column=2)

window.mainloop()
