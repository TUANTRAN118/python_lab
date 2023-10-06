# import pyodbc

# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=TUANTRAN\SQLEXPRESS;Trusted_Connection=yes')
# cursor = conn.cursor()
# cursor.execute("SELECT @@version")
# # conn.close()
# db_version = cursor.fetchone()
# print("Ban dang dung he quan tri CSDL SQL server version ", db_version)



import sqlite3

def get_connection():
    connection = sqlite3.connect('QLSinhVien.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select sqlite_version();")
        db_version = cursor.fetchone()
        print("Bạn đang sử dụng SQLite phiên bản : ", db_version)
        close_connection(connection)


    except(Exception, sqlite3.Error) as error:
        print("Đã có lỗi. Thông tin lỗi: ",error )
read_database_version()








