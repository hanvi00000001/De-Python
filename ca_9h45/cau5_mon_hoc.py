"""Cau 5 - De thi ca 9h45: lop MonHoc."""

class MonHoc:
    def __init__(self, MaMonHoc, TenMonHoc, SoTinChi, KhoaPhuTrach):
        self.MaMonHoc = MaMonHoc
        self.TenMonHoc = TenMonHoc
        self.SoTinChi = SoTinChi
        self.KhoaPhuTrach = KhoaPhuTrach

    def thongtinmonhoc(self):
        print("Ma mon hoc:", self.MaMonHoc)
        print("Ten mon hoc:", self.TenMonHoc)
        print("So tin chi:", self.SoTinChi)
        print("Khoa phu trach:", self.KhoaPhuTrach)


def main():
    CSDL = MonHoc(229008, "Co so du lieu", 3, "Cong nghe thong tin")
    TA1 = MonHoc(224604, "Tieng Anh 1", 2, "Ngoai ngu")

    print("Thong tin mon hoc 1:")
    CSDL.thongtinmonhoc()
    print("\nThong tin mon hoc 2:")
    TA1.thongtinmonhoc()


if __name__ == "__main__":
    main()
