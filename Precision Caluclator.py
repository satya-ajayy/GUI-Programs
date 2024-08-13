import sympy as sp
import textwrap as tw
from tkinter import *


def calculate():
    num = eval(entry_1.get())
    den = eval(entry_2.get())
    p = eval(entry_3.get())
    str_exp = num/den
    expr = sp.sympify(str_exp)
    b = expr.evalf(p)
    b = str(b)
    answer = tw.fill(b, 50)
    output.configure(text=answer, bg="skyblue")


root = Tk()
root.title("PRECISION-CALCULATOR")
root.configure(bg="blue")
root.geometry("380x350")
title_label = Label(root, text="PRECISION CALCULATOR", borderwidth=10, fg="red", bg="blue")
title_label.config(font=("Arial Rounded MT Bold", 20))
title_label.grid(row=0, column=0, columnspan=3)
Label(text="Numerator:", font=("candara", 18), bg="blue").grid(row=1, column=0)
Label(text="Denominator:", font=("candara", 18), bg="blue").grid(row=2, column=0)
Label(text="Precision:", font=("candara", 18), bg="blue").grid(row=3, column=0)
entry_1 = Entry(font=("calibri", 15, "bold"), bg="yellow", width=15, borderwidth=4)
entry_2 = Entry(font=("calibri", 15, "bold"), bg="yellow", width=15, borderwidth=4)
entry_3 = Entry(font=("calibri", 15, "bold"), bg="yellow", width=15, borderwidth=4)
button = Button(text="CALCULATE", font=("calibri", 15, "bold"), width=20, command=calculate,
                bg="brown", borderwidth=5)
f1 = LabelFrame(root, text='YOUR-ANSWER', bg='skyblue')
f1.place(x=10, y=220, width=360, height=120)
output = Label(f1, font=("calibri", 10, "bold"), bg="skyblue")
output.pack()
entry_1.grid(row=1, column=1)
entry_2.grid(row=2, column=1)
entry_3.grid(row=3, column=1)
button.grid(row=4, column=0, columnspan=25)

root.mainloop()
