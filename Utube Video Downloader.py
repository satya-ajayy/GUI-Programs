from tkinter import Tk, Label, Entry, Button, StringVar, filedialog, messagebox
from pytube import YouTube

def Widgets():
    Label(root, text='YOUTUBE VIDEO DOWNLOADER', fg='chartreuse', bg='#1874a5',
          font=('Arial Rounded MT Bold', 20), pady=10).grid(row=0, column=0, columnspan=3)

    Label(root, text='Video Link:', fg='#f54242', bg='#1874a5', font=('Arial Rounded MT Bold', 14)).grid(row=1, column=0, pady=5, padx=5, sticky='e')
    Entry(root, textvariable=video_Link, font=('Arial', 14), width=40).grid(row=1, column=1, columnspan=2, pady=5, padx=5)

    Label(root, text='Destination:', fg='#f54242', bg='#1874a5', font=('Arial Rounded MT Bold', 14)).grid(row=2, column=0, pady=5, padx=5, sticky='e')
    Entry(root, textvariable=download_Path, font=('Arial', 14), width=30).grid(row=2, column=1, pady=5, padx=5)
    Button(root, text='Browse', font=('Arial', 12), bg='#e28743', command=Get_Path).grid(row=2, column=2, pady=5, padx=5)

    Button(root, text='Download', font=('Arial', 14), bg='#e28743', command=Download_Video).grid(row=3, column=1, pady=10)

def Get_Path():
    download_Path.set(filedialog.askdirectory())

def Download_Video():
    try:
        video = YouTube(video_Link.get()).streams.filter(res='360p', progressive=True).first()
        video.download(download_Path.get())
        messagebox.showinfo('Success', 'Video Downloaded Successfully')
    except Exception as e:
        messagebox.showerror('Error', f'Error Occurred: {e}')

root = Tk()
root.configure(bg='#1874a5')
root.title('YouTube Video Downloader')
root.geometry('600x250')
video_Link, download_Path = StringVar(), StringVar()
Widgets()
root.mainloop()