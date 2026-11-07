tests = {
    "Cau1a": [
        {"input": "0\n1\n", "expected": ["1"]},
        {"input": "100\n99\n", "expected": ["99"]},
    ],
    "Cau1b": [
        {"input": "12\n", "expected": ["28"]},
        {"input": "7\n", "expected": ["8"]},
    ],
    "Cau1c": [
        {"input": "1\n", "expected": ["1"]},
        {"input": "3\n", "expected": ["32"]},
    ],
    "Cau2a": [
        {"input": "Hello WORLD\n", "expected": ["4"]},
        {"input": "123 abc\n", "expected": ["3"]},
    ],
    "Cau2b": [
        {"input": "level\n", "expected": ["chuoi doi xung"]},
        {"input": "hello\n", "expected": ["chuoi khong doi xung"]},
    ],
    "Cau2c": [
        {"input": "lap trinh python\n", "expected": ["Lap Trinh Python"]},
        {"input": "hello WORLD\n", "expected": ["Hello World"]},
    ],
    "Cau3a": [
        {"input": "1\n-2\n4\n0\n", "expected": ["[1, -2, 4]"]},
    ],
    "Cau3b": [
        {"input": "2\n-4\n6\n3\n0\n", "expected": ["[2, 6]"]},
        {"input": "-2\n-4\n0\n", "expected": ["khong co so duong chan"]},
    ],
    "Cau3c": [
        {"input": "2\n3\n2\n0\n2\n", "expected": ["2 xuat hien 2 lan", "2 xuat hien 2"]},
        {"input": "1\n0\n9\n", "expected": ["9 khong co trong danh sach"]},
    ],
    "Cau4a": [
        {"input": "1\nPC01\n8\n512\nDell\n2022\n", "expected": ["'PC01': [8, 512, 'Dell', 2022]"]},
    ],
    "Cau4b": [
        {"input": "1\nPC01\n8\n512\nDell\n2022\nPC01\n", "expected": ["da duoc xoa", "{}"]},
        {"input": "1\nPC01\n8\n512\nDell\n2022\nPC99\n", "expected": ["khong co so hieu may tinh can xoa"]},
    ],
    "Cau5a": [
        {"input": "", "expected": ["__CLASS_DEFINITION__"]},
    ],
    "Cau5b": [
        {"input": "", "expected": ["229008", "Co so du lieu", "224604", "Tieng Anh 1"]},
    ],
}
scores = {"Cau1a":0.5,"Cau1b":0.75,"Cau1c":0.75,"Cau2a":1.0,"Cau2b":0.5,"Cau2c":0.5,"Cau3a":0.75,"Cau3b":0.75,"Cau3c":0.5,"Cau4a":1.5,"Cau4b":0.5,"Cau5a":1.0,"Cau5b":1.0}
