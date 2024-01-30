import sys
input = sys.stdin.readline
#########
# 시작시간 240130 15:40 마무리시간
# 못품

# dp[종료일] = max(이전까지의 수익+현재 수익, dp[종료일])

#
# dp[i+t-1] == 해당 상담의 종료일
#

n = int(input())
dp = [0] * (n+1)

for i in range(1, n+1):
  t, p = map(int ,input().split())
  dp[i] = max(dp[i - 1], dp[i])
  # 종료 날짜보다 작
  if i + t <= n + 1:
    dp[i+t-1] = max(dp[i-1] + p, dp[i+t-1])
print(dp)
print(dp[-1])


