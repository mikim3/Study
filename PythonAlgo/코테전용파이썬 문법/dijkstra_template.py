import heapq

def dijkstra(graph, start, final):
  # 각 노드들의 비용을 저장
  costs = {}
  # 우선순위 큐
  pq = []
  # (해당위치까지 가는 총 비용, 노드위치)
  heapq.heappush(pq, (0, start))

  while pq:
    # heappop을 하면 가장 작은 원소가 튀어 나온다.
    cur_cost, cur_v = heapq.heappop(pq)
    # 방문하지 않은 백터 일때만 작동
    if cur_v not in costs:
      #
      costs[cur_v] = cur_cost
      for cost, next_v in graph[cur_v]:
        next_cost = cur_cost + cost
        heapq.heappush(pq, (next_cost, next_v))
  return costs[final]

graph = {
  1: [(2,2),(1,4)],
  2: [(1,3),(9,5),(6,6)],
  3: [(4,6)],
  4: [(3,3),(5,7)],
  5: [(1,8)],
  6: [(3,5)],
  7: [(7,6),(9,8)],
  8: [],
}
print(dijkstra(graph,1,8)) # 11
print(dijkstra(graph,1,4)) # 1
print(dijkstra(graph,1,3)) # 1

# graph = {
#   "A": [("B", 2), ("D", 1)],
#   "B": [("C", 2), ("E", 2), ("F", 4)],
#   "C": [("F", 4)],
#   "D": [("G", 5)],
#   "E": [("H", 1)],
#   "F": [("E", 3)],
#   "G": [("F", 7), ("H", 6)],
#   "H": [],
# }

