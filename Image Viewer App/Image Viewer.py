from tkinter import *
from PIL import ImageTk, Image


def func(inc):
    global i
    if inc == 1:
        if i == 11:
            i = 0
        else:
            i += 1
    if inc == -1:
        if i == 0:
            i = 11
        else:
            i -= 1
    label.configure(image=Photos[i])


root = Tk()
root.title('IMAGE VIEWER APP')
root.geometry('400x400')
root.configure(bg='black')
Photos, Buttons = [], []
for i in range(12):
    img = Image.open(f'Actress Images\\Photo {i}.jpg')
    img = img.resize((400, 400))
    img = ImageTk.PhotoImage(img)
    Photos.append(img)
for i in range(12, 14):
    img = Image.open(f'Button Images\\Photo {i}.png')
    img = img.resize((30, 30))
    img = ImageTk.PhotoImage(img)
    Buttons.append(img)
i = 0
label = Label(image=Photos[i])
label.grid(row=0, column=0, columnspan=3)
button1 = Button(image=Buttons[1], command=lambda: func(-1))
button1.place(x=0, y=180)
button2 = Button(image=Buttons[0], command=lambda: func(1))
button2.place(x=364, y=180)
mainloop()
