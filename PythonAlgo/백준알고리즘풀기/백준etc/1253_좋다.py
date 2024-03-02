##########################
# 시작시간 240224 0757  마무리시간
# 이분탐색으로만 풀면 

# n = int(input())
# li = list(map(int,input().split()))
# li.sort()

# # 서로 다른 2개의 수를 더한다. n^2  쌉가능
# max_value = max(li)+1
# two_sum = []
# for i in range(n):
#   for j in range(i + 1,n):
#     if max_value >= li[i] + li[j]:
#       two_sum.append(li[i] + li[j])
# tmp = set(two_sum)
# two_sum = list(tmp)
# two_sum.sort()
# count = 0
# print(two_sum)
# # n개에 대하여 찾기
# for i in range(n):
#   lt = 0
#   rt = len(two_sum) - 1
  
#   while lt <= rt:
#     mid = (lt + rt) // 2
#     if li[i] == two_sum[mid]:
#       count += 1
#       break
#     elif li[i] > two_sum[mid]:
#       lt = mid + 1
#     else:
#       rt = mid - 1
# print(count)


# 시작시간 240125 15:33
# 못품 # 아애 까먹은 알고리즘 이였음
# 서로 다른 두개의수를 대입해봐야 된다는 점에서 해당 알고리즘이 투 포인터임을 알 수 있다.

###모범답안

# n = int(input())
# li = list(map(int, input().split()))

# li.sort()

# count = 0
# for i in range(n):
#   left, right = 0, n - 1
#   while left < right:
#     if left == i:
#       left += 1
#     elif right == i:
#       right -= 1
#     else:
#       current_sum = li[left] + li[right]
#       if current_sum == li[i]:
#         count += 1
#         break
#       elif current_sum < li[i]:
#         left += 1
#       else:
#         right -= 1
# print(count)
