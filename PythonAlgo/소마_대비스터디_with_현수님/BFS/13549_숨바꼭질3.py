# 시작시간 1933 마무리시간 2050
# 비슷한 유형에 답을 보고 다시와서 풀음

from collections import deque
# 시작 n
# 목적지 k
MAX = 100000
#
time = [9999999] * (MAX + 1)
n, k = map(int, input().split())
# 출발점에서 지난 시간 0
time[n] = 0
# bfs 가야할 다음 위치들을 담고 있는 deque
queue = deque()
queue.append(n)

while queue:
  # 현재 위치
  now = queue.popleft()
  next = now * 2
  if 0 <= next <= MAX:
    if time[now] < time[next]:
      queue.append(next)
      time[next] = time[now]
  for next in (now-1, now+1):
    if 0 <= next <= MAX:
      # 만약에 다음 좌표에 시간에 +1 된게 현재 저장되어 있는 시간보다 크면
      if time[now] + 1 < time[next]:
        queue.append(next)
        time[next] = time[now] + 1

# print(time)
print(time[k])
