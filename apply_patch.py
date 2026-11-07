from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT if (ROOT / "Đề số 01 - CBP090725").is_dir() else ROOT / "De-Python"
FILES = [
    PROJECT / "Đề số 01 - CBP090725" / "autograde_de1_v1.py",
    PROJECT / "Đề số 01 - CBP090725" / "autograde_de1_v2.py",
    PROJECT / "Đề số 02 - CBP090725" / "autograde_de2_v1.py",
    PROJECT / "Đề số 02 - CBP090725" / "autograde_de2_v2.py",
]

NEW_MATCHES = r'''def matches(output, expected):
    """So khop output co bien, tranh loi substring (vi du 2 khong khop 12)."""
    import re
    target = str(expected).strip()
    numeric = re.fullmatch(r"-?\d+(?:\.\d+)?", target) is not None
    for raw_line in output:
        line = raw_line.strip()
        clean_line = " ".join(line.casefold().strip(" .;").split())
        clean_target = " ".join(target.casefold().strip(" .;").split())
        if clean_line == clean_target:
            return True
        if numeric:
            tail = re.split(r"[:=]", line)[-1].strip()
            if re.fullmatch(re.escape(target) + r"[.,]?", tail):
                return True
            if re.fullmatch(re.escape(target) + r"[.,]?", line):
                return True
            # Cho phep so nam trong list/dict, nhung khong khop mot phan cua so khac.
            if re.search(r"(?<![\w.])" + re.escape(target) + r"(?![\w.])", line):
                return True
        else:
            if re.search(r"(?<!\w)" + re.escape(clean_target) + r"(?!\w)", clean_line):
                return True
        candidate = re.split(r"[:=]", line)[-1].strip()
        try:
            actual = ast.literal_eval(candidate)
            wanted = ast.literal_eval(target)
            if actual == wanted:
                return True
        except (ValueError, SyntaxError, TypeError):
            pass
    return False
'''

OLD_LINE = '            ok = return_code == 0 and any(matches(output, expected) for expected in expected_options)'
NEW_BLOCK = '''            if "expected_all" in case:
                ok = return_code == 0 and all(
                    matches(output, item) for item in case["expected_all"]
                )
            else:
                ok = return_code == 0 and any(
                    matches(output, expected) for expected in expected_options
                )'''

for path in FILES:
    if not path.exists():
        raise SystemExit(f"Khong tim thay autograder: {path}")
    source = path.read_text(encoding="utf-8")
    start = source.find("def matches(output, expected):")
    end = source.find("\ndef check_class(", start)
    if start < 0 or end < 0:
        raise SystemExit(f"Khong tim thay vung ham matches trong {path.name}")
    source = source[:start] + NEW_MATCHES + source[end+1:]
    if OLD_LINE not in source:
        raise SystemExit(f"Khong tim thay dong cham test trong {path.name}")
    source = source.replace(OLD_LINE, NEW_BLOCK, 1)
    path.write_text(source, encoding="utf-8")
    print(f"Patched: {path}")
print("Da cap nhat ca 4 autograder.")
