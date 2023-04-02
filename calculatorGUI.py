# author: Jaisuraj Kaleeswaran
# date: March 6, 2023
# file: calculatorGUI.py makes a calculator GUI
# input: Expression(s) from clicking buttons on the calculator GUI
# output: Answer(s) to these expressions

# create a GUI calculator using tkinter
from tkinter import *
from calculator import calculate

def calculator(gui):   
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,= 
    b0 = addButton(gui,entrybox,'0')
    b1 = addButton(gui,entrybox,'1')
    b2 = addButton(gui,entrybox,'2')
    b3 = addButton(gui,entrybox,'3')
    b4 = addButton(gui,entrybox,'4')
    b5 = addButton(gui,entrybox,'5')
    b6 = addButton(gui,entrybox,'6')
    b7 = addButton(gui,entrybox,'7')
    b8 = addButton(gui,entrybox,'8')
    b9 = addButton(gui,entrybox,'9')
    b_add = addButton(gui,entrybox,'+')
    b_sub = addButton(gui,entrybox,'-')
    b_mult = addButton(gui,entrybox,'*')
    b_div = addButton(gui,entrybox,'/')
    b_clr = addButton(gui,entrybox,'c')
    b_eq = addButton(gui,entrybox,'=')

    # add buttons to the grid
    buttons =[ b7,    b8, b9,    b_clr, 
               b4,    b5, b6,    b_sub, 
               b1,    b2, b3,    b_add, 
               b_mult,b0, b_div, b_eq ]          
    for i in range(4):
        for j in range(4):
            buttons[i*4+j].grid(row=i+1, column=j, columnspan=1)

def addButton(gui, entrybox, value):
    return Button(gui, text=value, height=4, width=9, command = lambda: clickButton(entrybox, value))

def clickButton(entrybox, value):
    if value == '=' and entrybox.get() != '':
        value = calculate(entrybox.get())
        entrybox.delete(0, END)
        entrybox.insert(0, value)
    elif value == 'c':
        entrybox.delete(0, END)
    else:
        entrybox.insert(END, value)
    
# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator(gui)
# update the window
gui.mainloop()