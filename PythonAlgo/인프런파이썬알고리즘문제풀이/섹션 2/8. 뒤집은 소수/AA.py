# 14 17

def reverse(x):
    x_str = str(x)
    x_str_r=x_str[::-1]    
    return int(x_str_r)

def isPrime(x):
    res = 1  
    for i in range(2,x//2+1):
        if x % i == 0:
            res = 0
    if x == 1:
        res = 0
    return res;    

n = int(input())
li = list(map(int,input().split()))

for i in range(n):
    int_r = reverse(li[i])
    if isPrime(int_r):
        print(int_r)
# 에라토스테네스체

# 특정 수의(2이상부터) 배수는 소수가 아닌게 확정임으로 미리 체크를하고

# print(isPrime(5))
# print(isPrime(3))
# print("1212")
# print(isPrime(12))

