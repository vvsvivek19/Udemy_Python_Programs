from tkinter import *
from tkinter import font
import random

win = Tk()
win.title('Suffle List')
win.geometry('+460+150')

def change_color(event=None):
    color_label['bg'] = f'#{var_red.get():02x}{var_green.get():02x}{var_blue.get():02x}'
    var_entry.set( f'#{var_red.get():02x}{var_green.get():02x}{var_blue.get():02x}')

color_label = Label(win, bg='#ffffff',width=50,height=2)
color_label.grid(row=0,column=0,columnspan=2)

red_label = Label(win,text='Red',fg='red')
red_label.grid(row=1,column=0)
var_red = IntVar()
red_scale = Scale(win,command=change_color,from_=0,to=255,orient=HORIZONTAL,sliderlength=20, length= 150,variable=var_red)
red_scale.grid(row=1,column=1)

green_label = Label(win,text='Green',fg='green')
green_label.grid(row=2,column=0)
var_green = IntVar()
green_scale = Scale(win,command=change_color,from_=0,to=255,orient=HORIZONTAL,sliderlength=20, length= 150,variable=var_green)
green_scale.grid(row=2,column=1)

blue_label = Label(win,text='Blue',fg='blue')
blue_label.grid(row=3,column=0)
var_blue = IntVar()
blue_scale = Scale(win,command=change_color,from_=0,to=255,orient=HORIZONTAL,sliderlength=20, length= 150,variable=var_blue)
blue_scale.grid(row=3,column=1)

copy_label = Label(win,text='Hexadecimal Code')
copy_label.grid(row=4,column=0)
var_entry = StringVar()
copy_entry = Entry(win,textvariable=var_entry,state='readonly')
copy_entry.grid(row=4,column=1)


win.mainloop()