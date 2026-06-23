from datetime import datetime

def calculate_dday():
    print("\n[기능 3] 디데이(D-Day) 계산기")
    try:
        target_input = input("목표 날짜를 입력하세요 (예: 2026-12-25): ").strip()
        target_date = datetime.strptime(target_input, "%Y-%m-%d").date()
        today = datetime.today().date()
        
        diff = (target_date - today).days
        
        if diff > 0:
            print(f"목표일인 {target_date}까지 D-{diff}일 남았습니다.")
        elif diff < 0:
            print(f"목표일인 {target_date}로부터 D+{abs(diff)}일 지났습니다.")
        else:
            print(f"오늘이 바로 목표일(D-Day)입니다!")
    except ValueError:
        print("날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 입력해 주세요.")

if __name__ == "__main__":
    calculate_dday()