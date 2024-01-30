# 시작시간 240130 15:15 마무리시간 15:29
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = li[0]
for i in range(1,n):
  dp[i+1] = dp[i] + li[i]
  # for j in range(n):
for _ in range(m):
  i, j = map(int,input().split())
  print(dp[j] - dp[i-1])
