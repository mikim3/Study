# 시작시간 0939 마무리시간 0950


n = int(input())
li = list(map(int,input().split()))
li.insert(0,0)
# print(li)
dp = [0] * (n+1)
dp[1] = 1  # 

for i in range(2,n+1):
  now_num = li[i]  # 
  temp = 0 # 가장큰 이전 dp
  for j in range(1,i):
    if now_num > li[j]: #
      if temp < dp[j]:
        temp = dp[j]
  dp[i] = temp + 1
print(max(dp))
  


"""
8
5 3 7 8 6 2 9 4
"""
