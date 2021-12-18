# 1단계 입출력과 사칙연산

# 10869 번 사칙연산
# a,b=list(map(int,input().split()))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# 2588 곱셈

# a=int(input())
# b=int(input())
# c=str(b)
# for i in range(len(c)-1,-1,-1):
#     print(a*int(c[i]))    
# print(a*b)


# 2단계 if문 단계

# 2753번
# 윤년이면 1  아니면 0
# n= int(input())  
# yun = 0  # 윤년값
# # 4의배수이면서 100의 배수가 아니면 윤년
# # 100의 배수중에서 400의 배수가 아니라면 윤년이 아니다.
# # 400의 배수라면 윤년이다.
# # 1900은 100의 배수이고 400의 배수는 아니여서 윤년아님
# if n%400==0:  # 400의 배수라면 무조건 윤년
#     yun = 1
# elif n%100==0:
#     yun = 0
# elif n%4==0:
#     yun=1
# else:
#     yun=0
# print(yun)

# 14681 번
# 사분면 고르기
# x=int(input())
# y=int(input())
# saboon=0
# if x>0 and y>0:
#     saboon=1
# elif x<0 and y>0:
#     saboon=2
# elif x<0 and y<0:
#     saboon=3    
# else:
#     saboon=4
# print(saboon)

# 2884 번
# 알람시계
# h,m=list(map(int,input().split()))
# if m-45<0:  # 분이 빼면 음수가 될때
#     m=60+m-45
#     if h-1<0:
#         h=23
#     else:
#         h-=1
# else:  # 분이 음수 안될때
#     m-=45
# print(h,m)
    


# 3단계 for 문 유형

# 15552번 문제
# 빠른 A+B
# import sys
# T = int(input())
# for i in range(T):
#     a,b = map(int,sys.stdin.readline().split())
#     print(a+b)

# 2742번 문제
# 기찍 N
# n=int(input())

# for i in range(n,0,-1):
#     print(i)

# 2438번 문제
# 별 찍기 - 1
# n = int(input())
# for i in range(1,n+1):
#     print("*"*i)

# 2439번 
# 별 찍기 - 2

# n = int(input())

# for i in range(n):
#     print(" "*(n-i-1)+"*"*(i+1))

# 10871번 문제 
# X보다 작은 수

# n,x = map(int,input().split())
# arr=list(map(int,input().split()))
# g=[]
# for i in range(n):
#     if arr[i]<x:
#         print(arr[i],end=' ')
###############for 유형 끝

############ 4단계 while문

# 10952번
# A+B - 5
# while True:
#     a,b=list(map(int,input().split()))
#     if a==0 and b==0:
#         break
#     print(a+b)

# 10951번
# A+B-4
# 문제가 이해가 안가서 답지를 봄
# 입력의 끝범위를 알려주지 않은 문제
# 예외를 처리하는 식으로 해야하는 문제이다.
# while True:
#     try:
#         a,b=list(map(int,input().split()))
#         print(a+b)
#         n+=1
#     except:
#         break

# 1110번
# 더하기 사이클
# 직접 풀었지만 이상하게 이해안감
# 0<=N <=99
# 만약 10보다 작으면 0을붙여 두자리수로 만든다  ex 40  ex 26
# 각자리의 숫자를 더한다  ex 4+0 = 4  ex 2+6 =8
# 주어진수 N의 가장 오른쪽 자리수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들수 있다.  ex 4, 4 -> 44    ex 6, 8 -> 68 
# n=int(input())
# a=-1  # 가장 최근 새로운수 
# b=0
# count=0
# c=0 # 앞에서 구한합
# while n!=a:
#     if count==0:  # 처음에만 a에 n값대입
#         a=n
#     if a<10: #만약 10보다 작으면
#         a=a*11 
#         count+=1
#         continue
#     else:
#         pass
#     c=int(str(a)[-1])+int(str(a)[0])  # 각자리의 수를 더한다. 
#     a=int(str(a)[-1]+str(c)[-1]) #N의 가장 오른쪽 자리수
#     count+=1
# print(count)
###### 4단계 while 끝

############ 5단계 1차원 배열유형

# 10818번 문제
# 최소값, 최대값 출력 
# n=int(input())
# arr=list(map(int,input().split()))
# arr.sort()#오른차순

# print(arr[0],arr[len(arr)-1])

# 2562번 문제
# 최댓값
# arr=[]
# ma=0
# maxIndex=0
# for i in range(9):
#     arr.append(int(input()))

# for i in range(9):
#     if arr[i]>ma:
#         maxIndex=i+1
#         ma=arr[i]
# print(ma)
# print(maxIndex)
        
        
# 2577번 문제
# 숫자의 개수
# 혼자품 str로 바꾼다는게 꽤 중요하다고 생각됨

# a=int(input())
# b=int(input())
# c=int(input())
# d= a*b*c
# st=str(d)

# arr=[0 for i in range(10)]
# for i in range(10):  # 각 숫자 마다 반복
#     for j in range(len(st)):  # 계산된 값 숫자마다 반복
#         if int(st[j])==int(i):  # 
#             arr[i]+=1
# for i in range(10):
#     print(arr[i])
            
            
            
# 3052번 문제
# 나머지 
# set() 을 생각못해서 못 풀었었음

