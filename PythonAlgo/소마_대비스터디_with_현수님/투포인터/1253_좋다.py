# 시작시간 2324 마무리시간 2350

# 3번쨰 값부터만 앞에 있는 것들로 좋아질수 있다.

n = int(input())
li = list(map(int,input().split()))
li.sort()
count = 0
for i in range(n):
  dest = li[i]
  left = 0
  right = n - 1
  while left < right: 
    if left == i:  # 현재 숫자는 사용할 수 없으므로 건너뜀
      left += 1
      continue
    if right == i:  # 현재 숫자는 사용할 수 없으므로 건너뜀
      right -= 1
      continue
    hap = li[left] + li[right]
    if hap == dest:
      count += 1
      break
    elif hap < dest:
      left+=1
    elif hap > dest:
      right -= 1
      
print(count)
