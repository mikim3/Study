#
# x,y
# 보통 수학의 상식과는 다르게 오른쪽으로 가는게 y가 + 인거다.  위로가면 x가 -인 거고 
# [x,y]
# [0,0] [0,1] [0,2]
# [1,0] [1,1] [1,2]
# [2,0] [2,1] [2,2]

# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
# 현재 위치
x, y = 2, 2
for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)


