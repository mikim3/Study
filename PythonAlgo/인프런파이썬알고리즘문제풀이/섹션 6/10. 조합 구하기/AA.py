###########################
# 시작시간 240212 1643 마무리시간 17:05
# 답봄
# 근데 사실 나 혼자 잘 풀고 있었는데 오타였음

def dfs(level, start):
  global count
  if level >= m:
    for i in range(1,n+1):
      if checked[i] == 1:
        print(i, end=' ')
    print()
    count+= 1
  else:
    for i in range(start, n + 1):
      checked[i] = 1
      dfs(level + 1, i + 1)
      checked[i] = 0

n, m = map(int, input().split())
result = [0] * (n+1)
checked = [0] * (n+1)
count = 0
dfs(0,1)
print(count)

# #########################
# # 시작시간 231227 2040 마무리시간 2054
# # 아직 많이 헷갈림
# def DFS(level, start):
#   global count
#   if level == m:
#     for i in range(m):
#       print(result[i], end=' ')
#     print()
#     count+=1
#   else:
#     # start ~ n 까지 반복
#     for i in range(start, n + 1):
#       result[level] = i
#       # 한 레벨 올라가면 start 값도 1 올라감
#       DFS(level + 1, i + 1)
# n, m = map(int, input().split())
# result = [0] * n
# count = 0
# DFS(0,1)
# print(count)

# ##########################
# # 시작시간 231226 21:16 마무리시간 22:00
# # 못 풀고 강의에서 아이디어만 듣고 풀기시작

# def DFS(level, start):
#   global count
#   if level == m:
#     for i in range(m):
#       print(result[i], end=' ')
#     print()
#     count += 1
#   else:
#     # i가 뜻하는건 현재 level에 넣을 result값임
#     for i in range(start - 1, n):
#       if check[i] == 0:
#         check[i] = 1
#         result[level] = i+1
#         DFS(level + 1, i + 1)
#         check[i] = 0
# n, m = map(int, input().split())
# check = [0] * n
# result = [0] * m
# count = 0
# DFS(0,1)
# print(count)

# #########################
