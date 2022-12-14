#   10 20 30 40  50
# 0 10 30 60 100 150


import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]    # init prefix_sum    
 
temp = 0    
for i in arr:    # accumulate arr section 
    temp += i
    prefix_sum.append(temp)
 
for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])











## 시간초과!!

# arr = list(map(int,input().split()))

# print(arr)

# arr_sum = []
# arr_sum.append(0)
# sum = 0
# for i in range(0,len(arr)):
#     sum += arr[i]
#     arr_sum.append(sum)    
# print(arr_sum)

# left = 0
# right = 0









