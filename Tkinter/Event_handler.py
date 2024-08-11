from tkinter import *
from tkinter.messagebox import *


def My_handler(e):
    # showinfo('My Info', lbl.cget('text'))
    # lbl.config(bg='black',fg='White')
    # showinfo('My Info',lbl['bg'])
    if int(e.type) == 7:
        lbl['bg']= 'black'
        lbl['fg']= 'white'
        lbl['text'] = 'Black Color'
    elif int(e.type) == 8:
        lbl['bg'] = 'Blue'
        lbl['fg'] = 'White'
        lbl['text'] = 'Blue Color'


win = Tk()
win.title('Event Binding')
win.geometry('600x400+450+150')

lbl = Label(win, text='Blue', bg='blue', width=20, height=2)
lbl.pack()

lbl.bind('<Enter>', My_handler)
lbl.bind('<Leave>',My_handler,add='+')

win.mainloop()
