##########################
# 모범답안
def DFS(now):
  global count
  if now==n:
    for i in result:
      print(i, end=' ')
    print()
    count+=1
  else:
    for i in range(1, n + 1):
      if graph[now][i] == 1 and check[i] == 0:
        check[i] = 1
        result.append(i)
        DFS(i)
        check[i] = 0
        result.pop()
    
n, m = map(int,input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
count = 0
result = []
result.append(1)
check= [0] * (n+1)
check[1] = 1
for i in range(m):
  a,b = map(int,input().split())
  graph[a][b] = 1

DFS(1)
print(count)

# ######################
# # 시작시간 231229 22:50 마무리시간 23:20

# def DFS(now, result:list):
#   global count
#   if now==n:
#     # for i in range(len(result)):
#     #   print(result[i], end=' ')
#     # print()
#     count+=1
#   else:
#     for i in range(1, n + 1):
#       if i not in result:
#         if graph[now][i] == 1:
#           result.append(i)
#           DFS(i, result)
#           result.pop()
    
# n, m = map(int,input().split())
# graph = [[0] * (n + 1) for _ in range(n + 1)]
# count = 0
# for i in range(m):
#   a,b = map(int,input().split())
#   graph[a][b] = 1
# # for i in range(1, n+1):
# #   for j in range(1, n+1):
# #     print(graph[i][j], end=' ')
# #   print()

# DFS(1,[1])
# print(count)

# ##########################
# # 시작시간 231228 21:25    마무리시간 22:24 못품  나중에 더 해보기
# # 순열 + graph 문제임

# # d위로 올라가면 result도 복귀

# # level 현재순서 역할도 함
# def DFS(level, now):
#   if level == n:
#     for i in range(1, n + 1):
#       print(result[i], end=' ')
#     print()
#     for i in range(2, n + 1):
#       result[i] = 0
#   else:
#     # i 는 다음에 이동할 좌표
#     for i in range(1, n + 1):
#       #
#       if graph[now][i] == 1:
#         # j번째로 이동한 위치를 i로 설정
#         for j in range(1,n+1):
#           if result[j] == 0:
#             result[j] = i
#             break
#         DFS(level + 1, i)
#         # result[i] = 0

# n, m  = map(int, input().split())
# graph = [[0] * (n + 1) for _ in range(n + 1)]
# for i in range(m):
#   a, b = map(int, input().split())
#   graph[a][b] = 1
# for i in range(1, n+1):
#   for j in range(1, n+1):
#     print(graph[i][j], end=' ')
#   print()
# # 해당 순서에 지나간 노드가 어디인지 표시
# result = [0] * (n + 1)
# result[1] = 1
# # 이미 지나간 위치 표시
# check_already = [0] * (n + 1)

# # 1번을 지나서 1레벨은 이미 통과한거임
# DFS(1, 1)


# #########################
