# 3개의 x,y 좌표중 각각다른 좌표에 x 나 y 가 한번씩만 나온 좌표가 원하는 좌표다.
# 두번씩 겹쳐나온 좌표는 후보에서 제거해야 한다.

def solution(v):
    x = []
    y = []
    answer = []
    
    # 이중배열 순회
    for i in v:
        # 현재 보는 점의 x 좌표가 x안에 없으면 추가
        if i[0] not in x:
            x.append(i[0])
        # 만약 또 같은 X 좌표가 나오면 그거는 제거
        else:
            x.remove(i[0])
        if i[1] not in y:
            y.append(i[1])
        else:
            y.remove(i[1])
    answer = x + y
    return answer
