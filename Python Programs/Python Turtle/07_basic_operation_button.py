from tkinter import *
root = Tk()
root.title("basic operation on button")
root.geometry("300x300")
frame1 = Frame(root,bg="blue")
frame1.pack(fill=BOTH,expand=True)
button = Button(
    frame1,text="Button",
    font=("Ariel",15,"bold"),
    fg="red",
    height=5,
    width=15,
    bd=4,
    bg="black"
    )
button.pack(anchor="nw",padx=80,pady=100)
root.mainloop()