n=int(input("Nhap so luong may tinh: "))
while n<=0: n=int(input("Nhap so luong may tinh: "))
maytinh={}
for _ in range(n):
    sohieu=input("Nhap so hieu may tinh: ")
    bonho=int(input("Nhap dung luong bo nho: "))
    ocung=int(input("Nhap dung luong o cung: "))
    hang=input("Nhap hang san xuat: ")
    nam=int(input("Nhap nam san xuat: "))
    maytinh[sohieu]=[bonho,ocung,hang,nam]
print(maytinh)
