#The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. 

#At each step in time, the following transitions occur:

    #Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    #Any live cell with two or three live neighbours lives on to the next generation.
    #Any live cell with more than three live neighbours dies, as if by overpopulation.
    #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#These rules, which compare the behaviour of the automaton to real life, can be condensed into the following:

    #Any live cell with two or three live neighbours survives.
    #Any dead cell with three live neighbours becomes a live cell.
    #All other live cells die in the next generation. Similarly, all other dead cells stay dead.

#The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick.[nb 1] Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations. 



class Cell:
    def __init__(self, index, size, list, new_list):
        self.index = index
        self.size = size
        self.list = list #turn into list of lists - rows and columns
        self.new_list = new_list
        self.live_neighbors = 0

    def set_alive():
        self.list[self.index] = 1

    def count_neighbors(self):
        neighbor_list = []
        row = self.index[0]
        column = self.index[1]
        neighbor_list.append(self.list[(row - 1) % self.size][(column  - 1) % (self.size*2)])
        neighbor_list.append(self.list[(row - 1) % self.size][column % (self.size*2)])
        neighbor_list.append(self.list[(row - 1) % self.size][(column  + 1) % (self.size*2)])
        neighbor_list.append(self.list[row % self.size][(column  - 1) % (self.size*2)])
        #current cell = self.list[row % self.size][column % self.size])
        neighbor_list.append(self.list[row % self.size][(column  + 1) % (self.size*2)])
        neighbor_list.append(self.list[(row + 1) % self.size][(column  - 1) % (self.size*2)])
        neighbor_list.append(self.list[(row + 1) % self.size][column % (self.size*2)])
        neighbor_list.append(self.list[(row + 1) % self.size][(column  + 1) % (self.size*2)])
        return neighbor_list.count(1)
 

    def iterate(self):
        count = self.count_neighbors()
        if self.list[self.index[0]][self.index[1]] == 1:
            if count == 2 or count == 3:
                return 1
            else:  
                return 0
        else:
            if count == 3:
                return 1
            else:
                return 0


