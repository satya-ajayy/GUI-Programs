# importing modules
from tkinter import *
from datetime import date

root = Tk()  # creating window
root.title("AGE-CALCULATOR")  # setting up title
root.configure(bg="lightgreen")  # setting up background color
root.geometry("400x300")  # fixing the size of the window
new = Label(root, bg="lightgreen")  # declaring a label
new.grid(row=5, column=0, columnspan=3)

today = str(date.today())  # getting current date using datetime module
list_today = today.split("-")  # converting into a list


# defining a function to calculate age
def age():

    global today
    global new

    new.grid_forget()
    b_date = int(entry_date.get())
    b_month = int(entry_month.get())
    b_year = int(entry_year.get())
    c_date = int(list_today[2])
    c_month = int(list_today[1])
    c_year = int(list_today[0])

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if b_date > c_date:
        c_month = c_month - 1
        c_date = c_date + month[b_month - 1]
    if b_month > c_month:
        c_year = c_year - 1
        c_month = c_month + 12
    resultd = str(c_date - b_date)
    resultm = str(c_month - b_month)
    resulty = str(c_year - b_year)
    new = Label(root, fg="#CD5C5C", bg="#D5C6FF", borderwidth=6)
    new.configure(text="YOUR AGE \n" + resulty + " YEARS " + resultm + " MONTHS " + resultd + " DAYS ",)
    new.config(font=("Arial Rounded MT Bold", 15))
    new.grid(row=5, column=0, columnspan=3)


# defining a function to clear the previous entries
def clean(Date, Month, Year):
    global new
    new.grid_forget()
    Date.delete(0, END)
    Month.delete(0, END)
    Year.delete(0, END)


# creating widgets such as labels,entry boxes and buttons and fixing its position onto window
title_label = Label(root, text="AGE CALCULATOR", borderwidth=10, fg="red", bg="lightgreen")
title_label.config(font=("Arial Rounded MT Bold", 29))
title_label.grid(row=0, column=0, columnspan=3)
label_date = Label(root, text="BIRTH DATE : ", borderwidth=4, fg="darkblue", bg="lightgreen")
label_date.config(font=("Arial Rounded MT Bold", 15))
label_date.grid(row=1, column=0)
label_month = Label(root, text="BIRTH MONTH : ", borderwidth=5, fg="darkblue", bg="lightgreen")
label_month.config(font=("Arial Rounded MT Bold", 15))
label_month.grid(row=2, column=0)
label_year = Label(root, text="BIRTH YEAR : ", borderwidth=9, fg="darkblue", bg="lightgreen")
label_year.config(font=("Arial Rounded MT Bold", 15))
label_year.grid(row=3, column=0)

entry_date = Entry(root, width=20, borderwidth=3)
entry_month = Entry(root, width=20, borderwidth=3)
entry_year = Entry(root, width=20, borderwidth=3)

entry_date.grid(row=1, column=2)
entry_month.grid(row=2, column=2)
entry_year.grid(row=3, column=2)


# calling age function in button widget
submit = Button(root, text="GET AGE!!", width=10, anchor=CENTER, fg="black", bg="#4B8BBE")
submit.configure(command=lambda: age(), borderwidth=5)

submit.grid(row=4, column=0)

# calling clean function in button widget
Clear = Button(root, text="CLEAR", width=10, bg="#4B8BBE", borderwidth=5)
Clear.configure(command=lambda: clean(entry_date, entry_month, entry_year), fg="black")
Clear.grid(row=4, column=2)
root.mainloop()
