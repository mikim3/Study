from collections import deque

def bfs(graph, start_vector):
  visited = []
  visited.append(start_vector)
  queue = deque()
  queue.append(start_vector)
  while queue:
    current_vector= queue.popleft()
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
