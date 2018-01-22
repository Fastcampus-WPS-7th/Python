#import game
from game import play_game
#import shop
from shop import buy_item

CHOICE = '''1. Play game
2. Buy item
0. exit'''

if __name__ == '__main__':
    # 1. 실행 메시지를 표시 (Turn on game)
    # 2. 사용자에게 무엇을 할 것인지 물어보기
    #     1. play game
    #     2. buy_item
    #     0. exit
    # 3. 1또는 2를 입력 시 해당 함수 실행 후 다시 사용자에게 무엇을 할 지 물어보기
    # 4. 0을 입력하면 물어보는 반복문을 탈출하고 게임종료 메시지 표시 (Game over)
    print('= Turn on game =')

    while True:
        print(CHOICE)
        choice = input('무엇을 하실래요: ')

        if choice == '1':
            play_game()
        elif choice == '2':
            buy_item()
        elif choice == '0':
            break
        else:
            print('가능한 명령의 번호를 입력해주세요')
        print('')
    print('= Game over =')

#print(f'lol.py의 module name: {__name__}')

