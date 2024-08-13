from tkinter import *
hours, minutes, seconds = 0, 0, 0
update_time, running = None, False


def Update():
    global hours, minutes, seconds, update_time
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    timer = '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
    label1.configure(text=timer)
    update_time = label1.after(1000, Update)


def Start():
    global running
    if not running:
        Update()
        running = True


def Pause():
    global running
    if running:
        label1.after_cancel(update_time)
        running = False


def Reset():
    global running
    if running:
        label1.after_cancel(update_time)
        running = False

    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    label1.configure(text='00:00:00')


root = Tk()
root.title('STOP-WATCH')
root.configure(bg='black')
root.resizable(False, False)
root.geometry('500x330')
label1 = Label(text='00:00:00', fg='#ADFF2F', bg='black', font=('ShowCard Gothic', 80))
label1.place(x=20, y=-10)
label2 = Label(text='By-Ajay', fg='#ADFF2F', bg='black', font=('ShowCard Gothic', 15))
label2.place(x=400, y=293)
button1 = Button(text='Start', font=('ShowCard Gothic', 25), fg='#ADFF2F', bg='black')
button1.configure(width=7, anchor='center', command=Start)
button1.place(x=70, y=130)
button2 = Button(text='Pause', font=('ShowCard Gothic', 25), fg='#ADFF2F', bg='black')
button2.configure(width=7, anchor='center', command=Pause)
button2.place(x=250, y=130)
button3 = Button(text='ReSet', font=('ShowCard Gothic', 25), fg='#ADFF2F', bg='black')
button3.configure(width=7, anchor='center', command=Reset)
button3.place(x=70, y=220)
button4 = Button(text='Quit', font=('ShowCard Gothic', 25), fg='#ADFF2F', bg='black')
button4.configure(width=7, anchor='center', command=root.quit)
button4.place(x=250, y=220)
mainloop()
