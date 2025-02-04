# 시작시간 1616 마무리시간  1626
# 그냥 진짜 최대힙임
import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())
li = []
for i in range(n):
  tmp_in = int(input().strip())
  if tmp_in == 0:
    if not li:
      print(0)
    else:
      print(-heapq.heappop(li))
  else:
    heapq.heappush(li, -tmp_in)
