##########################
# 시작시간  0525 19:20   마무리시간

def recur(x):
    if x == 0:
        return
    else:
        recur(x//2)
        print(x % 2, end='')

n = int(input())
recur(n)


#########################
