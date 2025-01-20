# 다익스트라 알고리즘 시간 복잡도 O(ElogE)  E는 간선Edge
# ******* heapq는 알아서 가장 작은 값을 맨앞으로 보낸다. ===
# === heappop을 하면 알아서 제일 비용이 작은 이동경로를 첫번쨰로 간다. **********

import heapq
from collections import defaultdict


def dijkstra(graph, start, final):
  costs = {}  # 몇번노드가 몇 비용이 들었는지 넣을 딕셔너리
  pq = []
  heapq.heappush(pq, (0, start))

  while pq:
    cur_cost, cur_v = heapq.heappop(pq) # 가장 비용이 적게드는 녀석으로 pop
    if cur_v not in costs: # 처음 방문하는 곳인지 확인(처음 방문했으면 가장 효율적인 길임{heapq성질때문임})
      costs[cur_v] = cur_cost # 현재 비용 넣기
      for cost, next_v in graph[cur_v]: # cost: 현재에서 다음 벡터까지 거리
        next_cost = cur_cost + cost  # 지금까지 오는데쓴 비용 + 다음벡터까지거리
        heapq.heappush(pq, (next_cost, next_v))
  return costs[final]

graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: []
}

dijkstra(graph, 1, 8)






