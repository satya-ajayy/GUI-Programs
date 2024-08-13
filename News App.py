import requests
from tkinter import *


def GetNews():
    api_key = 'a6bf40d19c94490c970d85a01f6ea2d1'
    url = 'https://newsapi.org/v2/top-headlines?country=in&apikey='+api_key
    html_data = requests.get(url)
    json_data = html_data.json()
    articles = json_data['articles']
    news = ''
    for i, article in enumerate(articles):
        news = news + str(i+1).zfill(2) + ' '*5 + article['title'] + '\n'
    news_label.config(text=news, justify='left')


root = Tk()
root.title('FLASH NEWS')
root.geometry('900x500')
root.resizable(False, False)
title_label = Label(root, text=' FLASH NEWS '*3, fg='blue')
title_label.config(borderwidth=10, font=('Arial Rounded MT Bold', 30))
title_label.grid(row=0, column=0, columnspan=3)
news_label = Label(root, text='')
news_label.config(borderwidth=10, font=('Arial Rounded MT Bold', 10))
news_label.grid(row=1, column=0, columnspan=3)
button1 = Button(text='Re Load', font=('Arial Rounded MT Bold', 25))
button1.config(fg='black', command=GetNews)
button1.grid(row=2, column=0, columnspan=5)
root.mainloop()
