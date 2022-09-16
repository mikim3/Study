# 16 23


n = int(input())
li = list(map(int, input().split()))
sum = 0
bonus = 0

for i in range(n):
    if li[i] == 1:
        bonus += 1
        sum+=bonus
    else:
        bonus = 0
print(sum)


