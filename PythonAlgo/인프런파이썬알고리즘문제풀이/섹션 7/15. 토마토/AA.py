import sys
from collections import deque
from typing import Deque
# 너무 긴 인풋값을 처리
sys.stdin = open("/goinfre/mikim3/Study/PythonAlgo/인프런파이썬알고리즘문제풀이/섹션 7/15. 토마토/input.txt", "r")

########################
# 시작시간 240123 16:00 마무리시간 16:30

# 최소 일수
# 1익음  0 익지 않은  -1빈공간 벽

m, n = map(int,input().split())
li = []
for i in range(n):
  li.append(list(map(int, input().split())))
print(li)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(queue : Deque):
  while queue:
    now = queue.popleft()
    for i in range(4):
      next_x = now[0] + dx[i]
      next_y = now[1] + dy[i]
      if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
        continue
      if li[next_x][next_y] == 0:
        li[next_x][next_y] = li[now[0]][now[1]] + 1
        queue.append((next_x,next_y))
  max_value = 0
  for i in range(n):
    if max(li[i]) > max_value:
      max_value = max(li[i])
  count_zero = 0
  for i in range(n):
    for j in range(m):
      if li[i][j] == 0:
        count_zero += 1
  if count_zero > 0:
    return -1
  return max_value-1
queue = deque()
count_zero = 0
for i in range(n):
  for j in range(m):
    if li[i][j] == 1:
      queue.append((i,j))
    if li[i][j] == 0:
      count_zero += 1
if count_zero > 0:
  print(bfs(queue))
else:
  print(0)



# ##########################
# # 시작시간  240115 19:45   마무리시간
# # 20:17분에 결국 답 봤음
# # 해설 아이디어만 보고 20:45에 품

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# m, n = map(int, input().split())
# distance = []
# for i in range(n):
#   distance.append([0] * m)

# matrix = []
# for i in range(n):
#   matrix.append(list(map(int, input().split())))
# queue = deque()

# for i in range(n):
#   for j in range(m):
#     if matrix[i][j] == 1:
#       queue.append([i,j])

# def bfs(queue : Deque):
#   while queue:
#     now = queue.popleft()
#     for i in range(4):
#       next_x = now[0] + dx[i]
#       next_y = now[1] + dy[i]
#       if 0 <= next_x < n and 0 <= next_y < m and \
#         matrix[next_x][next_y] == 0 and distance[next_x][next_y] == 0:
#         distance[next_x][next_y] = distance[now[0]][now[1]] + 1
#         queue.append([next_x, next_y])
#         matrix[next_x][next_y] = 2
# bfs(queue)

# for i in range(n):
#   for j in range(m):
#     if matrix[i][j] == 0:
#       print(-1)
#       sys.exit(0)

# max_distance = 0
# for i in range(n):
#   max_distance = max(distance[i])
# print(max_distance)

# #########################
