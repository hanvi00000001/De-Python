def S(n):
    return sum(1/(2*i) for i in range(1,n+1))
n=int(input("Nhap n: "))
print("S =",S(n))
