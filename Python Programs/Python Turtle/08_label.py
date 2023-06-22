from tkinter import *
root = Tk()
root.title("label")
root.geometry("300x300")
label=Label(
    root,
    text="Hello World",
    fg="red",
    font=("arial",20,"bold")
    )
label.pack()
root.mainloop()