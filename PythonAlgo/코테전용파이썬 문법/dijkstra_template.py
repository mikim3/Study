import heapq

def dijkstra(graph, start, end):
  distances = {node: float('inf') for node in graph}
  distances[start] = 0
  pq = []
  heapq.heappush(pq, (0, start))
  while pq:
    cur_distance, cur_vector = heapq.heappop(pq)
    if distances[cur_vector] < cur_distance:
      continue
    distances[cur_vector] = cur_distance
    for next_distance , next_vector in graph[cur_vector]:
      distance = cur_distance + next_distance
      if distance < distances[next_vector]:
        distances[next_vector] = distance
        heapq.heappush(pq, (distance, next_vector))
  return distances[end]

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

# print(dijkstra(graph,'A','B')) # 2
# print(dijkstra(graph,'A','G')) # 6
# print(dijkstra(graph,'A','F')) # 6
# print(dijkstra(graph,'A','H')) # 5
# print(dijkstra(graph,'A','D')) # 1
