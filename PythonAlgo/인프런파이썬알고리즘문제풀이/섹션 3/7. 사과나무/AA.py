#  1104 시작  11:44

n = int(input());

li = []

for i in range(n):
    li.append(list(map(int, input().split()))) 

sum = 0
for i in range(0,n):
    if (i <= (n//2)):
        for j in range((n//2)-i,n-(n//2) + i):
            sum += li[i][j]
    else: 
        for j in range(i - (n//2),n + (n//2) - i):
            sum += li[i][j]


print(sum)





