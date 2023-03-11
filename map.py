import random
from cell import Cell

class Map:
    def __init__(self):
        self.list = []
        self.size = 100

    def generate(self): 
        map = []
        list_length = 0
        self.size = int(self.size)
        for list_length in range(self.size * self.size):
            value = random.randint(0, 1)
            self.list.append(value)
        return map


    def ngenerate(self):
        for row in range(self.size):
            column_list = []
            for column in range(self.size):
                column_list.append(0) 
            self.list.append(column_list)


    def display(self):
        col = 0
        row = 0
        x = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.list[(col+x)] == 1:
                    print("X", end="")
                else:
                    print(" ", end="")
            x = x + self.size
            print("")


    def ndisplay(self):
        col = 0
        row = 0
        x = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.list[row][col] == 1:
                    print("X", end="")
                else:
                    print(" ", end="")
            print("")

    def update(self):
        new_list = []
        for i in range(self.size * self.size):
            cell = Cell(i, self.size, self.list, new_list)
            new_list = cell.iterate()
        self.list = new_list