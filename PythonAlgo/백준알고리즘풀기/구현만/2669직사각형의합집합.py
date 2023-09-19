# 시작 시간 230920 00:12 12:12
# 답 봤음

















# ---------------------------------------------

# 0으로 차있는 2차원 배열을 만든다.
# 좌표안에 들어가면 1로 바꾼다.

# 1갯수를 구한다.


# [0] 이 101개 들어있는 배열 101개 만들기
matrix = [[0] * 101 for _ in range(101)] 
# print(matrix)

for i in range(4):
  x1, y1, x2, y2 = map(int, input().split())
  for j in range(x1, x2):
    for z in range(y1, y2):
      matrix[j][z] = 1

total = 0
for i in range(101):
  for j in range(101):
    if matrix[i][j] == 1:
      total += 1

print(total)



