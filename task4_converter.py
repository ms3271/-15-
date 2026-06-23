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

if __name__ == "__main__":
    currency_converter()