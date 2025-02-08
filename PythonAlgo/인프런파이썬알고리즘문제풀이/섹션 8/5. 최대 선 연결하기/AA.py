# 시작시간 1030 마무리시간 1100

"""
수가 중간에 있는게 더 큰게 나오면 선이 엇갈림
오름차순으로 선이 연결되어야함
즉 증가하는 부분수열을 구하는 문제가 됨
10
4 1 2 3 9 7 5 6 10 8
"""
n = int(input())
li = list(map(int,input().split()))
li.insert(0,0)
dp = [0] * (n+1)
dp[1] = 1

for i in range(2,n+1):
  now_num = li[i]
  temp = 0
  for j in range(1,i):
    if li[j] < now_num:
      if temp < dp[j]:
        temp = dp[j]
  dp[i] = temp + 1
print(max(dp))
  

