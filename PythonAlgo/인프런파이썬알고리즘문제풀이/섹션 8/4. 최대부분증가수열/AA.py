# 다시풀어보기













# 까먹어서 풀이봄
# 다시풀어보기

# n = int(input())
# li = list(map(int,input().split()))
# dp = [0] * len(li) # 현재 보는게 마지막인 부분증가수열
# dp[0] = 1 # 0번째까지 보면 본인만 부분수열됨

# for i in range(1,len(li)):
#   now_max = 0
#   for j in range(0,i):
#     if li[i] > li[j]:
#       now_max = max(dp[j], now_max)
#   dp[i] = now_max + 1
# print(max(dp))

# 시작시간 0939 마무리시간 0950
# n = int(input())
# li = list(map(int,input().split()))
# li.insert(0,0)
# # print(li)
# dp = [0] * (n+1)
# dp[1] = 1  # 

# for i in range(2,n+1):
#   now_num = li[i]  # 
#   temp = 0 # 가장큰 이전 dp
#   for j in range(1,i):
#     if now_num > li[j]: #
#       if temp < dp[j]:
#         temp = dp[j]
#   dp[i] = temp + 1
# print(max(dp))
  


"""
8
5 3 7 8 6 2 9 4
"""
