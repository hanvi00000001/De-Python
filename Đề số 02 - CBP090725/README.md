# Đề số 02 - CBP090725

## Thành phần
- PDF đề thi kèm đáp án chính thức.
- `submissions_de2/`: bài giải, mỗi ý nhỏ là một file `Cau*.py`.
- `test_de2.py`: bộ test đầu vào/đầu ra cho từng bài.
- `autograde_de2_v1.py`, `autograde_de2_v2.py`: hai phiên bản chương trình chấm tự động.
- `submissions/`: thư mục tương thích với cách tổ chức bài nộp tổng quát trong bộ mẫu.

## Luồng xử lý
1. Sinh viên đặt các file bài làm vào `submissions_de2/`.
2. Bộ chấm đọc test từ `test_de2.py`.
3. Autograder chạy từng file bằng subprocess, cấp input mẫu, thu stdout, so sánh với expected và giới hạn 3 giây/test.
4. Điểm từng ý được tính theo trọng số trong đề, tổng tối đa 10 điểm.

## Chạy chấm
Mở terminal tại thư mục này và chạy:
```bash
python autograde_de2_v1.py MSSV
# hoặc
python autograde_de2_v2.py MSSV
```


## Chạy chương trình chấm bài (giao diện nâng cấp)

Mở Terminal trong VS Code tại thư mục của đề tương ứng, sau đó chạy:

**Đề số 01**
```powershell
python autograde_de1_v1.py "Nguyen Van A"
# Hoặc
python autograde_de1_v2.py "Nguyen Van A"
```

**Đề số 02**
```powershell
python autograde_de2_v1.py "Nguyen Van A"
# Hoặc
python autograde_de2_v2.py "Nguyen Van A"
```

Có thể thay `Nguyen Van A` bằng tên sinh viên. Nếu bỏ tên, chương trình hiển thị `Chua nhap ten`.

Autograder hiển thị banner, tiến trình kiểm thử, thời gian chạy từng test, bảng điểm từng câu, tổng điểm, tỷ lệ đạt và xếp loại. Khi test thất bại, chương trình in lý do cùng output mong đợi và output thực tế. Bộ chấm vẫn sử dụng các test và trọng số điểm trong `test_de1.py` / `test_de2.py`; phần nâng cấp tập trung vào giao diện và báo lỗi.
