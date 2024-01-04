from collections import deque

# 암시적 BFS문제

# check 면 넘어가고
# 0 이여도 넘어가고
# 1면 BFS로 다 탐색


def BFS(graph, start_vector):
  visited = [start_vector]

  queue = deque(start_vector)
  while queue:
    current_v = queue.popleft()

    for next_v in graph[current_v]:

      if next_v not in visited:

        visited.append(next_v)
        queue.append(next_v)
      print(visited)
  return visited

graph = {
  'A': ['B', 'D', 'E'],
  'B': ['A','C','D'],
  'C': ['B'],
  'D': ['A', 'B'],
  'E': ['A']
}

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

BFS(graph, 'A')
