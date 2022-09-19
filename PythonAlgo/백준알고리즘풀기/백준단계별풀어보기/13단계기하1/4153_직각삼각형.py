# 11:37 시작

a, b, c = map(int,input().split())

while a+b+c > 0:
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")

    a, b, c = map(int,input().split())

