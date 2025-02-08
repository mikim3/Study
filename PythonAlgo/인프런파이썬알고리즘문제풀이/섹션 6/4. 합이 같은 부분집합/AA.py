##################
# 시작시간 2145 마무리시간 2152
import sys

def dfs(level):
  if level >= n:
    half = 0
    for i in range(n):
      if checked[i] == 0:
        half += li[i]
    su = 0
    for i in range(n):
      if checked[i] == 1:
        su += li[i]
    if su == half:
      print("YES")
      sys.exit()
  else:
    checked[level] = 1
    dfs(level+1)
    checked[level] = 0
    dfs(level+1)
  
n = int(input())
li = list(map(int,input().split()))
checked = [0] * (n)

dfs(0)
print("NO")











# ############################
# # 시작시간 240210 19:02 마무리시간 19:13
# import sys

# def dfs(level,tm_sum):
#   if tm_sum * 2 > sum_li:
#     return
#   if level >= n:
#     if tm_sum * 2 == sum_li:
#       print("YES")
#       sys.exit(0) 
#   else:
#     checked[level] = 1
#     dfs(level+1, tm_sum + li[level])
#     checked[level] = 0
#     dfs(level+1, tm_sum)

# n = int(input())
# li = list(map(int,input().split()))
# li.sort(reverse=True)
# sum_li = sum(li)
# checked = [0] * (n+1)

# dfs(0, 0)
# print("NO")

# ##################################
# # 시작시간 231222 2157 마무리시간 2219

# # import sys

# # def DFS(index):
# #   global flag
# #   if index >= n:
# #     sum1= 0
# #     sum2= 0
# #     for i in range(n):
# #       if check[i]==1:
# #         sum1 += li[i]
# #       else:
# #         sum2 += li[i]
# #     if sum1 == sum2:
# #       print("YES")
# #       flag = 1
# #       sys.exit(0)
# #   else:
# #     check[index] = 1
# #     DFS(index + 1)
# #     check[index] = 0
# #     DFS(index + 1)

# # n = int(input())
# # li= list(map(int,input().split()))
# # check = [0] * (n+1)
# # flag = 0
# # DFS(0)

# # if flag == 1:
# #   print("YES")
# # else:
# #   print("NO")


# ###########################
# # # 예제 코드
# # import sys

# # def DFS(level, sum):
# #   # 더 이상 진행할 필요가 없는경우
# #   if sum > total / 2:
# #     return
# #   # 다 수행함
# #   if level == n:
# #     if sum == (total - sum):
# #       print("YES")
# #       sys.exit(0)
# #   else:
# #     DFS(level+1, sum + li_input[level]) # a[level]이라는 값을 사용하는 경우 == 는 현재 레벨을 사용하는경우
# #     DFS(level+1, sum) # 사용 안하는 경우

# # n = int(input())
# # li_input = list(map(int, input().split()))
# # total = sum(li_input)
# # DFS(0,0)
# # print("NO")


# # ##########################
# # # 시작시간 231005 21:50    마무리시간 22:13
# # # 부분집한 구하기 소스를 보면서 풀음
# # # 해당문제를 푸는데는 내 소스가 교수님 소스보다 좋은듯

# # import sys

# # def dfs(node):
# #   if node == n+1:
# #     for i in range(1, n+1):
# #       if check[i] == 1:
# #         li_1.append(li_input[i-1])
# #       else:
# #         li_2.append(li_input[i-1])
# #     if sum(li_1) == sum(li_2):
# #       # print("li_1,2",li_1 , "--------", li_2)
# #       print("YES")
# #       sys.exit(0)
# #     li_1.clear()
# #     li_2.clear()
# #   else:
# #     check[node] = 1
# #     dfs(node + 1)
# #     check[node] = 0
# #     dfs(node + 1)

# # n = int(input())
# # li_input = list(map(int,input().split()))
# # li_1 = []
# # li_2 = []
# # check = [0] * (n+1)
# # dfs(1)

# # print("NO")
# # #########################
