class MonHoc:
    def __init__(self,MaMonHoc,TenMonHoc,SoTinChi,KhoaPhuTrach):
        self.MaMonHoc=MaMonHoc; self.TenMonHoc=TenMonHoc
        self.SoTinChi=SoTinChi; self.KhoaPhuTrach=KhoaPhuTrach
    def thongtinmonhoc(self):
        print("Ma mon hoc:",self.MaMonHoc); print("Ten mon hoc:",self.TenMonHoc)
        print("So tin chi:",self.SoTinChi); print("Khoa phu trach:",self.KhoaPhuTrach)
