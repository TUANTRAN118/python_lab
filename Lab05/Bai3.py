# lấy thông tin lớp học, sinh viên theo mã 

# fetchone() trả về duy nhất, fetchall() trả về một danh sách
import pyodbc



connectionString = '''DRIVER={ODBC Driver 17 for SQL Server};
                      SERVER=TUANTRAN\SQLEXPRESS;DATABASE=QLSinhVien;Trusted_Connection=yes'''


def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
       conn.close() 


MaLop = input('Nhập ID lớp: ')

def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        #    ? vi tri tham so truyen vao
        select_query = 'SELECT * FROM Lop WHERE ID = ?'
        params = (class_id,)
        cursor.execute(select_query, params)
        record = cursor.fetchone()

        print(f'Thông tin lớp có ID = {class_id} là : ')
        print("Mã lớp: ", record[0])
        print("Tên lớp:", record[1])

        close_connection(connection)


    except(Exception, pyodbc.Error) as error:
        print('Đã cso lỗi xảy ra khi thực thi!! Thông tin lỗi: ', error)

get_class_by_id(MaLop)

print('\n'*2)
# lay sinh vien theo Id



MaSV =  input('Nhập mã sinh viên: ')

def get_student_by_id(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = '''SELECT * FROM SinhVien WHERE ID = ?'''
        params = (student_id,)
        cursor.execute(select_query, params)
        records = cursor.fetchone()

        print(f'Thông tin các sinh viên có Mã Số = {student_id} là: ')
        print('Mã số \t Họ tên \t\t Mã lớp')

        print(records[0],'\t',records[1],'\t',records[2]) 


        close_connection(connection)



    except(Exception, pyodbc.Error) as error:
        print('Đã có lỗi xảy ra khi thực thi!, thông tin lỗi: ',error)

get_student_by_id(MaSV)



print('\n'*2)
# Hiển thị danh sách sinh viên theo lớp



MaLop_id = 0
TenLop_id =''

print('Bạn muốn tìm sinh viên theo mã lớp hay tên lớp (1 theo mã), (2 theo tên)')
num = int(input('Nhập lựa chọn: '))
if num ==1:
    MaLop_id = input('Nhập mã lớp: ')
elif num ==2:
    TenLop_id = input('Nhập tên lớp: ')
else:
    print('Số không hợp lệ !!')



def list_of_student_by_id(class_id, class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = '''SELECT b.ID, b.HoTen, b.MaLop, a.TenLop
                        FROM Lop a, SinhVien b
                        WHERE a.ID = b.MaLop AND (b.MaLop = ? OR a.TenLop LIKE ?) '''
        params = (class_id, class_name,)
        cursor.execute(select_query, params)
        records = cursor.fetchall()

        print(f'Danh sách các sinh viên có mã lớp = {class_id} hoặc tên lớp = {class_name} là :')
        print('Mã số \t Họ tên \t\t Mã lớp \t\t Tên Lớp')

        for row in records:
            print(row[0],'\t', row[1],'\t',row[2],'\t'*3, row[3])
 
    except(Exception, pyodbc.Error) as error:
        print('Đã có lỗi xảy ra!!, Thông tin lỗi :', error)

list_of_student_by_id(MaLop_id , TenLop_id)




print('\n'*2)
# tìm sinh viên theo mã lớp và tên 


x = input('Nhập mã số lớp: ')
y = input('Nhập mã số sinh viên: ')


def find_student(Class_id, Student_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = '''SELECT b.ID, b.HoTen, b.MaLop, a.TenLop
                            FROM Lop a, SinhVien b
                            WHERE a.ID = b.MaLop AND (b.MaLop = ? AND CHARINDEX(?,b.HoTen) >0)'''
        params = (Class_id, Student_name,)
        cursor.execute(select_query, params)
        records = cursor.fetchall()

        print(f'Danh sách tất cả sinh viên có tên {Student_name} ở lớp có mã {Class_id} là : ')
        print(f'Mã sô \t Họ tên \t\t Mã lớp \t Tên lớp')
        for row in records:
            print(row[0],'\t',row[1],'\t',row[2],'\t\t',row[3]) 

        close_connection(connection)


    except(Exception, pyodbc.Error) as error:
        print('Đã xảy ra lỗi khi thực thi chương trình!! Thông tin lỗi: ',error)

find_student(x,y)











