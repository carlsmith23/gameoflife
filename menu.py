from window import Window
from settings import Settings

class Menu:
    def __init__(self):
        self.b = ""
        self.run = 1


    def main_menu(self):
        window = Window()
        while self.run == 1:
            print("")
            print("")
            print("")
            print("CONWAY'S GAME OF LIFE")
            print("")            
            print("1: Start game with random seed")
            print("")
            print("2: Start game with set seed")
            print("")
            print("3: Settings")
            print("")
            print("4: Quit")
            print("")
            b = int(input("?:"))
            
            #if b.isnumeric() and b < 5:
            if b == 1:
                window.open()
            elif b == 2:
                pass
            elif b == 3:
                settings_menu()
            elif b == 4:
                self.run = 0
            else:
                pass    
            #else:
                #print("Error: Not a valid selection")


    def settings_menu(self):
        pass
            

            
            
            
            

