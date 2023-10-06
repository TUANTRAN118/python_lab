import math

class PhanSo:

    def __init__(self, tu, mau) -> None:
        self.tu = tu
        self.mau = mau

    
    def rutGon(self) -> None:
        ucln = math.gcd(self.tu, self.mau)
        tu_moi = self.tu//ucln
        mau_moi = self.mau//ucln
        return PhanSo(tu_moi, mau_moi)
    

    def tinhGiaTri(self):
        return self.tu/self.mau
    
    def mauNhoHon(self, other):
        return self.mau < other.mau
        

    def __add__(self, other) -> None:
        # tu * mau + tu * mau
        tu_moi = self.tu * other.mau + other.tu * self.mau
        mau_moi = self.mau * other.mau
        # tạo kq moi
        resulf = PhanSo(tu_moi, mau_moi)
        return resulf
    
    def __sub__(self,other) -> None:
        tu_moi = self.tu * other.mau - other.tu * self.mau
        mau_moi = self.mau * other.mau
        resulf = PhanSo(tu_moi, mau_moi)
        return resulf

    def __mul__(self,other) -> None:
        tu_moi = self.tu * other.tu
        mau_moi = self.mau * other.mau
        resulf = PhanSo(tu_moi, mau_moi)
        resulf.rutGon()
        return resulf

        
    def __truediv__(self,other) -> None:
        tu_moi = self.tu * other.mau
        mau_moi = self.mau * other.tu
        resulf = PhanSo(tu_moi, mau_moi)
        return resulf
    

    # ktra phân so am 
    def laPsAm(self):
        return self.tu * self.mau < 0
    

    


    # in dang chuoi
    def __str__(self) -> str:
        return(f"{self.tu}/{self.mau}")
    

    # hanh vi lop doi tuong
    def print(self):
        print(f"{self.tu}/{self.mau}")
    








# a = PhanSo(2,3)
# b = PhanSo(3,5)

# print(f"a = {a.tu} / {a.tu}")
# print(f"b = {b.tu} / {b.tu}")


# print(f"{a} + {b} = {a + b}")
# print(f"{a} - {b} = {a - b}")
# print(f"{a} * {b} = {a * b}")
# print(f"{a} / {b} = {a / b}")






