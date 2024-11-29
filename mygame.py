import random

def rps_game():
    option = ['가위','바위','보']

    user_choice = input("가위, 바위, 보 중 하나 선택").strip()

    if user_choice not in option:
        print("잘못된 입력입니다. '가위',' 바위',' 보' 중 하나를 선택해주세요.")
        return

    computer_choice = random.choice(option)

    print(f"사용자 선택: {user_choice}")
    print(f"컴퓨터 선택: {computer_choice}")

    if user_choice == computer_choice:
        print("비겼습니다")
    elif (user_choice == '가위' and compter_choice == '보') or \
         (user_choice == '보' and computer_choice == '바위') or \
         (user_choice == '바위' and computer_choice == '가 위'):
             print("사용자가 이겼습니다!")
         else:
             print("컴퓨터가 이겼습니다!")

rps_game()
        
