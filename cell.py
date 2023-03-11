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
        neighbor_list[0] = (self.index - self.size) - 1
        neighbor_list[1] = self.index - self.size
        neighbor_list[2] = (self.index - self.size) + 1
        neighbor_list[3] = self.index - 1
        neighbor_list[4] = self.index + 1
        neighbor_list[5] = (self.index + self.size) - 1
        neighbor_list[6] = self.index + self.size
        neighbor_list[7] = (self.index + self.size) + 1
        return neighbor_list.count(1)
 

    def iterate(self):
        count = self.count_neighbors()
        if list[self.index] == 1:
            if count == 2 or count == 3:
                self.new_list[self.index] = 1
            else:  
                self.new_list[self.index] = 0
        else:
            if count == 3:
                self.new_list[self.index] = 1
            else:
                self.new_list[self.index] = 0
        return self.new_list

