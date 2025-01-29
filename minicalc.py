from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.title("Mini Calculator")
screen.geometry('400x400')

num0 = Label(screen, text="Number 1")
num0_e = Entry(screen)

num1 = Label(screen, text="Number 2")
num1_e = Entry(screen)


def calculate():
    a = float(num0_e.get())
    b = float(num1_e.get())

    selection = types.get()
    if selection == "+":
        print(a + b)
    elif selection == "-":
        print(a - b)
    elif selection == "x":
        print(a * b)
    elif selection == "/":
        print(a / b)


types = Combobox(screen, state='readonly')  # normal (grafei) readonly, disable(den mporei na dialexei)
types['values'] = ('+', '-', '/', 'x')
types.current(2)
types.grid()

btn = Button(screen, text="Calculate", command=calculate)

lbl = Label(screen, text="")

num0.grid(row=0, column=0)
num0_e.grid(row=0, column=1)
num1.grid(row=1, column=0)
num1_e.grid(row=1, column=1)
btn.grid(row=3, column=0)
types.grid(row=2, column=0)

btn.grid()
screen.mainloop()