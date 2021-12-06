

# 5단계 1차원 배열유형

# 10818번 문제
# 최소값, 최대값 출력 
# n=int(input())
# arr=list(map(int,input().split()))

# arr.sort()#오른차순

# print(arr[0],arr[len(arr)-1])

# 3052번 문제
# 나머지 
# set() 을 생각못해서 못 풀었었음

# arr=set()  # set() 으로 중복되는 요소를 제거     # 집합자료형은 중복되는 수를 하나로 본다.
# for i in range(10): # 10번반복
#     n=int(input())   # 한번씩 입력받을 수
#     arr.add(n%42)
# print(len(arr))
    
    
# 8958번 문제
# OX퀴즈
    
# n = int(input())  # 시도할 횟수
# arr=[] #한번 반복마다 바뀔 배열
# sum =0 # 점수 0 부터시작
# contin=0# 연승확인
# sumarr=[] # 연승리스트
# for i in range(n): # 전체 시도할 횟수 반복
#     arr=input() # 초기화 겸 입력
#     sum=0
#     contin=0
#     for j in range(len(arr)): # OX갯수 만큼 반복
#         if arr[j]=='O': # O일 경우
#             contin+=1 # 연승점수 +1  
#             sum+=contin  # 연승점수를 총합에 더함
#         if arr[j]=='X':#X일경우
#             contin=0
#     sumarr.append(sum)
    
# for i in range(n):
#     print(sumarr[i])
    
            
    
   



# 4344번 
# 평균은 넘겠지

# n = int(input())
# sum=0
# avg = 0
# avgup=0
# avgarr=[]
# for i in range(n):
#     arr = list(map(int,input().split()))  #  5 50 50 70 80 100
#     sum=0 # 점수합
#     avgup=0
#     for j in range(arr[0]): # 한 반에 인원수
#         sum+=arr[j+1] # 1번인덱스부터 총합에 더한다
#     avg=sum/(arr[0])  # 총합/인원수 는 평균
    
#     for x in range(arr[0]):
#         if  arr[x+1]-avg>0:
#             avgup+=1    #평균보다 높은사람 +1
#     # avgarr[i]=round(avgup/n,3)
#     avgarr.append(round(avgup/arr[0]*100,3))
#     avgarr[i]=round(avgup/arr[0]*100,3)
    
# for i in range(n):
#     print("{:.3f}%".format(avgarr[i],end='%\n'))  # format 함수는 몰랐네
    

############ 6단계 함수

##### 1065번 한수
# 정수 X의 각 자리가 등차수열을 이루면 그 수를 한수라고 한다.
# 두자리수는 다 한수다
# 세자리부터 비교하면 된다
n=int(input())  # 알아야할 한수의 범위를 알려줄 수
num=0 
for i in range(1,n+1):
    nArray=list(map(int,str(i)))   # 그 수의 각자리를 비교하기 위해 각자리를 분리
    if i < 100:
        num+=1  # 한수 맞으니 카운트
    elif nArray[0]-nArray[1]==nArray[1]-nArray[2]:
        num+=1
print(num)

######### 10단계 재귀방식 시작
# 팩토리얼 구현하기
# 입력

#

# 재귀함수로 풀어보자 
#N!
# n=int(input())

# def factorial(m):
#     if m==0:
#         return 1
        
    
#     return m*factorial(m-1) 

# print(factorial(n))

#피보나치 수열
# n이 1이면 0, 1 까지 출력 답이 1이됨 
# 

# n=int(input())

# def pivonachi(m):
#     if m==2:
#         return 1
#     elif m==0:
#         return 0
#     elif m==1:
#         return 1
#     else:
#         return pivonachi(m-2)+pivonachi(m-1)

# print(pivonachi(n))
#########재귀방식 끝


#########그리디방식 시작
#

# 동전 최소 개수 구하기 문제
# 핵심은 가장 큰 돈부터 쓰자
# n,k=list(map(int,input().split()))
# moneyKind=[]

# print(n,k)

# for i in range(n):
#     moneyKind[i]=int(input())
    
# for i in range(n-1,-1,-1):
    
