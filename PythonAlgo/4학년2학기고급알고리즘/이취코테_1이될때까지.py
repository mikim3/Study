
# 1. N에서 1을 뺍니다.
# 2. N을 K로 나눕니다.
n, k = map(int,input().split())
count = 0
while n != 1:
    if n % k == 0:
        n = n / k
    else:
        n = n - 1
    count += 1
print(count)
