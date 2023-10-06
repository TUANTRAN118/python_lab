#  kết nối CSDL dùng pyodbc
import pyodbc

connectionString = '''DRIVER={ODBC Driver 17 for SQL Server};
                      SERVER=TUANTRAN\SQLEXPRESS;DATABASE=QLSinhVien;Trusted_Connection=yes'''


def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()


# lấy danh sách lớp
def insert_class(id,class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # c1 truc tiep
        # select_query = f"INSERT INTO Lop(ID,TenLop) values ({id},'{class_name}')"
        # cursor.execute(select_query)


        # c2 tham so
        # select_query = 'INSERT INTO Lop(ID,TenLop) values (?,?)'
        # cursor.execute(select_query,(id,class_name,))


        # Xuat
        select_query ='SELECT * FROM Lop'
        cursor.execute(select_query)
        records= cursor.fetchall()

        print('ID \t TenLop')
        for row in records:
            print(row[0],'\t',row[1])



        connection.commit()

        print('Thêm thành công')
        close_connection(connection)


    except(Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra!!!. thông tin lỗi: ",error )
insert_class(0,0)



# Delete
def Delete_class(id,class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # c2 tham so
        # select_query = 'DELETE FROM Lop WHERE ID =? AND TenLop = ?'
        # cursor.execute(select_query,(id,class_name,))


        # Xuat
        select_query ='SELECT * FROM Lop'
        cursor.execute(select_query)
        records= cursor.fetchall()

        print('ID \t TenLop')
        for row in records:
            print(row[0],'\t',row[1])


        connection.commit()

        print('Xóa thành công')
        close_connection(connection)


    except(Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra!!!. thông tin lỗi: ",error )
Delete_class(6,'CTK46A')




# Update
def Update_class(id,class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()


        # c2 tham so
        # select_query = 'UPDATE Lop SET TenLop = ? WHERE ID = ?'
        # cursor.execute(select_query,(class_name,id,))


        # Xuat
        select_query ='SELECT * FROM Lop'
        cursor.execute(select_query)
        records= cursor.fetchall()

        print('ID \t TenLop')
        for row in records:
            print(row[0],'\t',row[1])


        connection.commit()

        print('Cập nhật thành công')
        close_connection(connection)


    except(Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra!!!. thông tin lỗi: ",error )
Update_class(5,'CTK46AB')
