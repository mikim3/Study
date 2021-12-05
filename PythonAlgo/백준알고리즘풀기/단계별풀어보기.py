

# 1차원 배열유형

# 최소값, 최대값 출력 
# n=int(input())
# arr=list(map(int,input().split()))

# arr.sort()#오른차순

# print(arr[0],arr[len(arr)-1])



# 3052번 문제
# 나머지 


    
# 8958번 문제
# OX퀴즈
    
n = int(input())  # 시도할 횟수
arr=[] #한번 반복마다 바뀔 배열
sum =0 # 점수 0 부터시작
contin=0# 연승확인
sumarr=[] # 연승리스트
print("n입력받음")
for i in range(n): # 전체 시도할 횟수 반복
    print("문제한 묶음 처리하고 돌아옴")
    arr=list(map(str,input().split())) # 초기화 겸 입력
    sum=0
    contin=0
    for j in range(len(arr)): # OX갯수 만큼 반복
        if arr[j]=='O': # O일 경우
            contin+=1 # 연승점수 +1  
            sum+=contin  # 연승점수를 총합에 더함
        if arr[j]=='X':#X일경우
            contin=0
    print("sumarr 추가직전")
    sumarr.append(sum)
    
for i in range(n):
    print(sumarr[i])
    
            
    
   



# 4344번 
# 평균은 넘겠지

n = int(input())
sum=0
avg = 0
avgup=0
avgarr=[]
for i in range(n):
    arr = list(map(int,input().split()))  #  5 50 50 70 80 100
    sum=0 # 점수합
    avgup=0
    for j in range(arr[0]): # 한 반에 인원수
        sum+=arr[j+1] # 1번인덱스부터 총합에 더한다
    avg=sum/(arr[0])  # 총합/인원수 는 평균
    
    for x in range(arr[0]):
        if  arr[x+1]-avg>0:
            avgup+=1    #평균보다 높은사람 +1
    # avgarr[i]=round(avgup/n,3)
    avgarr.append(round(avgup/arr[0]*100,3))
    avgarr[i]=round(avgup/arr[0]*100,3)
    
for i in range(n):
    print("{:.3f}%".format(avgarr[i],end='%\n'))  # format 함수는 몰랐네
    



#########재귀방식 시작
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
    
