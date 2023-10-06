def doi_giay_sang_gio_phut_giay(soGiay):
    gio = soGiay // 3600
    soGiay %= 3600
    phut = soGiay // 60
    giay = soGiay % 60
    return f"{gio}:{phut}:{giay}"

soGiay = int(input("Nhập số giây: "))
ketQua = doi_giay_sang_gio_phut_giay(soGiay)
print("Kết quả:", ketQua)
