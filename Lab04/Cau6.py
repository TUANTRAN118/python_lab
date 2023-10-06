from openpyxl import *
from tkinter import *
from tkinter import ttk


# wb = load_workbook("D:\\Python\\Lab04\\test5.xlsx")
# sheet = wb.active

# def excel():





if __name__ == "__main__":
    root =Tk()
    root.configure(background='light gray')
    root.title('Đăng ký học phần')
    root.geometry("500x300")



heading = Label(root, text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", bg = "light gray", font=("bold"))
heading.grid(row=0, column=1)

mssv = Label(root, text="Mã số sinh viên", bg="light gray")
mssv.grid(row =1, column =0)

name = Label(root, text="Họ Tên", bg = "light gray")
name.grid(row =2, column =0)

date = Label(root, text="Ngày sinh", bg="light gray")
date.grid(row=2, column=0)

email_id = Label(root, text="Email", bg = "light gray")
email_id.grid(row=3, column=0)

contact_no = Label(root, text="Số điện thoại", bg = "light gray")
contact_no.grid(row=5, column=0)

sem = Label(root, text="Hoc kì", bg = "light gray")
sem.grid(row=6, column=0)

# year = ttk.Combobox()
# year.grid(row=7, column=0)


form_no = Label(root, text="Số biểu mẫu", bg = "light gray")
form_no.grid(row=4, column=0)






address = Label(root, text="Địa chỉ", bg = "light gray")
address.grid(row=7, column=0)





name_field = Entry(root)
name_field.grid(row=1, column=1, ipadx="130")
course_field = Entry(root)
course_field.grid(row=2, column=1, ipadx="130")
sem_field = Entry(root)
sem_field.grid(row=3, column=1, ipadx="130")
form_no_field = Entry(root)
form_no_field.grid(row=4, column=1, ipadx="130")
contact_no_field = Entry(root)
contact_no_field.grid(row=5, column=1, ipadx="130")
email_id_field = Entry(root)
email_id_field.grid(row=6, column=1, ipadx="130")
address_field = Entry(root)
address_field.grid(row=7, column=1, ipadx="130")




root.mainloop()
