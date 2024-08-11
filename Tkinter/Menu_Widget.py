from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('My First Application')
win.geometry('600x400+460+150')


#Button Functionality
def undo():
    try:
        txt.edit_undo()
    except Exception as e:
        messagebox.showerror('Error',f'{e}')
def redo():
    try:
        txt.edit_redo()
    except Exception as e:
        messagebox.showerror('Error',f'{e}')
def print_text():
    try:
        print(txt.get(1.0,2.4))
    except Exception as e:
        messagebox.showerror('Error',f'{e}')

#--------------------------------Creating a Menubar------------------------------
menubar = Menu(win) # creating the menubar first where you will place your menu items
win['menu'] = menubar #attaching the menu to application

file = Menu(menubar,tearoff=0) # by default tearoff is 1 which makes the menu tearable which then can be 
                               # placed anywhere
menubar.add_cascade(label='File',menu=file)

file.add_command(label='New')
file.add_command(label='Open')
file.add(itemType='command',label = 'Save')
file.add_separator()
file.add_checkbutton(label='Save as',onvalue=1,offvalue=0)




#Creating a frame to pack text widget and scrollbar together
txt_frame = Frame(win)
txt_frame.pack(fill=BOTH, expand=True)

txt = Text(txt_frame, undo=True, wrap="none", width=40, height=10)
txt.pack(fill=BOTH, side=LEFT, expand=True)

# Create a vertical Scrollbar and associate it with the Text widget
scrollbar_y = Scrollbar(txt_frame,orient=VERTICAL,command=txt.yview)
scrollbar_y.pack(side=RIGHT,fill=Y)

# Create a horizontal Scrollbar and associate it with the Text widget
scrollbar_x = Scrollbar(win,orient=HORIZONTAL,command=txt.xview)
scrollbar_x.pack(side=BOTTOM,fill=X)

# Configure the Text widget to use the scrollbars
txt.config(yscrollcommand=scrollbar_y.set,xscrollcommand=scrollbar_x.set)

#Buttons for various functions
btn1 = Button(win, text='UNDO',command=undo)
btn1.pack(pady=10)

btn2 = Button(win, text='REDO',command=redo)
btn2.pack(pady=10)

btn3 = Button(win, text='Print',command=print_text)
btn3.pack(pady=10)

win.mainloop()