
# LRUD
dx = [-1,1,0,0]
dy = [0,0,-1,1]


n = int(input())
li = list(map(str,input().split()))
# x,y
x, y = 1,1
# next x,y
nx, ny = 1, 1
for i in range(len(li)):
    if li[i] == "L":
        nx = x + dx[0]
        ny = y + dy[0]
    if li[i] == "R":
        nx = x + dx[1]
        ny = y + dy[1]
    if li[i] == "U":
        nx = x + dx[2]
        ny = y + dy[2]
    if li[i] == "D":
        nx = x + dx[3]
        ny = y + dy[3]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        pass
    else:
        x = nx
        y = ny

print(y,x)


