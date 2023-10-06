##########################
# 시작시간     마무리시간
# 바로 수업들음

import sys
from collections import deque
MAX = 10000
check = [0] * (MAX + 1)
dis = [0]
n, m = map(int, input().split())
# 현재위치 지나간 곳이니까 체크
check[n] = 1
#
dis[n] = 0

#
dQ = deque()
dQ.append(n)

while dQ:
  now = dQ.popleft()
  if now == m:
    break
  for next in(now - 1, now + 1, now + 5):
    if 0 < next <= MAX:
      if check[next] == 0:
        dQ.append(next)
        check[next] = 1
        dis[next] = dis[now] + 1


#########################
