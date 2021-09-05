from tkinter import *
from tkinter import ttk
from tkinter import font
import datetime

# CLOSE BUTTON
def quit():
    root.destroy()

# COUNTDOWN FUNCTION
def cant_wait():
    timeleft = endTime - datetime.datetime.now()
    txt.set(timeleft)
    root.after(1000, cant_wait)

# tkinter lib for showing clock
root = Tk()
root.attributes("-fullscreen", False)
root.configure(background="black")
root.bind("x", quit)
root.after(1000, cant_wait)

# input the date and time for your countdown
endTime = datetime.datetime(2021, 12, 31, 0, 0, 0)

fnt = font.Font(family="Times New Roman", size=45, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='white', background='black')
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
