"""Cau 4 - De thi ca 9h45: quan ly may tinh bang tu dien."""

def main():
    so_luong = int(input("Nhap so luong may tinh: "))
    while so_luong < 0:
        so_luong = int(input("So luong khong duoc am. Nhap lai: "))

    tu_dien_may_tinh = {}
    for i in range(so_luong):
        print(f"\nNhap thong tin may tinh thu {i + 1}:")
        so_hieu = input("So hieu may tinh: ").strip()
        bo_nho = int(input("Dung luong bo nho: "))
        o_cung = int(input("Dung luong o cung: "))
        hang_san_xuat = input("Hang san xuat: ").strip()
        nam_san_xuat = int(input("Nam san xuat: "))

        tu_dien_may_tinh[so_hieu] = {
            "DungLuongBoNho": bo_nho,
            "DungLuongOCung": o_cung,
            "HangSanXuat": hang_san_xuat,
            "NamSanXuat": nam_san_xuat,
        }

    print("\nTu dien may tinh:", tu_dien_may_tinh)

    so_hieu_can_xoa = input("\nNhap so hieu may tinh can xoa: ").strip()
    if so_hieu_can_xoa in tu_dien_may_tinh:
        del tu_dien_may_tinh[so_hieu_can_xoa]
        print(f"Da xoa may tinh co so hieu {so_hieu_can_xoa}.")
    else:
        print("Khong co may tinh can tim.")

    print("Tu dien sau khi xu ly:", tu_dien_may_tinh)


if __name__ == "__main__":
    main()
