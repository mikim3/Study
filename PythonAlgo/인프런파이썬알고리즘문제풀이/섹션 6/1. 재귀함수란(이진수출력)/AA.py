########################
# 시작시간 231001  1544 마무리 시간
# 답봄

def recur(n):
  if n == 0:
    return
  else:
    recur(n // 2)
    print(n % 2, end='' )

n = int(input())
recur(n)


##########################
# 시작시간  0525 19:20   마무리시간

# def recur(x):
#     if x == 0:
#         return
#     else:
#         recur(x//2)
#         print(x % 2, end='')

# n = int(input())
# recur(n)


#########################
