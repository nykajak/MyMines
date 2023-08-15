from tkinter import Tk,ttk
from Assets.Main import MainMenu, Game, MineFieldInfo
from time import time

class App(Tk):
    def __init__(self):
        super().__init__()
        self.rowconfigure(0,weight = 1)
        self.columnconfigure(0,weight = 1)
        self.resizable(False,False)
        self.title("Mines")
        self.geometry("400x400")

        self.start_time = None

        #Loading Menu
        self.curr_focus = MainMenu(self)
        self.curr_focus.grid(row = 0, column = 0)

        self.mainloop()

    def start(self,num_rows,num_cols,num_bombs):
        self.curr_focus.destroy()
        minefield_info = MineFieldInfo(num_rows,num_cols,num_bombs)
        minefield_info.generate_grid()

        self.curr_focus = Game(self,minefield_info)
        self.start_time = time()
        # self.curr_focus.grid(row = 0, column = 0)

    def end(self,won):
        width = self.winfo_width()
        height = self.winfo_width()

        self.geometry(f"{width}x{height + 50}")

        if won:
            ttk.Label(self,text = "You Won!").pack()
        
        else:
            ttk.Label(self,text = "You Lost!").pack()

        seconds = int(time() - self.start_time)
        minutes = seconds // 60
        seconds = seconds % 60

        ttk.Label(self,text = f"{minutes} minutes {seconds} seconds").pack()
        ttk.Button(self,text = "Play Again?", command = self.restart).pack()

    def restart(self):
        self.destroy()
        App()

if __name__ == "__main__":
    App()