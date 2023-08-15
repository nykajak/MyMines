from Assets.Supporting import MineField

class Game():
    def __init__(self, window, minefield_info):
        self.minefield = MineField(window,minefield_info)
        self.minefield.pack()
        self.minefield_info = minefield_info