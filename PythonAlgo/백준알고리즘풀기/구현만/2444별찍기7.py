# 23:47시작

# 4 3 2 1 0

# 1 3 5 7 9
n = int(input())

for i in range(n):
  print(' '*(n-i-1) + '*'*(2*i+1))
for i in range(n, 0, -1):
  print(' '*(n-i+1) + '*' * (2*i-3))
