from tkinter import *
from tkinter import messagebox

drawing = None

def first_point(event):
    pressflag.set(True)
    x1.set(event.x)
    y1.set(event.y)
    x2.set(event.x)
    y2.set(event.y)
    draw_shape()

def dragging(event):
    if pressflag.get() == True:
        can1.coords(drawing,x1.get(),y1.get(),event.x,event.y)

def second_point(event):
    can1.coords(drawing,x1.get(),y1.get(),event.x,event.y)
    pressflag.set(False)

def draw_shape():
    global drawing
    funs = [can1.create_line, can1.create_rectangle, can1.create_oval]
    if shape_var.get() == 0:
        drawing = funs[shape_var.get()](x1.get(), y1.get(), x2.get(), y2.get(), fill=color_var.get(), width=width_var.get())
    else:
        drawing = funs[shape_var.get()](x1.get(), y1.get(), x2.get(), y2.get(), outline=color_var.get(), width=width_var.get())



win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

can1 = Canvas(win, bg='#ffffbb')
can1.pack(fill=BOTH,expand=True)

can1.bind('<ButtonPress>',first_point)
can1.bind('<ButtonRelease>',second_point)
can1.bind('<Motion>',dragging)

x1 = IntVar(value=0)
x2 = IntVar(value=0)
y1 = IntVar(value=0)
y2 = IntVar(value=0)
pressflag = BooleanVar(value=False)

shape_var = IntVar(value=0)
color_var = StringVar(value = 'red')
width_var = IntVar(value=1)

menubar = Menu(win)
shape_menu = Menu(menubar, tearoff=0)
shape_menu.add_radiobutton(label='Line',variable=shape_var,value=0)
shape_menu.add_radiobutton(label='Rectangle',variable=shape_var,value=1)
shape_menu.add_radiobutton(label='Oval',variable=shape_var,value=2)
menubar.add_cascade(label='Shapes',menu=shape_menu)

color_menu = Menu(menubar,tearoff=0)
color_menu.add_radiobutton(label='Red',variable=color_var,value='red')
color_menu.add_radiobutton(label='Green',variable=color_var,value='green')
color_menu.add_radiobutton(label='Blue',variable=color_var,value='blue')
menubar.add_cascade(label='Colors',menu=color_menu)

width_menu = Menu(menubar,tearoff=0)
width_menu.add_radiobutton(label='1',variable=width_var,value=1)
width_menu.add_radiobutton(label='2',variable=width_var,value=2)
width_menu.add_radiobutton(label='3',variable=width_var,value=3)
menubar.add_cascade(label='Colors',menu=width_menu)

win['menu'] = menubar

win.mainloop()