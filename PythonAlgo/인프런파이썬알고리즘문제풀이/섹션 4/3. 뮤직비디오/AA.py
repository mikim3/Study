# import sys
# sys.stdin = open("/goinfre/mikim3/Study/PythonAlgo/인프런파이썬알고리즘문제풀이/섹션 4/3. 뮤직비디오/input.txt", "r")

###############################
# 시작시간 240222 2044 마무리시간 2105
# 나중에 다시 풀기
# 밑에 코드에서 전날에 힌트를 얻음
# 영상 틀자마자 갑자기 꺠달음

# DVD 크기가 너무 작으면 묶음 수가 크게 나옴
# 너무 크면 최소가 아님

# 묶음의 크기가 최종 반환값

# n, m = map(int, input().split())
# li = list(map(int, input().split()))

# # 길이가 mid res
# lt = max(li)
# rt = sum(li)
# res = 99999
# while lt <= rt:
#   mid = (lt + rt) // 2
#   count = 1
#   su = 0
#   for i in range(n):
#     # 이번 길이까지 합치면 너무 클때
#     if su + li[i] > mid:
#       count += 1
#       su = li[i]
#     else:
#       su += li[i]

#   if count <= m:
#     res = min(res, mid)
#     rt = mid - 1
#   else:
#     lt = mid + 1
# print(res)

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
