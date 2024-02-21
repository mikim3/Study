###############################
#
















# 시작시간 :  3:50     종료시간 : 4시 30

# def Count(len):
#     cnt = 1
#     ep = li[0]
#     for i in range(1,n):
#         if li[i] - ep >= len:
#             cnt += 1
#             ep = li[i]
#     return cnt

# n , c = map(int, input().split())
# li = []

# for i in range(n):
#     li.append(int(input()))
# li.sort()
# lt = 1
# rt = li[n-1]

# while lt <= rt:
#     mid = (lt + rt) // 2
#     if Count(mid) >= c:
#         res = mid
#         lt = mid + 1
#     else:
#         rt = mid - 1
# print(res)
