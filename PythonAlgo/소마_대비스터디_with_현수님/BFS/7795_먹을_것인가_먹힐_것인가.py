# 시작시간 1743  마무리시간 18
# 시간 초과 걸림
# 투 포인터가 왜 투 포인터인지 생각해보면 이해하기 쉬움

# 쓸데없이 탐색하는 경우
# 
t = int(input())

for _ in range(t):
  n, m= map(int, input().split())
  li_a = list(map(int, input().split()))
  li_b = list(map(int, input().split()))

  li_a.sort()
  li_b.sort()

  count = 0
  b_p = 0
  for a_p in range(n):
    while b_p < m and li_a[a_p] > li_b[b_p]:
      b_p += 1
    count += b_p

  print(count)
