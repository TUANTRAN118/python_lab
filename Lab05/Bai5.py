import tkinter as tk
import pyodbc
from tkinter import ttk



connectionString = ('''
    DRIVER={ODBC Driver 17 for SQL Server};
                      SERVER=TUANTRAN\SQLEXPRESS;DATABASE=QLMonAn;Trusted_Connection=yes'''
)


# Hàm để kết nối CSDL và hiển thị dữ liệu trong Data Grid View
def get_connection():
    try:
        conn = pyodbc.connect(connectionString)
        cursor = conn.cursor()
        cursor.execute('''
                            SELECT MaMonAn, TenMonAn, DonViTinh, DonGia, TenNhom 
                        FROM MonAn, NhomMonAn  
                        where MonAn.Nhom = NhomMonAn.MaNhom 
''')
                        
                       
        rows = cursor.fetchall()
    
        for item in tree.get_children():
            tree.delete(item)
        
        # Hiển thị dữ liệu trong Data Grid View
        for row in rows:
            tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))
        
        conn.close()
        message_label.config(text="CONECTED SUCCESSFULL")
    except Exception as e:
        message_label.config(text="Lỗi kết nối: " + str(e)) 


#  chọn món ăn từ Combobox
def select_foot(event):
    selected_nhom = nhom_mon_an_combobox.get()


root = tk.Tk()
root.title("Quản lý món ăn")


label = tk.Label(root, text="Nhóm món ăn", font=('BOLD',16))
label.grid(row=0, column=1, columnspan=2, pady=10) 



# Tạo Data Grid View
tree = ttk.Treeview(root, columns=("Mã Món Ăn", "Tên Món Ăn", "Đơn Vị Tính", "Đơn Giá", "Nhóm"), show="headings")
tree.heading("Mã Món Ăn", text="Mã Món Ăn")
tree.heading("Tên Món Ăn", text="Tên Món Ăn")
tree.heading("Đơn Vị Tính", text="Đơn Vị Tính")
tree.heading("Đơn Giá", text="Đơn Giá")
tree.heading("Nhóm", text="Nhóm")
tree.grid(row=2, column=1, columnspan=10)

# Label để hiển thị thông báo
message_label = tk.Label(root, text="", fg="black")
message_label.grid(row=3, column=1, columnspan=2)


# Tạo Frame để đặt Combobox và tiêu đề "Nhóm món ăn" 
frame_nhom_mon_an = tk.Frame(root)
frame_nhom_mon_an.grid(row=1, column=2, padx=10)  

# Label cho tiêu đề "Nhóm món ăn"
label_nhom_mon_an = tk.Label(frame_nhom_mon_an, )
label_nhom_mon_an.pack(side=tk.LEFT, padx=300,) 

# Tạo Combobox để chọn nhóm món ăn
nhom_mon_an_combobox = ttk.Combobox(frame_nhom_mon_an, values=["Hải sản", "Khai vị", "Bia- Nước ngọt", "Lẩu"])
nhom_mon_an_combobox.set("Chọn món")
nhom_mon_an_combobox.pack(side=tk.TOP,ipadx=30)

# Gắn sự kiện khi chọn nhóm món ăn
nhom_mon_an_combobox.bind("<<ComboboxSelected>>", select_foot)




get_connection()
root.mainloop()