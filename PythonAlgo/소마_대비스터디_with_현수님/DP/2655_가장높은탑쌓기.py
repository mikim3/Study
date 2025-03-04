# 시작시간 1514 마무리시간 1611
"""
다시 풀기

문제를 살짝 잘못 이해했다. 답은 안 봄

5
25 3 4
4 4 6
9 2 3
16 2 5
1 5 2
"""

n = int(input())
li = []
for i in range(n):
  a,b,c = map(int,input().split())
  li.append([a,b,c,i+1])
li.sort(key=lambda x: (x[0], x[2]), reverse=True)
dp = [0] * n # 최대 쌓을때 높이
dp2 = [[] for _ in range(n)] 
dp[0] = li[0][1]
dp2[0].append(li[0][3])

for i in range(1,n):
  max_value = 0
  max_index = -1
  for j in range(0,i): # 이전에 쌓은애 위에 올릴지 판단
    if li[i][0] < li[j][0] and li[i][2] < li[j][2]:
      if max_value < dp[j]:
        max_value = dp[j]
        max_index = j
  dp[i] = max_value + li[i][1]
  if max_index >= 0:
    dp2[i] = dp2[max_index].copy()
  dp2[i].append(li[i][3])
# print(f"dp2 {dp2} \n dp1 {dp}]")
max_i = 0
for i in range(len(dp)):
  if max(dp) == dp[i]:
    max_i = i
print(len(dp2[max_i]))
for i in range(len(dp2[max_i])-1 , -1, -1):
  print(dp2[max_i][i])