import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(map(int,input().split()))
arr_sum = [0]
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    arr_sum.append(sum)    
# print(arr_sum)
left = 0
right = 0
i = 0
while(i < m):
    left, right = map(int,input().split())    
    print(arr_sum[right] - arr_sum[left - 1])
    i += 1