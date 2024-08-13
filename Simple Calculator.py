from tkinter import *


def Buttons(val):
    global equation_text
    equation_text = equation_text + str(val)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        answer = str(eval(equation_text))
        equation_label.set(answer)
        equation_text = answer
    except SyntaxError:
        equation_label.set('SyntaxError')
        equation_text = ''
    except ZeroDivisionError:
        equation_label.set('Can\'t divide With 0')
        equation_text = ''


def clear():
    global equation_text
    equation_label.set('')
    equation_text = ''


def delete():
    global equation_text
    equation_label.set(equation_text[:-1])
    equation_text = equation_text[:-1]


root = Tk()
root.title('SIMPLE-CALCULATOR')
root.geometry('440x400')

equation_text = ''
equation_label = StringVar()

label = Label(root, textvariable=equation_label, font=('consolas', 20))
label.configure(bg='black', fg='white', width='20', height='1', borderwidth='5')
label.pack()

frame1 = Frame(root)
frame1.pack()

button1 = Button(frame1, text='1', height=2, width=7, font=35)
button1.configure(command=lambda: Buttons(1))
button1.grid(row=0, column=0)

button2 = Button(frame1, text='2', height=2, width=7, font=35)
button2.configure(command=lambda: Buttons(2))
button2.grid(row=0, column=1)

button3 = Button(frame1, text='3', height=2, width=7, font=35)
button3.configure(command=lambda: Buttons(3))
button3.grid(row=0, column=2)

button4 = Button(frame1, text='4', height=2, width=7, font=35)
button4.configure(command=lambda: Buttons(4))
button4.grid(row=0, column=3)

button5 = Button(frame1, text='5', height=2, width=7, font=35)
button5.configure(command=lambda: Buttons(5))
button5.grid(row=1, column=0)

button6 = Button(frame1, text='6', height=2, width=7, font=35)
button6.configure(command=lambda: Buttons(6))
button6.grid(row=1, column=1)

button7 = Button(frame1, text='7', height=2, width=7, font=35)
button7.configure(command=lambda: Buttons(7))
button7.grid(row=1, column=2)

button8 = Button(frame1, text='8', height=2, width=7, font=35)
button8.configure(command=lambda: Buttons(8))
button8.grid(row=1, column=3)

button9 = Button(frame1, text='9', height=2, width=7, font=35)
button9.configure(command=lambda: Buttons(9))
button9.grid(row=2, column=0)

button0 = Button(frame1, text='0', height=2, width=7, font=35)
button0.configure(command=lambda: Buttons(0))
button0.grid(row=2, column=1)

dot = Button(frame1, text='.', height=2, width=7, font=35)
dot.configure(command=lambda: Buttons('.'))
dot.grid(row=2, column=2)

equal = Button(frame1, text='=', height=2, width=7, font=35)
equal.configure(command=lambda: equals())
equal.grid(row=2, column=3)

plus = Button(frame1, text='+', height=2, width=7, font=35)
plus.configure(command=lambda: Buttons('+'))
plus.grid(row=3, column=0)

minus = Button(frame1, text='-', height=2, width=7, font=35)
minus.configure(command=lambda: Buttons('-'))
minus.grid(row=3, column=1)

into = Button(frame1, text='*', height=2, width=7, font=35)
into.configure(command=lambda: Buttons('*'))
into.grid(row=3, column=2)

div = Button(frame1, text='/', height=2, width=7, font=35)
div.configure(command=lambda: Buttons('/'))
div.grid(row=3, column=3)

frame2 = Frame(root)
frame2.pack()

Delete = Button(frame2, text='Delete', height=2, width=15, font=35)
Delete.configure(command=lambda: delete())
Delete.grid(row=0, column=0)

Clear = Button(frame2, text='Clear', height=2, width=15, font=35)
Clear.configure(command=lambda: clear())
Clear.grid(row=0, column=1)

root.mainloop()
