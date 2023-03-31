import random
from cell import Cell
from settings import Settings

class Map:
    def __init__(self):
        self.list = []
        self.count = 1
        settings = Settings()
        self.columns = settings.columns


    def generate_random(self):
        for row in range(self.columns):
            column_list = []
            for column in range(self.columns*3):
                column_list.append(0)
                column_list.append(random.randint(0, 1)) 
            self.list.append(column_list)


    def generate(self):
        for row in range(self.columns):
            column_list = []
            for column in range(self.columns*3):
                column_list.append(0)
                #column_list.append(random.randint(0, 1)) 
            self.list.append(column_list)
        self.make_alive()
        

    def make_alive(self): #manual initial state, currently two gliders
        self.list[6][6] = 0
        self.list[6][7] = 1
        self.list[6][8] = 0
        self.list[7][6] = 0
        self.list[7][7] = 0
        self.list[7][8] = 1
        self.list[8][6] = 1
        self.list[8][7] = 1
        self.list[8][8] = 1
        self.list[11][32] = 0
        self.list[11][33] = 1
        self.list[11][34] = 0
        self.list[12][32] = 1
        self.list[12][33] = 0
        self.list[12][34] = 0
        self.list[13][32] = 1
        self.list[13][33] = 1
        self.list[13][34] = 1


    def display(self):
        list_as_string = ""
        count_as_string = ""
        count_as_string = str(self.count)
        list_as_string = count_as_string + "\n"
        #if len(self.list) < 0:
        for row in range(self.columns):
            for col in range(self.columns*3):
                if self.list[row][col] == 1:
                    list_as_string = list_as_string + "x"
                else:
                    list_as_string = list_as_string + " "
            list_as_string = list_as_string + "\n"
        return list_as_string
        #else:
            #return "Error: Generate map first"


    def update(self):
        new_list = []
        for row in range(self.columns):
            new_col_list = []
            for col in range(self.columns*3):
                index = row, col
                cell = Cell(index, self.columns, self.list, new_list)
                new_col_list.append(cell.iterate())
            new_list.append(new_col_list)
        self.list = new_list
        self.count += 1


    class Set_seed:
        def __init__(self):
            pass