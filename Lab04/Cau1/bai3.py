# scale

from tkinter import Tk, BOTH, IntVar, LEFT
from tkinter.ttk import Frame, Label, Scale ,Style

class Vidu(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
    

    def initUI(self):
        self.parent.title("Thanh Cuon")
        self.style= Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        scale = Scale(self, from_=0, to =100, command = self.onScale )
        scale.pack(side= LEFT, padx=15)

        # lien ket Intvar voi label bang textvariable
        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack(side=LEFT)

    def onScale(self,val):
        v = int(float(val))
        self.var.set(v)


root = Tk()
vd = Vidu(root)
root.geometry("250x100+300+300")
root.mainloop()
                        
    
