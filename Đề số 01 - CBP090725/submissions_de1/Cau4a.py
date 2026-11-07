from datetime import datetime
n=int(input("Nhap so luong sach (n>0): "))
while n<=0: n=int(input("Nhap so luong sach (n>0): "))
tudien={}
namhientai=datetime.now().year
for _ in range(n):
    ma=input("Nhap ma so sach: ")
    ten=input("Nhap ten sach: ")
    tacgia=input("Nhap ten tac gia: ")
    nxb=input("Nhap nha xuat ban: ")
    nam=int(input("Nhap nam xuat ban: "))
    while nam>namhientai: nam=int(input(f"Nam xuat ban khong hop le, vui long nhap nam <= {namhientai}: "))
    tudien[ma]=[ten,tacgia,nxb,nam]
print(tudien)
