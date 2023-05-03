# 0503    20:02 시작

# 입력값으로 2차원 배열 받는법 서칭으로 알아냄
# 더하는 경우의 수중에 가장 큰 수를 찾는다.
n = int(input())
li = []

# 값 입력
for i in range(n):
    li.append(list(map(int, input().split())))

sum_val = 0
max_val = 0

# 행계산
for i in range(n):
    if (max_val < sum(li[i])):
        max_val = sum(li[i])

# 열계산
for i in range(n):
    for j in range(n):
        sum_val += li[j][i]
    if (max_val < sum_val):
        max_val = sum_val
    sum_val = 0

for i in range(n):
    sum_val += li[i][i] 
if (max_val < sum_val):
    max_val = sum_val
sum_val = 0

for i in range(n):
    sum_val += li[i][n-i- 1]
    # print(li[i][n - i - 1])
if (max_val < sum_val):
    max_val = sum_val
sum_val = 0

print(max_val)



# # 10 51 시작  11 15분 해결
# # 문제를 이해하는데 너무 많은 시간을 썼다.

# n = int(input())

# li = []

# for i in range(n):
#     li.append(list(map(int,input().split())))
# ## a = [list(map(int, input().split())) for _ in range(n)]  # 이런 표현도 가능

# a = [list(map(int,input().split())) for _ in range(n)]

# tot = [0] * (2*n+2)  # tot = -1  로 시작해서 tot_now  더 큰 값만 대입해도 됌

# for i in range(len(li)):
#     tot[0] += li[i][i]

# for i in range(n):
#     for j in range(n):
#         tot[i+1] += li[i][j] 
# for i in range(n):
#     for j in range(n):
#         tot[i+1+n] += li[j][i] 

# print(max(tot))


