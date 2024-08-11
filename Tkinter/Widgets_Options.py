from tkinter import *

win = Tk()

win.title('My First Application')

win.geometry('600x400+460+150')

win.state('zoomed')
l = Entry(win,text='Hello Tkinter!',width=100)

l['justify'] = 'right'
l['bd'] = 5
l['bg'] = 'red'
l['fg'] = 'yellow'

l.config(font='Ariel,20')

l.pack(pady=50)

win.mainloop()

