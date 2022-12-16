# 아이디어

# 바로 앞과 바로 뒤를 합치는 경우 두가지 수만 나온다 
# 그 두 수만 합치면 그대로 정렬했을떄 가장큰수를 만들떄 쓸수 있는 경우인지 결정할 수 있다.

# : {10, 68, 75, 7, 21, 12 }
# Output: 77568211210

arr = list(map(int,input().split()))

for i in range(len(arr)):
    arr[i] = str(arr[i])

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] < arr[j] + arr[i]:
            arr[i],arr[j] = arr[j],arr[i]

for i in range(len(arr)):
    print(arr[i],end='')

# print(arr)


        