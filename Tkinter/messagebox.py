import tkinter as tk
import tkinter.messagebox as msg

win = tk.Tk()
win.title('My First Application')
win.geometry('600x400+460+150')

def myhandler():
    # Temporarily disable the win window to make the messagebox modal
    '''
        win.grab_set(): This function call ensures that the win window captures all events, effectively making the messagebox modal, meaning you cannot interact with other windows in the application until you respond to the messagebox.
        
        win.grab_release(): This function call releases the event capture, allowing normal interaction with the win window after the messagebox is closed.
    '''
    win.grab_set()
    ans = msg.askyesno('Message','Do you wish to continue?',default='yes',parent=win)
    win.grab_release()
    print(ans)


btn1 = tk.Button(win,text='CLICK ME',command=myhandler)
btn1.pack()

win.mainloop()
