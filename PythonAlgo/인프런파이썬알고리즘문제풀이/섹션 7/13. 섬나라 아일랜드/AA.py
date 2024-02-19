from collections import deque

###############################
# 시작시간 240219 1921 마무리시간 1932

def bfs(start):
  li[start[0]][start[1]] = 2
  queue = deque()
  queue.append(start)
  while queue:
    now = queue.popleft()
    for i in range(8):
      next_x = now[0] + dx[i]
      next_y = now[1] + dy[i]
      if 0 <= next_x < n and 0 <= next_y < n and li[next_x][next_y] == 1:
        li[next_x][next_y] = 2
        queue.append([next_x, next_y])

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

n = int(input())
li = []
for i in range(n):
  li.append(list(map(int, input().split())))
checked = [[0] * n for _ in range(n)]
count = 0

for i in range(n):
  for j in range(n):
    if li[i][j] == 1:
      bfs([i,j])
      count += 1

print(count)

# ##########################
# # 시작시간  240115 15:35    마무리시간 15:49

# # 대각선 연결
# dx = [-1,-1,0,1,1,1,0,-1]
# dy = [0,1,1,1,0,-1,-1,-1]

# def island():
#   global matrix
#   global count
#   for i in range(n):
#     for j in range(n):
#       if matrix[i][j] == 1:
#         bfs(i, j)
#         count += 1

# def bfs(x, y):
#   global matrix
#   queue = deque()
#   queue.append([x,y])
#   while queue:
#     now = queue.popleft()
#     for i in range(8):
#       next_x = now[0] + dx[i]
#       next_y = now[1] + dy[i]
#       if 0 <= next_x < n and 0 <= next_y < n and matrix[next_x][next_y] == 1:
#         matrix[next_x][next_y] = 2
#         queue.append([next_x, next_y])

# n = int(input())
# matrix = []
# for i in range(n):
#   matrix.append(list(map(int,input().split())))
# count = 0

# island()
# print(count)

# #########################
