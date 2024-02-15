from collections import deque
import sys
input = sys.stdin.readline
#################################
# 시작시간 240215 20:38  마무리시간 21:02

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(start):
  global total
  queue = deque()
  queue.append(start)
  while queue:
    now = queue.popleft()
    for i in range(4):
      next_x = now[0] + dx[i]
      next_y = now[1] + dy[i]
      if 0 <= next_x < n and  0 <= next_y < n and checked[next_x][next_y] == 0 and checked[now[0]][now[1]] < n//2:
        checked[next_x][next_y] = checked[now[0]][now[1]] + 1
        total += li[next_x][next_y]
        queue.append([next_x, next_y])

n = int(input())
li = []
for i in range(n):
  li.append(list(map(int,input().split())))
total = 0
checked = [[0] * n for _ in range(n)]
bfs([n//2,n//2].copy())
print(total)

###############################
# 시작시간 231219 1516 마무리 시간 15:52
# from collections import deque

# 좌표중앙인 n//2, n//2 부터 시작
# 상하좌우 확인하면서 더하기
# 해당 행위를 하면 십자가 모양으로 퍼짐
# 깊이가 n//2 만큼 가면 원하는 만큼 십자가 모양으로 퍼짐
#

# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
# n = int(input())
# ch = [[0] * n for _ in range(n)]
# matrix = [list(map(int, input().split())) for _ in range(n)]
# dQ = deque() #
# dQ.append((n//2, n//2))
# L = 0 # 레벨
# su = matrix[n//2][n//2] # 합친거 총합
# ch[n//2][n//2] = 1
# while True:
#   if L== n//2:
#     break
#   size = len(dQ)
#   for i in range(size):
#     now = dQ.popleft()
#     for j in range(4):
#       x = now[0] + dx[j]
#       y = now[1] + dy[j]
#       dQ.append((x,y))
#       if ch[x][y] == 0:
#         su+= matrix[x][y]
#         ch[x][y] = 1
#   L+=1
# for i in range(n):
#   print(ch[i])
# print(su)


###########################
# 시작시간 231218 마무리시간
# BFS 풀이는 강의 봄
# from collections import deque

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# n = int(input())
# matrix_input = [list(map(int, input().split())) for _ in range(n)]
# ch = [[0] * n for _ in range(n)]
# sum = 0
# dQ = deque()
# ch[n//2][n//2] = 1
# sum += matrix_input[n//2][n//2]
# dQ.append((n//2, n//2))
# L = 0
# while True:
#   if L == n//2:
#     break
#   size = len(dQ)
#   for i in range(size):
#     tmp = dQ.popleft()
#     for j in range(4):
#       x = tmp[0] + dx[j]
#       y = tmp[1] + dy[j]
#       if ch[x][y] == 0:
#         sum+= matrix_input[x][y]
#         ch[x][y] = 1
#         dQ.append((x,y))
#   print(L, size)
#   for x in ch:
#     print(x)
#   L += 1
# print(sum)

##########################
# 시작시간  231217 20:15  마무리시간 20:55?
# 그냥 점화식으로 풀음

# n = int(input())
# li = []
# for i in range(n):
#   li.append(list(map(int, input().split())))

# print(li)
# su = 0
# for i in range(n):
#   if i <= n // 2:
#     for j in range(n//2-i, n//2+1+i):
#       su += li[i][j]
#   else:
#     for j in range(i - n//2, n - i + n//2):
#       su += li[i][j]
# print(su)
#########################
