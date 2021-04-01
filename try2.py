# !/usr/bin/python3
from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.place (x = 153, y = 0, width = 15, height = 20)

mylist = Listbox(root, yscrollcommand = scrollbar.set)
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.place (x = 0, y = 0, width = 150, height = 20)
scrollbar.config( command = mylist.yview )

mainloop()
