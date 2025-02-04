# 답 봐도 모름

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합을 저장할 리스트 va (인덱스 0은 0으로 초기화)
va = [0] * (n + 1)
cnt = 0

# 1부터 n까지 누적합 계산 및 누적합이 k와 같을 경우 카운트
for i in range(1, n + 1):
    va[i] = va[i - 1] + nums[i - 1]
    if va[i] == k:
        cnt += 1

# 누적합의 등장 횟수를 저장할 딕셔너리
ma = {}

# 1부터 n까지, 누적합 va[i]와 va[i]-k가 짝을 이루는 경우의 수 계산
for i in range(1, n + 1):
    # va[i] - k가 이전에 나온 적이 있다면 그 횟수만큼 cnt에 더함
    cnt += ma.get(va[i] - k, 0)
    # 현재 누적합 va[i]의 등장 횟수를 1 증가시킴
    ma[va[i]] = ma.get(va[i], 0) + 1

print(cnt)

# # 시작시간   마무리시간
# # 누적합이 
# from collections import defaultdict

# n, k = map(int,input().split())
# li = list(map(int,input().split()))

# # 누적합을 카운트
# prefix_count = defaultdict(int)
# prefix_count[0] = 1 # 지금까지 누적합 0이 1번 등장했다.

# current_sum = 0 # 현재까지 누적합
# result = 0  # 조건에 맞는 부분합

# # 어떤 구간 A[i] ... A[j] 의 합은
# # S[j] - S[i-1]
# # 즉 부분합이 K가 되는 조건은
# # S[j] - S[i-1] = K   -----> S[i-1] = S[j] - K 로 수정가능

# # 부분 합중 합이 k
# for i in range(n):
#   current_sum += li[i]
#   # 만약 (현재 누적합 - K) 값이 이전에 나온 적이 있다면
#   # 그만큼 현재 부분합 (어떤 i부터시작해 현재 j까지)이 K가 되는 경우가 있다는 의미 
#   # (current_sum - k) 
#   result += prefix_count[current_sum - k]
#   prefix_count[current_sum] += 1 # 현재 누적합을 딕셔너리에 추가

# print(result)
# print("prefix_count == ",prefix_count,"current_sum", current_sum)
