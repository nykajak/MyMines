from tkinter import Tk
from Assets.Main import MainMenu, Game, GridInfo

class App(Tk):
    def __init__(self):
        super().__init__()
        self.rowconfigure(0,weight = 1)
        self.columnconfigure(0,weight = 1)
        self.resizable(False,False)
        self.title("Mines")
        self.geometry("400x400")

        #Loading Menu
        self.curr_focus = MainMenu(self)
        self.curr_focus.grid(row = 0, column = 0)

        self.mainloop()

    def start(self,num_rows,num_cols,num_bombs):
        self.curr_focus.destroy()
        grid_info = GridInfo(num_rows,num_cols,num_bombs)
        grid_info.generate_grid()

        self.curr_focus = Game(self,grid_info)
        # self.curr_focus.grid(row = 0, column = 0)


if __name__ == "__main__":
    App()