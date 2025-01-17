# 시작시간 마무리시간
# 답봄
# DP로 푸는게 속편함

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

# dp[x][y][각도]       
dp = [[[0] * 3 for _ in range(n)] for __ in range(n)]

# 초깃값 설정: (0,1) 에 가로방향놓임
dp[0][1][0] = 1

for x in range(n):
  for y in range(n):
    if house[x][y] == 1:
      continue # 벽만남

    # x,y 에 가로로 놓인 경우의수
    # 현재 좌표 (x,y)에 가로로 놓으려면, (x, y-1)가 가로 또는 대각이여야함
    if y - 1 >= 0:
      dp[x][y][0] += dp[x][y - 1][0] + dp[x][y-1][1]
      
    # (x,y) 위치에 세로 방향으로 놓인 경우의수
    # (x-1, y) 에서 이미 세로 방향(dp[x-1][y][2]) 또는 대각방향 (dp[x-1][y][1]) 로 놓여 있어야함
    if x - 1 >= 0:
      dp[x][y][2] += dp[x-1][y][2] + dp[x-1][y][1]
    
    # 대각
    if x-1 >= 0 and y-1 >= 0:
      if house[x][y-1] == 0 and house[x-1][y] == 0:
        dp[x][y][1] += (dp[x-1][y-1][0] +
                        dp[x-1][y-1][1] +
                        dp[x-1][y-1][2])
  

# 결국 (n-1, n-1)에 놓일수 있는 모든 경우의수를 검사
print(dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2])


# # 시작시간  마무리시간
# # bfs는 시간초과
# # heapq는 가능하다
# # 근데 메모리제이션을 해야 돼서 그냥 DP로 푸는게 좋은 문제다.

# from collections import deque
# import heapq
# import sys

# input = sys.stdin.readline

# # 회전은 45도
# # 미는건 오른쪽 아래 또는 오른쪽 아래 대각선
# # 텍스트로는 안 그래 보이는데 그림보면
# # 45도 옮길때 반드시 이동도 해야함
# # 생각해보면 머리의 위치만 중요함


# # 
# # 파이프 한 쪽 끝을 N,n

# # 벽은 1
# # 빈칸은 0 

# # start_vec (x,y,각도)
# def bfs(start_vec):
#   count = 0 # 
#   queue = deque()
#   queue.append(start_vec)
#   while queue:
#     x,y,angle = queue.popleft()
    
#     for next_angle in range(3):
#       nx = x + dx[next_angle]
#       ny = y + dy[next_angle]
#       # 다음으로 나올수 없는 각도
#       if (angle == 0 and next_angle == 2) or (angle == 2 and next_angle == 0):
#         continue
#       if nx < 0 or nx >= n or ny < 0 or ny >= n or li[nx][ny] == 1:
#         continue
#       # 대각선일때는 2곳 더 확인해야함
#       if (next_angle == 1 and li[x][y + 1] == 1) or (next_angle == 1 and li[x + 1][y] == 1):
#         continue
#       queue.append((nx, ny, next_angle))
#       if nx == n-1 and ny == n - 1:
#         count += 1
#   return count

# dx = [0,1,1]
# dy = [1,1,0]
# # angle 0
# now_angle = 0

# n = int(input())

# li = []
# for i in range(n):
#   li.append(list(map(int, input().split())))
  
# # 머리가 (0,1) 각도 0
# count = bfs((0, 1, 0))

# print(count)

# # 시작시간 2053 마무리시간

# from collections import deque
# import sys

# input = sys.stdin.readline

# # 회전은 45도
# # 미는건 오른쪽 아래 또는 오른쪽 아래 대각선
# # 텍스트로는 안 그래 보이는데 그림보면
# # 45도 옮길때 반드시 이동도 해야함
# # 생각해보면 머리의 위치만 중요함


# # 
# # 파이프 한 쪽 끝을 N,n

# # 벽은 1
# # 빈칸은 0 

# # start_vec (x,y,각도)
# def bfs(start_vec):
#   count = 0 # 
#   queue = deque()
#   queue.append(start_vec)
#   while queue:
#     x,y,angle = queue.popleft()
    
#     for next_angle in range(3):
#       nx = x + dx[next_angle]
#       ny = y + dy[next_angle]
#       # 다음으로 나올수 없는 각도
#       if (angle == 0 and next_angle == 2) or (angle == 2 and next_angle == 0):
#         continue
#       if nx < 0 or nx >= n or ny < 0 or ny >= n or li[nx][ny] == 1:
#         continue
#       # 대각선일때는 2곳 더 확인해야함
#       if (next_angle == 1 and li[x][y + 1] == 1) or (next_angle == 1 and li[x + 1][y] == 1):
#         continue
#       queue.append((nx, ny, next_angle))
#       if nx == n-1 and ny == n - 1:
#         count += 1
#   return count

# dx = [0,1,1]
# dy = [1,1,0]
# # angle 0
# now_angle = 0

# n = int(input())

# li = []
# for i in range(n):
#   li.append(list(map(int, input().split())))
  
# # 머리가 (0,1) 각도 0
# count = bfs((0, 1, 0))

# print(count)
