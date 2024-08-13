import subprocess
from tkinter import *
import datetime as dt
from twilio.rest import Client
from tkinter import messagebox


def Send_Msg():
    data = '''\n Some one Entered Wrong Password \n If This Wasn't You HurryUp
    Some One Is Stealing Your Important Data Stored In Pdf'''
    sender = '+17134971717'
    receiver = '+918639253607'
    account = 'ACa9619e0cee67417f5249bc49f4d8fdf9'
    token = 'db55bf8d698515432a0631c18c587f1e'
    client = Client(account, token)
    client.messages.create(to=receiver, from_=sender, body=data)


def check():
    now = dt.datetime.now()
    pwd = int(now.strftime('%H%M'))
    if entry1.get() == '':
        messagebox.showinfo('show Info', 'Please Enter Password')
    elif int(entry1.get()) == pwd:
        root.destroy()
        path = r'C:\Users\AJAY\Documents\B.Tech\PYTHON\Learn-to-Program-with-Python.pdf'
        subprocess.Popen([path], shell=True)
    else:
        messagebox.showerror('Error', 'Don\'t Steal Others Data')
        root.destroy()
        Send_Msg()


root = Tk()
root.title('PASSWORD-CHECKER')
root.geometry('480x200')
root.configure(bg='chartreuse')
title_label = Label(root, text='PASSWORD-CHECKER', fg='blue', bg='chartreuse')
title_label.config(borderwidth=10, font=('Arial Rounded MT Bold', 30))
title_label.grid(row=0, column=0, columnspan=3)
new = Label(root, fg='black', bg='chartreuse', borderwidth=6)
new.configure(text='Enter Password :', font=('Arial Rounded MT Bold', 25))
new.grid(row=1, column=0)
entry1 = Entry(width=6, font=('Arial Rounded MT Bold', 25))
entry1.grid(row=1, column=1)
button1 = Button(text='Open Pdf', font=('Arial Rounded MT Bold', 25))
button1.config(bg='#FF2090', fg='black', command=check)
button1.grid(row=2, column=0, columnspan=5)
root.mainloop()
