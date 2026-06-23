import os
import json

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

if __name__ == "__main__":
    todo_manager()