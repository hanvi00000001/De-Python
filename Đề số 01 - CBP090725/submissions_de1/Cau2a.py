s=input("Nhap chuoi s: ")
dem=sum(ch.isupper() for ch in s)
if dem==0: print("Chuoi khong co ky tu chu hoa.")
else: print("So ky tu chu hoa:",dem)
