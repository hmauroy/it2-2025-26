"""
Grid og knapper med tkinter
"""
import tkinter as tk


vindu=tk.Tk()
vindu.minsize(500, 500)
vindu.configure(background="grey")
 
ToppBuffer=tk.Frame(width=500, height=25, background="grey")
ToppBuffer.pack()

OutputtFelt=tk.Frame(width=250, height=25)
OutputtFelt.pack_propagate(False)
OutputtFelt.pack()
 
Bunbuffer=tk.Frame(width=500, height=25, background="grey")
Bunbuffer.pack_propagate(False)
Bunbuffer.pack()






text=tk.Label(OutputtFelt)
text["text"]=""
text.configure(anchor="e")
text.pack(fill="both", expand=True)
 
hovedramme = tk.Frame(vindu,
    width=500,
    height=350,
    background="grey"
)
 
hovedramme.pack_propagate(False)
hovedramme.pack(fill=tk.BOTH, expand=True)
 
buffer_ramme = tk.Frame(hovedramme)
buffer_ramme.pack()
 
 
Ramme=tk.Frame(buffer_ramme, background="grey")
Ramme.grid(row=0,column=0)



# 5) Knapper i grid
HøydeKnapp=3
BreddeKnapp=5
 
Knapp7=tk.Button(Ramme, text="7", width=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="blue")
Knapp7.grid(row=2, column=0)
Knapp7.configure(
    command=lambda: les_Knapp7()
)
 
Knapp8=tk.Button(Ramme, text="8", width=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="blue")
Knapp8.grid(row=2, column=1)
Knapp8.configure(
    command=lambda: les_Knapp8()
)
 
Knapp9=tk.Button(Ramme, text="9", width=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="blue")
Knapp9.grid(row=2, column=2)
Knapp9.configure(
    command=lambda: les_Knapp9()
)
 
Knapp4=tk.Button(Ramme, text="4", width=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="blue")
Knapp4.grid(row=3, column=0)
Knapp4.configure(
    command=lambda: les_Knapp4()
)
 
Knapp5=tk.Button(Ramme, text="5", width=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="blue")
Knapp5.grid(row=3, column=1)
Knapp5.configure(
    command=lambda: les_Knapp5()
)
 
Knapp6=tk.Button(Ramme, text="6", width=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="blue")
Knapp6.grid(row=3, column=2)
Knapp6.configure(
    command=lambda: les_Knapp6()
)
 
Knapp1=tk.Button(Ramme, text="1", width=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="blue")
Knapp1.grid(row=4, column=0)
Knapp1.configure(
    command=lambda: les_Knapp1()
)
 
Knapp2=tk.Button(Ramme, text="2", width=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="blue")
Knapp2.grid(row=4, column=1)
Knapp2.configure(
    command=lambda: les_Knapp2()
)
 
Knapp3=tk.Button(Ramme, text="3", width=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="blue")
Knapp3.grid(row=4, column=2)
Knapp3.configure(
    command=lambda: les_Knapp3()
)
 
Knapp0=tk.Button(Ramme, text="0", width=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="blue")
Knapp0.grid(row=5, column=1)
Knapp0.configure(
    command=lambda: les_Knapp0()
)
 
DeleKnapp=tk.Button(Ramme, text="/", widt=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="red")
DeleKnapp.grid(row=2, column=3)
DeleKnapp.configure(
    command=lambda: les_DeleKnapp("resultat")
)
 
GangeKnapp=tk.Button(Ramme, text="*", widt=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="red")
GangeKnapp.grid(row=3, column=3)
GangeKnapp.configure(
    command=lambda: les_GangeKnapp("resultat")
)
 
MinusKnapp=tk.Button(Ramme, text="-", widt=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="red")
MinusKnapp.grid(row=4, column=3)
MinusKnapp.configure(
    command=lambda: les_MinusKnapp("resultat")
)
 
PlussKnapp=tk.Button(Ramme, text="+", widt=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="red")
PlussKnapp.grid(row=5, column=2)
PlussKnapp.configure(
    command=lambda: les_PlussKnapp("resultat")
)
 
Er_lik_Knapp=tk.Button(Ramme, text="=", widt=BreddeKnapp, height=HøydeKnapp, background="grey", foreground="red")
Er_lik_Knapp.grid(row=5, column=3)
Er_lik_Knapp.configure(
    command=lambda: les_Er_lik_Knapp("resultat")
)

backspace = tk.Button(Ramme, text="Back", width=10, height=3, foreground='red',background="grey", command=lambda: les_back())
backspace.grid(row = 1, column = 0, columnspan=2, sticky="nsew")
 
Clear=tk.Button(Ramme, text="C", width=10, height=3, foreground='red',background="grey", command=lambda: les_Clear())
Clear.grid(row=1, column=2, columnspan=2, sticky="nsew")

tom=tk.Button(Ramme, text="", width=5, height=3, background="grey")
tom.grid(row=5, column=0)
 

stykke=[]






Størrelse=25
 
def les_Knapp1():
    if len(text["text"]) < Størrelse:
        text['text'] += "1"
 
def les_Knapp2():
    if len(text["text"]) < Størrelse:
        text['text'] += "2"
 
def les_Knapp3():
    if len(text["text"]) < Størrelse:
        text['text'] += "3"
 
def les_Knapp4():
    if len(text["text"]) < Størrelse:
        text['text'] += "4"
 
def les_Knapp5():
    if len(text["text"]) < Størrelse:
        text['text'] += "5"
 
def les_Knapp6():
    if len(text["text"]) < Størrelse:
        text['text'] += "6"
 
def les_Knapp7():
    if len(text["text"]) < Størrelse:
        text['text'] += "7"
 
def les_Knapp8():
    if len(text["text"]) < Størrelse:
        text['text'] += "8"
 
def les_Knapp9():
    if len(text["text"]) < Størrelse:
        text['text'] += "9"
 
def les_Knapp0():
    if len(text["text"]) < Størrelse:
        text['text'] += "0"
 



def les_PlussKnapp(kommando):
    print(stykke)
    if kommando == "resultat":
        stykke.append(text["text"])
        stykke.append("+")
        text['text'] += ' + '


def les_MinusKnapp(kommando):
    print(stykke)
    if kommando == "resultat":
        stykke.append(text["text"])
        stykke.append("-")
        text['text'] += ' - '

def les_GangeKnapp(kommando):
    print(stykke)
    if kommando == "resultat":
        stykke.append(text["text"])
        stykke.append("*")
        text['text'] += ' * '


def les_DeleKnapp(kommando):
    print(stykke)
    if kommando == "resultat":           
        stykke.append(text["text"])
        stykke.append("/")
        text['text'] += ' / '

    else:
        text["text"] = "Kan ikke dele med 0"

def les_Er_lik_Knapp(kommando):
    print(kommando)
    if kommando == "resultat":
        stykke.append(text["text"])
        print(stykke)
        svar=eval((stykke[0]) + (stykke [1]) + (stykke[2]))
        print(svar)

        
        for i in range(3, len(stykke), 2):
            svar = svar, eval((stykke[i]) + stykke[i+1]) 
        
    text["text"] = svar
    print(svar)

def les_back():
    if len(text['text']) > 0:
        text['text'] = text['text'][:-1]
 


def les_Clear():
    stykke.clear()
    text["text"]=""




vindu.mainloop()
