import datetime

class SinhVien:
    # dat bien cho lop
    truong = "Đại học Đà Lạt"
    # hàm khởi tạo, tạo lập, gán các thuộc tính
    def __init__(self, maSo:int, hoTen:str, ngaySinh: datetime) -> None:
        self.__maSo = maSo  #thuộc tính private,__ , truy cập các thuộc tính hoặc đối tượng
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    # truy xuat toi thuoc tinh thong qua truong maSo
    # property xem như la thuoc tinh getter (phuong thuc lay gia tri thuoc tinh)
    @property
    def maSo(self):
        return self.__maSo
    
    # setter phuong thuc gan gia tri thuoc tinh
    @maSo.setter
    def maSo(self, maso):
        if self.LaMaSoHopLe(maso):
            self.__maSo = maso

    #Phương thức tĩnh(k truy xuất đến thuộc tính, hành vi của class)
    @staticmethod
    def LaMaSoHopLe(maso:int):
        #len dùng để trả về số lượng phần tử (độ dài) của một đối tượng.
        return len(str(maso)) == 7


    # truy xuất tới biến thành viên, k truy xuất tới thuộc tính riêng
    @classmethod
    def doiTenTruong (self, tenmoi):
        self.truong = tenmoi

    # ghi đề phương thức
    def __str__(self) -> str:
        return f'{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}'

    # hành vi lớp đối tượng
    def Xuat(self):
        print(f'{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}')




# self đại diện cho đối tg đc tạo
class DanhSachSV:
    # khởi tạo
    def __init__(self) -> None:
        self.dssv = []


    # append them vao cuoi chuoi
    def themSinhVien(self, sv:SinhVien):
        self.dssv.append(sv)

    def Xuat(self):
        for sv in self.dssv:
            print(sv)

    def TimSvtheoMssv(self, mssv:int):
        return [sv for sv in self.dssv if sv.maSo == mssv]
    
    # Tim sv theo MS trả về vị trí
    def TimVtSvtheoMSSV(self, mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo ==mssv:
                return i
        return -1


dssv = DanhSachSV()

sv1 = SinhVien("21001", "Nguyễn Văn A", "01/01/2009")
sv2 = SinhVien("21002", "Nguyễn Văn B", "01/02/2004")
sv3 = SinhVien("21003", "Nguyễn Văn C", "03/05/2002")
sv4 = SinhVien("21004", "Nguyễn Văn D", "02/04/2005")

dssv.themSinhVien(sv1)
dssv.themSinhVien(sv2)
dssv.themSinhVien(sv3)
dssv.themSinhVien(sv4)

dssv.Xuat()



find = dssv.TimSvtheoMssv("21003")
for sv in find: 
    print(f"Sinh viên thứ có mã số {sv.maSo} là: {sv}")


location = dssv.TimVtSvtheoMSSV("21003")
print(f"Sinh viên thứ {location +1} có vị trí thứ {location +1} là: {dssv.dssv[location]}")














