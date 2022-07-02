# 
n, k = map(int,input().split())

count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
        if count == k:
            print(i)
            break
else:  # for ... else: 정상적으로 끝났을시 else구문 작동
    print(-1)    