# 시작시간 1743
t = int(input())

for i in range(t):
  n, m= map(int, input().split())
  li_a = list(map(int, input().split()))
  li_b = list(map(int, input().split()))
  count = 0
  # a보다 B가 작은쌍
  for j  in range(n):
    for z in range(m):
      if li_a[j] > li_b[z]:
        count+=1
  print(count)
