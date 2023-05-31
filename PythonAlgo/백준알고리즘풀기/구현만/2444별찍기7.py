# 22:22시작  22:31끝

# 4 3 2 1 0
# 1 3 5 7 9
# 1 2 3 4
# 7 5 3 1

n = int(input())

for i in range(n):
  print(" "  * (n - i - 1) + "*" * (i * 2 + 1))
  
for i in range(n - 1, 0 , -1):
  print(" " * (n - i) + "*" * (i * 2 - 1))
  
  
  
  
  
  
  
  
  
  