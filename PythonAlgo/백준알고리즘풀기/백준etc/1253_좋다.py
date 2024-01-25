# 시작시간 240125 15:33
# 못품 # 아애 까먹은 알고리즘 이였음
# 서로 다른 두개의수를 대입해봐야 된다는 점에서 해당 알고리즘이 투 포인터임을 알 수 있다.

###모범답안

n = int(input())
li = list(map(int, input().split()))

li.sort()

count = 0
for i in range(n):
  left, right = 0, n - 1
  while left < right:
    if left == i:
      left += 1
    elif right == i:
      right -= 1
    else:
      current_sum = li[left] + li[right]
      if current_sum == li[i]:
        count += 1
        break
      elif current_sum < li[i]:
        left += 1
      else:
        right -= 1
print(count)
