

from collections import deque

def bfs(x,y):
    queue = deque()
    # 첫 좌표 (x,y)
    queue.append((x,y))
    while queue:
        print(queue)
        # 
        x,y = queue.popleft()
        



n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))



