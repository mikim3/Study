# 
"""
6 6
1 4
5 4
4 3
2 5
2 3
6 2
▣ 출력예제 1
1 6 2 5 4 3
"""
from collections import deque

# n,m = map(int, input().split())
# graph = [[0] * (n+1) for _ in range(n+1)]
# degree = [0] * (n+1)
# dq = deque()
# for i in range(m):
#   a,b = map(int, input().split())
#   graph[a][b] = 1 # a다음 b를 하는 방향을 나타냄
#   degree[b] += 1
# for i in range(1,n+1):
#   if degree[i] == 0: # 선행해야할 것이 없다는 뜻
#     dq.append(i)
# while dq:
#   x = dq.popleft() # 
#   print(x, end=' ') 
#   for i in range(1,n+1):
#     if graph[x][i] == 1: # i가 x다음에 할 일이면 차수를 하나 줄인다.
#       degree[i] -= 1
#       if degree[i] == 0: # 결국 차수가 0이 됐으면 다시 큐에 넣는다.
#         dq.append(i)

n,m = map(int,input().split())

li = [[0]*(n+1) for _ in range(n+1)]
degree = [0] * (n+1)
dq = deque()
for i in range(m):
  a,b = map(int,input().split())
  li[a][b] = 1 # a에서 b로 갈수 있음
  degree[b] += 1
# 차수가 0이면 큐에 담기
for i in range(1, len(degree)):
  if degree[i] == 0:
    dq.append(i)

while dq:
  now = dq.popleft()
  print(now,end=' ')
  for i in range(1,n+1):
    if li[now][i] == 1: # 지금 한 일다음이 i이면
      degree[i] -= 1
      if degree[i] == 0:
        dq.append(i)
