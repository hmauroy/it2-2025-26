"""
Gjør bitwise operasjoner på binære tall og sjekker om bruker skriver inn riktig.
"""

from tkinter import *
import tkinter as tk

def processSelection(selectedItem):
    print(selectedItem)

def processInput():
    # 1) Read input
    # 2) Print inputs as binary
    # 3) Do operation
    # 4) Compare with users bitstring answer
    number1, number2, answer, operation = readInputs()
    result = 0
    if operation == "AND":
        result = number1 & number2
    elif operation == "OR":
        result = number1 | number2
    elif operation == "OCOMP":
        result = ~number1 & 255 # bit mask with 255 = "11111111" to remove leading bits
    elif operation == "XOR":
        result = number1 ^ number2
    elif operation == "SHIFTLEFT":
        result = number1 << 1
    elif operation == "SHIFTRIGHT":
        result = number1 >> 1
    if answer == result:
        entryAnswer["bg"] = "lawngreen"
    else:
        entryAnswer["bg"] = "tomato"
    labelNumber4["text"] = f'{result:08b}'


def readInputs():
    number1 = readInputNumber(1) 
    number2 = readInputNumber(2) 
    answer = txtAnswer.get()
    try:
        answer = int(answer,2)  # Converts from binary number stored as a string. E.g. "101" -> 5
    except ValueError as ex:
        entryAnswer.delete(0, 'end')
        entryAnswer.insert(0, 'INTEGER!')
        answer = 0
    operation = var_combobox.get()
    entryNumber1.delete(0, 'end')
    entryNumber2.delete(0, 'end')
    entryNumber1.insert(0, number1)
    entryNumber2.insert(0, number2)
    return (number1, number2, answer, operation)

def processFocusOutEvent(evt):
    entry_name = f'{evt.widget}'
    #current = window.focus_get()   # opposite: get which widget is in focus
    if entry_name == ".!frame.!frame.id01":
        number = readInputNumber(1) # Passes the id of widget to the function. Not very elegant, but it is difficult to get the id of the widget.
    elif entry_name == ".!frame.!frame.id02":
        number = readInputNumber(2) 
        

def readInputNumber(id):
    number = 0
    try:
        if id == 1:
            number = int(txtNumber1.get())
        elif id == 2:
            number = int(txtNumber2.get())
    except ValueError as ex:
        print(ex)
    # Overrides numbers if user does it wrong.
    if number > 255:
        number = 255
    elif number < 0:
        number = 0
    updateBitField(id,number)
    return number


def updateBitField(id, number):
    if id == 1:
        labelNumber1["text"] = f'{number:08b}' # prints number as 8-bit string
    elif id == 2:
            labelNumber2["text"] = f'{number:08b}'




window = Tk()   # Creates a window.
window.title("Bitwise Operation")
window.geometry("850x120")



# Frame 1
frame1 = Frame(window) 
frame1.grid(row=1, column=1)

# Frame 2
frame2 = Frame(window) 
frame2.grid(row=1, column=2)

# Frame 3
frame3 = Frame(window) 
frame3.grid(row=1, column=3)

# Deler frame 1 inn i 3 kolonner med grid
column1 = Frame(frame1,width=150)
column1.grid(row=1, column=1, sticky=W)
column2 = Frame(frame1)
column2.grid(row=1, column=2, sticky=N)
column3 = Frame(frame1)
column3.grid(row=1, column=3, sticky=E)

# Inputfelt for tall
#"Line 1"
info1 = Label(column1,text="First number, range 0-255")
txtNumber1 = StringVar()   # Lager en tekstvariabel
entryNumber1 = Entry(column1,textvariable=txtNumber1,width=3,name="id01")  # Binder Entry med tekstvariabelen.
info1.grid(row = 1, column = 1, sticky=W)
entryNumber1.grid(row = 1, column = 2)

labelNumber1 = Label(column3,text="00000000", width=8)
labelNumber1.grid(row=1, column=3)
# Binds event listener to the input field:
entryNumber1.bind("<FocusOut>", processFocusOutEvent)   # Event on focus out of entry-field.


# Line 2
info2 = Label(column1,text="Second number, range 0-255")
txtNumber2 = StringVar()   # Lager en tekstvariabel
entryNumber2 = Entry(column1,textvariable=txtNumber2,width=3, name="id02")  # Binder Entry med tekstvariabelen.
info2.grid(row = 2, column = 1, sticky=W)
entryNumber2.grid(row = 2, column = 2)

labelNumber2 = Label(column3,text="00000000", width=8)
labelNumber2.grid(row=2, column=3)
# Binds event listener to the input field:
entryNumber2.bind("<FocusOut>", processFocusOutEvent)   # Event on focus out of entry-field.

# Line 3
info3 = Label(column1,text="Your answer")
info3.grid(row = 3, column = 1, sticky=W)
txtAnswer = StringVar()   # Lager en tekstvariabel
entryAnswer = Entry(column3,textvariable=txtAnswer,width=7)  # Binder Entry med tekstvariabelen.
entryAnswer.grid(row = 3, column = 3)

# Line 4
info4 = Label(column1,text="Correct answer")
info4.grid(row = 4, column = 1, sticky=W)
labelNumber4 = Label(column3,text="00000000", width=8)
labelNumber4.grid(row=4, column=3)



# Innhold i Frame 2
# Info om at det kun er tall 1 som vil bli endret ved shiftL/shiftR og ocomp.
info_operation = Label(frame2,text="Only number 1 for SHIFTLEFT(1), SHIFTRIGHT(1) and OCOMP.", width=50)
info_operation.grid(row=1,column=1)

# Create combo menu with 6 strings
label_invisible = Label(frame2)
label_invisible.grid(row=3,column=1)
frame_combo = Frame(frame2,width=100)
frame_combo.grid(row=2,column=1)
label_invisible2 = Label(frame2)
label_invisible2.grid(row=4,column=1)
var_combobox = StringVar() # Holds value selected from combobox
var_combobox.set("OR") # initial value
comboBox = OptionMenu(frame_combo, var_combobox,  "AND", "OR", "OCOMP", "XOR", "SHIFTLEFT", "SHIFTRIGHT", command = processSelection)
comboBox.pack(fill=BOTH)

# Innhold Frame 3
# Check knapp
btnCheck = Button(frame3, text = "Check", command = processInput)
btnCheck.pack()

# Put all widgets into a list which can be processed by functions
widgets = [entryNumber1, entryNumber2, entryAnswer]




window.mainloop()