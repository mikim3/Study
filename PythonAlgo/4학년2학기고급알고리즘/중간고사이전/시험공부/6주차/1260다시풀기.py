#시작시간 16:43

from collections import deque
import queue

n, m, v= map(int,input().split())

def dfs(graph,start,visitied):
    
    visited[start] = True
    print(start,end=' ')
    
    for near in graph[start]:
        if visited[near] == False:
            visited[near] = True
            dfs(graph,near,visitied)
        
def bfs(graph,start,visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        now = queue.popleft()
        print(now,end=' ')
        for near in graph[now]:
            if not visited[near]:
                queue.append(near)
                visited[near] = True

graph = []
for i in range(n+1):
    graph.append([])

visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번 노드부터 작은값부터 탐색하게끔 정렬
for i in range(1,n+1):
    graph[i].sort()

visited = [False] * (n + 1)
dfs(graph,v,visited)

print()

visited = [False] * (n + 1)
bfs(graph,v,visited)

