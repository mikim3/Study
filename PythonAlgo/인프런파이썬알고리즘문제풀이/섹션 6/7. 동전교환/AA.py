####################
# 모범답안
#

def DFS(level, sum):
  global result
  if result <= level:
    return
  if sum > m:
    return
  if sum == m:
    if level<result:
      result=level
  else:
    for i in range(n):
      DFS(level+1, sum+li[i])

n = int(input())
li = list(map(int, input().split()))
m = int(input())
result = 500
li.sort(reverse=True)
DFS(0, 0)
print(result)

# ##########################
# # 시작시간  231223 19:29    마무리시간 20:14

# def DFS(level):
#   global min_count
#   sum_total = sum(total)
#   # 구하다 보니 줘야될 돈을 넘어섬
#   if min_count <= level:
#     return
#   if sum_total > m:
#     return
#   # 결국 거스름 계산 안될때
#   if max_count < level:
#     return
#   # 결국 딱 떨어짐
#   if m == sum_total:
#     if min_count > level:
#       min_count = level
#   else:
#     for i in range(len(li)): # 케이스 뒤집으면 어떻게 하지???
#       total[i] += li[i]
#       DFS(level + 1)
#       total[i] -= li[i] # 이건 답봄

# n = int(input())
# li = list(map(int,input().split()))
# li.sort(reverse=True)

# m = int(input())
# # 지금까지 준 동전수
# total = [0] * (n+1)
# max_count = int(m // min(li))
# min_count = 500

# DFS(0)
# print(min_count)
# #########################
