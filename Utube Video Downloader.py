from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox


def Widgets():
    title_label = Label(text='YOUTUBE-VIDEO-DOWNLOADER', fg='chartreuse', bg='#1874a5')
    title_label.config(borderwidth=10, font=('Arial Rounded MT Bold', 30))
    title_label.grid(row=0, column=0, columnspan=5)

    link_label = Label(text="Video  Link :", font=('Arial Rounded MT Bold', 20))
    link_label.configure(fg='#f54242', bg='#1874a5')
    link_label.grid(row=1, column=0, pady=10, padx=10)

    root.linkText = Entry(width=30, textvariable=video_Link)
    root.linkText.configure(font=('Arial Rounded MT Bold', 20))
    root.linkText.grid(row=1, column=1)

    label2 = Label(text='Destination :', font=('Arial Rounded MT Bold', 20))
    label2.configure(fg='#f54242', bg='#1874a5')
    label2.grid(row=2, column=0, pady=10, padx=10)

    root.destinationText = Entry(width=30, textvariable=download_Path)
    root.destinationText.configure(font=('Arial Rounded MT Bold', 20))
    root.destinationText.grid(row=2, column=1)

    button1 = Button(text='Browse', font=('Arial Rounded MT Bold', 20))
    button1.config(bg='#e28743', fg='black', command=Get_Path)
    button1.place(x=180, y=190)

    button2 = Button(text='Download', font=('Arial Rounded MT Bold', 20))
    button2.config(bg='#e28743', fg='black', command=Download_Vedio)
    button2.place(x=400, y=190)


def Get_Path():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    download_Path.set(download_Directory)


def Download_Vedio():
    vedio = YouTube(video_Link.get())
    all_streams = vedio.streams.filter(res='360p', progressive=True)
    all_streams.first().download(download_Path.get())
    messagebox.showinfo('INFO', 'Vedio Downloaded SuccessFully')


root = Tk()
root.configure(bg='#1874a5')
root.title('YOUTUBE-VIDEO-DOWNLOADER')
root.geometry('700x300')
video_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()
