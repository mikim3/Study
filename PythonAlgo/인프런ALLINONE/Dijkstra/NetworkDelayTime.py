from typing import List

class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

### https://leetcode.com/problems/network-delay-time/description/?orderBy=most_votes
############ 그림있음
# 네트워크 지연 시간
# 중간 난이도
# 주제
# 회사
# 힌트
# 1부터 n까지 레이블이 붙은 n개의 노드가 있는 네트워크가 주어집니다. 또한, 방향이 있는 간선으로서의 여행 시간 목록인 times가 주어지는데, 여기서 times[i] = (ui, vi, wi)는 ui가 출발 노드, vi가 도착 노드, wi가 신호가 출발 노드에서 도착 노드까지 이동하는 데 걸리는 시간을 나타냅니다.
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
