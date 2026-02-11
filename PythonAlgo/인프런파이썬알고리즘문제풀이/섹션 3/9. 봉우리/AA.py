# 260208 시작 2003 마무리 2015

n = int(input())
li = [[0]*(n+2)]
for i in range(n):
    li.append([0]+list(map(int,input().split()))+[0])
li.append([0]*(n+2))
count = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if li[i][j] > li[i-1][j] and li[i][j] > li[i][j-1] and li[i][j] > li[i+1][j] and li[i][j] > li[i][j+1]:
            count += 1
print(count)

# 11 21 시작 11 34 끝

# n = int(input())
# li = []

# li.append([0]*(n+2))
# for i in range(n):
#     li.append([0] + list(map(int,input().split())) + [0])
# li.append([0]*(n+2))

# bon = 0
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if li[i][j] > li[i-1][j] and li[i][j] > li[i+1][j] and li[i][j] > li[i][j-1] and li[i][j] > li[i][j+1]:
#             bon += 1    

# print(bon)
