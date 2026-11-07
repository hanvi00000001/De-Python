ds=[]
while True:
    x=int(input("Nhap danh sach: "))
    if x==0: break
    ds.append(x)
duong_chan=[x for x in ds if x>0 and x%2==0]
if duong_chan: print("Cac so duong chan co trong danh sach:",duong_chan)
else: print("Khong co so duong chan trong danh sach.")
