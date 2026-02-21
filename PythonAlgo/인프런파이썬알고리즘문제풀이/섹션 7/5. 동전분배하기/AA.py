# 260221 시작 0915  마무리 0943
# 오타 + 문제 잘못 읽어서 20분 날림

# def dfs(level):
#   global res
#   if level == n:
#     su_a, su_b,su_c = 0,0,0
#     for i in range(n):
#       if ch[i] == 0:
#         su_a +=li[i]
#       if ch[i] == 1:
#         su_b +=li[i]
#       if ch[i] == 2:
#         su_c += li[i]
#     if su_a != su_b and su_b != su_c and su_a != su_c: 
#       if res > max(su_a,su_b,su_c) - min(su_a,su_b,su_c):
#         # print(ch)
#         # print(su_a,su_b,su_c)
#         res =  max(su_a,su_b,su_c) - min(su_a,su_b,su_c)
#   else:
#     ch[level] = 0
#     dfs(level+1)
#     ch[level] = 1
#     dfs(level+1)
#     ch[level] = 2
#     dfs(level+1)
# n = int(input())
# li = []
# for i in range(n):
#   li.append(int(input()))
# ch = [0] * (n) # 0,1,2 abc
# res = 9999999
# dfs(0)
# print(res)


#########################
# 시작시간 240213 20:39   마무리시간 20:50
# 비효율적인가 고민 했는데 그게 맞음
# def dfs(level):
#   global min_value
#   if level == n:
#     a,b,c = 0,0,0
#     for i in range(n):
#       if checked[i] == 0:
#         a+=li[i]
#       if checked[i] == 1:
#         b+=li[i]
#       if checked[i] == 2:
#         c+=li[i]
#     if a!=b and b!=c and a!=c:
#       tmp = max(abs(a-b), abs(b-c), abs(a-c))
#       if tmp < min_value:
#         min_value = tmp
#   else:
#     checked[level] = 0
#     dfs(level+1)
#     checked[level] = 1
#     dfs(level+1)
#     checked[level] = 2
#     dfs(level+1)

# 3명에게 나누어서 총액의 최대 차가 가장 적도록하기
# n = int(input())
# li = []
# for i in range(n):
#   li.append(int(input()))
# checked = [0] * (n+1)
# min_value = 999999
# dfs(0)
# print(min_value)

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
