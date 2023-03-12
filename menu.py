from map import Map

class Menu:
    def __init__(self):
        self.b = ""
        self.run = 1

    def main_loop(self):
        map = Map()
        map.generate()
        while self.run == 1:
            map.display()
            print("\033[2J")
            map.update()
