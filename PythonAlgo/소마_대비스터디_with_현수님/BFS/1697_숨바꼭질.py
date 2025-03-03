# 시작시간 2026 마무리시간 2048

"""
x-1 x+1 2*x 이동 가능


"""
from collections import deque

def bfs(start, end):
  queue = deque()
  queue.append([start,0])
  visited = [0] * (5000001)
  visited[start] = 1
  while queue:
    now, time = queue.popleft() # 확인
    for next in now-1,now+1,now*2:
      if next < 0 or next > 2000001:
        continue
      if next == end:
        time += 1
        return time
      if visited[next] != 1:
        queue.append([next,time+1])
        visited[next] = 1
n,k = map(int,input().split())
if n == k:
  print(0)
else:
  print(bfs(n,k))
