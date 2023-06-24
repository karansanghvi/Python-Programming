from tkinter import *
root = Tk()
root.title("scroll bar")
root.geometry("300x300")

frame = Frame (
    root,
    bg="blue",
    height=100,
    width=100
)
frame.pack(side="right",fill=BOTH,expand=True)

scroll = Scrollbar (
    frame,
    orient=HORIZONTAL
)
scroll.pack(side=BOTTOM,fill=X)
scroll = Scrollbar(frame,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)

root.mainloop()