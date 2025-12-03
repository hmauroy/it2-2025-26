import tkinter as tk
import math
window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde, hoyde)
window.configure(background = "#FFFFFF")
 
# Setter inn en ramme
header = tk.Frame(window)
header.configure(
    background="#5d00ff",
    height=100,
    width=bredde
)
header.pack_propagate(False)
header.pack()
 
#Skjerm
skjerm = tk.Frame(header, background = "#FFFFFF", height = 50, width = 400)
skjerm.pack(pady = 25)
 
#skjerm tekst
utskrift = tk.Label(skjerm, font = ("Aptos", 30), height = 50, width = 20, foreground = "black")
utskrift["text"] = ""
utskrift.pack()
 
# Setter inn en ramme
hovedramme = tk.Frame(window)
hovedramme.configure(
    background = "#B4AEAE",
    height=350,
    width=bredde
)
hovedramme.pack_propagate(False)
hovedramme.pack(fill = tk.BOTH, expand = True)
 
#Buffer
buffer_ramme = tk.Frame(hovedramme)
buffer_ramme.configure(
    background = "#B4AEAE"
)
buffer_ramme.pack()
 
#Indre øvre ramme
ovre_ramme = tk.Frame(buffer_ramme, background = "#B4AEAE")
ovre_ramme.grid(row=0,column=0)
 
#Indre ramme
indre_ramme = tk.Frame(buffer_ramme, background = "#B4AEAE")
indre_ramme.grid(row=1,column=0)
 
 
#Input
 
#Over
 
 
#hoyde og bredde
btn_width = 8
btn_height = 4

def resett(start):
    global regne, ce_flag 
    ce_flag = True
    if start == 'start':
        utskrift['text'] = ''
        regne = []

ce_flag = True
def CE(ce):
    global regne, ce_flag
    if ce_flag == True:
        ce_flag = False
        if ce == 'ce':
            for i in range(len(regne)):
                if regne[i] == '*' or regne[i] == '+' or regne[i] == '/' or regne[i] == '-' or regne[i] == 'sqrt' or regne[i]=="%":
                    regne = regne[0:i+1]
                    utskrift['text'] = regne[0:i+1]
                    print(regne)
                    return


#Rad 0
btn_backspace = tk.Button(ovre_ramme, text = "Backspace", width = 13, height = btn_height)
btn_ce = tk.Button(ovre_ramme, text = "CE", width = 13, height = btn_height, command= lambda: CE('ce'))
btn_c = tk.Button(ovre_ramme, text = "C", width = 13, height = btn_height, command= lambda: resett('start'))
 
btn_backspace.grid(row=1,column=4,padx = (120,2), pady = (5,3))
btn_ce.grid(row=1,column=5,padx = 2, pady = (5,3))
btn_c.grid(row=1,column=6,padx = 2, pady = (5,3))
 
 
 
#Rad 1  
btn_mc = tk.Button(indre_ramme, text = "MC", width = btn_width, height = btn_height, command = lambda: lesKnapp("mc"))
btn7 = tk.Button(indre_ramme, text = "7", width = btn_width, height = btn_height, command = lambda: lesKnapp("syv"))
btn8 = tk.Button(indre_ramme, text = "8", width = btn_width, height = btn_height, command = lambda: lesKnapp("åtte"))
btn9 = tk.Button(indre_ramme, text = "9", width = btn_width, height = btn_height, command = lambda: lesKnapp("ni"))
btn_dele = tk.Button(indre_ramme, text = "/", width = btn_width, height = btn_height, command = lambda: lesKnapp("dele"))
btn_sqrt = tk.Button(indre_ramme, text = "sqrt", width = btn_width, height = btn_height, command = lambda: lesKnapp("sqrt"))
 
btn_mc.grid(row=2,column=1, padx = (0,15), pady = 3)
btn7.grid(row=2,column=2, padx = 2)
btn8.grid(row=2,column=3,padx = 2)
btn9.grid(row=2,column=4,padx = 2)
btn_dele.grid(row=2,column=5, padx = 2)
btn_sqrt.grid(row=2,column=6, padx = (2,0))
 
 
#Rad 2
btn_mr = tk.Button(indre_ramme, text = "MR", width = btn_width, height = btn_height, command = lambda: lesKnapp("mr"))
btn4 = tk.Button(indre_ramme, text = "4", width = btn_width, height = btn_height, command = lambda: lesKnapp("fire"))
btn5 = tk.Button(indre_ramme, text = "5", width = btn_width, height = btn_height, command = lambda: lesKnapp("fem"))
btn6 = tk.Button(indre_ramme, text = "6", width = btn_width, height = btn_height, command = lambda: lesKnapp("seks"))
btn_gange = tk.Button(indre_ramme, text = "*", width = btn_width, height = btn_height, command = lambda: lesKnapp("gange"))
btn_prosent = tk.Button(indre_ramme, text = "%", width = btn_width, height = btn_height, command = lambda: lesKnapp("prosent"))
 
btn_mr.grid(row=3,column=1, padx = (0,15), pady = 3)
btn4.grid(row=3,column=2)
btn5.grid(row=3,column=3)
btn6.grid(row=3,column=4)
btn_gange.grid(row=3,column=5)
btn_prosent.grid(row=3,column=6, padx = (2,0))
 
