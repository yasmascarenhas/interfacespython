from tkinter import *

class App:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.msg = Label(self.widget1, text="Seja Bem-Vindo")

root = Tk()
App(root)
root.mainloop()
