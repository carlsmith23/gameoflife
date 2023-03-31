class Settings:
    def __init__(self):
        self.columns = 80
        self.size = 40
        self.pause = 50 #time in ms to pause aftere each iteration
        self.font_size = 10


    def colsize(self):
        self.font_size = (int(self.size/self.columns)) * 10


    def set_columns(self):
        b = 0
        print("")
        print("How many columns?")
        print("")
        b = input("?:")
        self.columns = b


    def set_speed(self):
        sb = 0
        print("")
        print("How long to pause after each frame?")
        print("")
        sb = int(input("?:"))
        self.speed = sb

