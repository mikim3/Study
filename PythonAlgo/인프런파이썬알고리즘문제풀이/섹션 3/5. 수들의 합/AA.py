# 19:57 시작시간 20:02에 포기 어처피 문제뜻 정확히 모름 수열을 잘 알아보자

# 합이 m이 되는 경우의 수

# 합하면 


n, m = map(int,input().split())
li = list(map(int,input().split()))


for i in range(len(li)):
    for j in range()













# # 22 38  23 16 분까지 풀어도 시간초과나옴

# # 나중에 다시 풀어보기
# # 답지

# n , m = map(int,input().split())
# li = list(map(int,input().split()))
# lt = 0
# rt = 1
# tot = li[0]
# cnt = 0
# while True:
#     if tot < m:
#         if rt < n:
#             tot += li[rt]
#             rt += 1
#         else:  # 만약 rt가 인덱스 끝까지 갔는데 m보다 작다면 그 후에 모든 연산은 어처피 더 작은 값만 나온다 그러므로 더  이상의 연산은 필요없다.
#             break
#     elif tot == m:
#         cnt += 1
#         tot -= li[lt]
#         lt += 1
#     else:
#         tot -= li[lt]
#         lt += 1

# print(cnt)
    
# #### 내가푼 답안

# # n , m = map(int,input().split())

# # li = list(map(int,input().split()))
# # tot = 0
# # lt = 0 
# # rt = 0
# # cnt = 0
# # for lt in range(n):
# #     for rt in range(lt + 1, n):
# #         # print(rt)
# #         tot = sum(li[lt:rt+1])
# #         if tot < m:
# #             pass
# #         elif tot == m:
# #             cnt += 1
# #             # print("lt, rt",lt, rt)
# #             # print("tot",tot)
# #             # print("cnt", cnt)
# #             break
# #         else:
# #             break
# # print(cnt)