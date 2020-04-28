import sys    
from tkinter import *
import time

root = Tk()
time1 = ''
clock = Label(root, font=('Microsoft JhengHei', 25, 'bold'), bg='skyblue')
clock.pack(fill=BOTH, expand=1)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        
    clock.after(200, tick)

tick()
root.mainloop(  )
