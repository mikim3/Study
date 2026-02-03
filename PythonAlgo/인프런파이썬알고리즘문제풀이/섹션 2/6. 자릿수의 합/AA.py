# 시작 260203 1911 마무리 1929
# 더 빨리 풀수는 있었는데 문자열 없이 푸는거는 실패

def digit_sum(x:int): # 자연수의 자릿수의 합을 구하는 함수
    ret = 0
    x_str= str(x)
    for i in range(len(x_str)):
        ret += int(x_str[i])
    return ret

n = int(input())
li = list(map(int,input().split()))
max_d_s_va = 0
max_va = 0

for i in range(n):
    if digit_sum(li[i]) > max_d_s_va:
        max_d_s_va = digit_sum(li[i])
        max_va = li[i]
print(max_va)

# n = int(input())

# li = list(map(int, input().split()))
# def digit_sum(num):
#     sum_digit = 0
#     str_num = str(num)
#     for i in str_num:
#         sum_digit += int(i)
#     return sum_digit
# li_sum_digit = []
# for i in range(n):
#     li_sum_digit.append(digit_sum(li[i]))

# max_val = 0
# max_index = 0
# for i in range(n):
#     if (max_val < li_sum_digit[i]):
#         max_index = i
#         max_val = li_sum_digit[i]
# print(li[max_index])

# # 20분 걸림

# n = int(input())
# li = list(map(int,input().split()))
# def digit_sum(x):
#     sum = 0
#     x_str = str(x)
#     for i in range(len(x_str)):
#         sum += int(x_str[i])         
#     return sum
    
# max = 0
# max_v = 0
# for i in range(n):
#     if digit_sum(li[i]) > max:
#         max = digit_sum(li[i])
#         max_v = li[i]
# print(max_v)
