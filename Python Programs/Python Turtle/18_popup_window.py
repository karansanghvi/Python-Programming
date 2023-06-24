from tkinter import *
from tkinter import simpledialog

def getme():
    s = simpledialog.askfloat("Input number","enter any number")
    print(s)

root = Tk()
root.geometry("200x200")
button = Button (
    root,
    text="Popup",
    command=getme
)
button.pack()
root.mainloop()