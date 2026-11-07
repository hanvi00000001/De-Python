tests = {
    "Cau1a": [
        {"input": "0\n2\n", "expected": ["2"]},
        {"input": "1501\n1500\n", "expected": ["1500"]},
    ],
    "Cau1b": [
        {"input": "635\n", "expected": ["2"]},
        {"input": "2468\n", "expected": ["0"]},
        {"input": "13579\n", "expected": ["5"]},
    ],
    "Cau1c": [
        {"input": "1\n", "expected": ["0.5"]},
        {"input": "3\n", "expected": [str(1/2+1/4+1/6)]},
    ],
    "Cau2a": [
        {"input": "AbC DeF!\n", "expected": ["4"]},
        {"input": "python\n", "expected": ["khong co ky tu chu hoa"]},
    ],
    "Cau2b": [
        {"input": "abba\n", "expected": ["chuoi doi xung"]},
        {"input": "python\n", "expected": ["chuoi khong doi xung"]},
    ],
    "Cau2c": [
        {"input": "a1b2c3\n", "expected": ["6"]},
        {"input": "abc\n", "expected": ["0"]},
    ],
    "Cau3a": [
        {"input": "1\n-2\n3\n0\n", "expected": ["[1, -2, 3]"]},
    ],
    "Cau3b": [
        {"input": "2\n-4\n6\n3\n0\n", "expected": ["8"]},
        {"input": "-2\n3\n0\n", "expected": ["khong co so duong chan"]},
    ],
    "Cau3c": [
        {"input": "2\n3\n2\n0\n2\n", "expected": ["2 la: 2", "2 la 2"]},
        {"input": "1\n0\n9\n", "expected": ["khong co phan tu 9"]},
    ],
    "Cau4a": [
        {"input": "1\nB01\nPython Co Ban\nAn\nNXB Tre\n2020\n", "expected": ["'B01': ['Python Co Ban', 'An', 'NXB Tre', 2020]"]},
    ],
    "Cau4b": [
        {"input": "1\nB01\nPython\nAn\nNXB Tre\n2020\nB01\n", "expected": ["da duoc xoa", "{}"]},
        {"input": "1\nB01\nPython\nAn\nNXB Tre\n2020\nX99\n", "expected": ["khong tim thay cuon sach can xoa"]},
    ],
    "Cau5a": [
        {"input": "", "expected": ["__CLASS_DEFINITION__"]},
    ],
    "Cau5b": [
        {"input": "", "expected": ["DT01", "iPhone 15 Pro", "DT02", "Galaxy S24 Ultra"]},
    ],
}
scores = {"Cau1a":0.5,"Cau1b":0.75,"Cau1c":0.75,"Cau2a":0.75,"Cau2b":0.5,"Cau2c":0.75,"Cau3a":0.75,"Cau3b":0.75,"Cau3c":0.5,"Cau4a":1.5,"Cau4b":0.5,"Cau5a":1.0,"Cau5b":1.0}
