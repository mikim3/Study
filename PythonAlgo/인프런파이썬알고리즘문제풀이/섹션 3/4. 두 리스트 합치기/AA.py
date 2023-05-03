# 0503  19:50 시작 19:54 매무리

n = int(input())
li_n = list(map(int,input().split()))

m = int(input())
li_m = list(map(int,input().split()))

li = li_m + li_n

li.sort()
for i in range(len(li)):
    print(li[i],end=' ')


# # 12 39
# # 4분걸림


# n = int(input())

# li1 = list(map(int,input().split()))


# m = int(input())

# li2 = list(map(int,input().split()))

# li3 = li1 + li2 
# li3.sort()

# for i in range(n+m):
#     print(li3[i],end=' ')
    
