# 내답
# def solution(lottos, win_nums):
#     result = list()
#     # 
#     count_max=7
#     count_min=7
#     for i in range(len(lottos)):

#         if lottos[i] == 0:
#             count_max-=1
#         else:
#             for j in range(len(win_nums)):
#                 if lottos[i] == win_nums[j]:
#                     count_max-=1
#                     count_min-=1
#                     break  # 숫자 하나 맞았으면 다음으로 넘어감
#     if count_min == 7:
#         count_min = 6
#     if count_max == 7:
#         count_max = 6

#     result = [count_max,count_min]
#     return result 
    
# 최고의 답안


def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]



print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

