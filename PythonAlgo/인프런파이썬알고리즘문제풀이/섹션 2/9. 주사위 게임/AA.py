# 시작 260203 1951 마무리시간 2001
# 가장 상금 많은 사람 상금
import sys

input = sys.stdin.readline

n = int(input())
li = []
sang_max = 0
for i in range(n):
    a, b, c = map(int,input().split())
    if a == b == c:
        sang = 10000 +a * 1000
    elif a == b or a == c or b == c:
        if a == b or a == c:
            sang = 1000 + (a * 100)
        elif b == c:
            sang = 1000 + (b * 100)
    else:
        sang = max(a,b,c)*100
    if sang_max < sang:
            sang_max = sang
print(sang_max)

# 1639시작 1653 마무리

# import sys

# input = sys.stdin.readline
# n = int(input())

# reward_sum = []

# for i in range(n):
#     li = list(map(int, input().split()))
#     if (li[0] == li[1]) and (li[1] == li[2]):
#         reward_sum.append(10000 + (li[0] * 1000)) 
#     elif (li[0] == li[1]) or (li[1] == li[2]) or (li[0] == li[2]):
#         if (li[0] == li[1]) or (li[1] == li[2]):
#             reward_sum.append(1000 + (li[1] * 100))
#         else:
#             reward_sum.append(1000 + (li[2] * 100))
#     else:
#         reward_sum.append(max(li) * 100)
#     li.clear()

# print(max(reward_sum))

# import sys
# input = sys.stdin.readline

# n = int(input())
# score=[]

# for i in range(n):
#     li = list(map(int,input().split()))

#     if li[0] == li[1] == li[2]:
#         score.append(10000+li[0] * 1000)
#     elif li[0] == li[1] or li[1] == li[2] or li[0] == li[2]:
#         if li[0] == li[1] or li[0] == li[2]:
#             score.append(1000+ 100*li[0])
#         elif li[1] == li[2]:
#             score.append(1000+ 100*li[1])
#     else:
#         score.append(100*max(li))

# print(max(score))
    


