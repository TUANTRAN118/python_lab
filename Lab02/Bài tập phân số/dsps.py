from phan_so import PhanSo
import math


class DanhSachPhanSo:
    def __init__(self) -> None:
        self.ds = []

    def them(self,ps: PhanSo):
        self.ds.append(ps)

    def xuat(self):
        for ps in self.ds:
            print(ps)

    def DocTuFile(self, fileName):
        with open(fileName,'r',encoding='utf-8') as file:
            for row in file:
                du_lieu = row.split('/')
                self.them(PhanSo(int(du_lieu[0]), int(du_lieu[1])))


    # Đếm ps âm trong mảng 
    def DemPsAm(self):
        dem = 0 
        for ps in self.ds:
            if ps.laPsAm():
                dem +=1
        return dem
    

    # tìm phân số dương nhỏ nhất
    def timPhanSoDuongNhoNhat(self):
        ps_nho_nhat = 1_000_000_000
        for ps in self.ds:
            x = ps.tinhGiaTri()
            if x > 0 and x < ps_nho_nhat:
                ps_nho_nhat =x 
        return ps_nho_nhat
    

    # tìm danh sách phân số dương nhỏ nhất
    def timDSPhanSoDuongNhoNhat(self):
        gt_nho_nhat = self.timPhanSoDuongNhoNhat()
        kq = DanhSachPhanSo()
        for ps in self.ds:
            if math.isclose(ps.tinhGiaTri(),gt_nho_nhat):
                kq.them(ps)
        return kq
    

    # sắp xếp mảng tằng theo mẫu bằng cách đổi chỗ 
    def sapXepTangTheoMau(self):
        chieu_dai = len(self.ds)
        
        for i in range(chieu_dai):
            for j in range(i + 1, chieu_dai):
                if self.ds[j].mauNhoHon(self.ds[i]):
                    (self.ds[i], self.ds[j]) = (self.ds[j], self.ds[i])




    # tính tổng các ps âm trong mảng
    def SumPsAm(self):
        total = 0 
        for ps in self.ds:
            if ps.laPsAm():
                total += ps.tu / ps.mau 
        return total
    






    #  xóa phân số x trong mảng
    # def XoaPhanSo(self, x:PhanSo):
    #     for ps in self.ds:
    #         if ps == x:
    #             self.ds.remove(ps)

    def xoaPhanSo(self, x: PhanSo):
        while x in self.ds:
            self.ds.remove(x) 



    
            
            
            







