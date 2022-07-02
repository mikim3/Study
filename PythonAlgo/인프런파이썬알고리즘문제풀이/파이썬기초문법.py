

# 리스트와 내장함수(1)
import random as r

a = list(range(1,7))
print(a)

a.insert(3,7)  # 3번 인덱스에 7 삽입
print(a)

a.pop(3)
print(a)

a.remove(4)  # 4 값 삭제

print(a,"    " ,a.index(5))  # 5는 3번 인덱스에 있다
print(sum(a))
print(max(a))

print(a)
r.shuffle(a)
print(a)
sorted(a)  # 반환값이 정렬된 값
print(a)   
a.sort()  # 해당 리스트를 정렬하는 함수   리스트에 있는 함수  list.sort(reverse=false) 기본값 오름차순이다.
print(a)
a.clear()
print(a)

# 리스트와 내장함수(2) 
a = [23,12,36,53,19]

for x in enumerate(a):     # (0,23)  (1,12) (인덱스, 값)
    print(x)
    print(x[0], x[1])
for index, value in enumerate(a):
    print(index,value)    

if all(60>x for x in a):  # all()  하나라도 거짓이면 false
    print("YES")
else:
    print("NO")

if any(15>x for x in a):  # aby()  무엇 하나라도 참이면 True
    print("YES")
else:
    print("NO")

#2차원 리스트 생성과 접근

a = [[0]*3 for _ in range(3)]  # [0,0,0] 만들기를 3번 반복해라
print(a)
a[0][1] = 1
print(a)
a[2][1] = 7
print(a)
for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=' ')
    print()

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
















