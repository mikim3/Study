# 이론을 잘못 이해해서 굉장히 오래걸림
# 에라토스테네스 체 까먹음

# 에라토스테네스 체 방법
# 1. 원하는 크기  + 1의 배열 생성
# 2. 그 배열에서 처음부터 돌면서 값이 0 이면 1로 바꾸고 카운트를 1 높임 
# 3. 그 배열에 소수의 배수는 이미 소수가 아님이 증명된다.
#    그렇기에 배수들은 소수가 아니라고 체크
# 4. 다시 2,3을 반복

# n = int(input())

# ret_val = 0 # 소수의 갯수
# li = [0 for i in range(n + 1)]
# for i in range(2, len(li)):# 2부터 소수판별
#     if (li[i] == 0):
#         li[i] = 1
#         ret_val += 1
#         for j in range(i,len(li),i):
#             li[j] = 1
# # n == 4일때  0,1,2,3,4 의 배열을 가짐 즉 n + 1의 배열이 있는거임 len(li)는 n+1임
# print(ret_val)

###########################
# # 그냥 구현 20분 걸림

n = int(input())

ch = [0]*(n+1)
cnt = 0

for i in range(2,n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)

###################
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