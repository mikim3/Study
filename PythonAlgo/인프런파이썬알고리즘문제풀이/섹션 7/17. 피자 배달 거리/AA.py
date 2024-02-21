##########################
# 시작시간  240220 1653   마무리시간

# import math

# 각 집의 피자배달거리는 해당 집과 도시의 존재하는 피자집들과의 거리 중 최소값을 해당 집의 “피자배달거리”라고 한다.
# 도시의 피자 배달 거리는 각 집들의 피자 배달 거리를 합한 것을 말합니다.
# 피자배달거리는 |x1-x2|+|y1-y2|
# 피자집 m개만 살리고 나머지 폐업 시킬꺼다.

# 그때 최소값 도시의 피자배달거리를 구해라

# 집들의 좌표를 리스트에 담는다. [[,],,]
# 피자집 좌표랑 최소거리가 담겨 있는 리스트를 만든다.[[x,y, distance],,]

# n, m = map(int, input().split())

# li = []
# for i in range(n):
#   li.append(list(map(int, input().split())))
# print(li)







#########################

import sys
# sys.stdin=open("input.txt", "r")
def DFS(level, start):
  global res
  if level==m:
    sum=0
    for j in range(len(hs)):
      x1=hs[j][0]
      y1=hs[j][1]
      dis=2147000000
      for x in combination:
        x2=pz[x][0]
        y2=pz[x][1]
        dis=min(dis, abs(x1-x2)+abs(y1-y2))
      sum+=dis
    if sum<res:
      res=sum
  else:
    for i in range(start, len(pz)):
      combination[level]=i
      DFS(level+1, i+1)
       
if __name__=="__main__":
  n, m=map(int, input().split())
  board=[list(map(int, input().split())) for _ in range(n)]
  hs=[]
  pz=[]
  combination=[0]*m
  res=2147000000
  for i in range(n):
    for j in range(n):
      if board[i][j]==1:
        hs.append((i, j))
      elif board[i][j]==2:
        pz.append((i, j))
  DFS(0, 0)
  print(res)


