# 260212 시작 1916  마무리 1946
# 가장 가까운 두 말의 거리가 최대

n, c = map(int,input().split())

li = []
for i in range(n):
  li.append(int(input()))
li.sort()
lt = 1
rt = max(li) - min(li)
mid = (lt+rt)//2 # 현재 확인할 거리
max_v = 0
while lt <= rt:
  count = 1
  mid = (lt+rt)//2 # 현재 확인할 거리
  prv = li[0]
  for i in range(n):
    if li[i] - prv >= mid: # mid보다 멀면
      prv = li[i]
      count += 1
  # print(mid, count)
  if count < c: #너무 넓게 배치해서 말을 못 넣음
    rt = mid - 1
  elif count >= c:
    lt = mid + 1
    if mid > max_v:
      max_v = mid
print(max_v)


###############################
# 시작시간 240222 2122 마무리시간
# 못 품 아이디어는 되는데 구현이 안됨

# n, c = map(int, input().split())
# li = []
# for i in range(n):
#   li.append(int(input()))
# li.sort()

# print(li)
# lt = 1
# rt = li[-1] - li[0]

# 이전에 찾은 값보다 mid 만큼 뒤로 가는걸 c번 반복한다.
# 만약 c번 만큼 배치하는데 실패하면 mid값을 줄인다. (후보가 될수 없음)
# 만약 C번 만큼 배치하는데 성공하면 mid값을 높인다. (후보 쌉 가능)
# 거리 만큼 뒤로 가는데 만약에 이전 사이에 거리가 마지막 항보다 크면 답 후보에 올릴수 없다.

# # 최대거리
# res = 0
# while lt <= rt:
#   mid = (lt + rt) // 2

#   # 이전 말 위치
#   pri_horse = li[0]
#   # 배치된 말 마리수  1마리는 이미 완료
#   count = 1
#   for i in range(1, n):
#     # 이전 말과 거리~~~~
#     if li[i] - pri_horse >= mid:
#       count += 1
#       # 이전 말을 li[i]에 배치
#       pri_horse = li[i]
#     # 거리가 너무 짧으면 다음 i 반복
#   # 너무 많은 말을 배치하는게 가능하던가 딱 맞게 배치되면 거리가 너무 짧아서 많이 배치 된거다.
#   if count >= c:
#     res = mid
#     lt = mid + 1
#   else:
#     rt = mid - 1
# print(res)

# 시작시간 :  3:50     종료시간 : 4시 30

# def Count(len):
#     cnt = 1
#     ep = li[0]
#     for i in range(1,n):
#         if li[i] - ep >= len:
#             cnt += 1
#             ep = li[i]
#     return cnt

# n , c = map(int, input().split())
# li = []

# for i in range(n):
#     li.append(int(input()))
# li.sort()
# lt = 1
# rt = li[n-1]

# while lt <= rt:
#     mid = (lt + rt) // 2
#     if Count(mid) >= c:
#         res = mid
#         lt = mid + 1
#     else:
#         rt = mid - 1
# print(res)
