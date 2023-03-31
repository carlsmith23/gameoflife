from window import Window
from map import Map
from settings import Settings

class Menu:
    def __init__(self):
        self.b = ""
        self.sb = ""

    def settings_menu(self):
        print("CONWAY'S GAME OF LIFE")
        print("SETTINGS") 
        print("")
        print("Change (C)olumns")
        print("")
        print("Change (S)peed")
        print("")
        sb = input("?:")

        #if b.isnumeric() and b < 5:
        if sb == "C" or sb == "c":
            self.settings.set_columns()
        elif sbc == "S" or sb == "s":
            self.settings.set_speed()
        else:
            pass  


    def main_menu(self):
        settings = Settings()
        map = Map()
        window = Window()
        run = 1
        while run == 1:
            print("")
            print("")
            print("")
            print("CONWAY'S GAME OF LIFE")
            print("")    
            print("1: Start game with two gliders")
            print("")        
            print("2: Start game with random seed")
            print("")
            print("3: Settings")
            print("")
            print("4: Quit")
            print("")
            b = int(input("?:"))
            
            #if b.isnumeric() and b < 5:
            if b == 1:
                
                map.generate()
                window.open(map)
            elif b == 2:
                map.generate_random()
                window.open(map)
            elif b == 3:
                self.settings_menu()
            elif b == 4:
                self.run = 0
            else:
                pass    
            #else:
                #print("Error: Not a valid selection")


     

            
            
            
            

