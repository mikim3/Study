from typing import List

# 시작시간 15:40 마무리시간 16:23

# 10번째 계단에 오르는 비용 == (9번째 최소로 오른 비용 or 8번째를 최소로 오른 비용) <-- 둘중에 10번째로 \
# 가기 위한 비용이 더 적은놈

# 이전 두개 중에 더 작은놈 골라서 올라감

# memo = {0:0, 1:0}
# class Solution:
#   def minCostClimbingStairs(self, cost: List[int]) -> int:
#     # , 현재 몇번째 계단, 총 비용
#     n = len(cost)
#     for i in range(2, n+1):
#       tmp_min = 0
#       if memo[i-1] + cost[i-1] < memo[i-2] + cost[i-2]:
#         memo[i] = memo[i-1] + cost[i-1]
#       else:
#         memo[i] = memo[i-2] + cost[i-2]
#     return memo[n]

####################
# 모범답안
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(n):
            if n == 0 or n == 1:
                return 0
            if n not in memo:
                memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])
            return memo[n]

        result = dp(len(cost))
        return result

sol = Solution()
print(sol.minCostClimbingStairs([10,15,20])) # 15
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])) # 6

##########
####https://leetcode.com/problems/min-cost-climbing-stairs/description/
# 계단 오르기 최소 비용
# 계단에서 i번째 계단을 오를 때의 비용이 담긴 정수 배열 cost가 주어집니다.
# 비용을 지불하면 한 계단 또는 두 계단을 올라갈 수 있습니다.

# 0번째 계단에서 시작하거나 1번째 계단에서 시작할 수 있습니다.

# 맨 위층에 도달하는데 필요한 최소 비용을 반환하세요.

# 예시 1:
# 입력: cost = [10,15,20]
# 출력: 15
# 설명: 1번 인덱스에서 시작합니다.

# 15를 지불하고 두 계단을 올라 맨 위에 도달합니다.
# 총 비용은 15입니다.

# 예시 2:
# 입력: cost = [1,100,1,1,1,100,1,1,100,1]
# 출력: 6
# 설명: 0번 인덱스에서 시작합니다.

# 1을 지불하고 두 계단을 올라 2번 인덱스에 도달합니다.
# 1을 지불하고 두 계단을 올라 4번 인덱스에 도달합니다.
# 1을 지불하고 두 계단을 올라 6번 인덱스에 도달합니다.
# 1을 지불하고 한 계단을 올라 7번 인덱스에 도달합니다.
# 1을 지불하고 두 계단을 올라 9번 인덱스에 도달합니다.
# 1을 지불하고 한 계단을 올라 맨 위에 도달합니다.
# 총 비용은 6입니다.

# 제약 조건:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

