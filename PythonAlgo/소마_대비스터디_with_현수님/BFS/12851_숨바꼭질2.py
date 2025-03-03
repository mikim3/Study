# 시작시간 2049 마무리시간 2154
# 시작시간 0837 마무리시간 0915
# 살짝 납득 안되는거 있어서 다시 풀기




















# from collections import deque

# def bfs(start, end):
#   queue = deque([start])
#   MAX = 100001
#   time = [9999999] * (2*MAX+1) # 도착까지시간
#   ways = [0] * (2*MAX+1)
#   ways[start] = 1
#   time[start] = 0
  
#   while queue:
#     now = queue.popleft()
    
#     for next in (now-1,now+1,now*2):
#       if next < 0 or next > MAX:
#         continue
#       if time[next] > time[now] + 1: # 새로운 최단경로
#         ways[next] = ways[now] # 그 전 경로에서 이동
#         time[next] = time[now] + 1
#         queue.append(next)
#       elif time[next] == time[now] + 1: # 이미 갔던 최단경로
#         ways[next] += ways[now]
#         # queue.append(next)  # 이게 모르겠네
#       # if time[now] > time[end]:
#     #   break 
#   return [time[end], ways[end]]

# n, k = map(int,input().split())
# if n == k:
#   print(0)
#   print(1)
# else:
#   tim, gazi= bfs(n,k)
#   print(tim)
#   print(gazi)




# from collections import deque

# def bfs(start, end):
#   MAX = 100001
#   queue = deque([start])
#   visited = [float('inf')] * (MAX+1)
#   ways = [0] * (MAX + 1) # ways[i] 까지 최소시간으로 가는 경로의 수
#   visited[start] = 0 # 0초
#   ways[start] = 1 # 시작점 도달 방법 1가지
  
#   while queue:
#     now = queue.popleft()
#     for next in [now-1,now+1,now*2]:
#       if next < 0 or next > MAX:
#         continue
#       if visited[next] == float('inf'): # 첫방문
#         visited[next] = visited[now] + 1
#         ways[next] = ways[now]
#         queue.append(next)
#       elif visited[next] == visited[now] + 1: # 이미 최소시간 방문
#         ways[next] += ways[now]
#   # print(f"ways {ways[0:50]} visited {visited[0:50]}")
#   return visited[end], ways[end]
  
# n,k = map(int, input().split())
# time, gazi= bfs(n,k)
# print(time)
# print(gazi)