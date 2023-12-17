##########################
# 시작시간  231115 2345   마무리시간
# 바로 수업들음

import sys
from collections import deque

MAX = 10001
ch = [0] * (MAX+1) # 해당 위치를 지나갔는지 체크하는 배열
dis = [0] * (MAX+1) # 해당 위치를 몇 번 만에 갔는지 기록하는 배열
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)
while dQ: # 덱 비어있으면 멈춤
  now = dQ.popleft() 
  if now == m: # 목표지점 발견
    break
  for next in (now-1, now+1, now+5): # 튜플값을 하나씩 뻗음
    if 0 < next <= MAX:
      if ch[next] == 0:
        dQ.append(next)
        ch[next] = 1
        dis[next] = dis[now] + 1
print(dis[m])

#########################
