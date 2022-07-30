# 10 51 시작  11 15분 해결
# 문제를 이해하는데 너무 많은 시간을 썼다.

n = int(input())

li = []

for i in range(n):
    li.append(list(map(int,input().split())))
## a = [list(map(int, input().split())) for _ in range(n)]  # 이런 표현도 가능

tot = [0] * (2*n+2)  # tot = -1  로 시작해서 tot_now  더 큰 값만 대입해도 됌

for i in range(len(li)):
    tot[0] += li[i][i]

for i in range(n):
    for j in range(n):
        tot[i+1] += li[i][j] 
for i in range(n):
    for j in range(n):
        tot[i+1+n] += li[j][i] 

print(max(tot))


