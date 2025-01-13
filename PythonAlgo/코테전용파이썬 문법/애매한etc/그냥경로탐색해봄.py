def find_paths(maze, start_row, start_col, end_row, end_col):
  # 크기 알아내기
  rows, cols = len(maze), len(maze[0])
  # 방문표시 배열 만들기
  visited = [[False] * cols for _ in range(rows)]

  #
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
  paths = []
  current_path = []

  def is_valid(row, col):
    return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 1 and not visited[row][col]

  def search(row, col):
    if row == end_row and col == end_col:
      paths.append(current_path.copy() + [(row, col)])
      return

    visited[row][col] = True
    current_path.append((row, col))

    for dr, dc in directions:
      next_row, next_col = row + dr, col + dc
      if is_valid(next_row, next_col):
        search(next_row, next_col)

    current_path.pop()
    visited[row][col] = False

  search(start_row, start_col)
  return paths

# 미로 예시
maze = [
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1]
]

# 모든 경로 찾기
all_paths = find_paths(maze, 0, 0, 5, 5)
for path in all_paths:
    print("경로:", path)
