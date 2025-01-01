# 시작시간 2118 마무리 시간 2220
# 맨 밑에 있는 함수 썼으면 간단히 풀었을듯

# 구역의 갯수를 세야됨
# 근데 두가지 방법으로 세야됨

# 빨초 못 느낌

from collections import deque
import sys

input = sys.stdin.readline

def bfs(x,y, now_color):
  queue = deque()
  queue.append((x,y))
  
  while queue:
    cur_x, cur_y = queue.popleft()
    for i in range(4):
      nx = cur_x + dx[i]
      ny = cur_y + dy[i]
      
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if li[nx][ny] != now_color:
        continue
      if li[nx][ny] == now_color and visited[nx][ny] == 0:
        queue.append((nx,ny))
        visited[nx][ny] = 1


dx = [-1,0,1,0]
dy = [0,1,0,-1]

li = []
n = int(input())
for i in range(n):
  li.append(input().rstrip())

# 방문했으면 V로 바꾸기 
visited = [[0] * (n+1) for _ in range(n+1)]

count = 0
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      visited[i][j] = 1
      now_color = li[i][j]
      bfs(i,j, li[i][j])
      count += 1

print(count)

visited = [[0] * (n+1) for _ in range(n+1)]

#
# li 안에 값을 R과 G가 같아져야함
for i in range(n):
  word = li[i]
  li_word = [m for m in word]
  
  for j in range(n):
    if li_word[j] == 'G':
      li_word[j] = 'R'
  tmp_word = ""
  for j in range(n):
    tmp_word += li_word[j]
  li[i] = tmp_word
count = 0 
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      visited[i][j] = 1
      now_color = li[i][j]
      bfs(i,j, li[i][j])
      count += 1
print(count)

#######################################
# li 안에 값을 R과 G가 같아져야함
# for i in range(n):
#     li[i] = li[i].replace('G', 'R')
