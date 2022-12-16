arr = list(map(int,input().split()))

# 왼쪽부터 시작해 가장 큰값
# 5 5 6 6 10 10 10 이런식
leftMax = []
# rightMin = []

leftMax.append(-100)
for i in range(1,len(arr)):
    # arr이 더 크면 arr의 값으로 갱신
    if leftMax[i-1] < arr[i-1]:
        leftMax.append(arr[i-1])
    else:
        leftMax.append(leftMax[i-1])

print(leftMax)
rightMin = (len(arr)) * [100000000]
# rightMin.append(10000000)
for i in range(len(arr)-2,-1,-1):
    if rightMin[i + 1] > arr[i + 1]:
        rightMin[i] = arr[i + 1]
    else:
        rightMin[i] = rightMin[i + 1]

print("rightMin == ",rightMin)
for i in range(len(arr)):
    if arr[i] < leftMax[i] and arr[i] > rightMin[i]:
        print(arr[i])
        exit()

print(-1)
#        // for (int i = n-2; i >= 0; i++){
