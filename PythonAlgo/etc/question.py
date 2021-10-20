#a에는 2진수 8자리 숫자를 넣고 result 변수에는 a의 오른쪽에서 3번째와 4번째 bit가 모두 1이면 True가, 0이면 False가 들어가게 하시오.
a=0b01011110;  # 3,4 번째만 갖고 싶다
result = True
print(bin(a))
print(bin(a & 0b00001100))  # 3,4번쨰는 그대로 나머지 자리는 무조건 0  

if bin(a & 0b00001100) == bin(0b1100):
    result=True
else:
    result=False
print(result)

#구구단 시작하는단과 끝나는단을 입력 화면에 출력하시오
# print("구구단 문제")
# a,b= list(map(int,input().split()))  # 시작과 처음을 띄어쓰기로 나눠서 받습니다.
# for i in range(a,b+1):
#     for j in range(1,10):
#         print(i,"X",j,"==",i*j)

#  50부터 100까지의 정수 중에서 3의 배수만 더하는 프로그램 while 문으로 작성하시오
print("3의배수만 더하기 문제")

a=50  #50부터 시작하는 정수
sumv=0 # 더하는 값을 저장할 변수

while a<=100:
    if a%3==0:  # 3의 배수 조건을 표현
        sumv+=a 
    print(sumv)
    a+=1  # a=a+1 과 같습니다 I'm  I am
print(sumv) #출력하라는 말 없지만 없으면 허젼하니까 더함


# 임의 개수의 숫자를 인자로 받아 이들의 합계와 평균 튜플을 반환하는 함수

def sumavg(*args):
    return sum(args),sum(args)/len(args)

print(sumavg(1,2,3))

#문제 :  0을 입력할 때 까지 소수를 판별해주는 프로그램 작성 
# print("소수판별문제")

# prime=True
# while True:
#     num=int(input("소수 판별할 숫자:"))  #판별할 숫자 num 입력
#     if num==0: # 0 입력시 바로 나가리
#         break
#     for i in range(2,num):  # 1은 건너띄고 나머지중에 나누어지는수 판단
#         if num%i==0:  #만약 i로 나누어지는 수가 하나라도 있으면
#             prime=False  # 소수가 아니다
#     if prime==True:
#         print("소수입니다.")
#     else:
#         print("소수가 아닙니다.")

# 문제 : 5명의 학생을 입력받아 최고점과 최저점을 출력하시오.  0 ~ 100사이 점수만 갖는다.

max,min,score = 0,100,0  # 최고점 최저점 점수 

for i in range(5):
    score = int(input("점수 : "))  # 점수입력
    if score>=max:  #현재 최고점보다 점수가 높으니까 현제점수는== 최고점
        max=score
    if score<=min:
        min=score

print("최고점= ",max,"최저점= ",min)

