###########################
# 시작시간 17:33 마무리시간
# 주변방향으로 퍼지는데
#
import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
matrix_input = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
sum = 0
dQ = deque()
ch[n//2][n//2] = 1
sum += matrix_input[n//2][n//2]
dQ.append((n//2, n//2))
L = 0
while True:
  if L == n//2:
    break
  size = len(dQ)
  for i in range(size):
    tmp = dQ.popleft()
    for j in range(4):
      x = tmp[0] + dx[j]
      y = tmp[1] + dy[j]
      if ch[x][y] == 0:
        sum+= matrix_input[x][y]
        ch[x][y] = 1
        dQ.append((x,y))
  print(L, size)
  for x in ch:
    print(x)
  L += 1
print(sum)






##########################
# 시작시간  231217 20:15  마무리시간 20:55?
# 그냥 점화식으로 풀음
# import sys
# input = sys.stdin.readline

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
