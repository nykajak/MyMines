from tkinter import Canvas

class MineField(Canvas):
    def __init__(self, root, grid_info):
        width = grid_info.num_cols * 50
        height = grid_info.num_rows * 50

        super().__init__(root, width = width * 50, height = height)

        self.root = root
        self.grid_info = grid_info
        self.root.geometry(f"{width}x{height}")

        for i in range(grid_info.num_rows):
            for j in range(grid_info.num_cols):
                num = grid_info.layout[i][j]
                if 0 < num < 9:
                    self.draw_numbered(i,j,"white",num)

                elif num == 0:
                    self.draw_box(i,j,"white")

                elif num == 9:
                    self.draw_box(i,j,"red")

    def draw_box(self, row, col, color):
        self.create_rectangle(col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, fill = color)

    def draw_numbered(self,row, col, color, number):
        self.draw_box(row, col, color)
        self.create_text(col * 50 + 25, row * 50 + 25, text = str(number))

