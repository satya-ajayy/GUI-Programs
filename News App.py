import requests
from tkinter import *


def GetNews():
    api_key = 'a6bf40d19c94490c970d85a01f6ea2d1'
    url = 'https://newsapi.org/v2/top-headlines?country=us&apikey='+api_key
    html_data = requests.get(url)
    json_data = html_data.json()
    articles = json_data['articles']
    news = ''
    for i, article in enumerate(articles):
        news = news + str(i+1).zfill(2) + ' '*5 + article['title'] + '\n'
    news_label.config(text=news, justify='left')


root = Tk()
root.title('FLASH NEWS')
root.geometry('900x400')

news_label = Label(root, text='')
news_label.config(borderwidth=10, font=('Arial Rounded MT Bold', 10))
news_label.grid(row=1, column=0, columnspan=3)

GetNews()
root.mainloop()
