from tkinter import Tk
from Assets import MainMenu

class App(Tk):
    def __init__(self):
        super().__init__()
        self.rowconfigure(0,weight = 1)
        self.columnconfigure(0,weight = 1)
        self.resizable(False,False)
        self.title("Mines")
        self.geometry("400x400")

        #Loading Menu
        menu = MainMenu(self)
        menu.grid(row = 0, column = 0)

        self.mainloop()

if __name__ == "__main__":
    App()