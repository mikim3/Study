# 시작시간 1005 마무리시간 1025 
"""
# 유형코드 봤음
"""

import heapq

def dijkstra(start,end):
  heap = [] # [(최단시간, 위치)]
  MAX = 100001
  visited = [0] * (MAX * 2) # 방문체크
  heapq.heappush(heap, (0, start)) 
  next, next_time = 0, 0
  visited[start] = 1
  while heap:
    # 현재시간, 현재위치
    now_time, now = heapq.heappop(heap)
    if now == end:
      return now_time
      # break
    for i in range(3):
      if i == 0:
        next = now * 2
        next_time = now_time 
      elif i == 1:
        next = now - 1
        next_time = now_time + 1
      else:
        next = now + 1
        next_time = now_time + 1
      if next < 0 or next > MAX:
        continue
      if visited[next] == 0:
        heapq.heappush(heap, (next_time, next))
        visited[next] = 1
      
n, k = map(int,input().split())
print(dijkstra(n,k))
