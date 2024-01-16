
# 시작시간 240116 15:32 마무리시간

# tablenation 혹은 바텀업 방식
memo = {1:1, 2:2}
class Solution:
  def climbStairs(self, n: int) -> int:
    for i in range(3, n+1):
      memo[i] = memo[i-1] + memo[i-2]
    return memo[n]
# memo = {1:1, 2:2}
# class Solution:
#   def climbStairs(self, n: int) -> int:
#     if n == 1:
#       return 1
#     if n == 2:
#       return 2
#     if n not in memo:
#       memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
#     return memo[n]
# 여기에서 테스트 케이스를 실행합니다
sol = Solution()
print(sol.climbStairs(1))  # 예상 출력: 1
print(sol.climbStairs(3))  # 예상 출력: 3
print(sol.climbStairs(5))  # 예상 출력:
print(sol.climbStairs(45))  # 예상 출력:

########################### 문제
# 당신은 계단을 오르고 있습니다. 정상에 도달하기 위해서는 n개의 계단을 올라야 합니다.

# 매번 1계단 또는 2계단을 오를 수 있습니다. 몇 가지 고유한 방법으로 정상에 도달할 수 있나요?
# 예시 1:
# 입력: n = 2
# 출력: 2
# 설명: 정상에 오르는 두 가지 방법이 있습니다.

# 1계단 + 1계단
# 2계단
# 예시 2:
# 입력: n = 3
# 출력: 3
# 설명: 정상에 오르는 세 가지 방법이 있습니다.

# 1계단 + 1계단 + 1계단
# 1계단 + 2계단
# 2계단 + 1계단
# 제약 사항:
# 1 <= n <= 45
#############################
