# 20분 걸림

n = int(input())
li = list(map(int,input().split()))
def digit_sum(x):
    sum = 0
    x_str = str(x)
    for i in range(len(x_str)):
        sum += int(x_str[i])         
    return sum
    
max = 0
max_v = 0
for i in range(n):
    if digit_sum(li[i]) > max:
        max = digit_sum(li[i])
        max_v = li[i]
print(max_v)
