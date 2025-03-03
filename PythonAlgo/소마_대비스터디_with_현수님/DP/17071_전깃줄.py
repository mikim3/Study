# 시작시간 2350 마무리시간 2404
"""

"""

n = int(input())
dp = [1]*n
li = []
for i in range(n):
  li.append(list(map(int,input().split())))
li.sort()
dp[0] = 1

for i in range(n):
  max_value = 0
  for j in range(i):
    if li[j][1] < li[i][1]:
      max_value = max(max_value, dp[j])
  dp[i] = max_value + 1

print(n-max(dp))