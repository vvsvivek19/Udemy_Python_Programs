from tkinter import *
from tkinter.font import *

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

def scroll_scale(event):
    """
    Adjust the scale value based on the scroll direction.
    """
    # Increase or decrease the scale's value based on the scroll direction
    if event.delta < 0: # Mouse wheel down
        scl1.set(scl1.get()+2)
    else:  # Mouse wheel up
         scl1.set(scl1.get()-2)

def font_size(event):
    f = Font(size=str(scl1.get()))
    ent1['font'] = f


ent1_var = StringVar()
ent1 = Entry(win,textvariable=ent1_var, font= ('Helvetica', '16','bold'))
ent1.pack()
ent1_var.set('Welcome to my App!')

scl1 = Scale(win,from_=10,to=100,length=150,resolution=1,showvalue=True,sliderlength=20,command=font_size)
scl1.pack(pady=10)

# Bind the mouse scroll event to the scroll_scale function
scl1.bind("<MouseWheel>",scroll_scale)

win.mainloop()