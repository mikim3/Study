# 시작시간 1140 마무리시간
import sys
sys.setrecursionlimit(1000000)

def dp(i):
  if i <= 0:
    return 1
  if i not in memo:
    memo[i] = dp(i // P - X) + dp(i // Q - Y)
  return memo[i]
N, P, Q, X, Y = map(int,input().split())

memo = {}
if N == 0:
  print(1)
  sys.exit()
dp(N)

print(memo[N])
