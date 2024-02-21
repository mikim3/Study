#########################
# 시작시간 240221 2256  마무리시간 2304

# 8 32
# 23 87 65 12 57 32 99 81

n, m = map(int, input().split())
li = list(map(int, input().split()))

li.sort()
lt = 0
rt = len(li) - 1

while lt <= rt:
  mid = (lt + rt) // 2
  if li[mid] == m:
    print(mid+1)
    break
  elif li[mid] > m:
    rt = mid - 1
  else:
    lt = mid + 1

# 약 10분 소요

# n , m = map(int,input().split())
# a = list(map(int, input().split()))
# a.sort()
# lt = 0
# rt = n - 1
# while lt <= rt:
#     mid = (lt + rt) // 2
#     if a[mid] == m:
#         print(mid+1)
#         break
#     elif a[mid] > m:
#         rt = mid - 1
#     else:
#         lt = mid + 1

# 이분탐색 생각안한 무지성 코드

# n , m = map(int,input().split())

# li = []

# li = list(map(int,input().split()))
# li.sort()
# for i in range(n):
#     if li[i] == m:
#         print(i+1)



