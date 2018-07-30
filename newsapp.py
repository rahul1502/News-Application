from tkinter import *
import requests
import webbrowser

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=aa8c1c36a1c448be95c5764aa97d49f6')
response = requests.get(url).json()
n = int(response['totalResults'])
index = 0

def showNews(index):
    title = response['articles'][index]['title']
    description = response['articles'][index]['description']
    url = response['articles'][index]['url']
    publishedAt = response['articles'][index]['publishedAt']
    newstitle.config(text = title)
    newsdescription.config(text = description)
    newsurl.config(text = url)
    newspublishedAt.config(text = publishedAt)

def searchNews(keyword):
    searchurl = ('https://newsapi.org/v2/everything?'
       'q='+ keyword +'&'
       'sortBy=popularity&'
       'apiKey=aa8c1c36a1c448be95c5764aa97d49f6')
    global response
    global n
    global index
    response = requests.get(searchurl).json()
    n = int(response['totalResults'])
    index = 0
    showNews(index)

def nextNews():
    global index
    if index == n-1:
        index = 0
    else:
        index+=1
    showNews(index)

def previousNews():
    global index
    if index == 0:
        index = n-1
    else:
        index-=1
    showNews(index)

def callback():
    webbrowser.open_new(newsurl.cget("text"))


root = Tk()
root.geometry("500x500")
keyword = Entry(root)
searchnews = Button (root, text = 'Search for Keyworkds', command = lambda: searchNews(keyword.get()))
nextnews = Button (root, text = 'Next Headline', command = lambda: nextNews())
previousnews = Button (root, text = 'Previous Headline', command = lambda: previousNews())


newstitle = Label (root, text = 'title', borderwidth=1, relief="solid", wraplength = 350)
newsdescription = Label (root, text = 'description', wraplength = 400, justify=LEFT)
newsurl = Button (root, text = 'url', wraplength = 350, justify=LEFT, fg="blue", cursor="hand2", command = lambda: callback())
newspublishedAt = Label (root, text = 'publishedAt',wraplength = 350, justify=LEFT)
showNews(index)

keyword.pack()
keyword.place( relx=0.32, rely=0.05, anchor=CENTER, height=30, width=250)
searchnews.pack()
searchnews.place( relx=0.75, rely=0.05, anchor=CENTER, height=30, width=140)
nextnews.pack()
nextnews.place(relx=0.8, rely=0.95, anchor=CENTER, height=40, width=120)
previousnews.pack()
previousnews.place(relx=0.2, rely=0.95, anchor=CENTER, height=40, width=120)

newstitle.pack()
newstitle.place(bordermode=OUTSIDE,relx=0.5, rely=0.15, anchor=CENTER, height=40, width=400)
newsdescription.pack()
newsdescription.place(relx=0.5, rely=0.4, anchor=CENTER, height=150, width=400)
newsurl.pack()
newsurl.place(relx=0.5, rely=0.7, anchor = CENTER, height=30, width=400)
newspublishedAt.pack()
newspublishedAt.place(relx=0.5, rely=0.8, anchor = CENTER, height=20, width=400)

root.mainloop()
