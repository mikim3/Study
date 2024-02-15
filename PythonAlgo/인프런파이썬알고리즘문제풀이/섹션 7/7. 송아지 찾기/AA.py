from collections import deque

# ########################
# # 시작시간 240215 20:00 마무리시간 20:37
# # 답봄

# def bfs(start):
#   result[start] = 0
#   queue = deque()
#   queue.append(start)
#   while queue:
#     now = queue.popleft()
#     if now == e:
#       break
#     for next in (now-1, now+1, now+5):
#       if result[next] == 999999:
#         result[next] = result[now] + 1
#         queue.append(next)

# # s에서 e 로 가기
# s, e = map(int,input().split())
# # checked = [0] * (max(e,s) + 100)
# result = [999999] * (max(e,s) + 100000)
# bfs(s)
# print(result[e])

# ##################################
# # 시작시간 240112 0125 마무리시간 0137

# #
# from collections import deque

# def bfs(checked):
#   checked[s] = 0
#   queue = deque()
#   queue.append(s)
#   while queue:
#     now = queue.popleft()
#     if now == e:
#       break
#     for next in (now + 1, now - 1, now + 5):
#       if checked[next] == 0:
#         queue.append(next)
#         checked[next] = checked[now] + 1

# checked = [0] * 20000
# s, e = map(int,input().split())
# bfs(checked)
# print(checked[e])

# ##################################
# # 시작시간 231217 19:50 마무리시간 20:10
# # 231217 강의 1시간후 혼자 다시 품
# # 최소 몇 번 만에 도착할 수 있는가?? 문제 BFS

# from collections import deque

# MAX = 10000
# distance = [0] * MAX
# check = [0] * MAX
# # 현수위치(출발점), 송아지위치(도착점)
# s,e = map(int,input().split())
# check[s] = 1
# distance[s] = 0
# dQ = deque()
# dQ.append(s)

# while dQ:
#   now = dQ.popleft()
#   if now == e:
#     break
#   for next in (now - 1, now + 1, now + 5):
#     if 0 < next <= MAX:
#       if check[next] == 0:
#         dQ.append(next)
#         check[next] = 1
#         distance[next] = distance[now] + 1
# print(distance[e])


###################
# from collections import deque

# MAX = 10000
# check = [0] * (MAX + 1) # 0이면 안 지나간곳 1은 지나간곳
# distance = [0] * (MAX + 1) # 지나간 곳이 몇 번째로 지나간것 인지 체크
# n,m = map(int, input().split())
# check[n] = 1
# distance[n] = 0
# dQ = deque()
# dQ.append(n) # 큐에 현재위치 삽입
# while dQ:
#   now = dQ.popleft() # 가장 처음에 본 곳을 큐에서 꺼내서 길 확인
#   if now == m:
#     break
#   for next in(now-1, now+1, now+5): # 현재 위치에서 다음에 갈수있는 3경우 다 확인
#     if 0 < next <= MAX: # 유효한 next값 확인
#       if check[next] == 0: # 처음 지나가는 곳이면
#         dQ.append(next)
#         check[next] = 1
#         distance[next] = distance[now] + 1
# print(distance[m])




# ##########################
# # 시작시간  231115 2345   마무리시간
# # 바로 수업들음

# import sys
# from collections import deque

# MAX = 10001
# ch = [0] * (MAX+1) # 해당 위치를 지나갔는지 체크하는 배열
# dis = [0] * (MAX+1) # 해당 위치를 몇 번 만에 갔는지 기록하는 배열
# n, m = map(int, input().split())
# ch[n] = 1
# dis[n] = 0
# dQ = deque()
# dQ.append(n)
# while dQ: # 덱 비어있으면 멈춤
#   now = dQ.popleft()
#   if now == m: # 목표지점 발견
#     break
#   for next in (now-1, now+1, now+5): # 튜플값을 하나씩 뻗음
#     if 0 < next <= MAX:
#       if ch[next] == 0:
#         dQ.append(next)
#         ch[next] = 1
#         dis[next] = dis[now] + 1
# print(dis[m])

# #########################
