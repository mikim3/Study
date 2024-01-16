
### Top-down 방식
# memo = {}
# def fibo(n):
#   if n == 1 or n == 2:
#     return 1
#   if n not in memo:
#     memo[n] = fibo(n-1) + fibo(n-2)
#   return memo[n]

# print(fibo(5))
# 1 1 2 3 5 8 13

### Bottom-up
memo = {1:1 , 2:1}
def fibo(n):
  for i in range(3, n+1):
    memo[i] = memo[i-1] + memo[i-2]
  return memo[n]
print(fibo(7))
