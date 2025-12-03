import tkinter as tk
 
window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde, hoyde)
window.configure(background = "#bab9b6")
 
# Setter inn en ramme
header = tk.Frame(window)
header.configure(
    background="#bab9b6",
    height=100,
    width=bredde,
   
)
header.pack_propagate(False)
header.pack()
 
inputLabel = tk.Label(window, text="", font=("Aptos", 20), bg="white", width=27, anchor="w")
inputLabel.pack(pady=10)
tekst = tk.Label(header)
tekst["text"] =  "Calc"
tekst.configure(
    font = ("Aptos", 10),
    foreground = "white",
    background = "blue",
    width=500,
    height=150
)
tekst.pack(pady=25)
# Setter inn en ramme
hovedramme = tk.Frame(window)
hovedramme.configure(
    background="#bab9b6",
    height=350,
    width=bredde
   
)
hovedramme.pack_propagate(False)
hovedramme.pack(fill = tk.BOTH, expand=True)
 
 
 
#Buffer
buffer_ramme = tk.Frame(hovedramme)
buffer_ramme.pack()
 
 
indre_ramme = tk.Frame(buffer_ramme, background="#bab9b6")
indre_ramme.grid(row=0,column=0,ipadx=100)
 
 
   
 
 
utskrift = tk.Label(indre_ramme, text="", font=("Aptos", 20), bg="#bab9b6", fg="black", width=25, anchor="w")
utskrift.grid(row=8, column=0, columnspan=9, pady=10)
 
 
uttrykk = ""
 
def lesKnapp(kommando):
    global uttrykk
    if kommando == "=":
        uttrykk = str(eval(uttrykk))
        inputLabel["text"] = uttrykk
    elif kommando == "backspace":
        uttrykk = uttrykk[:-1]
        inputLabel["text"] = uttrykk
    elif kommando == "C":
        uttrykk = ""
        inputLabel["text"] = ""
    elif kommando == "CE":
       
        uttrykk = ""
        inputLabel["text"] = ""
    elif kommando == "MC":
        """"""
    elif kommando == "MR":
        """"""
    elif kommando == "MS":
        """"""
    elif kommando == "M+":
        """"""
    elif kommando == "1":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "2":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "3":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "4":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "5":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "6":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "7":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "8":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "9":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "+":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "-":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == ".":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "*":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "/":
        uttrykk += kommando
        inputLabel["text"] = uttrykk
    elif kommando == "sqrt":
        uttrykk = str(eval(uttrykk) ** 0.5)
        inputLabel["text"] = uttrykk
    elif kommando == "1/x":
        uttrykk = str(1 / eval(uttrykk))
        inputLabel["text"] = uttrykk
    elif kommando == "%":
        uttrykk = str(eval(uttrykk) / 100)
        inputLabel["text"] = uttrykk
    elif kommando == "+/-":
        uttrykk = str(eval(uttrykk) * -1)
        inputLabel["text"] = uttrykk
 
 
