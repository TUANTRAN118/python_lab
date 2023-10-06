# menu da cap
from tkinter import Tk, Frame, Menu

class ViDu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

# Simple menu
    # def initUI(self):
    #     self.parent.title("Menu")
    #     menuBar = Menu(self.parent)
    #     self.parent.config(menu = menuBar)

    #     fileMenu = Menu(menuBar)
    #     fileMenu.add_command(label="Label1")
    #     fileMenu.add_command(label="Exit", command=self.onExit)

    #     menuBar.add_cascade(label="File", menu=fileMenu)
        
# Sub menu
    def initUI(self):
        self.parent.title("Submenu")
        menubar = Menu(self.parent)
        self.parent.config(menu = menubar)
        
        fileMenu = Menu(menubar)
        submenu = Menu(fileMenu)

        submenu.add_command(label="This is one")
        submenu.add_command(label="This is two")
        submenu.add_command(label="This is three")
        fileMenu.add_cascade(label= "This is submenu", menu = submenu)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu = fileMenu )


    def onExit(self):
        self.quit()




root = Tk()
root.geometry("250x150+300+300")
app = ViDu(root)
root.mainloop()