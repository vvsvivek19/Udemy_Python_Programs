from tkinter import *
from time import *
from datetime import *

win = Tk()
win.title('Stop Watch')
win.geometry('+460+150')

Flag = False
elapased_time = 0
sec = 0
milisec = 0
min = 0
hour = 0

# Button Functionality

def update_watch():
    global Flag, elapased_time, sec, milisec, min, hour
    if Flag == True:
        elapased_time = elapased_time + 1
        milisec = elapased_time % 1000
        sec = elapased_time // 1000
        min = sec // 60
        sec = sec % 60
        hour = min // 60
        min = min % 60
        
        time_lable['text'] = (f'{hour:02d}:{min:02d}:{sec:02d}:{milisec:03d}')
        win.after(1, update_watch)


def start_time():
    global Flag 
    Flag = True
    update_watch()
    
def stop_time():
    global Flag
    Flag = False
    update_watch()

def reset_time():
    time_lable['text'] = '00:00:000'
    global Flag, elapased_time, sec, milisec, min, hour
    Flag = False
    elapased_time = 0
    sec = 0
    milisec = 0
    min = 0
    hour = 0
    update_watch()

time_lable = Label(win, text='00:00:000',font=('Sans',40))
time_lable.pack(fill=BOTH,expand=True)

button_frame = Frame(win)
button_frame.pack(fill=BOTH,expand=True)

start_button = Button(button_frame,command=start_time,text='Start',width=20,height=2,bg='black',fg='gold',activebackground='black',activeforeground='gold')
start_button.grid(row=0,column=0)

stop_button = Button(button_frame,command=stop_time,text='Stop',width=20,height=2,bg='black',fg='gold',activebackground='black',activeforeground='gold')
stop_button.grid(row=0,column=1)

reset_button = Button(button_frame,command=reset_time,text='Reset',width=20,height=2,bg='black',fg='gold',activebackground='black',activeforeground='gold')
reset_button.grid(row=0,column=2)

button_frame.columnconfigure(0,weight=1)
button_frame.columnconfigure(1,weight=1)
button_frame.columnconfigure(2,weight=1)

win.mainloop()