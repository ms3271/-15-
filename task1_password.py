import random
import string

def generate_password():
    print("\n[기능 1] 안전한 비밀번호 생성기")
    try:
        length = int(input("생성할 비밀번호 길이를 입력하세요 (최소 8자): "))
        if length < 8:
            print("보안을 위해 8자 이상으로 설정해 주세요. 기본값 8자로 생성합니다.")
            length = 8
    except ValueError:
        print("올바른 숫자가 아닙니다. 기본값 8자로 생성합니다.")
        length = 8

    # 알파벳 대소문자, 숫자, 특수문자 조합
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    
    print(f"생성된 비밀번호: {password}")
    return password

if __name__ == "__main__":
    generate_password()