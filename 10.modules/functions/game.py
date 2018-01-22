import time
# from 모듈 import *로 이 모듈이 import되었을 경우
# 전달할 식별자를 정의함
__all__ = (
    'PLAY_MESSAGE',
    'play_game',
)
PLAY_MESSAGE = 'Play game!'

def play_game():
    print(PLAY_MESSAGE)

def buy_game():
    print('Buy game!')

if __name__ == '__main__':
    play_game()
    buy_game()
#print(f'game.py의 module name: {__name__}')

