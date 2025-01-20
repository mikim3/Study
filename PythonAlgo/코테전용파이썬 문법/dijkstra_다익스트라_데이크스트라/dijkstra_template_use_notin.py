import heapq

# def dijkstra(graph, start, end):
#   costs = {}
#   pq = []
#   heapq.heappush(pq, (0,start))
#   while pq:
#     now_cost, now_node = heapq.heappop(pq)
#     if now_node not in costs:
#       costs[now_node] = now_cost
#       for next_cost, next_node in graph[now_node]:
#         cost = now_cost + next_cost
#         heapq.heappush(pq,(cost, next_node))
#   return costs[end]

######## 리스트 버젼
# costs에 값을 미리 넣고 해당 값이랑 같은지 판단하는걸로 not in  을 탐색하는게 좋음
def dijkstra(graph, start, end):
    n = len(graph)
    costs = [float('inf')] * (n + 1)
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        now_cost, now_node = heapq.heappop(pq)
        if costs[now_node] == float('inf'):
            costs[now_node] = now_cost
            for next_cost, next_node in graph[now_node]:
                cost = now_cost + next_cost
                heapq.heappush(pq, (cost, next_node))
    return costs[end]

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
print(dijkstra(graph,1,3)) # 3
