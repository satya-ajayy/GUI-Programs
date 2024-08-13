from tkinter import Label, Button, mainloop, Entry, Tk
import sympy as sp
import numpy as np
from sympy.abc import x


def calculate():
    a = sp.Matrix(np.zeros((3, 3), dtype='i'))
    for p in range(3):
        for q in range(3):
            a[p, q] = int(e[p][q].get())
    b = a - x * sp.eye(3)
    expr = sp.det(b) * -1
    label.configure(text=expr, fg="orange", bg="black")


root = Tk()
root.configure(bg='pink')
root.geometry("510x250")
root.title("CHARACTERISTIC EQUATION")
e = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(3):
    for j in range(3):
        e[i][j] = Entry(font=('Verdana', 25), width=3, borderwidth=3, bg='#0047AB')
        e[i][j].configure(fg="white")
        e[i][j].grid(row=i, column=j)

label = Label(font=('Verdana', 20), bg='pink')
label.grid(row=5, column=1)
button = Button(text="CHARACTERISTIC EQUATION", font=('Verdana', 16))
button.configure(width=25, borderwidth=5, command=calculate)
button.configure(bg='yellow', fg='blue')
button.grid(row=3, column=1)
mainloop()
