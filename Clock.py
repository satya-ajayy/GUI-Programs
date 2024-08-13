from tkinter import *
from datetime import datetime


def update_label():
    current_time = datetime.now()
    current_time = current_time.strftime('%I:%M:%S %p')
    label.configure(text=current_time)
    label.after(100, update_label)


root = Tk()
root.title('DIGITAL-CLOCK')
root.configure(bg='black')
root.geometry('600x159')
root.resizable(False, False)
label = Label(fg='#ADFF2F', bg='black', font=('ShowCard Gothic', 80))
update_label()
label.grid(row=0, column=0)
mainloop()
