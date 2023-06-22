# 230622 시작시간 16:46 17:02 답봄
# 너무 틱택토 게임을 알고 해봐야 하는 문제라고 판단되었다.

# 첫사람이 x 두번째 O


# 불가능 한 경우
# 1. x가 승리하려면 x개수 = o개수 + 1 이고 O가 승리하려면 x개수 = o개수 이다.

# 2. x,O 둘다 끝나 있는 경우
# xo.
# xo.
# xox


# 3. 모든 칸이 다 채워지지 않았는데 게임이 종료되는 경우
# xo. xo. ...

from sys import stdin

input = stdin.readline

def solv():
    while True:
        case = input().strip()
        if case == 'end':
            break
        x_count = case.count('X')
        o_count = case.count('O')

        if x_count == o_count+1 or x_count == o_count:
            typ1,typ2 = ('X','O') if x_count == o_count+1 else ('O','X')
            game_result1 = check_game_end(case, typ1)
            game_result2 = check_game_end(case, typ2)

            if game_result2:
                print('invalid')
            elif not game_result1:
                if case.count('.') == 0:
                    print('valid')
                else:
                    print('invalid')
            else:
                print('valid')
        else:
            print('invalid')
def check_game_end(case,typ):
    if case[0] == typ and case[0] == case[1] == case[2]:
        return True
    elif case[0] == typ and case[0] == case[3] == case[6]:
        return True
    elif case[4] == typ and case[1] == case[4] == case[7]:
        return True
    elif case[4] == typ and case[3] == case[4] == case[5]:
        return True
    elif case[8] == typ and case[6] == case[7] == case[8]:
        return True
    elif case[8] == typ and case[2] == case[5] == case[8]:
        return True
    elif case[4] == typ and case[0] == case[4] == case[8]:
        return True
    elif case[4] == typ and case[2] == case[4] == case[6]:
        return True
    else:
        return False

solv()

