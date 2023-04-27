# 답봄
n = int(input())
li = list(map(int,input().split()))

av = int(sum(li)/n + 0.5)
min = 2147000000

for idx, x in enumerate(li):
    tmp = abs(x-av)
    if tmp<min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(av, res)

