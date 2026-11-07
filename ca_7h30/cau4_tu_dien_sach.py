"""Cau 4 - De thi ca 7h30: quan ly sach bang tu dien."""
from datetime import date


def main():
    so_luong = int(input("Nhap so luong sach (n > 0): "))
    while so_luong <= 0:
        so_luong = int(input("So luong phai > 0. Nhap lai: "))

    tu_dien_sach = {}
    nam_hien_tai = date.today().year

    for i in range(so_luong):
        print(f"\nNhap thong tin sach thu {i + 1}:")
        ma_so = input("Ma so sach: ").strip()
        ten_sach = input("Ten sach: ").strip()
        ten_tac_gia = input("Ten tac gia: ").strip()
        nha_xuat_ban = input("Nha xuat ban: ").strip()
        nam_xuat_ban = int(input("Nam xuat ban: "))
        while nam_xuat_ban > nam_hien_tai:
            nam_xuat_ban = int(input(
                f"Nam xuat ban khong hop le, nhap nam <= {nam_hien_tai}: "
            ))

        tu_dien_sach[ma_so] = {
            "TenSach": ten_sach,
            "TenTacGia": ten_tac_gia,
            "NhaXuatBan": nha_xuat_ban,
            "NamXuatBan": nam_xuat_ban,
        }

    print("\nTu dien sach:", tu_dien_sach)

    ma_can_xoa = input("\nNhap ma so sach can xoa: ").strip()
    if ma_can_xoa in tu_dien_sach:
        del tu_dien_sach[ma_can_xoa]
        print(f"Da xoa cuon sach co ma so {ma_can_xoa}.")
    else:
        print("Khong tim thay cuon sach can xoa.")

    print("Tu dien sau khi xu ly:", tu_dien_sach)


if __name__ == "__main__":
    main()
