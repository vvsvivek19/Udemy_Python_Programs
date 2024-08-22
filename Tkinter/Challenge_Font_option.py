from tkinter import *
from tkinter import font

win = Tk()
win.title('Font Options')
win.geometry('+460+150')

# Checkbutton functionality
def update_label():
    b = ''
    i = ''
    u = None
    if var_bold.get() == 1:
        b = 'bold'
    else:
        b = 'normal'
    if var_italic.get() == 1:
        i = 'italic'
    else:
        i = 'roman'
    if var_underline.get() == 1:
        u = 1
    else:
        u = 0
    
    #Taking a comman custom font object so that all the changes happen finally in this custom object
    custom_font = font.Font(family='Sans',size=30,weight=b,slant=i,underline=u)
    font_label.config(font=custom_font)
    

font_label = Label(win,text='Welcome User!',font=('Time New Roman',30))
font_label.grid(row=0,column=0,columnspan=3)

var_bold = IntVar(value=0)
bold_checkbutton = Checkbutton(win,text='Bold',command=update_label,onvalue=1, offvalue=0,variable=var_bold)
bold_checkbutton.grid(row=1,column=0)

var_italic = IntVar(value=0)
italic_checkbutton = Checkbutton(win,text='Italic',command=update_label,onvalue=1, offvalue=0,variable=var_italic)
italic_checkbutton.grid(row=1,column=1)

var_underline = IntVar(value=0)
underline_checkbutton = Checkbutton(win,text='Underline',command=update_label,onvalue=1, offvalue=0,variable=var_underline)
underline_checkbutton.grid(row=1,column=2)

win.mainloop()