#Rad 3
btn_ms = tk.Button(indre_ramme, text = "MS", width = btn_width, height = btn_height, command = lambda: lesKnapp("ms"))
btn1 = tk.Button(indre_ramme, text = "1", width = btn_width, height = btn_height, command = lambda: lesKnapp("en"))
btn2 = tk.Button(indre_ramme, text = "2", width = btn_width, height = btn_height, command = lambda: lesKnapp("to"))
btn3 = tk.Button(indre_ramme, text = "3",   width = btn_width, height = btn_height, command = lambda: lesKnapp("tre"))
btn_minus = tk.Button(indre_ramme, text = "-", width = btn_width, height = btn_height, command = lambda: lesKnapp("minus"))
btn_minusopphoyd = tk.Button(indre_ramme, text = "1/x", width = btn_width, height = btn_height, command = lambda: lesKnapp("minusopphoyd"))
 
btn_ms.grid(row=4,column=1, padx = (0,15), pady = 3)
btn1.grid(row=4,column=2)
btn2.grid(row=4,column=3)
btn3.grid(row=4,column=4)
btn_minus.grid(row=4,column=5)
btn_minusopphoyd.grid(row=4,column=6, padx = (2,0))
 
#Rad 4
btn_mpluss = tk.Button(indre_ramme, text = "M+", width = btn_width, height = btn_height, command = lambda: lesKnapp("mpluss"))
btn0 = tk.Button(indre_ramme, text = "0", width = btn_width, height = btn_height, command = lambda: lesKnapp("null"))
btn_noe = tk.Button(indre_ramme, text = "", width = btn_width, height = btn_height)
btn_komma = tk.Button(indre_ramme, text = ",", width = btn_width, height = btn_height, command = lambda: lesKnapp("komma"))
btn_pluss = tk.Button(indre_ramme, text = "+", width = btn_width, height = btn_height, command = lambda: lesKnapp("pluss"))
btn_lik = tk.Button(indre_ramme, text = "=", width = btn_width, height = btn_height, command = lambda: lesKnapp("lik"))
 
btn_mpluss.grid(row=5,column=1, padx = (0,15), pady = 3)
btn0.grid(row=5,column=2)
btn_noe.grid(row=5,column=3)
btn_komma.grid(row=5,column=4)
btn_pluss.grid(row=5,column=5)
btn_lik.grid(row=5,column=6, padx = (2,0))
 
#Liste for utregning


           
regne = []
 
def lesKnapp(kommando):
    global ce_flag
    if ce_flag == False:
        ce_flag = True
    if kommando == "en":
        regne.append(1)
        utskrift["text"] += str(1)
    elif kommando == "to":
        regne.append(2)
        utskrift["text"] += str(2)
    elif kommando == "tre":
        regne.append(3)
        utskrift["text"] += str(3)
    elif kommando == "fire":
        regne.append(4)
        utskrift["text"] += str(4)
    elif kommando == "fem":
        regne.append(5)
        utskrift["text"] += str(5)
    elif kommando == "seks":
        regne.append(6)
        utskrift["text"] += str(6)
    elif kommando == "syv":
        regne.append(7)
        utskrift["text"] += str(7)
    elif kommando == "åtte":
        regne.append(8)
        utskrift["text"] += str(8)
    elif kommando == "ni":
        regne.append(9)
        utskrift["text"] += str(9)
    elif kommando == "null":
        regne.append(0)
        utskrift["text"] += str(0)
 
    elif kommando == "pluss":
        regne.append("+")
        utskrift["text"] += " + "
    elif kommando == "minus":
        regne.append("-")
        utskrift["text"] += " - "
    elif kommando == "gange":
        regne.append("*")
        utskrift["text"] += " * "
    elif kommando == "dele":
        regne.append("/")
        utskrift["text"] += " / "
    elif kommando == "prosent":
        regne.append("%")
        utskrift["text"]+="%"
    elif kommando == "sqrt":
        regne.append("sqrt")
        utskrift["text"]+="sqrt"
    elif kommando == "minusopphoyd":
        regne.append("^")
        utskrift["text"]+="^-1"
   

    
    if kommando == "lik":
        utskrift["text"]=regnUt(regne)



def regnUt(verdi):
    tall1: str=""
    tall2: str=""
    tall: str=""
    listeTall=[]
    listeOperator=[""]
    operator: str=""
    summ =0
    for i in range(len(verdi)):
        if verdi[i] == "+":
            listeTall.append(tall)
            tall=""
            listeOperator.append("+")
        elif verdi[i] == "-":
            listeTall.append(tall)
            tall=""
            listeOperator.append("-")
        elif verdi[i] == "*":
            listeTall.append(tall)
            tall=""
            listeOperator.append("*") 
        elif verdi[i] == "/":
            listeTall.append(tall)
            listeOperator.append("/")
        elif verdi [i] == "%":
            listeTall.append(tall)
            tall=""
            listeOperator.append("%")
        elif verdi [i] == "":
            listeTall.append(tall)
            tall=""
            listeOperator.append("%")
        elif verdi [i] == "^":
            listeTall.append(tall)
            tall=""
            listeOperator.append("^")
        else: 
            tall= str(tall) + str(verdi[i])
          
    listeTall.append(tall) 
    print(listeOperator)
    print(listeTall)
    summ=listeTall[0]
    

    for j in range(1, len(listeOperator)):    
        if listeOperator[j]=="+":
            summ = int(summ) + int(listeTall[j])
        if listeOperator[j]=="-":
            summ = int(summ) - int(listeTall[j])
        if listeOperator[j]=="*":
            summ = int(summ) * int(listeTall[j])
        if listeOperator[j]=="/":
            summ = int(summ) / int(listeTall[j])
        if listeOperator[j]=="%":
            return (int(summ)/int(tall1[j]))*100 , "%"
        if listeOperator[j]=="^":
            summ = (int(summ) **-1)
    return summ





 
 
window.mainloop()