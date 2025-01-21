# 시작시간 0850 마무리시간 
import sys
import bisect
input = sys.stdin.readline

# 배열안에 값이 인덱스가 뒤로 갈수록 값이 커져야됨
# 값하나 추가할 때마다 

n = int(input().strip())
a = list(map(int, input().split()))

# 10 20 
lis = []  # 증가하는 수열함수

for x in a:
  # lis가 비어있거나, lis의 마지막 원소보다 x가 더 크면 바로 뒤에 붙임
  if not lis or lis[-1] < x:
    lis.append(x)
  else:
    # lis에 x라는 값이 가야할 위치 찾기
    index = bisect.bisect_left(lis, x)
    lis[index] = x

print(len(lis))
# for i in range(len(lis)):
#   print(lis[i], end=' ')

# 시작시간 마무리시간

def lower_bound(arr, target):
    # arr 내에서 target 이상의 값이 처음으로 등장하는 위치(인덱스)를
    # 이분 탐색으로 찾는 함수.
    
    # arr정렬돼 있어야함
    left, right = 0, len(arr) - 1
    position = len(arr)  # 기본적으로 마지막에 삽입
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            position = mid
            right = mid - 1
        else:
            left = mid + 1
    return position

# n = int(input().strip())
# a = list(map(int, input().split()))

# lis = []

# for x in a:
#     # 만약 lis가 비어있거나, x가 lis의 마지막보다 더 크면 그대로 append
#     if not lis or x > lis[-1]:
#         lis.append(x)
#     else:
#         # x가 들어갈 인덱스를 lower_bound로 찾고, 그 위치에 x를 대체
#         idx = lower_bound(lis, x)
#         lis[idx] = x

# print(len(lis))
