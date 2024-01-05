from collections import deque

# 상하좌우라고 만 표현하고 각 노드가 이름이 따로 있지 않음
# 그래서 그 노드를 탐색하기 위한 코드가 추가적으로 필요함

def bfs(graph, start_vector):
  visited = [start_vector]
  queue = deque()
  queue.append(start_vector)
  while queue:
    current_vector = queue.popleft()
    for next_v in graph[current_vector]:
      if next_v not in visited:
        visited.append(next_v)
        queue.append(next_v)
  return visited

graph = {
  'A': ['B', 'D', 'E'],
  'B': ['A','C','D'],
  'C': ['B'],
  'D': ['A', 'B'],
  'E': ['A']
}

print(bfs(graph, 'A'))
