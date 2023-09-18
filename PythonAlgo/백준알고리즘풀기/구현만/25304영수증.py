# 230919 11:58 12:03

x = int(input())
n = int(input())

total = 0
for i in range(n):
    price, count= list(map(int,input().split()))
    total += price * count

if ( total == x):
    print('Yes')
else:
    print('No')
