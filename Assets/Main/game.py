from tkinter import ttk

class Game(ttk.Frame):
    def __init__(self, window, grid_info):
        super().__init__(window)
        self.minefield = None
        self.gri_info = grid_info