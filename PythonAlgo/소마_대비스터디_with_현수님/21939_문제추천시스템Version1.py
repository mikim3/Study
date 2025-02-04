import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
li = []
heapq.heapify(li)


# 문제번호: 난이도
problems = {}

for i in range(n):
  p, l = map(int,input().strip().split())
  heapq.heappush(li,(l,p))
  problems[p] = l  # 문제번호에 난이도 넣기

print(heapq.nlargest(1,li))
print(heapq.nsmallest(1,li))


# dict   === map   map  
m = int(input().strip())
for i in range(m):
  tmp_li = list(map(str,input().strip().split()))
  for j in range(1,len(tmp_li)):
    tmp_li[j] = int(tmp_li[j])
  if tmp_li[0] == 'recommend':
    if tmp_li[1] == 1:
      while li:
      print(heapq.nlargest(1,li)[0])
    if tmp_li[1] == -1:
      print(heapq.nsmallest(1,li)[0])
  if tmp_li[0] == 'add':
    heapq.heappush(li,(tmp_li[2],tmp_li[1]))
    problems[tmp_li[1]] = tmp_li[2]
  if tmp_li[0] == 'solved':
    target = tmp_li[1]
    if target in problems:# 문제 목록에서 삭제
      del problems[target]  # 

# # 시작시간  마무리시간
# # 답봄
# import sys
# import heapq

# input = sys.stdin.readline

# n = int(input().strip())
# li = []
# heapq.heapify(li)
# # 문제번호: 난이도
# problems = {}

# for i in range(n):
#   p, l = map(int,input().strip().split())
#   heapq.heappush(li,(l,p))
#   problems[p] = l  # 문제번호에 난이도 넣기

# print(heapq.nlargest(1,li))
# print(heapq.nsmallest(1,li))


# # dict   === map   map  
# m = int(input().strip())
# for i in range(m):
#   tmp_li = list(map(str,input().strip().split()))
#   for j in range(1,len(tmp_li)):
#     tmp_li[j] = int(tmp_li[j])
#   if tmp_li[0] == 'recommend':
#     if tmp_li[1] == 1:
#       while li:
#       print(heapq.nlargest(1,li)[0])
#     if tmp_li[1] == -1:
#       print(heapq.nsmallest(1,li)[0])
#   if tmp_li[0] == 'add':
#     heapq.heappush(li,(tmp_li[2],tmp_li[1]))
#     problems[tmp_li[1]] = tmp_li[2]
#   if tmp_li[0] == 'solved':
#     target = tmp_li[1]
#     if target in problems:# 문제 목록에서 삭제
#       del problems[target]  # 


##################  실패 코드
# # 시작시간 1140 마무리시간
# import sys
# from collections import deque
# import heapq

# input = sys.stdin.readline

# # recommend x
# # 1이면 가장 어려운 문제의 번호 출력
# # 여러개면 문제 번호 큰것
# # -1 이면 가장 쉬운 문제
# # 만약 가장 쉬운 문제 여러개면 문제번호 작은것

# # add P L
# # 난이도가 L인 문제번호 P를 추가
# # 

# # solved P
# # 추천문제리스트에서 P 문제 제거

# # 난이도가 가장 큰 것과 난이도가 가장 작은 것을 빨리 찾아야함 -> 앞뒤 == queue

# n = int(input().strip())
# li = []
# heapq.heapify(li)

# for i in range(n):
#   p, l = map(int,input().strip().split())
#   heapq.heappush(li,(l,p))

# print(heapq.nlargest(1,li))
# print(heapq.nsmallest(1,li))

# m = int(input().strip())
# for i in range(m):
#   tmp_li = list(map(str,input().strip().split()))
#   for j in range(1,len(tmp_li)):
#     tmp_li[j] = int(tmp_li[j])
#   if tmp_li[0] == 'recommend':
#     if tmp_li[1] == 1:
#       print(heapq.nlargest(1,li)[0])
#     if tmp_li[1] == -1:
#       print(heapq.nsmallest(1,li)[0])
#   if tmp_li[0] == 'add':
#     heapq.heappush(li,(tmp_li[2],tmp_li[1]))
#   if tmp_li[0] == 'solved':
#     target = tmp_li[1]
#     for item in li:
#       if item[1] == target:
#         li.remove(item)
#         heapq.heapify(li)
#         break