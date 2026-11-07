# Bộ đề Python mã đề 11301

Hai đề thi thực hành được tách thành hai thư mục độc lập, theo cấu trúc thư mục CBP trong bộ mẫu `Tests Python 2026`. Mỗi thư mục có PDF, submissions, test và hai phiên bản autograder.

## Cấu trúc
```text
De-Python-11301-complete/
├── README.md
├── .gitignore
├── Đề số 01 - CBP090725/
│   ├── Đề số 01-CBPYTHON.pdf
│   ├── submissions/
│   ├── submissions_de1/
│   ├── test_de1.py
│   ├── autograde_de1_v1.py
│   ├── autograde_de1_v2.py
│   └── README.md
└── Đề số 02 - CBP090725/
    ├── Đề số 02-CBPYTHON.pdf
    ├── submissions/
    ├── submissions_de2/
    ├── test_de2.py
    ├── autograde_de2_v1.py
    ├── autograde_de2_v2.py
    └── README.md
```

## Luồng xử lý tổng quát
`PDF đề/đáp án → submissions_deX/Cau*.py → test_deX.py → autograde_deX_v1/v2.py → bảng điểm`.

Các bộ test được viết từ yêu cầu và đáp án trong hai PDF. Chúng là test chức năng do bộ này xây dựng, không phải file test gốc do đề thi phát hành.
