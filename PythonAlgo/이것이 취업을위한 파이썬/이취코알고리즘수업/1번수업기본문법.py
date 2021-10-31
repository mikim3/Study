
#  2차원 리스트 초기화 효과적으로 하기
n=4
m=5        
array = [[0] * m for _ in range(n)]   # for _ in range(3)  _ 는 아무 변수도 없다고 의미 그저 3번반복 할때
print(array)

# append()   변수명.append() 리스트에 원소를 하나 삽입
# sort()   변수명.sort(reverse=True)   # 내림차순   정렬

a = [1,4,3]
print("기본 리스트: ",a)

#삽입
a.append(2)
print("삽입: ",a)

#내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ",a)

a=[4,3,2,1]
#리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ",a)

# 특정 인덱스에 데이터 추가
a.insert(0,3)
print("인덱스 2에 3 추가: ",a)

#특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))  # 3 데이터 갯수

#특정 값 데이터 삭제  (하나만)
a.remove(1)
print("값이 1인 데이터 삭제: ",a)


a= [1,2,3,4,5,5,5]
remove_set = {3,5}  # {} 집합 자료형은 순서가 없고 인덱스가 없다
result = [i for i in a if i not in remove_set]
print(result)

# 파이썬에서 문자열에서 특정 문자열을 바꾸는 건 불가능 하다.
a= "Hello"
print(a)
#a[2] = 'a'  # 오류

#  ()  튜플
# 튜플은 한 번 선언된 값을 변경할 수 없다.
# 튜플은 리스트에 비해 상대적으로 공간 효율 적이다.      
# 튜플도 인덱스가 있다.


# dict() 사전 자료형 
# 사전 자료형은 키와 값(Value)의 쌍을 데이터로 가지고 있는 자료형이다.
# 키와 값의 쌍을 데이터로 가진다.
# 원하는 '변경불가능'한 자료형을 키로 사용할 수 있다.


# {} 집합 자료형  set()  집합 자료형   
# 중복을 허용하지 않는다
# 순서가 없다
# 집합은 리스트 혹은 문자열을 이용해서 초기화 할 수 있다. ( 이때 set() 함수 사용)??
# 또는 중괄호{} 안에 각 원소를 콤마를 기준으로 구분하여 삽입하여 초기화 사용

# 집합 초기화로 리스트 중복값제거
data = set([1,1,2,3,4,4,5])   
print(data)

# 집합 자료형 초기화 방법 2
data = {1,1,2,3,4,4,5}
print(data)

# 집합 자료형을 연산할수 있다.  합집합, 교집합, 차집합 연산 등이 있다.

# 집합 연산 방법
a = set([1,2,3,4,5])
b= set([3,4,5,6,7])

#합집합  |
print(a | b)

# 교집합
print(a & b)

# 차집합 
print(a - b)


#입출력

#list(map(int,input().split()))


#조건문
score=80
if score>=80:
    pass  #그냥 넘김  #pass 안적으면 오류난다.  컴터 입장에서 들여쓰기된 무언가가 작성되길 원한다.
else:
    print("80이상아닐때")
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)


#함수

# 전역변수 사용
array = [1,2,3,4,5]

def func():
    global array  # 함수밖에 변수 쓰기 
    array = [3,4,5]
    array.append(6)

func()
print(array)


# 람다 표현식 
print((lambda a,b: a+ b)(3,7))

array = [('홍길동',50),('이순신',32),('아무개',74)]

def my_key(x):
    return x[1]

print(sorted(array,key=my_key))
print(sorted(array,key=lambda x:x[1])) # 람다함수로 두번째원소를 기준으로 정렬하게끔 key값을 정했다.



