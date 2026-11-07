"""Cau 3 - De thi ca 9h45: danh sach so nguyen."""

def main():
    danh_sach = []
    while True:
        x = int(input("Nhap phan tu (nhap 0 de dung): "))
        if x == 0:
            break
        danh_sach.append(x)

    print("Danh sach vua nhap:", danh_sach)

    so_duong_chan = [x for x in danh_sach if x > 0 and x % 2 == 0]
    if so_duong_chan:
        print("Cac so duong chan trong danh sach:", so_duong_chan)
    else:
        print("Khong co so duong chan trong danh sach.")

    k = int(input("Nhap k can dem: "))
    dem = danh_sach.count(k)
    if dem == 0:
        print(f"{k} khong co trong danh sach.")
    else:
        print(f"{k} xuat hien {dem} lan.")


if __name__ == "__main__":
    main()
