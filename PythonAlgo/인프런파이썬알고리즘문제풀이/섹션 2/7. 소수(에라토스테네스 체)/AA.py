# 시작 끝
# 에라토스테네스 체 까먹음

n = int(input())

for i in range(n):










# # 그냥 구현 20분 걸림

# n = int(input())

# ch = [0]*(n+1)
# cnt = 0

# for i in range(2,n+1):
#     if ch[i] == 0:
#         cnt += 1
#         for j in range(i, n+1, i):
#             ch[j] = 1

# print(cnt)







# 그냥 구현한거
# n = int(input())

# count = 0  # 발견된 소수 갯수
# flag = 0

# for i in range(1, n+1):
#     for j in range(2,i+1):
#         # i가 하나라도 0 으로 나눠지면 약수가 아닌거 
#         if i % j == 0:
#             flag += 1

#     if flag == 1:
#         count += 1
#     flag = 0
# print(count)