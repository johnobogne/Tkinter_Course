from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=60)
e.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

memCurrent = 0
operation = ''

def buttonClick(number) :
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + number)

def buttonClear() :
    e.delete(0, END)

def buttonAdd() :
    global memCurrent
    memCurrent = int(e.get())
    global operation
    operation = '+'
    buttonClear()

def buttonSub() :
    global memCurrent
    memCurrent = int(e.get())
    global operation
    operation = '-'
    buttonClear()

def buttonMul() :
    global memCurrent
    memCurrent = int(e.get())
    global operation
    operation = '*'
    buttonClear()

def buttonDiv() :
    global memCurrent
    memCurrent = int(e.get())
    global operation
    operation = '/'
    buttonClear()

def buttonEqual() :

    if operation == '+' :
        result = memCurrent + int(e.get())
    elif operation == '-' :
        result = memCurrent - int(e.get())
    elif operation == '*' :
        result = memCurrent * int(e.get())
    elif operation == '/' :
        result = memCurrent / int(e.get())

    buttonClear()
    e.insert(0, result)

frame = ttk.Frame(root, padding=10, width=500, height=300)
frame.grid()

button_1 = Button(frame, text='1', padx=40, pady=20, command=lambda: buttonClick('1')).grid(row=1, column=0)
button_2 = Button(frame, text='2', padx=40, pady=20, command=lambda: buttonClick('2')).grid(row=1, column=1)
button_3 = Button(frame, text='3', padx=40, pady=20, command=lambda: buttonClick('3')).grid(row=1, column=2)

button_4 = Button(frame, text='4', padx=40, pady=20, command=lambda: buttonClick('4')).grid(row=2, column=0)
button_5 = Button(frame, text='5', padx=40, pady=20, command=lambda: buttonClick('5')).grid(row=2, column=1)
button_6 = Button(frame, text='6', padx=40, pady=20, command=lambda: buttonClick('6')).grid(row=2, column=2)

button_7 = Button(frame, text='7', padx=40, pady=20, command=lambda: buttonClick('7')).grid(row=3, column=0)
button_8 = Button(frame, text='8', padx=40, pady=20, command=lambda: buttonClick('8')).grid(row=3, column=1)
button_9 = Button(frame, text='9', padx=40, pady=20, command=lambda: buttonClick('9')).grid(row=3, column=2)

button_0 = Button(frame, text='0', padx=40, pady=20, command=lambda: buttonClick('0')).grid(row=4, column=0)

button_add = Button(frame, text='+', padx=40, pady=20, command=buttonAdd).grid(row=1, column=3)
button_sub = Button(frame, text='-', padx=40, pady=20, command=buttonSub).grid(row=2, column=3)
button_mul = Button(frame, text='x', padx=40, pady=20, command=buttonMul).grid(row=3, column=3)
button_div = Button(frame, text='÷', padx=40, pady=20, command=buttonDiv).grid(row=4, column=3)

button_equal = Button(frame, text='=', padx=40, pady=20, command=buttonEqual).grid(row=4, column=2)
button_clear = Button(frame, text='AC', padx=40, pady=20, command=buttonClear).grid(row=4, column=1)

root.mainloop()
