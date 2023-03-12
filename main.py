from menu import Menu
from map import Map

#menu = Menu()
#menu.main_loop()

from tkinter import Tk, Text
map = Map()

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=48)
text.pack()

map.generate()
map.make_alive()
text.insert('1.0', map.display())

def task():
    text.delete('0.0', '42.42')
    map.update()
    text.insert('1.0', map.display())
    root.after(500, task)  # reschedule event in 2 seconds

root.after(500, task)
root.mainloop()


    
