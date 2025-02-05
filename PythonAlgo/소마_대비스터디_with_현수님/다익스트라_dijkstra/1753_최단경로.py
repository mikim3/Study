# 시작시간 1348 마무리시간
import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph,start):
  pq = []
  heapq.heappush(pq, (0, start))
  while pq:
    now_cost, now_node = heapq.heappop(pq)
    if costs[now_node] == float('inf'):
      costs[now_node] = now_cost
      for next_cost, next_node in graph[now_node]:
        cost = now_cost + next_cost
        heapq.heappush(pq, (cost, next_node))

V,E = map(int,input().split())
start = int(input())
# [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]
graph = [[] for _ in range(V+1)]
for i in range(E):
  u,v,w = map(int, input().split())
  graph[u].append((w,v))
n = len(graph)
costs = [float('inf')] * (n+1)

dijkstra(graph, start)

for i in range(1,V+1):
  if costs[i] != float('inf'):
    print(costs[i])
  else:
    print('INF')

# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6