# arr=set()  # set() 으로 중복되는 요소를 제거     # 집합자료형은 중복되는 수를 하나로 본다.
# for i in range(10): # 10번반복
#     n=int(input())   # 한번씩 입력받을 수
#     arr.add(n%42)
# print(len(arr))
    
# 1546 문제
# 평균    

# n= int(input())
# arr=list(map(int,input().split()))
# m=0
# ma=max(arr)
# sum=0
# avg=0

# for i in range(n): # 값 조작
#     arr[i]=arr[i]/ma*100
# for i in range(n):
#     sum+=arr[i]
# avg=sum/n
# print(avg)
    
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
    
############ 1차원 배열 끝
############ 6단계 함수

# 15596번 
# 정수 N개의 합

# def solve(a):   #  a는 리스트
    
#     n=len(a)  # 
#     su=0
#     for i in range(n):
#         su+=a[i]
    
#     return  su # a 에 포함되어 있는 정수 n개의 합(정수)
# print(solve([1,2,3,4,5]))

# 4673
# 셀프 넘버
# 처음에 문제를 제대로 안봐서 애먹었음
# def solve(n):  # solve(75) = 75 + 7 + 5 = 87
#     m=0
#     nstr=str(n)  # 자리수를 인덱스로 나눈다
#     if len(nstr)==1:  # 한자리수
#        m=n+n 
#     elif len(nstr)==2:  # 두자리수
#        m=n+int(nstr[0])+int(nstr[1]) 
#     elif len(nstr)==3:  # 세자리수
#        m=n+int(nstr[0])+int(nstr[1])+int(nstr[2])
#     elif len(nstr)==4:  # 네자리수
#        m=n+int(nstr[0])+int(nstr[1])+int(nstr[2])+int(nstr[3])
#     return m
# # 문제에서 요구하는 것은 생성자 즉 solve로 값이 한번이라도 나오는 값은 뺴고 나머지를 출력해야함
# # 즉 차집합을 구하자
# # s1- s2 또는 s1.difference(s2)  이런식으로 표현가능
# s=set(i for i in range(10001))
# for i in range(1,10001):
#     s.discard(solve(i))  # 집합에 생성자가 한번이라도 포함되면 제거
# for i in range(1,10001):
#     if i in s:
#         print(i)

##### 1065번 한수
# 정수 X의 각 자리가 등차수열을 이루면 그 수를 한수라고 한다.
# 두자리수는 다 한수다
# 세자리부터 비교하면 된다
# n=int(input())  # 알아야할 한수의 범위를 알려줄 수
# num=0 
# for i in range(1,n+1):
#     nArray=list(map(int,str(i)))   # 그 수의 각자리를 비교하기 위해 각자리를 분리
#     if i < 100:
#         num+=1  # 한수 맞으니 카운트
#     elif nArray[0]-nArray[1]==nArray[1]-nArray[2]:
#         num+=1
# print(num)

######## 6단계 함수 끝

######## 7단계 문자열
# 11654 번
# 아스키 코드

# a=input()
# print(ord(a))

# 11720 번
# 숫자의 합

# n = int(input())
# a = int(input())
# sum=0

# for i in range(len(str(a))):
#     sum+=int(str(a)[i])
# print(sum)

# 10809 번
# 알파벳 찾기
# 답지보았지만 다시 내 방법으로 품
# ord() 의 반대는 chr() 이라는 것을 몰랐음

# a가 97
# a=input()
# i='a'  # 97   ord('a')  # 97
# # 
# a.find('a')  #이러면 a 위치는 나옴
# a.find('b')
# for i in range(26):
#     print(a.find(chr(i+97)),end=' ')

# 2675 번
# 문자열 반복
# t = int(input())
# for i in range(t):
#     a,b=list(map(str,input().split()))  #
#     for z in range(len(b)):  # 글자수 만큼 반복
#         for j in range(int(a)):  # 입력받은 값 만큼 반복
#             print(b[z],end='')
#     print("")
    
# 1157번
# 단어 공부


# 중복되면 ? 출력
a=input()

a.count('i')

for i in range(52):  # 대소문자 반복
    



######## 8단계 기본수학1 

# 1712번 문제
# 손익분기점
#
# a,b,c = list(map(int,input().split()))
# d = c - b  # 한번 팔떄 수익
# sum=0
# count=0

# if d<= 0:  # 진짜로 손해보는장사
#     print(-1)
# else:
#     print(a//d+1)


# 2292번 문제
# 벌집
# 답지봄
# room_no = int(input())
# if room_no == 1:  # 시작지 그대로일때 한번
#     print(1)
# else:
#     i = 1  # room과 비교할 수 
#     n = 0  # 한 바퀴마다 1씩오름
#     while room_no > i:
#         n += 1
#         i += 6 * n
#     print(n + 1)

# 1193번 문제
# 분수찾기
# 답지봄
##########################################################################################################
# n=int(input())
# sum=0
# orda=0
# ordb=0
# for i in range(1,n+1):
#     sum+=i
#     if sum>=n:
#         orda=i
#         ordb=n-(sum-i)
#         break
# a=0
# b=0
# if orda%2!=0:
#     a=orda+1
#     b=0
#     for j in range(ordb):
#         a-=1
#         b+=1
# elif orda%2==0:
#     a=0
#     b=orda+1
#     for j in range(ordb):
#         b-=1
#         a+=1
# print(a,"/",b,sep="")




######### 10단계 재귀방식 시작
# 팩토리얼 구현하기
# 입력








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
    
