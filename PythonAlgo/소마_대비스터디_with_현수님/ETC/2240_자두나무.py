# 시작시간 1011 마무리시간
# 답봄 다시 풀어

# 몇번 움직였느냐가 곧 현재위치를 나타낸다.
# 이동횟수 홀수면 2번   짝수면 1번


t, w = map(int, input().split())

li = []
for i in range(t):
  li.append(int(input()))
dp = [[0] * (w+1) for _ in range(t+1)]

for now_t in range(1, t + 1):
  #
  plum = li[now_t - 1]
  for now_w in  range(w+1):
    if now_w == 0:
      if plum == 1:
        dp[now_t][now_w] = dp[now_t - 1][now_w] + 1
      else:
        dp[now_t][now_w] = dp[now_t - 1][now_w]
    else:
      if (now_w % 2 == 0 and plum == 1) or (now_w % 2 == 1 and plum == 2):
        dp[now_t][now_w] = max(dp[now_t - 1][now_w], dp[now_t - 1][now_w - 1]) + 1
      else:
        dp[now_t][now_w] = max(dp[now_t - 1][now_w], dp[now_t - 1][now_w - 1])

result = max(dp[t])
print(result)        
        

