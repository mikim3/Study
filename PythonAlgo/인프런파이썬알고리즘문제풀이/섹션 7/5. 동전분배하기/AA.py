#########################
# 시작시간 240213 19:00   마무리시간

def dfs(level):
  if level == n:

  else:


# 3명에게 나누어서 총액의 최대 차가 가장 적도록하기

n = int(input())
li = []
for i in range(n):
  li.append(int(input()))
checked = [0] * (n+1)




# ##########################
# # 시작시간  240102 15:50   마무리시간 16:40

# def DFS(level):
#   global min_diffcult
#   if level == n:
#     sum1 = 0
#     sum2 = 0
#     sum3 = 0
#     for i in range(n):
#       if check[i] == 2:
#         sum1 += li[i]
#       if check[i] == 1:
#         sum2 += li[i]
#       if check[i] == 0:
#         sum3 += li[i]
#     if sum1 == sum2 or sum1== sum3 or sum2 == sum3:
#       return
#     tmp_min_value = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)
#     if min_diffcult > tmp_min_value:
#       min_diffcult = tmp_min_value
#   else:
#     check[level] = 2
#     DFS(level+1)
#     check[level] = 1
#     DFS(level+1)
#     check[level] = 0
#     DFS(level+1)

# n = int(input())
# li = []
# for i in range(n):
#   li.append(int(input()))
# check = [0] * n
# min_diffcult = 10000000
# DFS(0)
# print(min_diffcult)
# #########################
