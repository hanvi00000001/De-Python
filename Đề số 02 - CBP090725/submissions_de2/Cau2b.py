def DoiXung(s):
    print("Chuoi doi xung." if s==s[::-1] else "Chuoi khong doi xung.")
s=input("Nhap chuoi s: ")
DoiXung(s)
