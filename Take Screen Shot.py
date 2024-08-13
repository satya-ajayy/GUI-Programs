from tkinter.filedialog import asksaveasfilename
import tkinter as tk
from PIL import ImageGrab


def screenshot():
    ss = ImageGrab.grab()
    save_path = asksaveasfilename()
    ss.save(save_path + ".png")


button = tk.Button(font=("Segoe script", 18), fg="black", bg="orange")
button.config(text="Take Screen Shot", command=screenshot)
button.pack()
tk.mainloop()
