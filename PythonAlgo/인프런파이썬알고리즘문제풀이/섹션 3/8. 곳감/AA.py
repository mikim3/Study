# 260208 시작 1731 마무리 1840
# 너무 느리게 품
# 행번호 방향 회전수
#  0이 왼쪽 1이 오른쪽

# n = int(input())
# li = []
# for i in range(n):
#     li.append(list(map(int,input().split())))
# t = int(input())
# li_c = []
# for i in range(t):
#     row,dir,rot = map(int,input().split())
#     row-=1
#     for z in range(rot):
#         li_tmp = [x for x in li[row]]
#         if dir == 0:
#             li[row][n-1] = li_tmp[0] 
#             for j in range(1,n):
#                 li[row][j-1]= li_tmp[j]
#         if dir == 1:
#             li[row][0] = li_tmp[n-1]
#             for j in range(0,n-1):
#                 li[row][j+1]= li_tmp[j]
# su = 0
# for i in range(n): # x축
#     if i <= n//2:
#         for j in range(0+i,n-i):
#             su+=li[i][j]
#     elif i > n//2:
#         for j in range(n-i-1,i+1):
#             su+=li[i][j]
# print(su)

# 11 : 50 시작 11:55
# n = int(input())

# a = [list(map(int,input().split())) for _ in range(n)]

# m = int(input())

# for i in range(m):
#     h, t, k =map(int, input().split())
#     if t==0:
#         for _ in range(k):
#             a[h-1].append(a[h-1].pop(0))
#     else:
#         for _ in range(k):
#             a[h-1].insert(0, a[h-1].pop())
# sum = 0
# s = 0
# e = n-1  # 5
# for i in range(n):
#     for j in range(s,e+1):
#         sum += a[i][j]
#     if i<n//2:
#         s+=1
#         e-=1
#     else:
#         s-=1
#         e+=1

# print(sum)


# li2 = [list(map(int,input().split())) for _ in range(m)]

# 2 0 3   2행을 왼쪽(0)으로  3칸만큼 옮겨라

# li[2-1]

# li2[i][0] == i번째 명령어가 몇번째행을 나타내는지 





