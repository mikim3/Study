# 260217 시작 1818 마무리 1825

import sys
import heapq

a = []

while True:
  n = int(input())
  if n == 0:
    if len(a) > 0:
      print(-heapq.heappop(a))
    else:
      print(-1)
  elif n == -1:
    sys.exit()
  else:
    heapq.heappush(a,-n)

##########################
# 그냥 강의 봄

# import heapq

# a = []
# while True:
#   n = int(input())
#   if n==-1:
#     break
#   if n==0:
#     if len(a) == 0:
#       print(-1)
#     else:
#       # print("yeah")
#       print(-heapq.heappop(a))
#   else:
#     heapq.heappush(a,-n)

#########################
