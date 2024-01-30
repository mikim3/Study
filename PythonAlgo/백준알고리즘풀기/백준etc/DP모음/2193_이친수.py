# 시작시간 240130 14:25 마무리시간 14:52

# dp[0] = 1
# dp[1] = 0
n = int(input())
dp = [0] * (n+3)
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
  dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
