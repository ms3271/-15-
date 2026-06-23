# 라이브러리 로드: 시스템 제어, 무작위 추출, 날짜 및 시간 처리를 위한 모듈
import os
import random
import string
import json
from datetime import datetime

# ==========================================
# 기능 1: 안전한 비밀번호 생성기
# ==========================================
def generate_password():
    print("\n기능 1 안전한 비밀번호 생성기")
    try:
        length = int(input("생성할 비밀번호 길이를 입력하세요 (최소 8자): "))
        if length < 8:
            print("보안을 위해 8자 이상으로 설정해 주세요. 기본값 8자로 생성합니다.")
            length = 8
    except ValueError:
        print("올바른 숫자가 아닙니다. 기본값 8자로 생성합니다.")
        length = 8

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    
    print(f"생성된 비밀번호: {password}")
    return password

# ==========================================
# 기능 2: 텍스트 기반 메모장
# ==========================================
MEMO_FILE = "mymemo.txt"

def simple_notepad():
    print("\n기능 2 텍스트 기반 메모장")
    print("1: 메모 읽기 | 2: 새 메모 쓰기 (기존 내용 삭제) | 3: 메모 이어 쓰기")
    sub_menu = input("원하는 작업 번호를 선택하세요: ").strip()
    
    if sub_menu == "1":
        if os.path.exists(MEMO_FILE):
            with open(MEMO_FILE, "r", encoding="utf-8") as f:
                print(f"\n[{MEMO_FILE} 내용]\n{f.read()}")
        else:
            print("저장된 메모 파일이 없습니다.")
    elif sub_menu in ("2", "3"):
        mode = "w" if sub_menu == "2" else "a"
        content = input("저장할 내용을 입력하세요: ")
        with open(MEMO_FILE, mode, encoding="utf-8") as f:
            f.write(content + "\n")
        print("메모가 성공적으로 저장되었습니다.")
    else:
        print("잘못된 선택입니다.")

# ==========================================
# 기능 3: 환율 계산기
# ==========================================
def currency_converter():
    print("\n기능 3 환율 계산기 (원화 - 달러)")
    EXCHANGE_RATE = 1350.0 
    
    print("1: 원화(KRW) -> 달러(USD) | 2: 달러(USD) -> 원화(KRW)")
    choice = input("원하는 계산을 선택하세요: ").strip()
    
    try:
        if choice == "1":
            krw = float(input("원화 금액을 입력하세요: "))
            usd = krw / EXCHANGE_RATE
            print(f"환전 결과: {usd:,.2f} USD (기준 환율: {EXCHANGE_RATE}원)")
        elif choice == "2":
            usd = float(input("달러 금액을 입력하세요: "))
            krw = usd * EXCHANGE_RATE
            print(f"환전 결과: {krw:,.0f} KRW (기준 환율: {EXCHANGE_RATE}원)")
        else:
            print("잘못된 선택입니다.")
    except ValueError:
        print("숫자만 입력해 주세요.")

# ==========================================
# 기능 4: D-Day 계산기
# ==========================================
def dday_calculator():
    print("\n기능 4 D-Day 계산기")
    target_input = input("목표 날짜를 입력하세요 (형식: YYYY-MM-DD): ").strip()
    
    try:
        target_date = datetime.strptime(target_input, "%Y-%m-%d").date()
        today = datetime.today().date()
        diff = (target_date - today).days
        
        if diff > 0:
            print(f"{target_date}까지 {diff}일 남았습니다. (D-{diff})")
        elif diff < 0:
            print(f"{target_date}로부터 {abs(diff)}일 지났습니다. (D+{abs(diff)})")
        else:
            print("오늘이 바로 그날(D-Day)입니다.")
    except ValueError:
        print("날짜 형식이 올바르지 않습니다. (예: 2026-12-25)")

# ==========================================
# 기능 5: 할 일 목록 관리
# ==========================================
TODO_FILE = "todolist.json"

def todo_manager():
    print("\n기능 5 할 일 목록(To-Do) 관리")
    
    todos = []
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, "r", encoding="utf-8") as f:
                todos = json.load(f)
        except json.JSONDecodeError:
            todos = []

    print("1: 목록 보기 | 2: 할 일 추가 | 3: 할 일 삭제")
    choice = input("원하는 작업을 선택하세요: ").strip()

    if choice == "1":
        if not todos:
            print("할 일이 없습니다.")
        else:
            print("\n[현재 할 일 목록]")
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")
    elif choice == "2":
        new_task = input("새로운 할 일을 입력하세요: ").strip()
        if new_task:
            todos.append(new_task)
            with open(TODO_FILE, "w", encoding="utf-8") as f:
                json.dump(todos, f, ensure_ascii=False, indent=4)
            print("추가되었습니다.")
    elif choice == "3":
        if not todos:
            print("삭제할 항목이 없습니다.")
            return
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")
        try:
            del_idx = int(input("삭제할 번호를 입력하세요: ")) - 1
            if 0 <= del_idx < len(todos):
                removed = todos.pop(del_idx)
                with open(TODO_FILE, "w", encoding="utf-8") as f:
                    json.dump(todos, f, ensure_ascii=False, indent=4)
                print(f"'{removed}' 항목이 삭제되었습니다.")
            else:
                print("범위 벗어난 번호입니다.")
        except ValueError:
            print("숫자만 입력해 주세요.")
    else:
        print("잘못된 선택입니다.")

# ==========================================
# 메인 루프
# ==========================================
def main():
    while True:
        print("\n파이썬 미니 툴킷 프로젝트")
        print("1. 안전한 비밀번호 생성기")
        print("2. 텍스트 기반 메모장")
        print("3. 환율 계산기")
        print("4. D-Day 계산기")
        print("5. 할 일 목록 관리")
        print("0. 프로그램 종료")
        
        menu = input("실행할 기능의 번호를 입력하세요: ").strip()
        
        if menu == "1":
            generate_password()
        elif menu == "2":
            simple_notepad()
        elif menu == "3":
            currency_converter()
        elif menu == "4":
            dday_calculator()
        elif menu == "5":
            todo_manager()
        elif menu == "0":
            print("프로그램 종료")
            break
        else:
            print("올바른 메뉴 번호를 선택해 주세요 (0-5).")

if __name__ == "__main__":
    main()
