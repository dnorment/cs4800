from tkinter import *

def buttonPress(symbol, expr):
    if expr.get() == "Error":
        expr.set(symbol)
    else:
        expr.set(expr.get() + symbol)

def evaluate(expr):
    try:
        expr.set(str(eval(expr.get())))
    except:
        expr.set("Error")

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("CS 4800 Calculator")

    expr = StringVar()
    exprEntry = Entry(root, textvariable=expr, justify='right', width=50)

    button1 = Button(root, text='1', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('1', expr))
    button2 = Button(root, text='2', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('2', expr))
    button3 = Button(root, text='3', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('3', expr))
    button4 = Button(root, text='4', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('4', expr))
    button5 = Button(root, text='5', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('5', expr))
    button6 = Button(root, text='6', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('6', expr))
    button7 = Button(root, text='7', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('7', expr))
    button8 = Button(root, text='8', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('8', expr))
    button9 = Button(root, text='9', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('9', expr))
    button0 = Button(root, text='0', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('0', expr))
    buttonAdd = Button(root, text='+', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('+', expr))
    buttonSub = Button(root, text='-', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('-', expr))
    buttonMul = Button(root, text='*', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('*', expr))
    buttonDiv = Button(root, text='/', fg='black', bg='lightgrey', height=2, width=10,
        command=lambda: buttonPress('/', expr))
    buttonEq = Button(root, text='=', fg='black', bg='lightgrey', height=2, width=20,
        command=lambda: evaluate(expr))

    exprEntry.grid(row=0, columnspan=4, ipady=10)

    button1.grid(row=1, column=0)
    button2.grid(row=1, column=1)
    button3.grid(row=1, column=2)
    buttonAdd.grid(row=1, column=3)

    button4.grid(row=2, column=0)
    button5.grid(row=2, column=1)
    button6.grid(row=2, column=2)
    buttonSub.grid(row=2, column=3)

    button7.grid(row=3, column=0)
    button8.grid(row=3, column=1)
    button9.grid(row=3, column=2)
    buttonMul.grid(row=3, column=3)

    button0.grid(row=4, column=0)
    buttonEq.grid(row=4, column=1, columnspan=2)
    buttonDiv.grid(row=4, column=3)

    root.mainloop()