from tkinter import *
root = Tk()
root.title("side operation on frame")
root.geometry("300x300")
frame1 = Frame(root,bg="blue",height="100",width="100")
frame1.pack(side=RIGHT)
root.mainloop()