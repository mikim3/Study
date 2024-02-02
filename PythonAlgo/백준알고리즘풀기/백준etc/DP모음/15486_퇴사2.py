import sys
input = sys.stdin.readline
#############
# 시작시간 240202 21:47 마무리시간 20:10  
# 변수 값을 다른 풀이들 보다 실수 안하게 잘 넣은듯

# i일에 t가 3이면 t+3일 부터 일을 할 수 있다.

n = int(input())
d = [0] * (n+2)
t, p = [0] * (n+2), [0] * (n+2)
for day in range(1, n + 1):
  t[day], p[day] = map(int, input().split())

# i가 날짜
for day in range(1, n + 1):
  # 가장 큰값
  d[day]= max(d[day], d[day - 1])
  if day + t[day] > n+1:
    continue
  d[day + t[day]] =  max(d[day] + p[day], d[day + t[day]])

print(max(d))


#########
# 시작시간 240130 15:40 마무리시간
# 못품

# dp[x] == x일 까지 얻을 수 있는 이익

# n = int(input())
# t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
# for day in range(1, n + 1):
#   t[day], p[day] = map(int, input().split())

# dp = [0 for _ in range(n + 1)]

# for day in range(1, n + 1):
#   dp[day] = max(dp[day], dp[day - 1])  # 이전까지의 최댓값
#   fin_date = day + t[day] - 1  # 당일 포함
#   if fin_date <= n:  # 최종일 안에 일이 끝나는 경우
#     # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구한다
#     dp[fin_date] = max(dp[fin_date], dp[day - 1] + p[day])
# print(max(dp))
