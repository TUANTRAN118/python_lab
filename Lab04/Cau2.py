# login form

from tkinter import Tk,Frame, BOTH,Label,Entry, StringVar,Button
import tkinter as tk

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent= parent
        self.initUI()


    def initUI(self):
        name_var=StringVar()
        passw_var=StringVar()

        self.parent.title("Login App")

        # create username
        name_label = Label(root, text = "Username", font = ('calibre', 10, 'bold'))
        name_label.grid(row=0, column=0)

        name_entry = Entry(root,textvariable= name_var, font=("calibre",10,"normal"))
        name_entry.grid(row=0, column=1)

        
        password_label = Label(self, text="Password")
        password_label.grid(row=1, column=0)

        password_entry = Entry(self, textvariable=passw_var, show='*')
        password_entry.grid(row=1, column=1)

        login_button = Button(self, text="Login", command=lambda: self.validate(name_var, passw_var))
        login_button.grid(row=2, column=0)

        self.pack(fill=BOTH, expand=True)

    def validate(self, username, password):
        user = username.get()
        pwd = password.get()


        valid_users = [("admin", "1234"), ("user", "abcd")]

        if (user, pwd) in valid_users:
            print("dang nhap thanh cong")
        else:
            print("fail")





root = Tk()
root.geometry("600x400")
app = Example(root)
root.mainloop()
