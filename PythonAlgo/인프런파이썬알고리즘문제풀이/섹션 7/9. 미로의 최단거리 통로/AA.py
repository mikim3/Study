import sys
input = sys.stdin.readline
############################
# 시작시간 240112 13:46 마무리시간 13:57
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

li = []
for i in range(7):
  li.append(list(map(int,input().split())))
print(li)

def dfs(li):
  queue = deque()
  queue.append((0,0))
  while queue:
    now = queue.popleft()
    if now[0] == 6 and now[1] == 6:
      return
    for i in range(4):
      next_x = now[0] + dx[i]
      next_y = now[1] + dy[i]
      if next_x < 0 or next_x >= 7 or next_y < 0 or next_y >= 7:
        continue
      if li[next_x][next_y] == 0:
        queue.append((next_x, next_y))
        li[next_x][next_y] = li[now[0]][now[1]] + 1

dfs(li)
if li[6][6] == 0:
  print(-1)
else:
  print(li[6][6])

# ##########################
# # 시작시간  231219 13:54    마무리시간 16:34
# from collections import deque

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
# matrix = []
# for i in range(7):
#   matrix.append(list(map(int, input().split())))
# dQ = deque() # 움직일 좌표 후보군 저장
# dQ.append((0,0))
# # ch = [[0] * 7 for _ in range(7)] # 현재까지 움직인 거리 저장

# # 다음 값이 0 이면 deque에 추가
# level = 0
# matrix[0][0] = 1
# while True:
#   if len(dQ) == 0:
#     break
#   now = dQ.popleft()
#   level = matrix[now[0]][now[1]]
#   for i in range(4):
#     x = now[0] + dx[i]
#     y = now[1] + dy[i]
#     if x < 0 or x > 6 or y < 0 or y > 6:
#       continue
#     if matrix[x][y] == 0:
#       dQ.append((x,y))
#       matrix[x][y] = level + 1
#   if matrix[6][6] != 0:
#     break
# if matrix[6][6] == 0:
#   print(-1)
# else:
#   print(matrix[6][6] - 1)

# #########################
