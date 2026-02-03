# 시작 260203 1849 마무리 1859

# 평균에 가장 가까운 학생 몇 번쨰

# 같으면 높은 학생 선정   그중에 빠른학생

n = int(input())
li = list(map(int,input().split()))

av = round(sum(li) / n)
min_va = 222222222 # 최소차이
ret_i = 0 #
ret_va = 0 # 반환할 값

for i in range(n):
    if abs(li[i]-av) < min_va:
        ret_i = i
        ret_va = li[i]
        min_va = abs(li[i]-av)
    elif abs(li[i]-av) == min_va:
        if ret_va < li[i]:
            ret_i = i
            ret_va = li[i]
print(av,ret_i+1)








# # 시작 1722 마무리
# # 답봄 당연히 알아서 풀었어야 됐을텐데 까비

# # n명의 학생중 평균에 가장 가까운 학생 구하기
# # 여러개면 점수 높은순 또 여러개면 번호 빠른순

# # 평균을 구한다.
# # 

# n = int(input())
# li = list(map(int,input().split()))

# # print(round(sum(li)/n,0)) # 74.0
# av = round(sum(li)/n,0)

# check_v = 0 # 가장 가까운 값 저장
# check_i = 0
# min_v = 999999999 # 최소랑 가장 가까운

# for i in range(n):
#     if abs(li[i]-av) < min_v: # 가장 가깝다면
#         check_v = li[i]
#         check_i = i
#         min_v = abs(li[i]-av)
#     elif abs(li[i]-av) == min_v: # 가장 가까운데 공동이면
#         # 값이커야됨
#         if li[i] > check_v:
#             check_v = li[i]
#             check_i = i
# print(int(av), check_i+1)



# # 시작 1628  마무리 1641

# # n = int(input())
# # li = list(map(int,input().split()))
# # li_sum = sum(li)
# # mean_val = round(li_sum / n)
# # min_val = 99999999999
# # ret_index = 0 # 결과 인덱스
# # ret_val = 0
# # for i in range(n):
# #     if (abs(li[i] - mean_val) < min_val):
# #         min_val = abs(li[i] - mean_val)
# #         ret_index = i
# #         ret_val = li[i]
# #     elif (abs(li[i] - mean_val) == min_val):
# #         if (ret_val < li[i]):
# #             min_val = abs(li[i] - mean_val)
# #             ret_index = i
# #             ret_val = li[i]

# # print(mean_val, ret_index + 1)

# # 19:50  시작
# # 20:35  마무리

# # 답지를 봤으나 알아서 풀음
# # 그냥 구현인데 쉽게 생각해내지 못했음

# # n = int(input())
# # li = list(map(int,input().split()))
# # sum_grade = 0
# # avg = 0

# # for i in range(n):
# #     sum_grade += li[i]

# # avg = round(sum_grade / n) # 소수점

# # check = 0 # 출력해야할 가장 차이가 적은 학생의 인덱스
# # # li_check = [] # 공동 1등 일단 체크
# # min = 22222222222
# # check_value = 0
# # for i in range(n):
# #     if (abs(li[i]-avg) < min):
# #         check = i
# #         check_value = li[i]
# #         min = abs(li[i]-avg)
# #     elif (abs(li[i]-avg) == min):
# #         if (li[i] > check_value):
# #             check = i
# #             check_value = li[i]
# #             min = abs(li[i]-avg)

# # print(avg, check + 1)

# # # 답봄
# # n = int(input())
# # li = list(map(int,input().split()))

# # av = int(sum(li)/n + 0.5)
# # min = 2147000000

# # for <원소> in enumrate(<목록>):
# # for <원소1(인덱스)> <원소2(값)> in enumrate(<목록>):
# # for <원소1(인덱스)> <원소2(값)> in enumrate(<목록>, start = 1):

# # for idx, x in enumerate(li):
# #     tmp = abs(x-av)
# #     if tmp<min:
# #         min = tmp
# #         score = x #현재 근접한 점수
# #         res = idx+1
# #     elif tmp == min:
# #         if x > score:
# #             score = x
# #             res = idx + 1
# # print(av, res)
