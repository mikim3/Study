# 시작시간 :  11:35   종료시간 : 12:40 
# n, m = map(int, input().split())

# li = list(map(int,input().split()))

# def Count(capacity):
#     cnt = 1
#     su = 0
    
#     for x in li:
#         # mid 값 보다 크면 한 묶음 처리   
#         if su + x > capacity:
#             cnt += 1
#             # 다음 묶음에도 값 더해지게 처리
#             su = x
#         else:
#             su += x
#     return cnt

# sum_li = sum(li)
# lt = 1
# rt = sum_li
# res = 0

# while lt <= rt:
#     mid = (lt + rt) // 2
#     # 더 크게 묶던가 작게 묶었다면 res에 들어갈 수 있다.
#     if Count(mid) <= m:
#         res = mid
#         rt = mid - 1
#     else:
#         lt = mid + 1
# print(res)
