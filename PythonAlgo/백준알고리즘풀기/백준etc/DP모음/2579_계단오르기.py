# 시작시간 240130 11:16 마무리시간
# 못품
# top-down 으로 한번
# bottom-up 으로 한번 이런식으로 두 번 생각하면서 점화식을 찾아보자

n = int(input())
dp = [0] * (n + 5)
li = []
for i in range(n):
  li.append(int(input()))

# 1,2,3 까지는 구하기

# 3 이후에
if n > 0:
  dp[0] = li[0]
if n > 1:
  dp[1] = li[0] + li[1]  # 이게 괜찮은지 모르겠네
if n > 2:
  dp[2] = max(li[0] + li[2], li[1] + li[2])

for i in range(3,n):
  dp[i] = max(dp[i-3] + li[i-1] + li[i], dp[i-2] + li[i])

# print(dp)
print(dp[n-1])

