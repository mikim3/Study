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

# for i in range(5):
#     score = int(input("점수 : "))  # 점수입력
#     if score>=max:  #현재 최고점보다 점수가 높으니까 현제점수는== 최고점
#         max=score
#     if score<=min:
#         min=score

print("최고점= ",max,"최저점= ",min)


#
class Figure:
    def __init__(self,diameter):
        self.diameter = diameter  # __init__ 으로 만든 변수는 객체변수이다.  객체변수는 다른 객체들에 영향을 받지 앟고 독립적인 값을 유지한다.
        
class Circle(Figure):  # Circle 클래스는 Figure클래스를 상속한다. 즉 Figure의 기본적인 기능을 이용할 수 있다.  Circle은 자식 Figure는 부모   자식은 부모의 능력을 물려받는다.
    def getKind(self):
        return 'I\'m a circle.'
    def getArea(self):
        radius = self.diameter
        return radius * radius * 3.14
    def __add__(self, other):  # __add__ 는 파이썬에 내장된 특수한 함수이다.  클래스에 + 연산을 할때 함수가 발동된다.
        if isinstance(other,Circle):
            return Circle(self.diameter+other.diameter)
        elif isinstance(other,int):
            return Circle(self.diameter + other)
class Square(Figure):
    def getKind(self):
        return 'I\'m a Square.'
    def getArea(self):
        return self.diameter * self.diameter
    def __add__(self, other):
        if isinstance(other,Square):
            return Square(self.diameter+other.diameter)
        elif isinstance(other,int):
            return Square(self.diameter + other)

figures = [Circle(5), Square(5)]
for figure in figures: # 첫번째로 Circle(5)로 한바퀴 돌고 다음 Square(5) 
    figure= figure + 5
    print(figure.getKind()+' : '+str(figure.getArea()))
