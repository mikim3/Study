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

# 자주 사용할 내장 함수 예시 ***
# sorted() with key
array = [('홍길동',35),('이순신',75),('아무개',50)]
result = sorted(array,key=lambda x: x[1],reverse=True)  # 점수별 내림차순
print(result)


#map함수는 각각의 원소에 어떤 함수를 적용할 수 있다.
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a,b: a+b, list1,list2)    # 리스트안에 각각의 원소에 값을 더해라 

print(list(result))  

# list(map(int,input().split()))  # input받은 값을 split으로 띄어쓰기마다 구분지어 리스트로 만든다 -> map함수로 int함수를 리스트 각각에 적용시킨다. -> map함수로 나온 값을 다시 list

#유용한 표준라이브러리


# iter





#******* 쌉중요 특정 상황에서 어떤것을 써야할까?
#
#튜플을 사용하면 좋은경우
# 서로 다른 성지르이 데이터를 묶어서 관리해야 할 때 
# 최단 경로 알고리즘에서 (비용, 노드번호)의 형태로 튜플 자료형을 자주 사용한다.
# 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용 될 수 있다.



