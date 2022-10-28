def dfs(x,y):
    if x <= -1 or y  <= -1 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        # 0,0 들오면 바로 graph[0][0] = 1 을 체크해주니까 graph[0][1] = 1 찍고 다시 dfs(0,1) -> dfs(0,0) 을 해도 두번째 왔을때는 if문에 못들어오고 바로 False반환 
        graph[x][y] = 1 
        dfs(x - 1, y)
        dfs(x,y - 1)
        dfs(x + 1,y)
        dfs(x,y + 1)
        return True
    return False

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1
print(count)
