##########################
# 그냥 강의 봄

import heapq

a = []
while True:
  n = int(input())
  if n==-1:
    break
  if n==0:
    if len(a) == 0:
      print(-1)
    else:
      # print("yeah")
      print(heapq.heappop(a))
  else:
    heapq.heappush(a,n)

#########################
