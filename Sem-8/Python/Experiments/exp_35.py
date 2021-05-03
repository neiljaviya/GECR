#Explain the major steps used to create widgets. Write a python program to display
#a label upon clicking a push button.
    #1. Import Tkinter
    #2. Create Top-level frame
    #3. Create GUI
    #4. Add Widgets
    #5. Handle Actions

from tkinter import *
root = Tk(className="btn_lbl")
root.geometry("200x200")
message = StringVar()
message.set("Welcome")
l1 = Label(root, text="")
def click():
    l1.config(text="Hello World")
b1 = Button(root, text="Click Me", command=click).pack()
l1.pack()
root.mainloop()