# 10 51 시작
n = int(input())

li = []

for i in range(n):
    li.append(list(map(int,input().split())))

tot = [0] * (2*n+2)
for i in range(len(li)):
    tot[0] += li[i][i]
    

for i in range(n):
    for j in range(n):
        tot[i+1] += li[i][j] 
for i in range(n):
    for j in range(n):
        tot[i+1+n] += li[j][i] 


print(max(tot))

# print(len(li[0]))
# print(len(li))