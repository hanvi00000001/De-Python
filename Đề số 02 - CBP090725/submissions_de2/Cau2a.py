s=input("Nhap chuoi s: ")
dem=sum(ch.islower() for ch in s)
if dem==0: print("Chuoi khong co ky tu chu thuong.")
else: print("So ky tu chu thuong trong chuoi:",dem)
