from collections import deque
from typing import List

# 열수 있는 방부터 접근하면서 해결하기 때문에 BFS문제

class Solution:
  def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    rooms_len = len(rooms)
    visited = [0] * rooms_len
    visited[0] = 1
    queue = deque()
    queue.append(rooms[0])
    while queue:
      now_keys = queue.popleft()
      for next_rooms in now_keys:
        if visited[next_rooms] == 0:
          queue.append(rooms[next_rooms])
          visited[next_rooms] = 1

    for i in range(rooms_len):
      if visited[i] == 0:
        return False
    return True
sol = Solution()
print(sol.canVisitAllRooms([[1],[2],[3],[]])) # true
print(sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])) # false
# print(sol.canVisitAllRooms([[1],[2],[3],[]]))

