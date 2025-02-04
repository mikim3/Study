# 시작시간 1230 마무리시간 0133
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
  global max_distance
  queue = deque()
  queue.append(start)
  checked[start] = 0
  while queue:
    now = queue.popleft()
    for neighbor in graph[now]:
      if checked[neighbor] == -1:
        checked[neighbor] = checked[now] + 1
        queue.append(neighbor)
  max_distance = max(checked[1:])
  
n, m = map(int,input().strip().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
  a, b = map(int,input().strip().split())
  graph[a].append(b)
  graph[b].append(a)
# 각 헛간까지 거리
checked = [-1] * (n + 1) 
checked[1] = 0
max_distance = 0
bfs(1)

maxs=0
for i in range(1,n+1):
  if max_distance == checked[i]:
    maxs+=1
max_index = 0
for i in range(1,n+1):
  if max_distance == checked[i]:
    max_index = i
    break
print(max_index, max_distance, maxs)
        