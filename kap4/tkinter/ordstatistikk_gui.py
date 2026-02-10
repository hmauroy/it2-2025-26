"""
Lage en app der man kan lime inn en lengre tekst som så analyseres for ordstatistikk.
De 10 mest forekomne ordene skal vises i et Text()-felt med antall forekomster. 
Hint: Tesultatet av analysen kan til slutt være en sortert 2D-liste med de 10 mest forekomne ordene
[["banan",25], ["eple",13], ["appelsin",10] …]
vil det være enkelt å skrive ut til Text()-feltet via en tekst-streng.
Hint 2: Konstruer en tekst-streng der du legger inn navn på frukt og deretter antall forekomster og så et linje skift med tegnene \n
tekst = "banan" + str(25) + \n
Tekstvariabelen kan så settes direkte inn i Text()-feltet.
)
"""


import tkinter as tk

window = tk.Tk()
window.lift()
window.focus_force()
bredde = 500
hoyde = 500
window.minsize(bredde,hoyde)
window.configure(background="#334467")

# Setter inn en ramme (Frame)
topp = tk.Frame(window,background="#dddddd")
topp.configure(
    height=100,
    width=bredde*0.75,
)
topp.pack_propagate(False) # Skrur av at children kan endre rammen.

topp.pack()

# Lager noe tekst med Label
tekst = tk.Label(topp)
tekst["text"] = "Ordanalyse"
tekst.configure(
    font = ("Aptos", 30),
    foreground="white",
    background="deeppink"
)
tekst.pack()

def sorterOrdbok(ordbok):
    sorted_items = sorted(ordbok.items(), key=lambda x: x[1])
    # Reverserer pga sortert i stigende rekkefølge
    sorted_items.reverse()
    # Convert back to dictionary (Python 3.7+ maintains insertion order)
    return dict(sorted_items)

def statistikkTekst(tekst):
    liste = tekst.split()
    statistikk = {}
    for ord in liste:
        if ord in statistikk:
            statistikk[ord] += 1
        else:
            # Legger til ordet med forekomst 1 hvis det ikke finnes i statistikk-ordboken. 
            statistikk[ord] = 1
    return sorterOrdbok(statistikk)

def analyserStatistikk(ordbok):
    sortert_synkende = []
    teller = 0
    for ord,verdi in ordbok.items():
        sortert_synkende.append([ord,verdi])
        teller += 1
        if teller >= 10:
            break
    return sortert_synkende


def konstruerTekst(liste):
    str1 = "De ti mest forekomne ordene: \n"
    for ordTuple in liste:
        str1 += ordTuple[0] + " " + str(ordTuple[1]) + "\n"
    
    return str1


    

def lesKnapp():
    # Legger henvisning til de globale variablene
    global utskrift, input1
    tekst1 = input1.get(1.0,tk.END)
    # Finner antall forekomster for hvert ord.
    statistikk = statistikkTekst(tekst1)
    # Trekker ut de 10 mest forekomne ordene
    ti_mest_forekomne_ord = analyserStatistikk(statistikk)
    # Lager en tekststreng som kan limes rett inn i utskriftsvinduet.
    tekst_utskrift = konstruerTekst(ti_mest_forekomne_ord)
    # Slett alle tegn fra og med det første tegnet på 0. linje.
    utskrift.delete("1.0", tk.END) # "1.0" refers to the first character of the first line
    utskrift.insert(tk.END, tekst_utskrift)


# Legger til et inputfelt (Entry)
input1 = tk.Text(window,
                width=45,
                height=5, 
                bg="white", fg="black",
                selectbackground="deeppink", 
                selectforeground="black",
                font=("Comic Sans MS", 14),)
input1.pack()

knapp = tk.Button(window)
knapp["text"] = "Analyser"
knapp.configure(
    command=lambda: lesKnapp()
)
knapp.pack()

# Legger til et utskriftsvindu med en ny Entry
utskrift = tk.Text(window,
                   width=45,
                   height=15, 
                   bg="white", fg="black",
                   selectbackground="deeppink", 
                   selectforeground="black",
                   font=("Comic Sans MS", 14),)
utskrift.pack()


# Kjører vinduet. Må være nederst i koden.
window.mainloop()





