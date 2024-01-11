import sys
input = sys.stdin.readline

#########################
# 시작시간 240111 21:25 마무리시간 21:55
# 10분만에 거의 다풀고 for i in range(li[level][1]+1):  +1 빼먹어서 20분 더 걸림

def dfs(level, now_money):
  global count
  if now_money > T:
    return
  if level == k:
    if now_money == T:
      count += 1
  else:
    for i in range(li[level][1]+1):
      dfs(level + 1, now_money + li[level][0] * i)
T = int(input())
k = int(input())
li = []
for i in range(k):
  li.append(list(map(int,input().split())))
print(li)
count = 0
dfs(0, 0)
print(count)

# #############################
# # 모범답안

# def DFS(level, sum):
#   global count
#   if sum > T:
#     return
#   if level == k:
#     if sum == T:
#       count += 1
#   else:
#     for i in range(coin_count[level] + 1):
#       DFS(level+1, sum + (coin_value[level] * i))

# T=int(input())
# k=int(input())
# count = 0
# coin_value = []
# coin_count = []
# for i in range(k):
#   a, b = map(int, input().split())
#   coin_value.append(a)
#   coin_count.append(b)
# DFS(0,0)
# print(count)

# ##########################
# # 시작시간 240101 19:33 240102 40분소비 14:46 마무리시간
# # 답봄
# # 시간초과해서 안됨

# def DFS(level):
#   global count
#   if level == k:
#     tmp_sum = 0
#     for i in range(k):
#       tmp_sum += li[i][0] * result[i]
#     if tmp_sum == t:
#       count += 1
#   else:
#     for i in range(li[level][1] + 1):
#       result[level] = i
#       DFS(level + 1)

# t= int(input())
# # 가지수
# k = int(input())
# li = []
# # 몇 번째 동전이 몇개 인지
# result = [0] * k
# count = 0
# for i in range(k):
#   li.append(list(map(int,input().split())))
# DFS(0)
# print(count)

# #########################
