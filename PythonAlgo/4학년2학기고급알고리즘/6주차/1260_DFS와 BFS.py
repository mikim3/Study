# 시작시간 18:57

from collections import deque


import sys
input = sys.stdin.readline

# 정점 n 연결 간선 개수 m 시작 정점 V 
n,m,v = map(int,input().split()) 


def bfs(graph,start,visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        

graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 
for i in range(1, n+1):
    graph[i].sort()

visited = [False] * (n+1)

bfs(graph,v,visited)







