# 14 17



def reverse(x):
    
    
    return 

# 에라토스테네스체

# 특정 수의(2이상부터) 배수는 소수가 아닌게 확정임으로 미리 체크를하고

def isPrime(x):
    res = 1  # 0 이 되면 소수
    for i in range(2,x):
        if x % i == 0:
            print("i=",i)
            res = 0

    return res;    
    

print(isPrime(5))
print(isPrime(3))
print("1212")
print(isPrime(12))

