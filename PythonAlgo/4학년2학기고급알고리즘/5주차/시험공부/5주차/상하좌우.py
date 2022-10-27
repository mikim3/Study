# 시작시간 10:41 10:50

n = int(input())
plans = list(map(str,input().split()))
x , y = 1,1

# L, R, U, D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx >= 1 and ny >= 1 and ny <= n and nx <= n:
        x = nx
        y = ny
print(x,y)


# 내가 푼답

# n = int(input())
# li = list(map(str,input().split()))

# # L, R, U, D
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]

# # nx = x + dx[0]
# # 현재위치
# x,y = 1,1
# for i in range(len(li)):
#     if li[i] == 'L':
#         nx = x + dx[0]
#         ny = y + dy[0]
#     if li[i] == 'R':
#         nx = x + dx[1]
#         ny = y + dy[1]
#     if li[i] == 'U':
#         nx = x + dx[2]
#         ny = y + dy[2]
#     if li[i] == 'D':
#         nx = x + dx[3]
#         ny = y + dy[3]
#     # 밖으로 나가는지 검사
#     if nx >= 1 and ny >= 1 and nx <= n and ny <= n:
#         x = nx
#         y = ny

# print(x,y)    



