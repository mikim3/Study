# 시작시간 0040 마무리시간 0100

n = int(input())
dp = [-1] * 1000
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4,n+1):
  dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

