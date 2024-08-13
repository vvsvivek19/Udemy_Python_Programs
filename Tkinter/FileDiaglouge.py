from tkinter import *
from tkinter.filedialog import *

win = Tk()
win.title('My First Application')
win.geometry('+460+150')

# Creating Handlers or Functions for Button Functionality

def openhandler():
    fname = askopenfile()
    content = fname.read()
    txt.insert(1.0,content)

def savehandler():
    fname = asksaveasfile(mode='w',defaultextension='.txt',filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  )
    fname.write(txt.get('1.0','end-1c'))
    fname.close()

def clearhandler():
    txt.delete('1.0','end-1c') # way to mention entire content of text widget

# Creating a frame to contain the Text widget and scrollbars
txt_frame = Frame(win)
txt_frame.grid(row=0,column=0,sticky=N+S+E+W)

# Configuring row and column weights inside txt_frame
txt_frame.grid_rowconfigure(0, weight=1)  # Allow row 0 (Text widget) to expand
txt_frame.grid_columnconfigure(0, weight=1)  # Allow column 0 (Text widget) to expand

# Creating the Text widget
txt = Text(txt_frame,wrap='none')
txt.grid(row=0,column=0,sticky=N+S+E+W)

# Creating the vertical scrollbar
scrollbar_y = Scrollbar(txt_frame,orient=VERTICAL,command=txt.yview)
scrollbar_y.grid(row=0,column=1,sticky=N+S)

# Creating the horizontal scrollbar
scrollbar_x = Scrollbar(txt_frame,orient=HORIZONTAL,command=txt.xview)
scrollbar_x.grid(row=1,column=0,sticky=E+W)

# Setting or Configuring the scroll bar
txt.config(yscrollcommand=scrollbar_y.set,xscrollcommand=scrollbar_x.set)

# Buttons
open_btn = Button(win,text='Open File',command=openhandler)
open_btn.grid(row=1,column=0)
save_btn = Button(win,text='Save File',command=savehandler)
save_btn.grid(row=2,column=0)
clear_btn = Button(win,text='Clear Text',command=clearhandler)
clear_btn.grid(row=3,column=0)

win.mainloop()
