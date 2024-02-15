###############################
# 시작시간 240215 21:20 마무리시간

def dfs(level):
  if :
  else:


li = []
for i in range(7):
  li.append(list(map(int, input().split())))
checked = [list()]










# ########################
# # 모범담안

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def DFS(x,y):
#   global count
#   if x == 6 and y == 6:
#     count += 1
#   else:
#     for next in range(4):
#       next_x = x + dx[next]
#       next_y = y + dy[next]
#       if 0 <= next_x <= 6 and 0 <= next_y <= 6 and board[next_x][next_y] == 0:
#         board[next_x][next_y] = 1
#         DFS(next_x,next_y)
#         board[next_x][next_y] = 0

# board = [list(map(int, input().split())) for _ in range(7)]
# count = 0
# board[0][0] = 1
# DFS(0, 0)
# print(count)

# ##########################
# # 시작시간  240114 10:56  마무리시간
# # 11:37에 포기
# # 도착하는 경우의수
# # checked를 나눠서 했더니 실수가 유발되어서 못 풀었었음

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# def DFS(now):
#   global count
#   if now == [6,6]:
#     count += 1
#   else:
#     for next in range(4):
#       next_x = now[0] + dx[next]
#       next_y = now[1] + dy[next]
#       if next_x < 0 or next_x > 6 or next_y < 0 or next_y > 6:
#         continue
#       if li[next_x][next_y] == 0:
#         li[next_x][next_y] = 1
#         DFS([next_x,next_y])
#         li[next_x][next_y] = 0
# li = []
# for i in range(7):
#   li.append(list(map(int, input().split())))
# count = 0
# li[0][0] = 1
# # x,y 좌표
# DFS([0,0])
# print(count)
# #########################
