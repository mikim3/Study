import sys

arr = list(map(int,input().split()))

# 왼쪽부터 시작해 가장 큰값
# 5 5 6 6 10 10 10 이런식
leftMax = []
# rightMin = []

leftMax.append(-100)
for i in range(1,len(arr)):
    if leftMax[i-1] > arr[i-1]:
        leftMax.append(arr[i-1])
    else:
        leftMax.append(leftMax[i-1])

# rightMin.append(10000000)
rightMin = 10000000

for i in range(len(arr)-1,0,-1):
    if leftMax[i] >= arr[i] and rightMin <= arr[i]:
        print(i)
        break
    else:
        if rightMin > arr[i]:
            rightMin = arr[i]


# for i in range(len(arr)-1,0,-1):
#     if rightMin[i-1] > arr[i-1]:
#         rightMin.append(arr[i-1])
#     else:
#         rightMin.append(rightMin[i-1])

