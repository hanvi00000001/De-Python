danhsach=[]
while True:
    x=int(input("Nhap danh sach: "))
    if x==0: break
    danhsach.append(x)
k=int(input("Nhap k: "))
dem=danhsach.count(k)
if dem==0: print("Khong co phan tu",k,"trong danh sach")
else: print("So lan xuat hien cua",k,"la:",dem)
