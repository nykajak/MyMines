class TileManager:
    def __init__(self, minefield, minefield_info):
        self.num_rows = minefield_info.num_rows
        self.num_cols = minefield_info.num_cols
        self.num_bombs = minefield_info.num_bombs