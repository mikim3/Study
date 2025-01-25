memo = {}

def fibo(n):
  if n == 1 or n == 2:
    return 1
  if n not in memo: # n이라는 key를 가진 값이 memo에 없으면
    memo[n] = fibo(n-1) + fibo(n-2)
  return memo[n]
print(fibo(6)) # 8
print(fibo(7)) # 13
print(fibo(8)) # 21