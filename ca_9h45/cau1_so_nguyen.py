"""Cau 1 - De thi ca 9h45.
Nhap n trong [1, 99], tinh tong uoc va S = 1**1 + 2**2 + ... + n**n.
"""

def tong_uoc_so(n: int) -> int:
    return sum(i for i in range(1, n + 1) if n % i == 0)


def tinh_s(n: int) -> int:
    return sum(i ** i for i in range(1, n + 1))


def main():
    n = int(input("Nhap so nguyen duong n (1 <= n <= 99): "))
    while n < 1 or n > 99:
        n = int(input("Gia tri khong hop le. Nhap lai n (1 <= n <= 99): "))

    print("Tong cac uoc so:", tong_uoc_so(n))
    print("S =", tinh_s(n))


if __name__ == "__main__":
    main()
