danhsach=[]
while True:
    x=int(input("Nhap danh sach: "))
    if x==0: break
    danhsach.append(x)
tong=sum(x for x in danhsach if x>0 and x%2==0)
if tong!=0: print("Tong cac so duong chan trong danh sach:",tong)
else: print("Khong co so duong chan trong danh sach.")
