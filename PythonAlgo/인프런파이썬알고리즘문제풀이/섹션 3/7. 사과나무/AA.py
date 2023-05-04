# 0504   1619 시작 1708  마무리   
# 처음 떠오른 방법을 안바꾸려고 너무 고집을 부렸음
# 2차원배열 만들기 위해 전에 푼 문제 다시봄

# 격자판에서 다이아몬드  모양만  수확한다.

n = int(input())
li = []
for i in range(n):
    li.append(list(map(int,input().split())))

sum_val = 0
for i in range(0, n // 2 + 1):
    for z in range(n//2 - i, n // 2 + 1 + i):
        sum_val += li[i][z]
row = n//2 + 1
for j in range(n // 2 - 1, -1, -1): # 1,0
    for z in range(n // 2 - j, n // 2 + j+1):
        sum_val += li[row][z]
    row += 1
print(sum_val)

###################################
# #  1104 시작  11:44

# # 더 간단

# n = int(input())
# a = [list(map(int,input().split())) for _ in range(n)]

# res = 0
# s = e = n//2

# for i in range(n):
#     for j in range(s, e+1):
#         res += a[i][j]
#     if i < n//2:
#         s -= 1
#         e += 1
#     else:
#         s += 1
#         e -= 1
# print(res)

# # 내 풀이

# # n = int(input());

# # li = []
# # for i in range(n):
# #     li.append(list(map(int, input().split()))) 
# # sum = 0
# # for i in range(0,n):
# #     if (i <= (n//2)):
# #         for j in range((n//2)-i,n-(n//2) + i):
# #             sum += li[i][j]
# #     else:
# #         for j in range(i - (n//2),n + (n//2) - i):
# #             sum += li[i][j]
# # print(sum)





