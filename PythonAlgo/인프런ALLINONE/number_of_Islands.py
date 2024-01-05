from collections import deque

# 암시적 BFS문제

# 그래프를 순회하면서 만약에 BFS가 필요한 곳 이 있으면 거기부터 시작해서 BFS를 돌면 되는 문제

# 1만 지나갈수 있음

def number_of_islands(grid):
  grid_row = len(grid)
  grid_col = len(grid[0])
  visited = [[False] * grid_col for _ in range(grid_row)]

  def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
      cur_vector = queue.popleft()
      cur_x = cur_vector[0]
      cur_y = cur_vector[1]
      # 상하좌우 돌기
      for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        # True로 바꿔줘야 할 값
        if visited[next_x][next_y] == False and grid[next_x][next_y] == '1':
          visited[next_x][next_y] = True
          queue.append((next_x, next_y))

  for i in range(grid_row):
    for j in range(grid_col):
      if grid[i][j] == '1' or visited[i][j] == False:
        bfs(i, j)




# def BFS(graph, start_vector):
#   visited = [start_vector]

#   queue = deque(start_vector)
#   while queue:
#     current_v = queue.popleft()

#     for next_v in graph[current_v]:

#       if next_v not in visited:

#         visited.append(next_v)
#         queue.append(next_v)
#       print(visited)
#   return visited

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# BFS(graph, 'A')
