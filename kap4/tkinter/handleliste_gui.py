"""
	• Entry-felt der bruker skriver inn dagligvarer.
	• Knapp for å legge til varen.
	• Utskrift av handlelisten skjer i et Text()-felt. 
	• Tekstfultet får en ny linje for hver nye vare som legges inn.
		○ tekstfelt.insert(tk.END,varenavn) vil legge til varenavnet rett etter siste tegn som allerede finnes i tekstfeltet. 
        Du kan derfor legge til linjeskift etter hver vare som leggest til:
        tekstfelt.insert(tk.END, varenavn + "\n")
"""

import tkinter as tk

window = tk.Tk()
window.lift()
window.focus_force()
window.title("Handleliste")
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)
vindu_bakgrunn = "#5F64B0"
tekst_bakgrunn = "#aee0ff"
window.configure(background=vindu_bakgrunn)

# Setter inn en ramme (Frame)
topp = tk.Frame(window,background=tekst_bakgrunn)
topp.configure(
    height=100,
    width=bredde*0.75,
)
topp.pack_propagate(False) # Skrur av at children kan endre rammen.

topp.pack()

# Lager noe tekst med Label
overskrift = tk.Label(topp)
overskrift["text"] = "Skriv inn vare og antall"
overskrift.configure(
    font = ("Aptos", 20),
    foreground="black",
    background=tekst_bakgrunn
)
overskrift.pack()

def lesKnapp():
    global input1, utskrift
    vare = input1.get()
    antall = input2.get()
    utskrift.insert(tk.END, f"{vare}: {antall} \n")

# En overskrift for input
underoverskrift1 = tk.Label(window)
underoverskrift1["text"] = "Vare"
underoverskrift1.configure(
    font = ("Aptos", 14),
    foreground="black",
    background=tekst_bakgrunn
)
underoverskrift1.pack()


# Legger til et inputfelt (Entry)
input1 = tk.Entry(window)
input1.configure(
    width=30,
    fg="black",
    bg=tekst_bakgrunn,
    insertbackground = "black",)
input1.pack()

# En overskrift for input 2
underoverskrift2 = tk.Label(window)
underoverskrift2["text"] = "Antall"
underoverskrift2.configure(
    font = ("Aptos", 14),
    foreground="black",
    background=tekst_bakgrunn
)
underoverskrift2.pack()


# Legger til et inputfelt (Entry)
input2 = tk.Entry(window)
input2.configure(
    width=30,
    fg="black",
    bg=tekst_bakgrunn,
    insertbackground = "black",)
input2.pack()

# Knapp
knapp = tk.Button(window)
knapp.configure(
    text = "Legg til",
    command=lambda: lesKnapp()
)
knapp.pack()

# Legger til et utskriftsvindu med en ny Entry
utskrift = tk.Text(window,
                   width=45,
                   height=15, 
                   bg=tekst_bakgrunn, fg="black",
                   selectbackground="deeppink", 
                   selectforeground="black",
                   font=("Comic Sans MS", 14),)
utskrift.pack()




# Kjører vinduet. Må være nederst i koden.
window.mainloop()

