# hop thoai

from tkinter import Tk, Frame, Button, BOTH, SUNKEN,Text, Menu, END
# from tkinter.colorchooser import askcolor
# import tkinter.messagebox as mbox
from tkinter.filedialog import Open

class Vidu(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()


# message box
    # def initUi(self):
    #     self.parent.title("Message Box")
    #     self.pack()

    #     # create button
    #     error = Button(self, text="Error", command=self.onError)
    #     error.grid(padx=5, pady=5)

    #     warning = Button(self, text="warning", command=self.onWarn)
    #     warning.grid(row=1, column=0)

    #     question = Button(self, text="Question", command=self.onQUestion)
    #     question.grid(row=0, column=1)

    #     inform = Button(self, text= "information", command= self.onInfo)
    #     inform.grid(row=1, column=1)


    #     # hop thoai thong bao
    # def onError(self):
    #     mbox.showerror("Error", "Khong the mo file")

    # def onWarn(self):
    #     mbox.showwarning("Warning", "Khong the goi ham")
    
    # def onQUestion(self):
    #     mbox.askquestion("QUestion","Ban co muon thoat khong ?")

    # def onInfo(self):
    #     mbox.showinfo("Infomation", "Dowload completed")





# # Color Chooser

#     def initUI(self):
#         self.parent.title("Chon mau")
#         self.pack(fill=BOTH, expand=1)

#         self.btn = Button(self, text="Chon mau sac", command= self.onChoose)
#         self.btn.place(x=30,y=30)


#         self.frame = Frame(self, border= 1 , relief= SUNKEN, width= 100, height= 100)
#         self.frame.place(x=160, y =30)


#     def onChoose(self):
#         (rgb, hx) = askcolor()
#         self.frame.config(bg = hx)


    def initUI(self):
        self.parent.title("File dialog")
        self.pack(fill = BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu = menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu = fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)


    # mo file
    def onOpen(self):
        ftypes = [('Python file', '*.py'),('All files','*')]
        dlg = Open(self, filetypes = ftypes)
        fl =dlg.show()
        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END,text)


    def readFile(self,filename):
        f = open(filename,"r")
        text = f.read()
        return text    




root = Tk()
vd = Vidu(root)
root.geometry("300x150+300+300")
root.mainloop()