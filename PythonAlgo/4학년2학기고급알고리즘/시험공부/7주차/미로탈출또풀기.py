
# 큐에 값을 튜플로 받자

from collections import deque

#visited 는 값이 graph 좌표가 1이냐로 대체 된다

def bfs(x,y):

    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n - 1][m - 1]
    
    
    



# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

print(bfs(0,0))

