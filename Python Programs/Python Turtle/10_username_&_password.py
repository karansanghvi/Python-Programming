from tkinter import *
root = Tk()
root.title("username and password")
root.geometry("300x300")
frame = Frame(root,bg="blue")
frame.pack(fill=BOTH,expand=True)
username = Label(frame,text="Username",bg="white")
username.grid(row=0)
entry1 = Entry(frame)
entry1.grid(row=0, column=1)
password = Label(frame,text="Password",bg="white")
password.grid(row=1,column=0)
entry2 = Entry(frame)
entry2.grid(row=1,column=1)
root.mainloop()