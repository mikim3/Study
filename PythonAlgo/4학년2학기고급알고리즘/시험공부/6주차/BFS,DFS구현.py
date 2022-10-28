# 시작시간 15:45

from collections import deque

def bfs(graph,start,visited):
    
    # 방문표시
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for now in graph[v]:
            if not visited[now]:
                visited[now] = True
                queue.append(now)

def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for near in graph[v]:
        if not visited[near]:
            visited[near] = True
            dfs(graph,near,visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)
bfs(graph,1,visited)

print()
visited = [False] * len(graph)
dfs(graph,1,visited)

