"""Cau 3 - De thi ca 7h30: danh sach so nguyen."""

def main():
    danh_sach = []
    while True:
        x = int(input("Nhap phan tu (nhap 0 de dung): "))
        if x == 0:
            break
        danh_sach.append(x)

    print("Danh sach vua nhap:", danh_sach)

    tong_so_duong_chan = sum(x for x in danh_sach if x > 0 and x % 2 == 0)
    print("Tong cac so duong chan:", tong_so_duong_chan)

    k = int(input("Nhap k can dem: "))
    print(f"So lan xuat hien cua {k}:", danh_sach.count(k))


if __name__ == "__main__":
    main()
