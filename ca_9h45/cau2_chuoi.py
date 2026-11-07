"""Cau 2 - De thi ca 9h45: chu thuong, doi xung va viet hoa dau moi tu."""

def main():
    s = input("Nhap chuoi s: ")

    so_chu_thuong = sum(1 for ch in s if ch.islower())
    print("So ky tu chu thuong:", so_chu_thuong)

    if s == s[::-1]:
        print("Chuoi doi xung.")
    else:
        print("Chuoi khong doi xung.")

    chuoi_viet_hoa = s.title()
    print("Chuoi sau khi viet hoa ky tu dau moi tu:", chuoi_viet_hoa)


if __name__ == "__main__":
    main()
