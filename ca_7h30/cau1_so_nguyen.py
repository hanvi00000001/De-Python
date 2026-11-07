"""Cau 1 - De thi ca 7h30.
Nhap n trong [1, 1500], dem chu so le va tinh S = 1/2 + 1/4 + ... + 1/(2n).
"""

def dem_chu_so_le(n: int) -> int:
    dem = 0
    while n > 0:
        if (n % 10) % 2 != 0:
            dem += 1
        n //= 10
    return dem


def tinh_s(n: int) -> float:
    return sum(1 / (2 * i) for i in range(1, n + 1))


def main():
    n = int(input("Nhap so nguyen duong n (1 <= n <= 1500): "))
    while n < 1 or n > 1500:
        n = int(input("Gia tri khong hop le. Nhap lai n (1 <= n <= 1500): "))

    print("So luong chu so le:", dem_chu_so_le(n))
    print("S =", tinh_s(n))


if __name__ == "__main__":
    main()
