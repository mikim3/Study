###########################
# 시작시간  240219 1611      마무리시간 1643

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(x,y):
  global danji_num_of_num
  if 0:
    pass
  else:
    for i in range(4):
      next_x = x + dx[i]
      next_y = y + dy[i]
      if 0 <= next_x < n and 0 <= next_y < n and checked[next_x][next_y] == 0 and li[next_x][next_y] == 1:
        checked[next_x][next_y] = danji_num
        li[next_x][next_y] = 2
        danji_num_of_num += 1
        dfs(next_x,next_y)

n = int(input())
li = []
for i in range(n):
  li.append(list(map(int,input())))
checked = [[0] * n for _ in range(n)]
# 연결되면 한 단지이다.
# li에서 만나면 1 -> 2
# 
danji_num = 1
danji_num_of_num = 0
li_danji_num_of_num = []
for i in range(n):
  for j in range(n):
    if li[i][j] == 1:
      danji_num_of_num += 1
      li[i][j] = 2
      checked[i][j] = danji_num
      dfs(i, j)
      danji_num += 1
      li_danji_num_of_num.append(danji_num_of_num)
      danji_num_of_num = 0
    
print(danji_num - 1)
li_danji_num_of_num.sort()
for i in range(len(li_danji_num_of_num)):
  print(li_danji_num_of_num[i])


# ##########################
# # 시작시간 240114 15:30   마무리시간 16:36

# from collections import deque

# def danji_num_attach(matrix):
#   global danji_num
#   global gak_danji_house

#   # 단지당 집수
#   for i in range(n):
#     for j in range(n):
#       if matrix[i][j] == 1:
#         bfs(i,j)
#   print(danji_num - 2)
#   gak_danji_house.sort()
#   for i in gak_danji_house:
#     if i != 0:
#       print(i)
# def bfs(x,y):
#   global danji_num
#   global gak_danji_house
#   dx = [-1,0,1,0]
#   dy = [0,1,0,-1]
#   queue = deque()
#   matrix[x][y] = danji_num
#   gak_danji_house[danji_num] += 1
#   queue.append([x, y])
#   while queue:
#     now = queue.popleft()
#     for i in range(4):
#       next_x = now[0] + dx[i]
#       next_y = now[1] + dy[i]
#       if 0 <= next_x < n and 0 <= next_y < n and matrix[next_x][next_y] == 1:
#         matrix[next_x][next_y] = danji_num
#         gak_danji_house[danji_num] += 1
#         queue.append([next_x, next_y])
#   danji_num += 1

# n = int(input())
# matrix = [list(map(int, input())) for _ in range(n)]
# gak_danji_house = [0] * (int(25 ** 2 / 2))
# danji_num = 2
# danji_num_attach(matrix)
# ##############################
