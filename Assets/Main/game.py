from Assets.Supporting import MineField

class Game():
    def __init__(self, window, grid_info):
        self.minefield = MineField(window,grid_info)
        self.minefield.pack()
        self.grid_info = grid_info