#Knapper i Grid
btnBackspace = tk.Button(indre_ramme, width = 3, height = 3, command=lambda: lesKnapp("backspace"), background="#bab9b6", foreground="red")
btnBackspace = tk.Button(indre_ramme, text = "Backspace", width = 7, height = 2, command=lambda: lesKnapp("backspace"), background="#bab9b6", foreground="red")
btnCE = tk.Button(indre_ramme, text = "CE", width = 6, height = 2,command=lambda: lesKnapp("CE"), background="#bab9b6", foreground="red")
btnC = tk.Button(indre_ramme, text = "C", width = 6, height = 2,command=lambda: lesKnapp("C"), background="#bab9b6", foreground="red")
btnMC = tk.Button(indre_ramme, text = "MC", width = 3, height = 3,command=lambda: lesKnapp("MC"), background="#bab9b6", foreground="red")
btnSyv = tk.Button(indre_ramme, text = "7", width = 3, height = 3,command=lambda: lesKnapp("7"), background="#bab9b6", foreground="blue")
btnAatte = tk.Button(indre_ramme, text = "8", width = 3, height = 3,command=lambda: lesKnapp("8"), background="#bab9b6", foreground="blue")
btnNi = tk.Button(indre_ramme, text = "9", width = 3, height = 3,command=lambda: lesKnapp("9"), background="#bab9b6", foreground="blue")
btnDele = tk.Button(indre_ramme, text = "/", width = 3, height = 3,command=lambda: lesKnapp("/"), background="#bab9b6", foreground="red")
btnRot = tk.Button(indre_ramme, text = "sqrt", width = 3, height = 3,command=lambda: lesKnapp("sqrt"), background="#bab9b6", foreground="blue")
btnMR = tk.Button(indre_ramme, text = "MR", width = 3, height = 3,command=lambda: lesKnapp("MR"), background="#bab9b6", foreground="red")
btnFire = tk.Button(indre_ramme, text = "4", width = 3, height = 3,command=lambda: lesKnapp("4"), background="#bab9b6", foreground="blue")
btnFem = tk.Button(indre_ramme, text = "5", width = 3, height = 3,command=lambda: lesKnapp("5"), background="#bab9b6", foreground="blue")
btnSeks = tk.Button(indre_ramme, text = "6", width = 3, height = 3,command=lambda: lesKnapp("6"), background="#bab9b6", foreground="blue")
btnGange = tk.Button(indre_ramme, text = "*", width = 3, height = 3,command=lambda: lesKnapp("*"), background="#bab9b6", foreground="red")
btnModulus = tk.Button(indre_ramme, text = "%", width = 3, height = 3,command=lambda: lesKnapp("%"), background="#bab9b6", foreground="blue")
btnMS = tk.Button(indre_ramme, text = "MS", width = 3, height = 3,command=lambda: lesKnapp("MS"), background="#bab9b6", foreground="red")
btnEn = tk.Button(indre_ramme, text = "1", width = 3, height = 3,command=lambda: lesKnapp("1"), background="#bab9b6", foreground="blue")
btnTo = tk.Button(indre_ramme, text = "2", width = 3, height = 3,command=lambda: lesKnapp("2"), background="#bab9b6", foreground="blue")
btnTre = tk.Button(indre_ramme, text = "3", width = 3, height = 3,command=lambda: lesKnapp("3"), background="#bab9b6", foreground="blue")
btnMinus = tk.Button(indre_ramme, text = "-", width = 3, height = 3,command=lambda: lesKnapp("-"), background="#bab9b6", foreground="red")
btn1overx = tk.Button(indre_ramme, text = "1/x", width = 3, height = 3,command=lambda: lesKnapp("1/x"), background="#bab9b6", foreground="blue")
btnMpluss = tk.Button(indre_ramme, text = "M+", width = 3, height = 3,command=lambda: lesKnapp("M+"), background="#bab9b6", foreground="red")
btnNull = tk.Button(indre_ramme, text = "0", width = 3, height = 3,command=lambda: lesKnapp("0"), background="#bab9b6", foreground="blue")
btnPlussminus = tk.Button(indre_ramme, text = "+/-", width = 3, height = 3,command=lambda: lesKnapp("+/-"), background="#bab9b6", foreground="red")
btnKomma = tk.Button(indre_ramme, text = ".", width = 3, height = 3,command=lambda: lesKnapp("."), background="#bab9b6", foreground="red")
btnPluss = tk.Button(indre_ramme, text = "+", width = 3, height = 3,command=lambda: lesKnapp("+"), background="#bab9b6", foreground="red")
btnErlik = tk.Button(indre_ramme, text = "=", width = 3, height = 3,command=lambda: lesKnapp("="), background="#bab9b6", foreground="red")
 
 
btnBackspace.grid(row=2,columnspan=8,column=0)
btnCE.grid(row=2,columnspan=5,column=4)
btnC.grid(row=2,columnspan=5,column=7)
btnMC.grid(row=3,column=3,pady=5)
btnSyv.grid(row=3,column=4)
btnAatte.grid(row=3,column=5)
btnNi.grid(row=3,column=6)
btnDele.grid(row=3,column=7)
btnRot.grid(row=3,column=8)
btnMR.grid(row=4,column=3,pady=5)
btnFire.grid(row=4,column=4)
btnFem.grid(row=4,column=5)
btnSeks.grid(row=4,column=6)
btnGange.grid(row=4,column=7)
btnModulus.grid(row=4,column=8)
btnMS.grid(row=5,column=3,pady=5)
btnEn.grid(row=5,column=4)
btnTo.grid(row=5,column=5)
btnTre.grid(row=5,column=6)
btnMinus.grid(row=5,column=7)
btn1overx.grid(row=5,column=8)
btnMpluss.grid(row=6,column=3,pady=5)
btnNull.grid(row=6,column=4)
btnPlussminus.grid(row=6,column=5)
btnKomma.grid(row=6,column=6)
btnPluss.grid(row=6,column=7)
btnErlik.grid(row=6,column=8)
 
 
 
 
 
 
 
 
window.mainloop()