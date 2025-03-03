# 시작시간 1122 마무리시간 1211
"""
메모리초과 나와서 GPT물어봄

"""



# from collections import deque

# def bfs(start, end):
#   queue = deque([start])
#   MAX = 100001
#   visited = [[MAX,-MAX] for _ in  range(MAX*2)] # [큰시간, 없는 직전위치]
#   visited[start] = [0,-MAX]
#   while queue:
#     now = queue.popleft()
#     for next in now-1, now+1, now*2:
#       if next < 0 or next > MAX:
#         continue
#       if visited[next][0] > visited[now][0] + 1:
#         visited[next][0] = visited[now][0] + 1
#         visited[next][1] = now # 직전경로
#         queue.append(next)
#   # print(f"visited {visited[0:20]}")
#   soon = end # 직전경로
#   li = [soon]
#   while soon != -MAX:
#     li.append(visited[soon][1])
#     soon = visited[soon][1]
#   return [visited[end][0],li]
  
# n, k = map(int,input().split())
# time, li= bfs(n,k)
# print(time)
# li.reverse()
# for i in range(1, len(li)):
#   print(li[i],end=' ')

# from collections import deque

# def bfs(start, end):
#   queue = deque([start])
#   MAX = 100001
#   visited = []
#   for i in range(MAX+2): # append
#     visited.append([MAX,[]])
#   visited[start][0] = 0
#   visited[start][1].append(start)
#   while queue:
#     now = queue.popleft()
#     for next in now-1, now+1, now*2:
#       if next < 0 or next > MAX:
#         continue
#       if visited[next][0] > visited[now][0] + 1: # 미방문 
#         visited[next][0] = visited[now][0] + 1 # 방문처리
#         visited[next][1] = visited[now][1] # 방문처리
#         visited[next][1] = visited[now][1] + [next]
#         queue.append(next)
#       if next == end:
#         return visited[end]
#   # print(f"visited {visited[0:20]}")
#   return visited[end]
  
# n, k = map(int,input().split())
# time, li= bfs(n,k)
# print(time)
# for i in range(len(li)):
#   print(li[i], end=' ')


