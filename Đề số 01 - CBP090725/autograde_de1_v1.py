import ast
import os
import subprocess
import sys
import time
import unicodedata
from pathlib import Path
from test_de1 import tests, scores

# ========================== CAU HINH GIAO DIEN ==========================
USE_COLOR = sys.stdout.isatty() or os.environ.get("FORCE_COLOR") == "1"
RESET = "\033[0m" if USE_COLOR else ""
BOLD = "\033[1m" if USE_COLOR else ""
DIM = "\033[2m" if USE_COLOR else ""
RED = "\033[91m" if USE_COLOR else ""
GREEN = "\033[92m" if USE_COLOR else ""
YELLOW = "\033[93m" if USE_COLOR else ""
CYAN = "\033[96m" if USE_COLOR else ""
BLUE = "\033[94m" if USE_COLOR else ""
MAGENTA = "\033[95m" if USE_COLOR else ""
WHITE = "\033[97m" if USE_COLOR else ""

EXAM_NAME = "Đề số 01 - Lập trình Python"
EXAM_CODE = "11301"
BASE_DIR = Path(__file__).resolve().parent / "submissions_de1"
CLASS_NAME = "DienThoai"


def paint(text, color):
    return f"{color}{text}{RESET}"


def normalize(value):
    value = unicodedata.normalize("NFC", str(value)).lower()
    return "".join(ch for ch in value if not ch.isspace()).replace(":", "").replace("=", "")


def run_code(file_path, input_data):
    start = time.perf_counter()
    try:
        result = subprocess.run(
            [sys.executable, str(file_path)],
            input=input_data,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=3,
            cwd=str(file_path.parent),
            encoding="utf-8",
            errors="replace",
        )
        elapsed = time.perf_counter() - start
        output = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        return output, result.stderr, result.returncode, elapsed, None
    except subprocess.TimeoutExpired:
        return [], "Chuong trinh vuot qua gioi han 3 giay.", None, time.perf_counter() - start, "timeout"
    except Exception as exc:
        return [], str(exc), None, time.perf_counter() - start, "runtime"


def matches(output, expected):
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
def check_class(file_path):
    """Kiem tra class va ham __init__ bang AST, khong chi tim chuoi trong source."""
    try:
        source = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name == CLASS_NAME:
                has_init = any(
                    isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and item.name == "__init__"
                    for item in node.body
                )
                return has_init, "Da tim thay class va ham __init__." if has_init else "Thieu ham __init__ trong class."
        return False, f"Khong tim thay class {CLASS_NAME}."
    except FileNotFoundError:
        return False, "Khong tim thay file bai lam."
    except SyntaxError as exc:
        return False, f"Loi cu phap tai dong {exc.lineno}: {exc.msg}"
    except Exception as exc:
        return False, str(exc)


def progress_bar(current, total, width=28):
    ratio = current / total if total else 1
    filled = int(width * ratio)
    bar = "█" * filled + "░" * (width - filled)
    return f"{GREEN}{bar}{RESET} {current:>3}/{total:<3}  {ratio * 100:5.1f}%"


def print_header(student_id):
    width = 68
    print()
    print(paint("╔" + "═" * (width - 2) + "╗", CYAN + BOLD))
    print(paint("║" + "  PYTHON AUTO GRADER  ·  HỆ THỐNG CHẤM BÀI TỰ ĐỘNG".ljust(width - 2) + "║", CYAN + BOLD))
    print(paint("╠" + "═" * (width - 2) + "╣", CYAN + BOLD))
    print(paint("║", CYAN) + f"  Kỳ thi     : {EXAM_NAME}".ljust(width - 3) + paint("║", CYAN))
    print(paint("║", CYAN) + f"  Mã đề      : {EXAM_CODE}".ljust(width - 3) + paint("║", CYAN))
    print(paint("║", CYAN) + f"  Sinh viên  : {student_id}".ljust(width - 3) + paint("║", CYAN))
    print(paint("╚" + "═" * (width - 2) + "╝", CYAN + BOLD))
    print(paint("  ĐANG KHỞI TẠO BỘ CHẤM...", DIM))
    print()


