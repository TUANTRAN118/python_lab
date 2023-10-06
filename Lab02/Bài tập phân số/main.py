from phan_so import PhanSo
from dsps import DanhSachPhanSo






ds = DanhSachPhanSo()
ds.DocTuFile("D:\\Python\\Lab02\\Bài tập phân số\\data.txt")
ds.xuat()



# Đếm phân số âm trong mảng 
dem = ds.DemPsAm()
print(f'Mảng có {dem} phân số âm')


# Phan so duong nho nhat 1 phan tu
ps = ds.timPhanSoDuongNhoNhat()
print(f'Phân số dương nhỏ nhất tỏng mảng là: {ps}')

# Ds phân số dương nhỏ nhất 
print('Danh sách Phân số dương nhỏ nhất là')
ps = ds.timDSPhanSoDuongNhoNhat()
ps.xuat()


# Tổng phân số âm trong mảng
total = ds.SumPsAm()
print(f'Tổng các phân số âm trong mảng là : {total}')


#  Xuat ds phân số tăng theo mẫu
print('Danh sách ban đầu')
ds.xuat()
print('-'*50)
print('Danh sách sau khi tăng theo mẫu')
ds.sapXepTangTheoMau()
ds.xuat()





# xoa phan so x
x = PhanSo(4,6)
ds.xoaPhanSo(x)
print(f"Danh sách phân số sau khi xóa phân số {x}: ")
ds.xuat()


























# a = PhanSo(1,2)
# b = PhanSo(3,4)
# c = PhanSo(4,6)
# d = PhanSo(8,2)

# ds.them(a)
# ds.them(b)
# ds.them(c)
# ds.them(d)