

# 
def backtracking(level, start):
  if level == m:
    for i in range(m):
      if result[i] != 0:
        print(result[i], end=' ')
    print()
  else:
    temp = 0
    for i in range(start, n):
      if li[i] != temp:
        result[level] = li[i]
        temp = li[i]
        backtracking(level+1, i + 1)
        result[level] = 0
      
    
# 입력갯수, 수열 크기
n, m = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
result = [0] * (m+1)

backtracking(0,0)


# 시작시간 1637  마무리시간

# n개의 수 중에 m개의 조합을 골라야함
# 

# 경우의수 개 작음
# DFS
# def dfs(level):
#   if level>=m:
#     for i in range(n):
#       if checked[i] == 1:
#         print(li[i], end=' ')
#     print()
#     return
#   overlap = 0 # 이전 숫자랑 겹치는지 확인해야함
#   for i in range(level, n):
#     # 이미 방문한 곳 or 직전에 고른 값이랑
#     if checked[i] == 1 or overlap == li[i-1]:
#       continue
#     checked[i] = 1
#     overlap = li[i]
#     dfs(level+1)
#     checked[i] = 0

# # 입력갯수, 수열 크기
# n, m = map(int,input().split())
# li = list(map(int,input().split()))
# li.sort()
# checked = [0] * (n+1)

# dfs(0)


# # 시작시간 1637  마무리시간

# # n개의 수 중에 m개의 조합을 골라야함
# # 

# # 경우의수 개 작음
# # DFS
# def dfs(level, select):
#   if level>=n:
#     for i in range(n):
#       if checked[i] == 1:
#         print(li[i], end=' ')
#     print()
      
#   else:
#     if select < m:
#       checked[level] = 1
#       dfs(level + 1, select+1)
#     checked[level] = 0
#     dfs(level + 1, select)

# # 입력갯수, 수열 크기
# n, m = map(int,input().split())
# li = list(map(int,input().split()))
# li.sort()
# checked = [0] * (n+1)  # 해당 좌표 선택할지 저장
# dfs(0,0)