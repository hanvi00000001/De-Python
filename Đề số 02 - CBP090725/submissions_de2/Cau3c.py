ds=[]
while True:
    x=int(input("Nhap danh sach: "))
    if x==0: break
    ds.append(x)
k=int(input("Nhap k: "))
dem=ds.count(k)
if dem==0: print(f"{k} khong co trong danh sach")
else: print(f"{k} xuat hien {dem} lan")
