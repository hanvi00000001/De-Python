"""Cau 2 - De thi ca 7h30: chu hoa, doi xung va tong chu so."""

def la_chuoi_doi_xung(s: str) -> bool:
    return s == s[::-1]


def tong_cac_chu_so(s: str) -> int:
    return sum(int(ch) for ch in s if ch.isdigit())


def main():
    s = input("Nhap chuoi s: ")

    so_chu_hoa = sum(1 for ch in s if ch.isupper())
    print("So ky tu chu hoa:", so_chu_hoa)

    if la_chuoi_doi_xung(s):
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")

    print("Tong cac chu so trong chuoi:", tong_cac_chu_so(s))


if __name__ == "__main__":
    main()
