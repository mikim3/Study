import sys
input = sys.stdin.readline

n = int(input())
score=[]

for i in range(n):
    li = list(map(int,input().split()))

    if li[0] == li[1] == li[2]:
        score.append(10000+li[0] * 1000)
    elif li[0] == li[1] or li[1] == li[2] or li[0] == li[2]:
        if li[0] == li[1] or li[0] == li[2]:
            score.append(1000+ 100*li[0])
        elif li[1] == li[2]:
            score.append(1000+ 100*li[1])
    else:
        score.append(100*max(li))

print(max(score))
    


