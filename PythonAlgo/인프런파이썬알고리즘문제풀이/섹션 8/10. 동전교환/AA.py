














# 시작시간 2121 2136

# n = int(input())
# li = list(map(int,input().split()))
# want = int(input())
# dp = [1000] * (want+1) # dp[10] = 2  10거슬러주기 위해 2개의 동전필요 
# dp[0] = 0
# for i in range(len(dp)):
#   dp[i] = i

# for i in range(n):
#   for j in range(li[i],want+1): # j는 현재돈을 나타내게됨
#     dp[j] = min(dp[j-li[i]] + 1, dp[j])
# # print(dp)
# print(dp[want])

