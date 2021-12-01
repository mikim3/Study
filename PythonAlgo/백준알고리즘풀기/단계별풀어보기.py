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
n,k=list(map(int,input().split()))
moneyKind=[]

print(n,k)

for i in range(n):
    moneyKind[i]=int(input())
    
for i in range(n-1,-1,-1):
    
    

    
    
