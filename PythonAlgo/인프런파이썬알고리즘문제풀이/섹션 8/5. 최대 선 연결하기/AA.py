# 시작시간 2257 마무리시간

n = int(input())
li = list(map(int,input().split()))
dp = [0] * len(li)
dp[0] = 1
# li에 값은 항상 증가하게 구현해야함
for i in range(1,len(li)):
  max_value = 0 # 현재 가장 긴 앞에 올수 있는것
  for j in range(0,i):
    if li[j] < li[i]: # 조건상 앞에 올수 있음
      max_value = max(max_value, dp[j])
  dp[i] = max_value + 1
print(max(dp))








# 시작시간 1030 마무리시간 1100

"""
수가 중간에 있는게 더 큰게 나오면 선이 엇갈림
오름차순으로 선이 연결되어야함
즉 증가하는 부분수열을 구하는 문제가 됨
10
4 1 2 3 9 7 5 6 10 8
"""
# n = int(input())
# li = list(map(int,input().split()))
# li.insert(0,0)
# dp = [0] * (n+1)
# dp[1] = 1

# for i in range(2,n+1):
#   now_num = li[i]
#   temp = 0
#   for j in range(1,i):
#     if li[j] < now_num:
#       if temp < dp[j]:
#         temp = dp[j]
#   dp[i] = temp + 1
# print(max(dp))
  

