# 12 39
# 4분걸림


n = int(input())

li1 = list(map(int,input().split()))


m = int(input())

li2 = list(map(int,input().split()))

li3 = li1 + li2 
li3.sort()

for i in range(n+m):
    print(li3[i],end=' ')
    
