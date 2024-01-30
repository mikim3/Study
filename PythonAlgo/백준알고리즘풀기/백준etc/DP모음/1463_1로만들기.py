##############
# 시작시간 240130 10:05 마무리시간
n = int(input())
dp = [0] * (1000100)
dp[2] = 1
dp[3] = 1
dp[4] = 2
for i in range(5, n + 1):
  if i % 3 == 0:
    if dp[i] != 0:
      dp[i] = min(dp[i], dp[i//3] + 1)
    else:
      dp[i] = dp[i//3] + 1
  if i % 2 == 0:
    if dp[i] != 0:
      dp[i] = min(dp[i], dp[i//2] + 1)
    else:
      dp[i] = dp[i//2] + 1
  if dp[i] != 0:
    dp[i] = min(dp[i], dp[i-1] + 1)
  else:
    dp[i] = dp[i-1] + 1
print(dp[n])

################
# 시작시간 240127 18:20
# 못품

n = int(input())
# base로 다 0 으로 초기화
d = [0] * (n + 1)

# 2부터 시작하고 d[i] = d[i - 1] + 1 를 먼저한 덕에 d[1] = 0이 기본 값이 됨 실제로 d[1]은 0 회가 맞음
# 그리고 바로 d[2]는 1이 된다.
# 그 두개의 base값을 가지고 나머지를 bottom-up하게 계산해 나간다.
# 추가로 d[i] = d[i - 1] + 1을 먼저하면
# 그 아래 코드에서는 d[i]가 비어 있지 않는다. 즉 min(d[i], ~~) 코드에서 비교하는 d[i]값이 기본값 0이 아니라 유효한 값이 된다.
for i in range(2, n + 1):
  d[i] = d[i - 1] + 1
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
print(d[n])
