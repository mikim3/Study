# 시작시간 0927 마무리시간 0945
n = int(input())
li = []
for i in range(n):
  a,b,c, = map(int,input().split())
  li.append([a,b,c])
li.sort(reverse=True)
dp = [0] * n # n개의 벽돌이 본인입장에서 쌓을수 있는 최대높이
dp[0] = li[0][1]

for i in range(1,n):
  max_value = 0
  for j in range(0,i):
    if li[i][0] < li[j][0] and li[i][2] < li[j][2]: 
      max_value = max(max_value, dp[j]) # i 높이 제외하고 밑에 쌓을수 있는 최대
  dp[i] = max_value + li[i][1]
# print(dp)
print(max(dp))

# 시작시간 2303
"""
밑면이 넓어져야함
무거운 벽돌이 가벼운 벽돌위에 있을수 없다.
넓은게 밑에 무거운게 밑에
"""

# n = int(input())
# li = []
# for i in range(n):
#   # 넓이,높이,무게
#   a,b,c = map(int,input().split())
#   li.append([a,b,c])
# li.sort(reverse=True)

# dp = [0] * n
# dp[0] = li[0][1]
# for i in range(1,n):
#   max_value = 0
#   for j in range(0,i):
#     if li[j][0] > li[i][0] and li[j][2] > li[i][2]:
#       max_value = max(max_value, dp[j])
#   dp[i] += (max_value + li[i][1]) 
# # print(dp)
# print(max(dp))


