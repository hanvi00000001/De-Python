# De-Python

Repository lưu đề thi và lời giải môn **Lập trình Python** (mã môn học `229152`).

## Cấu trúc lời giải

Mỗi đề được chia thành một thư mục gồm 5 chương trình Python độc lập, tương ứng với 5 câu trong đề.

```text
De-Python/
├── README.md
├── ca_7h30/
│   ├── cau1_so_nguyen.py
│   ├── cau2_chuoi.py
│   ├── cau3_danh_sach.py
│   ├── cau4_tu_dien_sach.py
│   └── cau5_dien_thoai.py
└── ca_9h45/
    ├── cau1_so_nguyen.py
    ├── cau2_chuoi.py
    ├── cau3_danh_sach.py
    ├── cau4_tu_dien_may_tinh.py
    └── cau5_mon_hoc.py
```

> Các chương trình được viết lại theo nội dung đề và đáp án mẫu trong hai PDF. Một số lỗi gõ/OCR và lỗi cú pháp trong bản đáp án scan đã được chỉnh để mã có thể chạy bằng Python 3. Mỗi file chạy độc lập, không cần thư viện ngoài.

---

## Đề thi ca 7h30

### Câu 1 – Số nguyên
- Nhập số nguyên `n`, yêu cầu `1 <= n <= 1500`.
- Đếm số chữ số lẻ của `n`.
- Tính tổng `S = 1/2 + 1/4 + 1/6 + ... + 1/(2n)`.

**File:** [`ca_7h30/cau1_so_nguyen.py`](ca_7h30/cau1_so_nguyen.py)

### Câu 2 – Chuỗi
- Đếm ký tự chữ hoa.
- Kiểm tra chuỗi đối xứng.
- Tính tổng các chữ số xuất hiện trong chuỗi.

**File:** [`ca_7h30/cau2_chuoi.py`](ca_7h30/cau2_chuoi.py)

### Câu 3 – Danh sách
- Nhập số nguyên đến khi nhập `0`.
- Tính tổng các số dương chẵn.
- Đếm số lần xuất hiện của phần tử `k`.

**File:** [`ca_7h30/cau3_danh_sach.py`](ca_7h30/cau3_danh_sach.py)

### Câu 4 – Từ điển sách
- Nhập mã sách, tên sách, tác giả, nhà xuất bản và năm xuất bản.
- Lưu thông tin theo mã sách trong từ điển.
- Tìm và xóa sách theo mã; nếu không có thì thông báo.

**File:** [`ca_7h30/cau4_tu_dien_sach.py`](ca_7h30/cau4_tu_dien_sach.py)

### Câu 5 – Lớp `DienThoai`
- Thuộc tính: `MaMay`, `TenMay`, `HangSanXuat`, `DungLuongPin`, `GiaBan`.
- Phương thức: `__init__()` và `thongtindienthoai()`.
- Tạo hai đối tượng DT01 (iPhone 15 Pro) và DT02 (Galaxy S24 Ultra).

**File:** [`ca_7h30/cau5_dien_thoai.py`](ca_7h30/cau5_dien_thoai.py)

---

## Đề thi ca 9h45

### Câu 1 – Số nguyên
- Nhập số nguyên `n`, yêu cầu `1 <= n <= 99`.
- Tính tổng tất cả các ước số của `n`.
- Tính `S = 1^1 + 2^2 + 3^3 + ... + n^n` (theo biểu thức và đáp án mẫu trong PDF).

**File:** [`ca_9h45/cau1_so_nguyen.py`](ca_9h45/cau1_so_nguyen.py)

### Câu 2 – Chuỗi
- Đếm ký tự chữ thường.
- Kiểm tra chuỗi đối xứng.
- Chuyển ký tự đầu mỗi từ thành chữ hoa bằng `title()`.

**File:** [`ca_9h45/cau2_chuoi.py`](ca_9h45/cau2_chuoi.py)

### Câu 3 – Danh sách
- Nhập số nguyên đến khi nhập `0`.
- In các số dương chẵn.
- Đếm số lần xuất hiện của phần tử `k`.

**File:** [`ca_9h45/cau3_danh_sach.py`](ca_9h45/cau3_danh_sach.py)

### Câu 4 – Từ điển máy tính
- Nhập số hiệu, dung lượng bộ nhớ, dung lượng ổ cứng, hãng sản xuất và năm sản xuất.
- Lưu thông tin theo số hiệu máy tính trong từ điển.
- Tìm và xóa máy tính theo số hiệu; nếu không có thì thông báo.

**File:** [`ca_9h45/cau4_tu_dien_may_tinh.py`](ca_9h45/cau4_tu_dien_may_tinh.py)

### Câu 5 – Lớp `MonHoc`
- Thuộc tính: `MaMonHoc`, `TenMonHoc`, `SoTinChi`, `KhoaPhuTrach`.
- Phương thức: `__init__()` và `thongtinmonhoc()`.
- Tạo hai đối tượng: (229008, Cơ sở dữ liệu, 3, Công nghệ thông tin) và (224604, Tiếng Anh 1, 2, Ngoại ngữ).

**File:** [`ca_9h45/cau5_mon_hoc.py`](ca_9h45/cau5_mon_hoc.py)

---

## Cách chạy chương trình

Mở Terminal/PowerShell tại thư mục repository, sau đó chạy file cần làm. Ví dụ:

```powershell
python ca_7h30/cau1_so_nguyen.py
python ca_9h45/cau5_mon_hoc.py
```

Các file có phần `if __name__ == "__main__":` nên có thể chạy trực tiếp. Các hàm và lớp cũng có thể được import để kiểm thử hoặc tái sử dụng.
