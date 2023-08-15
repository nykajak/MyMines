from random import randint
class MineFieldInfo:
    def __init__(self, num_rows, num_cols, num_bombs):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_bombs = num_bombs

        self.layout = [[0 for i in range(num_cols)] for j in range(num_rows)] #Stores the actual board.

    def get_neighbours(self,x,y):
        for x_offset in range(-1,2):
            for y_offset in range(-1,2):
                if (x_offset != 0 or y_offset != 0):
                        new_x, new_y = x + x_offset, y + y_offset
                        if (0 <= new_x < self.num_rows and 0 <= new_y < self.num_cols):
                            yield (new_x,new_y)
    
    def generate_bombs(self):
        count = 0
        pos = set()
        while (count < self.num_bombs):
            x,y = randint(0,self.num_rows - 1),randint(0,self.num_cols - 1)

            if self.layout[x][y] != 9:
                self.layout[x][y] = 9
                pos.add((x,y))

            count+=1

        return pos

    def compute_nums(self,pos):
        for x,y in pos:
            for coords in self.get_neighbours(x,y):
                if self.layout[coords[0]][coords[1]] != 9:
                    self.layout[coords[0]][coords[1]] += 1

    def generate_grid(self):
        pos = self.generate_bombs()
        self.compute_nums(pos)
