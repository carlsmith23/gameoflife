import random
from cell import Cell

class Map:
    def __init__(self):
        self.list = []
        self.size = 36


    def generate(self):
        for row in range(self.size):
            column_list = []
            for column in range(self.size):
                column_list.append(0) 
            self.list.append(column_list)

    def make_alive(self):
        self.list[6][6] = 1
        self.list[6][7] = 1
        self.list[6][8] = 1
        self.list[7][6] = 1
        self.list[7][7] = 1
        self.list[7][8] = 1
        self.list[8][6] = 1
        self.list[8][7] = 1
        self.list[8][8] = 1

    def display(self):
        list_as_string = ""
        #if len(self.list) < 0:
        for row in range(self.size):
            for col in range(self.size):
                if self.list[row][col] == 1:
                    list_as_string = list_as_string + "⬛"
                else:
                    list_as_string = list_as_string + "🔲"
            list_as_string = list_as_string + "\n"
        return list_as_string
        #else:
            #return "Error: Generate map first"


    def update(self):
        new_list = []
        for row in range(self.size):
            new_col_list = []
            for col in range(self.size):
                index = row, col
                cell = Cell(index, self.size, self.list, new_list)
                new_col_list.append(cell.iterate())
            new_list.append(new_col_list)
        self.list = new_list