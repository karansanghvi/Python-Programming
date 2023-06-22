from tkinter import *

def follow():
    print("You have subscribed successfully!!")

root = Tk()
root.title("Give Command to Button")
root.geometry("300x300")

button = Button(
    root,
    text="Subscribe",
    command=follow,
    bg="black",
    fg="yellow"
)
button.pack()

root.mainloop()
