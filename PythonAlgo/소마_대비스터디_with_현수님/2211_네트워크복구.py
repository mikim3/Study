# 시작시간 0917 마무리시간
# 답봄 (GPT한테 물어봄)

# 최소 스패닝 트리, 다익스트라 알아야됨



# 무방향 그래프

# 최소 개수의 회선만을 복구(네트워크 복구한 후에 서로 다른 두 ㅓㅁ퓨터 간에 통신이 가능해야함)
# 슈퍼컴퓨터가 다른 컴퓨터들과 통신하는데 걸리는 최소 시간이 원래읜 네트워크에서 통신하는 최소시간보다 커지면 안됨

# 문제의 핵심은 최단경로가 되는데 필요없는 회선은 없애고 효율적인 회선만 남기는 것이다.
# 모든 노드를 한번씩은 지나가야함
# 

import heapq
import sys
input = sys.stdin.readline

def dijkstra(graph, start, end):
  costs = {}
  pq = []
  heapq.heappush(pq, (0, start))
  
  while pq:
    cur_cost, cur_v = heapq.heappop(pq)
    if cur_v not in costs:
      costs[cur_v] = cur_cost
      for cost, next_v in graph[cur_v]:
        next_cost = cur_cost + cost
        heapq.heappush(pq,(next_cost, next_v))  

n, m = map(int,input().split())
graph = [[20000] * (n+1) for _ in range(n+1)]
print(graph)
for i in range(m):
  a,b,c = map(int,input().split())
# 각자의 입장에서 최단경로를 다 지나가 보기
for i in range(1, n+1):
  for j in range(2, n+1):
    if i != j:
      visited = [[0]*(n+1) for _ in range(n+1)]
      dijkstra(graph, i,j)

