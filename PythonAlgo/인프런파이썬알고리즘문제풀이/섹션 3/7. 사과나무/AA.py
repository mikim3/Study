#  1104 시작  11:44

# 더 간단

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

res = 0
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)






# 내 풀이

# n = int(input());

# li = []
# for i in range(n):
#     li.append(list(map(int, input().split()))) 
# sum = 0
# for i in range(0,n):
#     if (i <= (n//2)):
#         for j in range((n//2)-i,n-(n//2) + i):
#             sum += li[i][j]
#     else: 
#         for j in range(i - (n//2),n + (n//2) - i):
#             sum += li[i][j]
# print(sum)





