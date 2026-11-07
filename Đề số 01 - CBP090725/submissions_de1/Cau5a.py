class DienThoai:
    def __init__(self,MaMay,TenMay,HangSanXuat,DungLuongPin,GiaBan):
        self.MaMay=MaMay; self.TenMay=TenMay; self.HangSanXuat=HangSanXuat
        self.DungLuongPin=DungLuongPin; self.GiaBan=GiaBan
    def thongtindienthoai(self):
        print("Ma may:",self.MaMay); print("Ten may:",self.TenMay)
        print("Hang san xuat:",self.HangSanXuat); print("Dung luong pin:",self.DungLuongPin)
        print("Gia ban:",self.GiaBan)
