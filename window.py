from tkinter import *
from map import Map
from settings import Settings

class Window:
    def __init__(self):
        self.x = 0

    

    def open(self):
        map = Map()
        settings = Settings()

        root = Tk()
        root.resizable(False, False)
        root.title("Text Widget Example")

        text = Text(root, height=map.size, width=((map.size*2)))
        text.pack()

        map.generate()
        #map.make_alive()
        text.insert('1.0', map.display())

        def loop():
            text.delete('0.0', END)
            map.update()
            text.insert('1.0', map.display())
            root.after(settings.speed, loop)  # reschedule event in 2 seconds
        

        root.after(settings.speed, loop)
        root.mainloop()

