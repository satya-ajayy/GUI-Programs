from tkinter import Tk, Label, Button
from PIL import ImageTk, Image
import os

def func(inc):
    global i
    i = (i + inc) % len(Photos)
    label.configure(image=Photos[i])

root = Tk()
root.title('IMAGE VIEWER APP')
root.geometry('400x400')
root.configure(bg='black')

Photos, Buttons = [], []
actress_dir = 'Actress-Images'
button_dir = 'Button-Images'

actress_files = sorted([f for f in os.listdir(actress_dir) if f.endswith(('.jpg', '.png'))])
button_files = sorted([f for f in os.listdir(button_dir) if f.endswith(('.png', '.jpg'))])

for file in actress_files:
    img = Image.open(os.path.join(actress_dir, file)).resize((400, 400))
    Photos.append(ImageTk.PhotoImage(img))

for file in button_files:
    img = Image.open(os.path.join(button_dir, file)).resize((30, 30))
    Buttons.append(ImageTk.PhotoImage(img))

i = 0
label = Label(image=Photos[i])
label.grid(row=0, column=0, columnspan=3)

button1 = Button(image=Buttons[1], command=lambda: func(-1))
button1.place(x=0, y=180)

button2 = Button(image=Buttons[0], command=lambda: func(1))
button2.place(x=364, y=180)

root.mainloop()
