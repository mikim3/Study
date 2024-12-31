# 시작시간 1746  마무리시간 22:08
# bfs 미로 관련 코드 보면서 품
# x,y 좌표가 내가 생각한거랑 문제에서 제시하는거랑 순서가 서로 달랐음 <- 문제 다시보고 손으로 그려보고 겨우 이해함

from collections import deque

import sys
input = sys.stdin.readline

# 연결되어 있는 배추의 구역의 갯수를 세야되는 문제

def bfs(x, y):
  queue = deque()
  queue.append((x,y))

  while queue:
    cur_x, cur_y = queue.popleft()
    for i in range(4):
      nx = cur_x + dx[i]
      ny = cur_y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
        graph[nx][ny] = 0 # 박멸

# t 테스트케이스수
t = int(input())

for _ in range(t):
  # m: 가로 n: 세로 k: 배추의 갯수
  m, n, k = map(int, input().split())

  graph = [[0] * m for _ in range(n)]

  in_x, in_y = 0, 0
  for i in range(k):
    in_x, in_y = map(int,input().split())
    graph[in_y][in_x] = 1
  # for i in range(len(graph)):
  #   print(graph[i])
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]
  count = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        bfs(i, j)
        count += 1
  print(count)
