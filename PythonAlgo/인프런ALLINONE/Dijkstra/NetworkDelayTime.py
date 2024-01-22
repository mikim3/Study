from typing import List
from collections import defaultdict
import heapq

######################################
# 시작시간 240122 17:20 마무리시간 18:05

# (시작노드, 도착노드, 소요시간)
# n = 노드갯수 k는 시작노드

class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for time in times:
      graph[time[0]].append((time[2], time[1]))
    print(graph)
    costs = {}
    pq = []
    heapq.heappush(pq, (0,k))
    while pq:
      now_cost, now_node = heapq.heappop(pq)
      if now_node not in costs:
        costs[now_node] = now_cost
        for next_cost, next_node in graph[now_node]:
          cost = now_cost + next_cost
          heapq.heappush(pq, (cost, next_node))
    print('costs ==',costs)
    max = 0
    for i in costs:
      if costs[i] > max:
        max = costs[i]
    if max == 0:
      return -1
    return max
#####################################################
# 그 전 템플릿 보았음
# 그래프 구현으로 주어진 인자를 가공했다면 좀더 쉽게 풀수 있었음

# 시작시간 17:15~17:45 + 18:45 ~ 19:33 마무리시간 1시간 18분 소용

# times[i] = [출발노드, 도착노드, 걸리는 시간]
# k 에서 신호시작 총 n개의 노드를 지나야함
# 모든 노드에 지나는 시간 알아야 되니까 지나는 값중에 최대값 구하라는 소리 맞나??
# times[i]에 첫번째 값을 통해

# distances에 하나라도 101이상인게 남아 있으면 -1 반환

# class Solution(object):
#   def networkDelayTime(self, times, n, k):
#     graph = defaultdict(list)
#     for time in times:
#       graph[time[0]].append((time[2], time[1]))
#     print(graph)

#     costs = {}
#     pq = []
#     heapq.heappush(pq, (0, k))

#     while pq:
#       cur_cost, cur_v = heapq.heappop(pq)
#       if cur_v not in costs:
#         costs[cur_v] = cur_cost
#         for cost, next_v in graph[cur_v]:
#           next_cost = cur_cost + cost
#           heapq.heappush(pq, (next_cost, next_v))
#     print(costs)
#     for i in range(1, n + 1):
#       if i not in costs:
#         return -1
#     return max(costs.values())

############################################
# import heapq

# BIGNUM = 100000000000

# class Solution:
#   def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#     distances = {vertex: BIGNUM for vertex in range(1, n+1)}
#     pq = []
#     # [소요된시간, 원하는 위치]  원하는 위치까지 소요된 시간
#     heapq.heappush(pq,[0,k])
#     while pq:
#       cur_distance, cur_vector = heapq.heappop(pq)
#       if distances[cur_vector] < cur_distance:
#         continue
#       distances[cur_vector] = cur_distance
#       for i in range(len(times)):
#         if times[i][0] == cur_vector:
#           next_vector, next_distance = times[i][1], times[i][2]
#           distance = cur_distance + next_distance
#           if distance < distances[next_vector]:
#             distances[next_vector] = distance
#             heapq.heappush(pq, (distance, next_vector))
#     if max(distances.values()) == BIGNUM:
#       return -1
#     return max(distances.values())
#########################################
s = Solution()
print(s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)) # 2
print(s.networkDelayTime([[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]], 4, 2)) # 4
print(s.networkDelayTime([[1,2,1]], 2, 1)) # 1
print(s.networkDelayTime([[1,2,1]], 2, 2)) # -1
print(s.networkDelayTime([[2,7,63],[4,3,60],[1,3,53],[5,6,100],[1,4,40],[4,7,95],[4,6,97],[3,4,68],[1,7,75],[2,6,84],\
  [1,6,27],[5,3,25],[6,2,2],[3,7,57],[5,4,2],[7,1,53],[5,7,35],[4,1,60],[5,2,95],[3,5,28],[6,1,61],[2,5,28]], 7, 3)) # 119

### https://leetcode.com/problems/network-delay-time/description/?orderBy=most_votes
############ 그림있음
# 네트워크 지연 시간
# 중간 난이도
# 1부터 n까지 레이블이 붙은 n개의 노드가 있는 네트워크가 주어집니다. 또한, 방향이 있는 간선으로서의 여행 시간 목록인 times가 주어지는데,
# 여기서 times[i] = (ui, vi, wi)는 ui가 출발 노드, vi가 도착 노드, wi가 신호가 출발 노드에서 도착 노드까지 이동하는 데 걸리는 시간을 나타냅니다.
# 주어진 노드 k에서 신호를 보낼 것입니다. 모든 n개 노드가 신호를 받는 데 필요한 최소 시간을 반환하세요. 모든 n개 노드가 신호를 받을 수 없는 경우 -1을 반환하세요.

# 예시 1:

# 입력: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# 출력: 2
# 예시 2:

# 입력: times = [[1,2,1]], n = 2, k = 1
# 출력: 1
# 예시 3:

# 입력: times = [[1,2,1]], n = 2, k = 2
# 출력: -1

# 제약 조건:

# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# 모든 쌍 (ui, vi)은 고유합니다. (즉, 중복 간선이 없습니다.)
