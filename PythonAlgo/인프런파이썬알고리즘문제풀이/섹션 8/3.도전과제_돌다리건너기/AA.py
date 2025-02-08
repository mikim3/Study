# 시작시간 0111 마무리시간

def dp(i):
  if i not in memo:
    memo[i] = dp(i-1) + dp(i-2)
  return memo[i]
n = int(input())
# dp = [-1] * 100
memo = {
  1:1,
  2:2
}
print(dp(n))
