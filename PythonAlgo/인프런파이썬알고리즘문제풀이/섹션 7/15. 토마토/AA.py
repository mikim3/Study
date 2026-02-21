import sys
from collections import deque

# 260221 시작 2109 마무리

# 최소 며칠 지나면 다익음?
# 1 익은 토마토  0 안익은 토마토  -1 빈곳
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
c, r = map(int,input().split())
li = [list(map(int, input().split())) for _ in range(r)]

# 여러 개의 익은 토마토(1)를 한 번에 시작점으로 잡는 "multi-source BFS"로 O(R*C)에 해결.
q = deque()
for i in range(r):
  for j in range(c):
    if li[i][j] == 1:
      q.append((i, j))

max_day = 1
while q:
  x, y = q.popleft()
  day = li[x][y]
  if day > max_day:
    max_day = day
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < r and 0 <= ny < c and li[nx][ny] == 0:
      li[nx][ny] = day + 1
      q.append((nx, ny))

for i in range(r):
  for j in range(c):
    if li[i][j] == 0:
      print(-1)
      sys.exit(0)

print(max_day - 1)


# 너무 긴 인풋값을 처리
# sys.stdin = open("/goinfre/mikim3/Study/PythonAlgo/인프런파이썬알고리즘문제풀이/섹션 7/15. 토마토/input.txt", "r")
# sys.stdin = open("c:/Users/minsuda/Documents/GitHub/Study/PythonAlgo/인프런파이썬알고리즘문제풀이/섹션 7/15. 토마토/input.txt", "r")

# 시작시간 240219 2045 마무리시간 2110

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# def bfs():
#   queue = deque()
#   for _ in range(len(li_done_tomato)):
#     queue.append(li_done_tomato.pop())
#   while queue:
#     now = queue.popleft()
#     for i in range(4):
#       next_x = now[0] + dx[i]
#       next_y = now[1] + dy[i]
#       if 0 <= next_x < n and 0 <= next_y < m and li[next_x][next_y] == 0:
#         li[next_x][next_y] = li[now[0]][now[1]] + 1 
#         queue.append((next_x, next_y))
      
# m,n = map(int, input().split())
# li = []
# for i in range(n):
#   li.append(list(map(int,input().split())))
# li_done_tomato = []
# for i in range(n):
#   for j in range(m):
#     if li[i][j] == 1:
#       li_done_tomato.append((i,j))
# bfs()
# max_value = 0
# for i in range(n):
#   for j in range(m):
#     if li[i][j] == 0:
#       print(-1)
#       sys.exit()
#     if li[i][j] > max_value:
#       max_value = li[i][j]
# print(max_value-1)

# ########################
# # 시작시간 240123 16:00 마무리시간 16:30

# # 최소 일수
# # 1익음  0 익지 않은  -1빈공간 벽

# m, n = map(int,input().split())
# li = []
# for i in range(n):
#   li.append(list(map(int, input().split())))
# print(li)

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def bfs(queue : Deque):
#   while queue:
#     now = queue.popleft()
#     for i in range(4):
#       next_x = now[0] + dx[i]
#       next_y = now[1] + dy[i]
#       if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
#         continue
#       if li[next_x][next_y] == 0:
#         li[next_x][next_y] = li[now[0]][now[1]] + 1
#         queue.append((next_x,next_y))
#   max_value = 0
#   for i in range(n):
#     if max(li[i]) > max_value:
#       max_value = max(li[i])
#   count_zero = 0
#   for i in range(n):
#     for j in range(m):
#       if li[i][j] == 0:
#         count_zero += 1
#   if count_zero > 0:
#     return -1
#   return max_value-1
# queue = deque()
# count_zero = 0
# for i in range(n):
#   for j in range(m):
#     if li[i][j] == 1:
#       queue.append((i,j))
#     if li[i][j] == 0:
#       count_zero += 1
# if count_zero > 0:
#   print(bfs(queue))
# else:
#   print(0)



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
