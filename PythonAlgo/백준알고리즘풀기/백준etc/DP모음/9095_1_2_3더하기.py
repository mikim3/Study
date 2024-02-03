import sys
input = sys.stdin.readline

#######################
# 시작시간 240203  13:42 마무리시간 14:00

t = int(input())
f = [0] * (10+1)

f[0] = 0
f[1] = 1
f[2] = 2
f[3] = 4

for i in range(4 ,11):
  f[i] = f[i - 3] + f[i - 2] + f[i - 1]

for i in range(t):
  case = int(input())
  print(f[case])

#################
# 시작시간 240130 11:10 마무리시간
# 못 품

# import sys
# input = sys.stdin.readline
# t = int(input())
# # 1    1
# # 2    1+1 2
# # 3    (2) + 1   1 + (2)  3  == 4
# # 4    (3) + 1   1 + (3)  == 7
# # 5                == 13
# dp = [0] * (10+1)
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4

# for i in range(4, 11):
#   dp[i] = dp[i-1] + dp[i - 2]+ dp[i - 3]

# for i in range(t):
#   n = int(input())
#   print(dp[n])
