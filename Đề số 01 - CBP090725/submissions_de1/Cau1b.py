def DemChuSoLe(n):
    dem=0
    while n!=0:
        if (n%10)%2!=0: dem+=1
        n//=10
    return dem
n=int(input("Nhap n: "))
print("So luong chu so le la:",DemChuSoLe(n))
