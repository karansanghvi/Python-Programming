from tkinter import *
def openWindow():
    top = Toplevel()
    top.title("Top Window")
    top.geometry("200x200")
    
    button1 = Button (
        top,
        text="Close",
        command=top.destroy
    )
    button1.pack()

root = Tk()
root.geometry("200x200")
button = Button (
    root,
    text="Open Window",
    command=openWindow
)
button.pack()

root.mainloop()