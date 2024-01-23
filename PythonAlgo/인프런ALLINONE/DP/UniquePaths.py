# 시작시간 240119 16:50 마무리 시간 17:50

# 문제에 DP로 풀어야 되는 근거가 숨겨져 있음

# 테스트 케이스는 답이 2* 10**9 이하가 되도록 생성됩니다.

# m,n 까지 가는 경우의수
# f(m,n) ==  f(m - 1, n) + f(m, n - 1)
memo = {(1,1):1, (2,1) : 1, (1, 2) : 1}
class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    if m < 1 or n < 1:
      return 0
    if m == 1 and n == 1:
      return 1
    if (m,n) not in memo:
      memo[m,n] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
    return memo[m, n]

sol = Solution()
print(sol.uniquePaths(3,2))

############## 그림 있음
# https://leetcode.com/problems/unique-paths/description/
# 유니크한 경로
# 중간 난이도
# 주제
# 회사
# m x n 격자 위에 로봇이 있습니다. 로봇은 처음에 격자의 왼쪽 상단 모서리(즉, grid[0][0])에 위치해 있습니다.
# 로봇은 오른쪽 하단 모서리(즉, grid[m - 1][n - 1])로 이동하려고 합니다.
# 로봇은 어느 시점에서든 오직 아래쪽 또는 오른쪽으로만 이동할 수 있습니다.
# 두 정수 m과 n이 주어졌을 때, 로봇이 오른쪽 하단 모서리에 도달할 수 있는 가능한 유니크한 경로의 수를 반환하세요.

# 테스트 케이스는 답이 2 * 10^9 이하가 되도록 생성됩니다.

# 예시 1:
# 입력: m = 3, n = 7
# 출력: 28

# 예시 2:
# 입력: m = 3, n = 2
# 출력: 3
# 설명: 왼쪽 상단 모서리에서 시작하여, 오른쪽 하단 모서리에 도달하는 총 3가지 방법이 있습니다:

# 오른쪽 -> 아래 -> 아래
# 아래 -> 아래 -> 오른쪽
# 아래 -> 오른쪽 -> 아래

# 제약 조건:
# 1 <= m, n <= 100
