n = int(input())

li = list(map(int,input().split()))
now_value = 0
dp = [0] * (n) # 현재까지 가장긴 부분수열
dp[0] = 1

for i in range(1,n):
  max_value = 0
  for j in range(0,i):
    if li[i] > li[j]:
      max_value = max(max_value, dp[j])
  dp[i] = max_value + 1
print(max(dp))
