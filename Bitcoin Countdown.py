#Bitcoin Halving Countdown
from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

global endTime

def quit(*args):
    root.destroy()
    
def cant_wait():
    timeLeft =endTime - datetime.datetime.now()
    timeLeft =timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)
    
    txt.set(timeLeft)
    
    root.after(1000,cant_wait)

root=Tk()
root.title('Bitcoin Halving')
root.attributes("-fullscreen", False)
root.configure(background='black')
root.bind("x", quit)
root.after(1000,cant_wait)

#Set the end date and time of the next Bitcoin Havling 
endTime=datetime.datetime(2020, 5, 26, 3, 42, 10)

#Font families are 'Times','Helvetica','Zapf-Chancery','Western','Courier'
fnt=font.Font(family='Western',size=15, weight='bold')
txt=StringVar()
lbl=ttk.Label(root, textvariable=txt, font=fnt, foreground="gold", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
