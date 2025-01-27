# 시작시간 2246 마무리 시간 2319

import sys
from collections import deque
input = sys.stdin.readline

def bfs(li, start):
  queue = deque()
  queue.append(start)
  # 실내공기 갈수있는 곳 체크
  checked_air = [[0] * m for _ in range(n)]
  checked_air[start[0]][start[1]] = 2
  checked_nokarm = [[0] * m for _ in range(n)] # 치즈에 공기가 닿을때마다 1씩 증가

  while queue:
    now = queue.popleft()
    for i in range(4):
      n_x = now[0] + dx[i]  
      n_y = now[1] + dy[i]  
      if n_x < 0 or n_x >= n or n_y < 0 or n_y >= m:
        continue
      # 아직 방문 안했고 치즈 위치 아니면
      if checked_air[n_x][n_y] == 0 and li[n_x][n_y] == 0:
        checked_air[n_x][n_y] = 2
        queue.append((n_x,n_y))
      # 다음 위치가 치즈위치면
      if li[n_x][n_y] == 1: 
        checked_nokarm[n_x][n_y] += 1
  for i in range(n):
    for j in range(m):
      if checked_nokarm[i][j] >= 2:
        li[i][j] = 0 # 녹아 버림
        
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n, m = map(int, input().split())
li = []
for i in range(n):
  li.append(list(map(int, input().split())))

time = 0  # 현재 지난시간  1시작인가??
while True:
  flag = 1
  for i in range(n):
    for j in range(m):
      if li[i][j] == 1:
        flag = 0
  if flag == 1:
    break
  bfs(li, (0,0))
  time += 1

print(time)