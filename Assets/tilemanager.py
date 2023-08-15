class TileManager:
    def __init__(self, minefield, grid_info):
        self.num_rows = grid_info.num_rows
        self.num_cols = grid_info.num_cols
        self.num_bombs = grid_info.num_bombs