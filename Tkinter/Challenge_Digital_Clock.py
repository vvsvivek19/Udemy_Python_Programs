from tkinter import *
from datetime import * 
import time

win = Tk()
win.title('Digital Clock')
win.geometry('600x400+460+150')

def my_time():
    try: 
        current_time = datetime.now()
        clock_lbl['text'] = current_time.strftime('%I:%M:%S:%p')
        # current_time = time.strftime("%-I:%M:%S:%p")
        # clock_lbl['text'] = current_time
        '''
            Another way of doing this: 
            (Although getting the AM and PM this is difficult)
            lt = localtime()
            hour = str(lt.tm_hour)
            minute = str(lt.tm_min)
            seconds = str(lt.tm_sec)
            clock_lbl['text'] = (f'{hour}:{minute}:{seconds}')
        '''
        win.after(1000, my_time)  # This is important
        '''
            Explaination of above code:
            - datetime.now(): This returns the current local date and time as a datetime object.
            - strftime('%I:%M:%S %p'): This formats the datetime object to display hours, minutes, seconds, and AM/PM in the format HH:MM:SS AM/PM.
            - win.after(1000, my_time): This ensures that the my_time() function is called every second to update the clock label with the current time.
        '''
    except Exception as e:
        print('Error in showing time')

clock_lbl = Label(win,text='Time',font=('Sans','40','bold'),bg='red',fg='white')
clock_lbl.pack(fill=BOTH,expand=True)


my_time()   

win.mainloop()
