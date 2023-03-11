from map import Map

class Menu:
    def __init__(self):
        self.b = ""
        self.run = 1

    def main_loop(self):
        map = Map()
        map.ngenerate()
        while self.run == 1:
            map.ndisplay()
            print("")
            self.b = input("(U)pdate")
            if self.b == "u" or self.b == "U":
                map.update()
