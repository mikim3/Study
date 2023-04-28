def plus_one(x):
    return x+1

print(plus_one(2))

# lambda x를 인자로 받아서 x에 2를 더하는 람다 함수
plus_two = lambda x : x + 2

print(plus_two(1))

a = [1,2,3]
# map(2번쨰 인자의 내부에 각각적용할 함수, 적용될 인자)
b = list(map(plus_two,a))

print(a)
print(b)
print(list(map(lambda x : x+2, a))) # lambda로 한줄로 끝내기


# list(map(int, input().split()))
