from collections import deque
from typing import List

# 시작시간 230106 20분소요

class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if grid[0][0] == 1 or grid[-1][-1] == 1:
      return -1
    n = len(grid)
    queue = deque([(0, 0)])
    visited = [[0] * n for _ in range(n)]
    dx = [-1, -1, 1, 1, -1, 1, 0, 0]
    dy = [-1, 1, 1, -1, 0, 0, 1, -1]

    while queue:
      x, y = queue.popleft()
      if x == n - 1 and y == n - 1:
        return visited[x][y] + 1
      for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and grid[nx][ny] == 0:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))
      return -1

# 여기에서 테스트 케이스를 실행합니다
sol = Solution()
print(sol.shortestPathBinaryMatrix([[0,0,0], [1,1,0], [1,1,0]]))  # 예상 출력: 4
print(sol.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))  # 예상 출력: -1
print(sol.shortestPathBinaryMatrix([[0,1],[1,0]]))  # 예상 출력: 2
