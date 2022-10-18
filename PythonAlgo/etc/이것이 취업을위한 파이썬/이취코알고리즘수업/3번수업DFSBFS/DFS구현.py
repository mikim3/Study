
def dfs(graph,v,visited):
    # 시작위치를 방문 표시한다.
    visited[v] = True
    print(v,end=' ')
    # graph[v]의 값은 v 노드의 주변 노드를 의미
    for i in graph[v]:
        # 만약 방문하지 않았다면 재귀로 들어감 
        # 이 재귀로 들어가는 로직이 마치 스택에 쌓이는 모습과 비슷하다.
        if not visited[i]:
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
    [1,7]
]

visited = [False] * 9
dfs(graph,1,visited)
