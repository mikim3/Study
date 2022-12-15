
n = int(input())

# XOR(^)을 이용하여 홀짝구분
if (n ^ 1) + 1 == n:
    print("n is odd")
else:
    print("n is even")

# and를 이용해서 홀짝구분


if (n & 1) ==  0:
    print("n is even")
else:
    print("n is odd")
