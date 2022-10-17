# 시작시간 18:57  종료시간 19:57
# 답봄 나중에 다시 풀기

from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph,start,visited):
    print(start, end = ' ')
    visited[start] = True
    # print('\ngraph[start]',graph[start])
    for i in graph[start]:
        # print('i ==',i)
        if not visited[i]:
            dfs(graph,i,visited)

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
# 정점 n 연결 간선 개수 m 시작 정점 V 
n,m,v = map(int,input().split()) 

# graph = [[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]
# 위와 같다면 1 정점은 2,3 과 2정점은 1,5와 3정점은 1,4와 4정점은 3,5 5정점은 2,4와 연결되어있다.
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m):
    a,b = map(int, input().split())
    # 1 2 입력은   1이2와 연결되면서 2도1가 연결된 것이다.
    # 그래서 아래 두줄로 체크해준다.
    graph[a].append(b)
    graph[b].append(a)
    # print(graph)
# 
for i in range(1, n+1):
    graph[i].sort()

# print(graph)

visited = [False] * (n+1)
dfs(graph,v,visited)
print()

visited = [False] * (n+1)
bfs(graph,v,visited)







