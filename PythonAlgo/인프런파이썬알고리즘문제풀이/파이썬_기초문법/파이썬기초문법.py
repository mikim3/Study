# 함수 만들기

def isPrime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]
print(isPrime(12))

# 람다 함수

plus_two = lambda x: x+2
print(plus_two(1))

# print(list(map(plus_two,a)))
print(list(map(lambda x:x+1, a)))