def grade(student_id="Chua nhap ten"):
    print_header(student_id)
    total_possible = sum(scores.values())
    total_earned = 0.0
    total_tests = sum(len(cases) for cases in tests.values())
    completed_tests = 0
    passed_tests = 0
    failed_tests = 0
    missing_files = 0
    question_rows = []
    started = time.perf_counter()

    print(paint("  TIẾN TRÌNH KIỂM THỬ", BOLD + WHITE))
    print("  " + "─" * 62)

    for exercise, cases in tests.items():
        file_path = BASE_DIR / (exercise + ".py")
        weight = scores[exercise]

        if exercise == "Cau5a":
            ok, message = check_class(file_path)
            earned = weight if ok else 0.0
            total_earned += earned
            passed_tests += int(ok)
            failed_tests += int(not ok)
            completed_tests += 1
            status = paint("PASS", GREEN + BOLD) if ok else paint("FAIL", RED + BOLD)
            print(f"  {status}  {exercise:<8}  Kiem tra class {CLASS_NAME}  {earned:.2f}/{weight:.2f} diem")
            if not ok:
                print(paint(f"          ↳ {message}", RED))
            question_rows.append((exercise, int(ok), 1, earned, weight))
            continue

        if not file_path.is_file():
            missing_files += 1
            failed_tests += len(cases)
            completed_tests += len(cases)
            print(f"  {paint('MISSING', YELLOW + BOLD)} {exercise:<8} Khong tim thay {file_path.name}")
            question_rows.append((exercise, 0, len(cases), 0.0, weight))
            continue

        q_passed = 0
        for index, case in enumerate(cases, 1):
            output, error, return_code, elapsed, problem = run_code(file_path, case["input"])
            expected_options = case.get("expected", case.get("expected_all", []))
            if "expected_all" in case:
                ok = return_code == 0 and all(
                    matches(output, item) for item in case["expected_all"]
                )
            else:
                ok = return_code == 0 and any(
                    matches(output, expected) for expected in expected_options
                )
            completed_tests += 1
            if ok:
                q_passed += 1
                passed_tests += 1
                marker = paint("✓", GREEN + BOLD)
                detail = paint("ĐẠT", GREEN)
            else:
                failed_tests += 1
                marker = paint("✗", RED + BOLD)
                detail = paint("TRƯỢT", RED)
                if problem == "timeout":
                    reason = "Timeout: chương trình chạy quá 3 giây."
                elif return_code not in (0, None):
                    reason = f"Chương trình kết thúc với mã lỗi {return_code}."
                elif error.strip():
                    reason = error.strip().splitlines()[-1]
                else:
                    reason = "Output không khớp đáp án mong đợi."
                print(paint(f"       ↳ {reason}", RED))
                print(paint(f"         Mong đợi: {' | '.join(map(str, expected_options))}", YELLOW))
                print(paint(f"         Thực tế : {' | '.join(output) if output else '(không có output)'}", YELLOW))

            print(f"  {marker}  {exercise:<8} Test {index:02d}/{len(cases):02d}  {detail}  {elapsed * 1000:6.1f} ms")
            print("      " + progress_bar(completed_tests, total_tests))

        earned = weight * q_passed / len(cases)
        total_earned += earned
        question_rows.append((exercise, q_passed, len(cases), earned, weight))
        q_color = GREEN if q_passed == len(cases) else (YELLOW if q_passed else RED)
        print(f"      {paint('↳ Điểm câu:', DIM)} {paint(f'{earned:.2f}/{weight:.2f}', q_color + BOLD)}")

    elapsed_total = time.perf_counter() - started
    percent = (total_earned / total_possible * 100) if total_possible else 0
    ratio = total_earned / total_possible if total_possible else 0
    final_bar = "█" * int(40 * ratio) + "░" * (40 - int(40 * ratio))

    print()
    print(paint("  ╔" + "═" * 62 + "╗", MAGENTA + BOLD))
    print(paint("  ║" + "                 BẢNG TỔNG KẾT KẾT QUẢ                 ║", MAGENTA + BOLD))
    print(paint("  ╠" + "═" * 62 + "╣", MAGENTA + BOLD))
    print(paint("  ║", MAGENTA) + "  CÂU HỎI       TEST ĐẠT       ĐIỂM ĐẠT / TỐI ĐA".ljust(62) + paint("║", MAGENTA))
    print(paint("  ╟" + "─" * 62 + "╢", MAGENTA))
    for name, got, count, earned, weight in question_rows:
        color = GREEN if got == count else (YELLOW if got else RED)
        left = f"  {name:<13} {got:>2}/{count:<11} {earned:>5.2f} / {weight:<5.2f}"
        print(paint("  ║", MAGENTA) + paint(left.ljust(62), color) + paint("║", MAGENTA))
    print(paint("  ╠" + "═" * 62 + "╣", MAGENTA + BOLD))
    print(paint("  ║", MAGENTA) + f"  TEST ĐẠT: {passed_tests}/{total_tests}".ljust(62) + paint("║", MAGENTA))
    print(paint("  ║", MAGENTA) + f"  TEST LỖI: {failed_tests}    FILE THIẾU: {missing_files}".ljust(62) + paint("║", MAGENTA))
    print(paint("  ╟" + "─" * 62 + "╢", MAGENTA))
    print(paint("  ║", MAGENTA) + f"  TỔNG ĐIỂM: {total_earned:.2f} / {total_possible:.2f}".ljust(62) + paint("║", MAGENTA + BOLD))
    print(paint("  ║", MAGENTA) + "  " + paint(final_bar, GREEN if percent >= 80 else YELLOW if percent >= 50 else RED) + f"  {percent:.1f}%".ljust(11) + paint("║", MAGENTA))
    if percent >= 90:
        ranking, rank_color = "XUẤT SẮC", GREEN + BOLD
    elif percent >= 80:
        ranking, rank_color = "GIỎI", GREEN + BOLD
    elif percent >= 65:
        ranking, rank_color = "KHÁ", CYAN + BOLD
    elif percent >= 50:
        ranking, rank_color = "TRUNG BÌNH", YELLOW + BOLD
    else:
        ranking, rank_color = "CẦN CỐ GẮNG", RED + BOLD
    print(paint("  ║", MAGENTA) + "  XẾP LOẠI: " + paint(ranking, rank_color).ljust(62 - len("  XẾP LOẠI: ")) + paint("║", MAGENTA))
    print(paint("  ║", MAGENTA) + f"  THỜI GIAN CHẤM: {elapsed_total:.2f} giây".ljust(62) + paint("║", MAGENTA))
    print(paint("  ╚" + "═" * 62 + "╝", MAGENTA + BOLD))

    if failed_tests == 0 and missing_files == 0:
        print(paint("  ✨ HOÀN TẤT! TẤT CẢ BÀI KIỂM THỬ ĐỀU ĐẠT.", GREEN + BOLD))
    else:
        print(paint("  ⚠ ĐÃ CHẤM XONG. HÃY XEM CÁC TEST TRƯỢT/FILE THIẾU Ở TRÊN.", YELLOW + BOLD))
    print()
    return total_earned


if __name__ == "__main__":
    student = " ".join(sys.argv[1:]).strip() or "Chua nhap ten"
    grade(student)
