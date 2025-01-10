# 시작시간 2000 마무리시간

from collections import deque
import math
# L명 이상 R명이하 인구 차 발생시 하루 문염
# 이동가능한 국가는 서로 연합
# 연합을 이루는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다.  소수점 버려
# 연합을 해체하고 모든 국경선을 닫는다.

# 연합의 국가 갯수(땅사이즈)랑 연합인원 리턴하는게 좋을듯
def bfs(x, y, graph):
  #
  hap = 0 # 현재연합의 합
  #
  queue =deque()
  queue.append((x,y, graph[x][y]))
  while queue:
    now = queue.popleft()
    for i in range(4):
      nx = now[0] + dx
      ny = now[1] + dy
      # 현재 좌표 인구 뺴기 다음 좌표 인구
      cha = abs(now[2] - graph[nx][ny])
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      # checked == 0 을 넣어야 되나???? 고민되네
      if l <= cha <= r:
        queue.append((nx,ny,graph[nx][ny]))
        checked[nx][ny] = 1



# N, L, R
n, l, r = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 모든 국가에 인구를 기록할 리스트
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))
  
flag = 1
# 며칠 지나는지 카운트
day = 0
# 이동횟수가 0 이 될때까지 bfs 반복
while True:
  # 지나간 곳 췍
  checked = [[0] * n for _ in range(n)]  
  # 연합번호는 매번 초기화
  yun_number = 0
  
  for i in range(n):
    for j in range(n):
      # 이미 연합으로 계산 된 곳은 계산 X
      if checked != 1:
        bfs(i,j, graph)
        yun_number += 1
  # 다 돌았으므로 하루 지남
  day += 1
  # 연합이 하나도 형성 안되면 그 날이 마지막 날
  if yun_number == 0:
    break


