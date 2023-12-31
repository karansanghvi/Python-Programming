#importing libraries
from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfile,asksaveasfilename

win = Tk()
win.title("Notepad")

#functions we will use here to open existing files and save current file
def open_file():
    blank.delete("1.0",END)
    file = asksaveasfilename(mode='r',filetypes=[('text files','*.txt')])
    if file is not None:
        text = file.read()
        blank.insert("1.0",text)

def save_file():
    notepad_text = blank.get("1.0","end-1c")
    file = asksaveasfilename(title="Save",filetypes=[('text files','*.txt')])
    with open(file,"w") as data:
        data.write(notepad_text)

#creating menubar and add options into it
menubar = Menu(win)
win.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=open_file)
filemenu.add_command(label="Save",command=save_file)
filemenu.add_command(label="Exit",command=win.destroy)

blank = Text(win,font=("arial",10))
blank.pack()

win.mainloop()