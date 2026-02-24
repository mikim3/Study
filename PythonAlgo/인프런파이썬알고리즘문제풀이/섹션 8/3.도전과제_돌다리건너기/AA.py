# 시작 2017 마무리 2032

n = int(input())
dp = [-1] * (n+2)
dp[0] = 0
dp[1] = 1
dp[2] = 2
for i in range(3,n+2):
  dp[i] = dp[i-1] + dp[i-2]
print(dp[n+1])
# print(dp)



# 시작시간 0111 마무리시간

# def dp(i):
#   if i not in memo:
#     memo[i] = dp(i-1) + dp(i-2)
#   return memo[i]
# n = int(input())
# # dp = [-1] * 100
# memo = {
#   1:1,
#   2:2
# }
# print(dp(n))
