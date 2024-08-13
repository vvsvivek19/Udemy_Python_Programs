from tkinter import *
from time import *
from datetime import *

win = Tk()
win.title('Stop Watch')
win.geometry('600x400+460+150')

# Button Functionality




def reset_time():
    time_lable['text'] = '00:00:00'




time_lable = Label(win, text='00:00:00',font=('Sans',30))
time_lable.pack(fill=BOTH,expand=True)

button_frame = Frame(win)
button_frame.pack(fill=BOTH,expand=True)

start_button = Button(button_frame,text='Start',width=20,height=2,bg='black',fg='gold',activebackground='black',activeforeground='gold')
start_button.grid(row=0,column=0)

stop_button = Button(button_frame,text='Stop',width=20,height=2,bg='black',fg='gold',activebackground='black',activeforeground='gold')
stop_button.grid(row=0,column=1)

reset_button = Button(button_frame,command=reset_time,text='Reset',width=20,height=2,bg='black',fg='gold',activebackground='black',activeforeground='gold')
reset_button.grid(row=0,column=2)

button_frame.columnconfigure(0,weight=1)
button_frame.columnconfigure(1,weight=1)
button_frame.columnconfigure(2,weight=1)

win.mainloop()