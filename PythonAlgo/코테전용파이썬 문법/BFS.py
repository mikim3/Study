from collections import deque

# 가까운 노드 먼저 접근

# 노드A 접근
def bfs(graph, start_vector):
  visited = [start_vector]
  # 사전세팅으로 시작노드를 queue에 넣음
  queue = deque()
  queue.append(start_vector)
  # while문을 돌면서 queue를 하나씩 돌꺼임
  while queue:
    # first in first out
    current_v = queue.popleft()
    # cur_v에 근접한 모든 노드에 접근
    for next_v in graph[current_v]:
      # 만약 방문 안 했으면 처리
      if next_v not in visited:
        # 실제 방문하고
        visited.append(next_v)
        # 이후를 위해 큐에 쌓아 놓기
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

bfs(graph, 'A')
# print(bfs(graph, 'A'))
