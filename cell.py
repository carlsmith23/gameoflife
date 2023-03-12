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
        neighbor_list.append(self.list[(row - 1) % self.size][(column  - 1) % self.size])
        neighbor_list.append(self.list[(row - 1) % self.size][column % self.size])
        neighbor_list.append(self.list[(row - 1) % self.size][(column  + 1) % self.size])
        neighbor_list.append(self.list[row % self.size][(column  - 1) % self.size])
        #current cell = self.list[row % self.size][column % self.size])
        neighbor_list.append(self.list[row % self.size][(column  + 1) % self.size])
        neighbor_list.append(self.list[(row + 1) % self.size][(column  - 1) % self.size])
        neighbor_list.append(self.list[(row + 1) % self.size][column % self.size])
        neighbor_list.append(self.list[(row + 1) % self.size][(column  + 1) % self.size])
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


