#   10 20 30 40  50
# 0 10 30 60 100 150

arr = list(map(int,input().split()))

print(arr)

arr_sum = []
arr_sum.append(0)
sum = 0
for i in range(0,len(arr)):
    sum += arr[i]
    arr_sum.append(sum)    
print(arr_sum)

left = 0
right = 0









