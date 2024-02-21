####################################
# 시작시간 240221 2309 마무리시간 2335

k, n = map(int ,input().split())
li = []
for i in range(k):
  li.append(int(input()))

lt = 0
rt = max(li)

while lt <= rt:
  # mid로 잘라보기
  mid = (lt + rt) // 2
  total = 0
  # mid 크기로 잘라보기
  for i in range(k):
    total += li[i] // mid
  # 잘게 나누어짐
  if total >= n:
    res = mid
    lt = mid + 1
  elif total < n:
    rt = mid - 1
print(res)


################################
# 시작시간 :  11 40   종료시간 :  12:20  

# # 갯수 조건에 맞는 경우를 찾는다.   크기를 키우면서 확인한다.
# def Count(len):
#     cnt = 0
#     for x in li:
#         cnt += (x//len)
#     return cnt

# k , n = map(int, input().split())

# li = []
# for i in range(k):
#     li.append(int(input()))

# max_value = max(li)

# lt = 1
# rt = max_value 
# # 랜선 갯수
# div = 0
# # 이분탐색의 중간값이자 랜선 갯수를 알아내는 수

# while lt <= rt:
#     mid = (lt + rt) // 2
#     # 랜선 갯수가 n보다 크면  너무 작게 잘랐으니 lt를 옮겨서 mid도 키워서 자르는 랜선의 크기를 높인다.  
#     if Count(mid)>=n:        
#         res = mid
#         lt = mid + 1  #
#     # 너무 크게 잘랐으니 더 작게 자른다.
#     else:
#         rt = mid - 1

# print(res)




    