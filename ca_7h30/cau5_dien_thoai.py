"""Cau 5 - De thi ca 7h30: lop DienThoai."""

class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print("Ma may:", self.MaMay)
        print("Ten may:", self.TenMay)
        print("Hang san xuat:", self.HangSanXuat)
        print("Dung luong pin:", self.DungLuongPin)
        print("Gia ban:", self.GiaBan)


def main():
    DT01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    DT02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

    print("Thong tin dien thoai 1:")
    DT01.thongtindienthoai()
    print("\nThong tin dien thoai 2:")
    DT02.thongtindienthoai()


if __name__ == "__main__":
    main()
