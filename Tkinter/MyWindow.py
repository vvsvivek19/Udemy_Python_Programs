from tkinter import *

# Create the main window
win = Tk()

# Set the title of the window
win.title('My First Application')

# Set the size and position of the window
# '600x400' is the width and height
# '+460+150' is the position on the screen (x=460, y=150)
win.geometry('600x400+460+150')

# Allow the window to be resizable
# False means the window's width cannot be resized
# True means the window's height can be resized
win.resizable(False, True)

# Set the window's transparency level
# 1.0 is fully opaque, 0.0 is fully transparent
win.attributes('-alpha', 0.90)

# Start the Tkinter event loop
win.mainloop()
