
# 직사각형의 점3 개의 좌표를 줬을때 
# 나머지 한점의 위치를 알아내어라

#입출력 예
# [[1,4],[3,4],[3,10]]   출력->  [1,10]

#XOR 이용 답

def solution(v):
    x = [i[0] for i in v]
    y = [i[1] for i in v]

    for i in range(2):
        x[0] ^= x[i + 1]
        y[0] ^= y[i + 1]
    answer = [x[0], y[0]]

    return answer

print(solution([[1,5],[3,5],[3,7]]))



