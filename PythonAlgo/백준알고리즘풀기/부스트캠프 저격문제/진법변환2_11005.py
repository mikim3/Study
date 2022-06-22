#답봄

from sys import stdin
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = list(map(int,input().split()))
answer = ''

while n != 0:
    answer += str(tmp[n % b])
    n = n // b

print(answer[::-1])


