# 시작시간 1000 마무리시간 1020
# 두번째로 푸는중
# 무한수열 
import sys
sys.setrecursionlimit(1000000000)

def dp(n):
  if n==0:
    return 1
  if n == 1:
    return 2
  if n not in memo:
    memo[n] = dp(n//P) + dp(n//Q)
  return memo[n]

N,P,Q = map(int,input().split())
if N == 0:
  print(1)
  sys.exit()
memo = {}

print(dp(N))

# # 시작시간 1000 마무리시간
# # 무한수열 
# # 이렇게 풀면 메모리초과
# import sys

# N,P,Q = map(int,input().split())
# if N == 0:
#   print(1)
#   sys.exit()
# dp = [-1] * (N+1)
# dp[0] = 1
# # print(dp)
# dp[1] = 2  # 

# for i in range(2,N+1):
#   #
#   a1= i // P
#   a2=i // Q
#   dp[i] = dp[a1] + dp[a2] 

# # print(dp)
# print(dp[N])

