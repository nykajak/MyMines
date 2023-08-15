from tkinter import ttk
import tkinter as tk

class Item(ttk.Frame):
    def __init__(self,container,label,var,limits):
        super().__init__(container, border = 10)

        self.variable = var
        self.columnconfigure(0,weight = 1)
        self.columnconfigure(1,weight = 1)
        self.limits = limits

        ttk.Label(self, text = label).grid(row = 0, column = 0, sticky = tk.W)
        ttk.Label(self, textvariable = self.variable, width = 2).grid(row = 0, column = 1, sticky = tk.E)
        self.decrementor = ttk.Button(self,text = "-", command = lambda:self.setVar(-1),width = 2)
        self.decrementor.grid(row = 0, column = 2)
        self.incrementor = ttk.Button(self,text = "+",command = lambda: self.setVar(1),width = 2)
        self.incrementor.grid(row = 0, column = 3)

        for child in self.winfo_children():
            child.grid_configure(padx = 5, pady = 5)

    def setVar(self,change):
        curr_val = self.variable.get()
        self.variable.set(curr_val + change)

        self.freezeButton(curr_val + change)

    def freezeButton(self, val):
        if val == self.limits[0]:
            self.decrementor['state'] = 'disabled'
        
        elif val == self.limits[1]:
            self.incrementor['state'] = 'disabled'

        else:
            self.incrementor['state'] = 'enabled'
            self.decrementor['state'] = 'enabled'


class MainMenu(ttk.Frame):
    def __init__(self,window):
        super().__init__(window)

        self.rowconfigure(0,weight=1) 

        self.rows = tk.IntVar(value = 8)
        self.cols = tk.IntVar(value = 8)
        self.bombs = tk.IntVar(value = 10)

        Item(self,"Rows",self.rows,(1,10)).grid(row = 0, column = 0, sticky = [tk.W,tk.E])
        Item(self,"Cols",self.cols,(1,10)).grid(row = 1, column = 0, sticky = [tk.W,tk.E])
        Item(self,"Bombs",self.bombs,(1,20)).grid(row = 2, column = 0, sticky = [tk.W,tk.E])
        
        ttk.Button(self,text = "Start", command = self.start).grid(row = 3, column = 0, padx =5, pady = 5)

    def start(self):
        print(f"Rows = {self.rows.get()}!")
        print(f"Cols = {self.cols.get()}!")
        print(f"Bombs = {self.bombs.get()}!")
        print()