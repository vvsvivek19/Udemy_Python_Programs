from tkinter import *
from tkinter import font
import random

win = Tk()
win.title('Suffle List')
win.geometry('400x500+460+150')

def song_select(event):
    song_name_label['text'] = song_list.get(song_list.curselection())

def shuffle_list():
    random.shuffle(eminem_songs)
    song_list.delete(0,END)
    song_list_var = Variable(value=eminem_songs)
    song_list['listvariable'] = song_list_var

fnt = font.Font(family='Time New Roman',size=20,weight="bold")
song_name_label = Label(win,text='Select',font=fnt)
song_name_label.pack(pady=5)

eminem_songs = [
    "Lose Yourself",
    "The Real Slim Shady",
    "Stan",
    "Not Afraid",
    "Love the Way You Lie",
    "Without Me",
    "Rap God",
    "Till I Collapse"
]
song_list_var = Variable(value=eminem_songs)
song_list = Listbox(win,selectmode=SINGLE,width=30,listvariable=song_list_var)
song_list.pack(pady=10)
song_list.bind('<<ListboxSelect>>',song_select)

button_font = font.Font(family='Sans',size=10,weight="bold")
suffle_button = Button(win, text='Suffle',font=button_font,width=10,command=shuffle_list)
suffle_button.pack()

win.mainloop()