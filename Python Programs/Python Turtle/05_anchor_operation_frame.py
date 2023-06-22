from tkinter import *
root = Tk()
root.title("anchor operation on frame")
root.geometry("300x300")
frame1=Frame(root,bg="blue",height=100,width=100)
frame1.pack(anchor="nw")
root.mainloop()