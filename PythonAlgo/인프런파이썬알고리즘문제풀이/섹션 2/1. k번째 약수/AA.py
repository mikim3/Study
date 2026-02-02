# 시작시간 1612 마무리시간 1627

n, k = map(int, input().split())
count = 0
li = []
for i in range(1,n+1):
    if n % i ==0:
        li.append(i)

if len(li) >= k:
    print(li[k-1])
else:
    print(-1)

# n, k = map(int, input().split())
# count = 0

# for i in range(1, n + 1):
#     if (n % i == 0):
#         count += 1
#         if (count == k):
#             print(i)
#             count = -1
#             break
# if (count != -1):
#     print(-1)

### 다시풀기전
# # 
# n, k = map(int,input().split())

# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count += 1
#         if count == k:
#             print(i)
#             break
# else:  # for ... else: 정상적으로 끝났을시 else구문 작동
#     print(-1)    