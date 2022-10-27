# 시작시간 11:35

# v는 현재위치
def dfs(graph,v,visited):
    # 일단 방문해있는거니까 True 표시    
    visited[v] = True
    print(v, end=' ')
    # i 는 현재위치에서 탐색중인 주변 노드
    for i in graph[v]:
        if visited[i] != True:
            dfs(graph,i,visited)
    
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]
visited = [False] * len(graph)

print(visited)

visited = [False] * len(graph)
dfs(graph,1,visited)

