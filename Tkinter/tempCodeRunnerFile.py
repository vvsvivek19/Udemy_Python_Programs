
menubar = Menu(win) # creating the menubar first where you will place your menu items
win['menu'] = menubar # attaching the menu to application

# creating first item in the menubar
file = Menu(menubar,tearoff=0) # by default tearoff is 1 which makes the menu tearable which then can be placed anywhere
menubar.add_cascade(label='File',menu=file) # Since we are adding the file option inside the menubar, hence the menubar.add_cascade()

# now adding further options inside first menu item
file.add_command(label='New',command=add_text)
file.add_command(label='Open')
file.add(itemType='command',label = 'Save')
file.add_separator()
file.add_checkbutton(label='Save as',onvalue=1,offvalue=0)

# adding a sub-menu withing the file menu
rad1 = Menu(file,tearoff=0)
rad1.add_radiobutton(label='Option 1')
rad1.add_radiobutton(label='Option 2')
rad1.add_radiobutton(label='Option 3')
file.add_cascade(label='Options',menu=rad1) # Since we are adding the rad1 option inside the file, hence the file.add_cascade()

#Creating a frame to pack text widget and scrollbar together
txt_frame = Frame(win)
txt_frame.pack(fill=BOTH, expand=True)

txt = Text(txt_frame, undo=True, wrap="none", width=40, height=10)
txt.pack(fill=BOTH, side=LEFT, expand=True)

txt_frame.bind('<Button-2>',popupmenu)
