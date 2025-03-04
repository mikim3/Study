# 시작시간 1700 마무리시간 1721
# Bottom Up
"""
5
3 7 2 1 9
5 8 3 9 2
5 3 1 2 3
5 4 3 2 1
1 7 5 2 4

"""
n = int(input())
li = [[0] * (n+2)]
for i in range(n):
  li.append([0] + list(map(int,input().split())) + [0])
dp = [[99] * (n+2) for _ in range(n+1)]

dp[1][1] = li[1][1]
# print(li)
# print(dp)

for i in range(1,n+1):
  for j in range(1,n+1):
    if i == 1 and j == 1:
      continue
    dp[i][j] = min(dp[i-1][j]+li[i][j], dp[i][j-1]+li[i][j])

# print(dp)
print(dp[n][n])
# for i in range(n+1):
#   print(dp[i])
