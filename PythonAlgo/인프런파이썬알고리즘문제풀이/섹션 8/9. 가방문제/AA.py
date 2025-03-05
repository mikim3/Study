# 시작시간 2110 마무리시간 2120

n, han = map(int,input().split())
dp = [0] * (han+1)# dp[3] = 10  무게3kg채웠을떄 10의 가치가 최대다.
for _ in range(n):
  w,v = map(int,input().split()) #무게, 가치
  for j in range(w,han+1): # +1맞나?
    dp[j] = max(dp[j-w] + v, dp[j])

print(max(dp))
