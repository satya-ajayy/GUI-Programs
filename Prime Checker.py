from tkinter import *


def check():
    n = int(entry.get())
    if n in [0, 1]:
        label.configure(text="Neither Prime Nor Composite".format(n), bg="yellow", fg="blue")
    elif n == 2:
        label.configure(text="Even Prime Number".format(n), bg="yellow", fg="blue")
    else:
        for i in range(2, n // 2 + 2):
            if n % i == 0:
                label.configure(text="{} is a Composite number".format(n), bg="yellow", fg="blue")
                break
            else:
                label.configure(text="{} is a Prime Number".format(n), bg="yellow", fg="blue")
    entry.delete(0, END)


root = Tk()
root.title("Prime_checker")
root.configure(bg="skyblue")
root.geometry("500x150")
lab1 = Label(text="Enter a Positive Number: ", font=("Courier New CE", 16), borderwidth=4)
entry = Entry(font=("Courier New CE", 16), width=5, borderwidth=4)
button = Button(text="Check", font=("Courier New CE", 16), fg="black", bg="pink")
button.configure(width=7, anchor=CENTER, command=check, borderwidth=4)
lab1.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=0, column=2)
f1 = LabelFrame(root, text='YOUR-ANSWER', bg='skyblue')
f1.place(x=50, y=50, width=400, height=80)
label = Label(f1, font=("Courier New CE", 20), bg="skyblue")
label.pack()
mainloop()
