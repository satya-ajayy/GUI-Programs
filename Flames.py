from tkinter import *


def flames():
    boy = entry1.get()
    girl = entry2.get()
    boy = boy.replace(" ", "")
    girl = girl.replace(" ", "")
    l1 = list(boy)
    l2 = list(girl)
    x = len(l1)
    y = len(l2)
    for i in range(x):
        for j in range(y):
            try:
                if l1[i] == l2[j]:
                    c = l1[i]
                    l1.remove(c)
                    l2.remove(c)
                else:
                    continue
            except IndexError:
                x = x - 1
                y = y - 1
    ch = len(l1) + len(l2)
    if ch == 3 or ch == 5 or ch == 14 or ch == 16 or ch == 18 or ch == 21 or ch == 23:
        new.configure(text=boy + " and " + girl + "\n are both friends", fg="#FFA700", bg="#0047AB")
    elif ch == 10 or ch == 19:
        new.config(text=boy + " and " + girl + "\n are both  lovers", fg="#FFA700", bg="#0047AB")
    elif ch == 8 or ch == 12 or ch == 13 or ch == 17 or ch == 28:
        new.config(text=boy + " and " + girl + "\n have lots of Attraction", fg="#FFA700", bg="#0047AB")
    elif ch == 6 or ch == 11 or ch == 15 or ch == 26:
        new.config(text=boy + " , " + girl + "\n have Marriage in future", fg="#FFA700", bg="#0047AB")
    elif ch == 2 or ch == 4 or ch == 7 or ch == 9 or ch == 20 or ch == 22 or ch == 24 or ch == 25:
        new.config(text=boy + " and " + girl + "\n are both enemies", fg="#FFA700", bg="#0047AB")
    elif ch == 1 or ch == 27:
        new.config(text=boy + " and " + girl + "\n are siblings", fg="#FFA700", bg="#0047AB")
    else:
        new.config(text="Try with short names", fg="#FFA700", bg="#0047AB")


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)


root = Tk()
root.title("FLAMES-CALCULATOR")
root.geometry("480x300")
root.configure(bg="red")
title = Label(text="FLAMES-CALCULATOR", borderwidth=10, fg="black", bg="red")
title.configure(font=("Arial Rounded MT Bold", 29))
title.grid(row=0, column=0, columnspan=5)
new = Label(bg="red", font=("Arial Rounded MT Bold", 25))
new.grid(row=4, column=0, columnspan=3)
lab1 = Label(text="Boy Name : ", borderwidth=10, fg="#7FFFD4", bg="red")
lab1.configure(font=("Arial Rounded MT Bold", 20))
lab1.grid(row=1, column=0)
lab2 = Label(text="Girl Name : ", borderwidth=4, fg="#7FFFD4", bg="red")
lab2.configure(font=("Arial Rounded MT Bold", 20))
lab2.grid(row=2, column=0)
entry1 = Entry(font=("Arial Rounded MT Bold", 18), width=20, borderwidth=5)
entry1.grid(row=1, column=2)
entry2 = Entry(font=("Arial Rounded MT Bold", 18), width=20, borderwidth=5)
entry2.grid(row=2, column=2)
submit = Button(text="FLAMES!!", width=10, font=("Arial Rounded MT Bold", 15))
submit.configure(fg="blue", bg="yellow", borderwidth=5, command=flames)
submit.grid(row=3, column=0)
Clear = Button(text="CLEAR", width=10, font=("Arial Rounded MT Bold", 15))
Clear.configure(fg="blue", bg="yellow", borderwidth=5, command=clear)
Clear.grid(row=3, column=2)
root.mainloop()
