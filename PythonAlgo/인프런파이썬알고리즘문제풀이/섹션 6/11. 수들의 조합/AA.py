##########################
# 시작시간 240212 1708 마무리시간 1723
# 오타때문에 10분날림

# def dfs(level, start):
#   global count
#   if level == k:
#     tmp = 0
#     for i in range(k):
#       tmp += result[i]
#     if tmp % m == 0:
#       count += 1
#   else:
#     # i는 지금 몇번째 카드 뽑을지
#     for i in range(start, n+1):
#       result[level] = li[i - 1]
#       dfs(level + 1, i + 1)

# n, k = map(int, input().split())
# li = list(map(int, input().split()))
# result = [0] * (k + 1)
# m = int(input())
# count = 0
# dfs(0,1)
# print(count)

#############################
# 시작시간 231228 17:13 마무리시간 17:25

# def DFS(level,start):
#   global count
#   if level == k:
#     su = 0
#     for i in range(k):
#       su += result[i]
#     if su % m == 0:
#       count += 1
#   else:
#     for i in range(start, n):
#       result[level] = li[i]
#       DFS(level + 1, i + 1)

# n, k = map(int,input().split()) # n개 중에 ,k개를 선택
# li = list(map(int,input().split())) # 조합 후보군
# m = int(input())
# result = [0] * k
# count = 0
# DFS(0, 0)
# print(count)

# ################################
# # 시작시간 231227 21:27 마무리시간 21:45
# # 배수찾기

# def DFS(level, start):
#   global count
#   if level == k:
#     su = 0
#     for i in range(k):
#       su+=result[i]
#     print('result ==',result, 'su == ', su)
#     if su % m == 0:
#       count += 1
#   else:
#     for i in range(start, n):
#       result[level] = li[i]
#       DFS(level + 1, i + 1)
# n, k = map(int,input().split())
# li = list(map(int, input().split()))
# m = int(input())
# result = [0] * k
# count = 0
# DFS(0,0)
# print(count)

# ####################
# # import itertools as it
# # #sys.stdin=open("input.txt", "r")
# # n, k=map(int, input().split())
# # a=list(map(int, input().split()))
# # m=int(input())
# # cnt=0
# # for x in it.combinations(a, k):
# #     if sum(x)%m==0:
# #         cnt+=1
# # print(cnt)
