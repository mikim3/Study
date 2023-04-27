# 시작시간 08:30 끝낸시간 09:06
# 중간에 수업도 들으면서해서 시ㅏㄴ이 좀더 걸렸지만 그래도 푸는시간이 꽤 걸렸다.


# 보통 (x,y) 라고 부른다.  x가 플러스면 아래로 간다.
# y가 플러면 오른쪽으로 간다.

st = input()
x = ord(st[0]) - ord('a') + 1
y = int(st[1])
move_case = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]
count = 0
for move in move_case:
    nx = x + move[0]
    ny = y + move[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        count += 1
# print(x,y)
print(count)
