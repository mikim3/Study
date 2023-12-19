
##############################
# 리스트 컴프리핸션
# rows, cols = 3,4 # 3행 4열
# matrix1 = [[0 for _ in range(cols)] for _ in range(rows)]

# print(matrix1)

#############################################
# 아래와 같은 입력값이 오면

# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

n = int(input())
matrix2 = []
for i in range(n):
  matrix2.append(list(map(int, input().split())))
print(matrix2)

matrix3 = [list(map(int, input().split())) for _ in range(n)]
print(matrix3)

#########################
# 0으로 채운 2차원 배열
matrix_pill_zero = [[0] * n for _ in range(n)]
print(matrix_pill_zero)
