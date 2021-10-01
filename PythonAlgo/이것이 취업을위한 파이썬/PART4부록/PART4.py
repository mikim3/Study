# 책 PART 4 에 있는 것중에 내가 까먹을수 있을 만한 것들을 모아 봤습니다.
#for 문
scores = [90,85,77,65,97]
cheating_list = {2,4}
for i in range(5):
    if i+1 in cheating_list:   # 만약 cheating_list에 포함된 인덱스값의 리스트라면
        continue # 다음 for문으로 넘어간다.
    if scores[i] >=80:  #만약 80보다 크면 
        print(i+1, "번 학생은 합겹입니다.")

#함수

#람다함수 사용법{
def add(a,b):
    return a + b
# 일반적인 add() 메서드 사용
print(add(3,7))
#람다 사용  lambda 인자:표현식 
print("람다함수이용",(lambda a,b:a+b)(3,7)) #(lambda 인자1,인자2:인자를 이용한식)(만든 함수 이용)
#}

#p.445 입력을 위한 전형적인 소스코드
# 파이썬에서 줄바꿈으로 입력을 구분하려면 int(input()) 을 이용하면 되고  띄어쓰기로 구분하려면 list(map(int,input().split())) 을 이용하면 된다.
# 과정 순서대로 설명하자면 input() 으로 리스트를 받는다. 그 리스트는 split()로 띄어쓰기 기준으로 받아 진다. 
# 그리고 map함수로 그 나눠진 값들을 int 함수로 각각 적용 시킨다. 그 적용시킨 결과를 list() 함수로 리스트 형태로 바꾼다.

# 데이터의 개수 입력
# n = int(input())

# 각 데이터를 공백으로 구분하여 입력 전형적인 소스
# data = list(map(int,input().split()))
# data.sort(reverse = True)
# print(data)

# map(변환 함수, 순회 가능한 데이터)  map 은 여러개의 데이터를 한번에 다른 형태로 바꿔준다

# input() 처리속도가 느리다고 한다.
# 처리속도가 빨라야 하는경우   sys.stdin.readline() 함수를 이용한다.
# sys라이브러리는 input() 처럼 한줄씩 입력 받기 위해 쓰인다.
# import sys
# data=sys.stdin.readline().rstrip()   #많이 쓰이는 외워야할 코드    
# print("readline()으로 입력받기  ",data);




#내장함수 p.450
result = eval("(3 + 5) * 6")
print(result)

result= sorted([9,1,8,6,4],reverse=True)
print(result)

data = [9,1,8,5,4]
data.sort()
print(data)


#itertools
# itertools는 반복되는 데이터를 처리하는 기능을 포함하고 있다.
# permutations, combinations 가 가장 융용한 클래스이다.

print("순열과 조합 라이브러리")
from itertools import permutations 
data = ['A','B','C','ㅇ']  # 데이터 준비

result= list(permutations(data,3))  # data에서 3개를 뽑아서 나열한 경우를 알려준다. 인자가 없다면 기본적으로 리스트에 갯수만큼 다뽑느다

print(result)

#조합 
from itertools import combinations
data =['A','B','C']
result = list(combinations(data,2))
print(result)

#중복을 허용한 순열  itertools 에 product 
from itertools import product
data=['A','B','C'] #
result = list(product(data,repeat=2))  # 중복을 허용해서 2개를 뽑는 모든 순열 구하기
print(result)

#중복을 허용한 조합 구하기
from itertools import combinations_with_replacement
data = ['A','B','C']
result = list(combinations_with_replacement(data,2))
print(result)

#p. 454   heapq
# PriorityQueue라이브러리로 heap을 쓸수도 있지만 코딩테스트환경에서 더 좋은 환경을 위해 heapq라이브러리를 써서 함수로 구현하자
# 힙에 원소를 삽입할 때는 heapq.heappush() 메서드를 사용  
# 힙에서 꺼낼때 heapq.heappop() 메서드 사용
# 최소힙(minheap) 작은 값부터 정렬
import heapq
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
### 작은값부터 정렬 됨

#최대 힙(큰 거부터 정렬)
import heapq
def heapsort(iterable):
    h=[]
    result=[]
    #
    for value in iterable:
        heapq.heappush(h, -value)
        #
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)















