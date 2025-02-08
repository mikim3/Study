##############
# 시작시간 2152 마무리시간 2157

def dfs(level):
  global count 
  if m == level:
    for i in range(m):
      print(result[i], end=' ')
    print()
    count += 1 
  else:
    for i in range(1, n+1):
      result[level] = i
      dfs(level+1)
      result[level] = 0
      
n, m = map(int,input().split())
result = [0] * (m+1)
count = 0
dfs(0)
print(count)



# ##################
# # 시작시간 240211 14:47  마무리시간 14:58

# def dfs(level):
#   global count
#   if level >= m:
#     for i in range(m):
#       print(checked[i], end = ' ')
#     count += 1
#     print()
#   else:
#     for i in range(1, n + 1):
#       checked[level] = i
#       dfs(level+1)
# n, m = map(int, input().split())
# checked = [0] * (m+1)
# count = 0
# dfs(0)
# print(count)

# # ##########################
# # # 시작시간  231223 1727  마무리시간 1824
# # # '==' 을 써야 될 곳에 '>'을 써서 30분 날림 원래는 1754에 풀음

# # # def DFS(level):
# # #   if level == m:
# # #     for i in range(m):
# # #       print(result[i], end=' ')
# # #     print()
# # #   else:
# # #     for i in range(n):
# # #       result[level]= i+1
# # #       DFS(level + 1)

# # # n, m = map(int, input().split())
# # # result = [0] * (n + 1)
# # # DFS(0)

# # #########################
# # # 모범답안
# # def DFS(level):
# #   global count
# #   if level == m:
# #     for i in range(m):
# #       print(result[i], end=' ')
# #     print()
# #     count+=1
# #   else:
# #     for i in range(n):
# #       result[level]= i+1
# #       DFS(level + 1)

# # n, m = map(int, input().split())
# # result = [0] * (n + 1)
# # count = 0
# # DFS(0)
# # print(count)
# # #########################
