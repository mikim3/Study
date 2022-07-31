# 11 : 50 시작 11:55

n = int(input())

a = [list(map(int,input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    h, t, k =map(int, input().split())
    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
sum = 0
s = -1
e = n+1  # 5
for i in range(n):
    if i <= n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
    for j in range(s,e):
        sum += a[i][j]
                         
print(sum)


# li2 = [list(map(int,input().split())) for _ in range(m)]

# 2 0 3   2행을 왼쪽(0)으로  3칸만큼 옮겨라

# li[2-1]

# li2[i][0] == i번째 명령어가 몇번째행을 나타내는지 





