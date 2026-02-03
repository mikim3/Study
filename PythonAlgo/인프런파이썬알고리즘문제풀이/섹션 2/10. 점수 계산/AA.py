# 시작 260203 2004  마무리 2010

n = int(input())
li = list(map(int,input().split()))

k = 0
sum = 0
for i in range(n):
    if li[i] == 0:
        k = 0 
    elif li[i] == 1:
        k+= 1
        sum += k
print(sum)

# 1713 시작 17:22 끝

# # 쉽게 풀음

# # 연속해서 맞으면 +점수가 1점 오름
# bonus_val = 0 # bonus + 점수
# sum_score = 0 # 

# n = int(input())
# li = list(map(int,input().split()))

# for i in range(n):
#     if (li[i] == 1):
#         sum_score += 1 + bonus_val
#         bonus_val += 1
#     else:
#         bonus_val = 0
# print(sum_score)

# # 16 23

# n = int(input())
# li = list(map(int, input().split()))
# sum = 0
# bonus = 0

# for i in range(n):
#     if li[i] == 1:
#         bonus += 1
#         sum+=bonus
#     else:
#         bonus = 0
# print(sum)