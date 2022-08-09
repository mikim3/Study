# 약 10분 소요

n , m = map(int,input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
# 이분탐색 생각안한 무지성 코드

# n , m = map(int,input().split())

# li = []

# li = list(map(int,input().split()))
# li.sort()
# for i in range(n):
#     if li[i] == m:
#         print(i+1)


