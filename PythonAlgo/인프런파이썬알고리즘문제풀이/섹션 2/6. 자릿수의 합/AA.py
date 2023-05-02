n = int(input())

li = list(map(int, input().split()))
def digit_sum(num):
    sum_digit = 0
    str_num = str(num)
    for i in str_num:
        sum_digit += int(i)
    return sum_digit
li_sum_digit = []
for i in range(n):
    li_sum_digit.append(digit_sum(li[i]))

max_val = 0
max_index = 0
for i in range(n):
    if (max_val < li_sum_digit[i]):
        max_index = i
        max_val = li_sum_digit[i]
print(li[max_index])

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
