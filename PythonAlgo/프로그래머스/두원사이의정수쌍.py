# 시작시간 240130 20:22 마무리시간 21:08
# 다시 풀어보기

# 같은 x값 중에 s와 e 사이값이 존재할 수 있는 지 판단해야함
# x = 1일때
# x**2 + y**2 = r**2 공식이용해서
# y = sqrt(r**2 - x**2)

import math
def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1):
        if i < r1:
            s = math.ceil(math.sqrt(r1**2 - i ** 2))
        else:
            s = 0
        e = math.floor(math.sqrt(r2**2 - i**2))
        answer = answer + e - s + 1
    answer = answer * 4

    return answer


