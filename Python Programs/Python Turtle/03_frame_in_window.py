from tkinter import *
root = Tk()
root.title("frame in window")
root.geometry("300x300")
frame1 = Frame(root,bg="blue")
frame1.pack(fill=BOTH,expand=True)
root.mainloop()