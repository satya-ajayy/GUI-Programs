import random as rd
from tkinter import *
from tkinter import messagebox

global captcha


def generateCaptcha():
    global captcha
    cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sma = 'abcdefghijklmnopqrstuwxyz'
    dig = '1234567890'
    spc = '!@#$%^&*=?'
    all_in_one = cap + sma + dig + spc
    password = rd.choices(all_in_one, k=6)
    captcha = ''.join(password)


def Refresh():
    global captcha
    generateCaptcha()
    entry.delete(0, END)
    label1.config(text=f'Captcha : {captcha}')
    label2.config(text='')


def check():
    global captcha
    if entry.get() == '':
        messagebox.showinfo('show Info', 'Please Enter Captcha')
    elif captcha == entry.get():
        label2.config(fg='green', text='SuccessFull')
    else:
        Refresh()
        label2.config(fg='red', text='Try Again!!')
        entry.delete(0, END)


root = Tk()
generateCaptcha()
root.geometry('390x250')
root.title('CAPTCHA-GENERATOR')
root.configure(bg='black')
label1 = Label(text=f'Captcha : {captcha}', borderwidth=10)
label1.config(fg='white', bg='black', font=('Arial Rounded MT Bold', 30))
label1.grid(row=0, column=0, columnspan=3)
entry = Entry(root, width=10, borderwidth=5)
entry.config(font=('Arial Rounded MT Bold', 21))
entry.place(x=10, y=65)
refresh = Button(root, text='Refresh', width=10, anchor=CENTER, fg='black', bg='#4B8BBE')
refresh.config(font=('Arial Rounded MT Bold', 17), command=lambda: Refresh())
refresh.place(x=220, y=65)
enter = Button(root, text='Enter', width=10, anchor=CENTER, fg='black', bg='#4B8BBE')
enter.config(font=('Arial Rounded MT Bold', 17), command=lambda: check())
enter.place(x=120, y=120)
label2 = Label(text='', borderwidth=10)
label2.config(bg='black', font=('Arial Rounded MT Bold', 40))
label2.place(x=35, y=160)
mainloop()
