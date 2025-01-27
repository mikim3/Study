
memo = {1 : 1, 2:2}

def fibo(n):
  # if n == 1 or n == 2: # basecase가 위에 이미 있음
  #   return 1
  for i in range(3, n+1):
    memo[i] = memo[i-1] + memo[i-2]
  return memo[n]

print(fibo(5))
print(fibo(6))
print(fibo(7))
