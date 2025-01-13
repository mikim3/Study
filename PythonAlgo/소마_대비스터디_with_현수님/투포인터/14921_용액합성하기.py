# 시작시간 1915 마무리시간 2000

# 오름차순으로 값이 입력됨
# 서로 다른 두개의 값을 더해서 0에 가장 가깝게 만드는 문제

# 모든 수를 직접 빼보면 (n^2 - n)/2
# 최악의 경우 대충 이정도 횟수를 수행해야함 4999950000

# 해결법
# 두개의 포인터를 맨앞 맨뒤에 두고 비교를 하는데
# 만약에 0 보다 결과가 크면 값이 작아야하니까 p2 -= 1
# 0보드 작으면 값이 커져야 되니까 p1 += 1
# 하면 될듯

n = int(input())
li = list(map(int, input().split()))

############
p1 = 0 # 앞에있는 포인터
p2 = n -1 # 뒤쪽 포인터

min_v = 10000000222
while p1 < p2:
  hap = li[p1] + li[p2]
  if hap > 0:
    p2 -= 1
    if abs(hap) < abs(min_v):
      min_v = hap
  elif hap <= 0:
    p1 += 1
    if abs(hap) < abs(min_v):
      min_v = hap
  elif hap == 0:
    min_v = 0
    break

print(min_v)
