import random as rd
from tkinter import *


def check_winner(com, us):
    if ((com == 'paper' and us == 'scissors') or (com == 'scissors' and us == 'rock')
            or (com == 'rock' and us == 'paper')):
        return 1
    if ((com == 'paper' and us == 'paper') or (com == 'scissors' and us == 'scissors')
            or (com == 'rock' and us == 'rock')):
        return 0
    else:
        return -1


def play(user):
    lab1.configure(text=user, bg='grey', fg='orange')
    computer = rd.choice(['rock', 'scissors', 'paper'])
    lab3.configure(text=computer, bg='grey', fg='orange')
    win = check_winner(computer, user)
    if win == 1:
        lab4.configure(text="Hurray!!")
        lab5.configure(text="You  Win")
        lab6.configure(text="The Game")
    elif win == 0:
        lab4.configure(text="Its Tie")
        lab5.configure(text="Plz try")
        lab6.configure(text="Again!!")
    else:
        lab4.configure(text="Oops!!!")
        lab5.configure(text="You Lost")
        lab6.configure(text="The Game")


root = Tk()
root.title("ROCK-PAPER-SCISSORS")
root.geometry("560x200")
b = [0, 0, 0]

lab1 = Label(font=("Segoe Script", 18), borderwidth=10, width=10)
lab1.grid(row=1, column=0)
lab2 = Label(text="VS", font=("Segoe Script", 18), borderwidth=10, width=10, fg='#39FF14', bg='black')
lab2.grid(row=1, column=1)
lab3 = Label(font=("Segoe Script", 18), borderwidth=10, width=10)
lab3.grid(row=1, column=2)
lab4 = Label(font=("Segoe Script", 18), borderwidth=10, width=10)
lab4.grid(row=2, column=0)
lab5 = Label(font=("Segoe Script", 18), borderwidth=10, width=10)
lab5.grid(row=2, column=1)
lab6 = Label(font=("Segoe Script", 18), borderwidth=10, width=10)
lab6.grid(row=2, column=2)

b[0] = Button(text='rock', font=("Segoe Script", 18), command=lambda x='rock': play(x))
b[0].configure(fg='#DA1884', bg='black', width=11)
b[0].grid(row=0, column=0)
b[1] = Button(text='paper', font=("Segoe Script", 18), command=lambda x='paper': play(x))
b[1].configure(fg='#DA1884', bg='black', width=11)
b[1].grid(row=0, column=1)
b[2] = Button(text='scissors', font=("Segoe Script", 18), command=lambda x='scissors': play(x))
b[2].configure(fg='#DA1884', bg='black', width=11)
b[2].grid(row=0, column=2)

mainloop()
