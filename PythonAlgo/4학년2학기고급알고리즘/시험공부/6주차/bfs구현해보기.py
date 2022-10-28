# 시작시간 13:07

from collections import deque

def bfs(graph,start,visitied):
    
    # 시작좌표를 큐에 넣고 시작    
    queue = deque([start])
    # 시작점 방문처리후 시작 
    visitied[start] = True

    # 큐가 다 비워질때까지 반복
    while queue:
        # 큐 맨 밑에 있는 값 pop 
        v = queue.popleft()
        # 팝 한값 출력
        print(v,end=' ')
        # 인접 좌표에 하나씩 접근
        for near in graph[v]:
            # 만약 방문하지 않은 좌표라면 True 표시 후 스택
            if visitied[near] == False:
                visitied[near] = True
                queue.append(near)

            


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

visitied = [False] * len(graph)

bfs(graph,1,visitied)

