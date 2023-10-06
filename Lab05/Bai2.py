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
def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query ='''select * from Lop''' 
        cursor.execute(select_query)
        records = cursor.fetchall()

        print("\nDanh sách lớp là: ")
        print("Mã lớp \t Tên lớp \t")
        for row in records:
            # print("*"*50)
            # print("Mã lớp\n",row[0])  
            # print("Tên lớp\n",row[1])

            print(row[0],"\t", row[1])

        close_connection(connection)

    except(Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra!!!. thông tin lỗi: ",error )
get_all_class()


# lấy danh sách sinh viên
def get_all_student():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query='''select * from SinhVien'''
        cursor.execute(select_query)
        records = cursor.fetchall()

        print('\nDanh sách sinh viên là: ')
        print('Mã số \t Họ tên','\t'*4 ,'Mã lớp ')
        for row in records:        
            print(row[0],'\t',row[1],'\t'*3,row[2])

        close_connection(connection)

    except(Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra !. Thông tin lỗi: ", error)

get_all_student()




# Lấy danh sách sinh viên và lớp của sinh viên
def get_all_class_student():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = ''' SELECT b.ID, b.HoTen, b.MaLop, a.TenLop
                           FROM Lop a, SinhVien b
                           WHERE a.ID = b.MaLop'''
        cursor.execute(select_query)
        records = cursor.fetchall()

        print('\nDanh sách sinh viên là: ')
        print('Mã số \t Họ tên','\t'*4 ,'Mã lớp \t Tên lớp')

        for row in records:
            print(row[0],'\t',row[1],'\t'*3,row[2],'\t'*2,row[3])



    except(Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra !. Thông tin lỗi: ", error)

get_all_class_student()















