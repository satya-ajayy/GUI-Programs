from tkinter import *


def calculate():
    temp = eval(entry.get())
    temp = 9 / 5 * temp + 32
    output_label.configure(text='Fahrenheit temperature is: {:.3f}'.format(temp))
    output_label.configure(fg="blue", bg="yellow")
    entry.delete(0, END)


root = Tk()
root.title("TEMPERATURE-CONVERTER")
root.configure(bg="pink")
root.geometry("550x120")
message_label = Label(text='Enter a temperature in degrees:', font=('Segoe Script', 16))
output_label = Label(font=('Segoe Script', 16), bg="pink")
entry = Entry(font=('Segoe Script', 16), width=5)
calc_button = Button(text='Convert', font=('Segoe Script', 16), command=calculate)
message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=3)
output_label.grid(row=1, column=0, columnspan=3)
mainloop()
