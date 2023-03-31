from tkinter import *
from map import Map
from settings import Settings

class Window:
    def __init__(self):
        self.x = 0


    def open(self, map):
        self.map = map
        settings = Settings()

        root = Tk()
        root.resizable(False, False)
        root.title("Conway's Game of Life")

        text = Text(root, height=settings.size, width=((settings.size*2)), font=('Courier New', settings.font_size), spacing2=0, spacing3=0 )
        text.pack()

        text.insert('1.0', map.display())

        def loop():
            text.delete('0.0', END)
            map.update()
            text.insert('1.0', map.display())
            root.after(settings.pause, loop)  # increase in settings to slow down
        

        root.after(settings.pause, loop)
        root.mainloop()

