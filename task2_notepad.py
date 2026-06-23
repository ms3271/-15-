import os

MEMO_FILE = "mymemo.txt"

def simple_notepad():
    print("\n[기능 2] 텍스트 기반 메모장")
    print("1: 메모 읽기 | 2: 새 메모 쓰기 (기존 내용 삭제) | 3: 메모 이어 쓰기")
    sub_menu = input("원하는 작업 번호를 선택하세요: ").strip()

    if sub_menu == "1":
        if os.path.exists(MEMO_FILE):
            with open(MEMO_FILE, "r", encoding="utf-8") as f:
                print(f"\n--- [{MEMO_FILE}] 내용 ---\n{f.read()}")
        else:
            print("\n저장된 메모 파일이 없습니다.")
            
    elif sub_menu == "2":
        content = input("새로 작성할 내용을 입력하세요:\n")
        with open(MEMO_FILE, "w", encoding="utf-8") as f:
            f.write(content + "\n")
        print(f"\n{MEMO_FILE}에 성공적으로 저장되었습니다.")
        
    elif sub_menu == "3":
        content = input("이어 쓸 내용을 입력하세요:\n")
        with open(MEMO_FILE, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        print("\n메모가 추가되었습니다.")
    else:
        print("\n잘못된 선택입니다.")

if __name__ == "__main__":
    simple_notepad()