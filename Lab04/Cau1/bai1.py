from tkinter import Tk,Frame, BOTH
from tkinter.ttk import Frame, Button, Style


class ViDu(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
        

    def initUI(self):
        self.parent.title("Console")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place (x=50, y=50)


root = Tk()
root.geometry("250x150+300+300")
app = ViDu(root)
root.mainloop()