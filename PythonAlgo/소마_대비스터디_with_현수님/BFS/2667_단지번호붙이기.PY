# 시작시간 2316  마무리시간 2400
# 딱봐도 BFS

# 시작자리도 꼭 visited = 1 처리를 하자 이걸로 30분 날림

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  # 단지내 집 갯수
  count = 1
  visited[x][y] = 1
  while queue:
    cur_x, cur_y = queue.popleft()
    for i in range(4):
      nx = cur_x + dx[i]
      ny = cur_y + dy[i]
      if nx >= n or nx < 0 or ny >= n or ny < 0:
        continue
      if visited[nx][ny] == 0 and li[nx][ny] == '1': 
        queue.append((nx, ny))
        visited[nx][ny] = 1
        count += 1
  return count
  
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
li = []
for i in range(n):
  li.append(input().strip())

visited = [[0]*(n+1) for _ in range(n+1)]
li_dan = []
count_dan = 0
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0 and li[i][j] == '1':
      count_dan += 1
      li_dan.append(bfs(i, j))

print(count_dan)
li_dan.sort()
for i in range(len(li_dan)):
  print(li_dan[i])