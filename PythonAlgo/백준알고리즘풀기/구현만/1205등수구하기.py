# 230621  00:15 재도전

# 테스트 케이스 
# 12 100 10
# 100 100 100 100 100 100 100 100 100 90 90 90
# -> 1

# 10 0 11
# 10 9 8 7 6 5 4 3 2 1
# -> 11

# 10 1 10
# 1 1 1 1 1 1 1 1 1 1
# -> -1

# 5 2 5
# 6 5 4 3 1
# 5

import sys
input = sys.stdin.readline
n, my_score, p = map(int,input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)

if (n == 0):
    print(1)
    sys.exit(0)

# my_score 와 일치하는 점수가 있으면 그 점수의 등수로 표시한다.
# 만약 공동점수로 입력되다가 p의 범위를 벗어나면 순위권 밖으로 인정되어서 -1출력
rank = 1
out = False
for i in range(n):
        if (li[i] > my_score):
            rank += 1
        # 점수가 같은경우
        elif (li[i] == my_score):
            # 몇개까지 점수가 같은지 확인
            equal_repeat = 0
            for j in range(i,n):
                    if (li[j] == my_score):
                        equal_repeat += 1
                    else:
                        break
            if (equal_repeat + i >= p):
                out = True
            break
        else:
            break
if (rank > p or out):
    print(-1)
else:
    print(rank)


# 21:10시작

# 공동등수는 높은 등수로 모두 표현
#
# import sys

# # 주어진 점수갯수, 태수의 점수 , 랭킹리스트에 올릴수 점수의 개수
# n, new_score, p = map(int,input().split())
# # 현재 랭킹리스트
# if (n > 0):
#     li = list(map(int,input().split()))
# else:
#     print(1)
#     sys.exit(0)
# li.sort(reverse=True)


# rank = 0
# tmp_score = 0
# check = 1
# # p 10  n  9
# for i in range(p):
#     if (i == n):
#         rank = i+1
#         break
#     tmp_score = li[i]
#     # 새 점수가 비교점수보다 더 크면
#     if (new_score > tmp_score): 
#         rank = i+1
#         check = 1
#         break
#     elif (new_score == tmp_score):
#         same = 0
#         out = False
#         # 같은거 개수 계산해서 괜찮으면 rank = i + 1  아니면 check는 0 인 상태로 종료
#         for j in range(i, n):
#             if (new_score == li[j]):
#                 same += 1
#             if (same + i == p): # 순위권을 벗어남
#                 out = True
#                 break
#         if (out):
#             check = 0
#             break
#         if (i == p - 1):
#             check = 0
#             break
#         rank = i + 1
#         check = 1
#         break
#     rank = i + 1
# if (check == 1):
#     print(rank)
# else:
#     print(-1)
