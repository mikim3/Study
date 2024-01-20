import heapq

# 다익스트라 알고리즘은
# 가중치가 있는 그래프에서 가장 효율저긴 경로 알려주는 알고리즘

# def dijkstra(graph,start,end):
#   costs = {vertex:111111 for vertex in graph}
#   pq = []
#   heapq.heappush(pq,(0,start))
#   while pq:
#     cur_cost, cur_v = heapq.heappop(pq)
#     if costs[cur_v] < cur_cost:
#       continue
#     for cost, next_v in graph[cur_v]:
#       next_cost = cur_cost + cost
#       if next_cost < costs[next_v]:
#         costs[next_v] = next_cost
#         heapq.heappush(pq, (next_cost, next_v))
#   return costs[end]

# def dijkstra(graph, start, end):
#   distance = [float("inf")] * (9 + 1)
#   distance[start] = 0
#   q = []
#   heapq.heappush(q, (0, start))
#   while q:
#     dist, now = heapq.heappop(q)
#     if distance[now] < dist:
#       continue
#     for vv, ww in graph[now]:
#       cost = distance[now] + ww
#       if cost < distance[vv]:
#         distance[vv] = cost
#         heapq.heappush(q, (cost, vv))
#   return distance[end]


def dijkstra(graph, start):
  # 그래프의 각 노드까지의 최단 거리를 저장할 딕셔너리
  distances = {vertex: float('infinity') for vertex in graph}
  distances[start] = 0  # 시작 노드까지의 거리는 0
  priority_queue = [(0, start)]

  while priority_queue:
    current_distance, current_vertex = heapq.heappop(priority_queue)
    # 현재 노드의 거리가 더 긴 경우 스킵
    if distances[current_vertex] < current_distance:
      continue
    # 인접 노드 거리 업데이트
    for neighbor, weight in graph[current_vertex].items():
      distance = current_distance + weight
      # 더 짧은 경로 발견시 업데이트
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(priority_queue, (distance, neighbor))
  return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)

# graph = {
#   1: [(2,2),(1,4)],
#   2: [(1,3),(9,5),(6,6)],
#   3: [(4,6)],
#   4: [(3,3),(5,7)],
#   5: [(1,8)],
#   6: [(3,5)],
#   7: [(7,6),(9,8)],
#   8: [],
# }

# INF = int(1e9)
# num_v = len(graph)
# distance = [INF] * (num_v + 1)
# print(dijkstra(graph,1,8)) # 11
# print(dijkstra(graph,1,4)) # 1
# print(dijkstra(graph,1,3)) # 1
