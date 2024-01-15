from collections import deque
# 240115 deepcopy함수 없애고 다시품

# 씨발
# 최소값부터 최대값까지 물 뿌려보면서 최대값 구하는 거였네

def bfs(x, y, h, visited):
  queue = deque()
  queue.append([x, y])
  visited[x][y] = True
  while queue:
    now = queue.popleft()
    for i in range(4):
      next_x = now[0] + dx[i]
      next_y = now[1] + dy[i]
      if 0 <= next_x < n and 0 <= next_y < n and \
        not visited[next_x][next_y] and matrix[next_x][next_y] > h:
        queue.append([next_x, next_y])
        visited[next_x][next_y] = True

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
matrix = []
for i in range(n):
  matrix.append(list(map(int,input().split())))

h_list = set()
for i in range(n):
  for j in range(n):
    h_list.add(matrix[i][j])

count_list = []
for h in h_list:
  visited = [[False] * n for _ in range(n)]
  count = 0
  for i in range(n):
    for j in range(n):
      if matrix[i][j] > h and not visited[i][j]:
        bfs(i, j, h, visited)
        count += 1
  count_list.append(count)
print(max(count_list))

# # 시작시간 240115 15:50 마무리시간 16:42
# import copy

# # 씨발
# # 최소값부터 최대값까지 물 뿌려보면서 최대값 구하는 거였네

# def bfs(x, y, h):
#   global tmp_matrix
#   queue = deque()
#   queue.append([x, y])
#   while queue:
#     now = queue.popleft()
#     for i in range(4):
#       next_x = now[0] + dx[i]
#       next_y = now[1] + dy[i]
#       if 0 <= next_x < n and 0 <= next_y < n and tmp_matrix[next_x][next_y] > h:
#         queue.append([next_x, next_y])
#         tmp_matrix[next_x][next_y] = -1

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# n = int(input())
# matrix = []
# for i in range(n):
#   matrix.append(list(map(int,input().split())))

# h_list = set()
# for i in range(n):
#   for j in range(n):
#     h_list.add(matrix[i][j])

# count_list = []
# for h in h_list:
#   tmp_matrix = copy.deepcopy(matrix)
#   count = 0
#   for i in range(n):
#     for j in range(n):
#       if tmp_matrix[i][j] > h:
#         bfs(i, j, h)
#         count += 1
#   count_list.append(count)
# print(max(count_list))

# import sys
# dx=[-1, 0, 1, 0]
# dy=[0, 1, 0, -1]
# sys.setrecursionlimit(10**6)
# def DFS(x, y, h):
#     ch[x][y]=1
#     for i in range(4):
#         xx=x+dx[i]
#         yy=y+dy[i]
#         if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
#             DFS(xx, yy, h)

# if __name__=="__main__":
#     n = int(input())
#     cnt = 0
#     res = 0
#     board=[list(map(int, input().split())) for _ in range(n)]
#     for h in range(100):
#         ch=[[0]*n for _ in range(n)]
#         cnt=0
#         for i in range(n):
#             for j in range(n):
#                 if ch[i][j]==0 and board[i][j]>h:
#                     cnt+=1
#                     DFS(i, j, h)
#         res=max(res, cnt)
#         if cnt==0:
#             break
#     print(res)





