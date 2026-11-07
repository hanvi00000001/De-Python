def TongUocSo(n):
    return sum(i for i in range(1,n+1) if n%i==0)
n=int(input("Nhap n: "))
print("Tong cac uoc so la:",TongUocSo(n))
