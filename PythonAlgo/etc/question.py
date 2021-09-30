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
print("구구단 문제")
a,b= list(map(int,input().split()))  # 시작과 처음을 띄어쓰기로 나눠서 받습니다.
for i in range(a,b+1):
    for j in range(1,10):
        print(i,"X",j,"==",i*j)

#  50부터 100까지의 정수 중에서 3의 배수만 더하는 프로그램 while 문으로 작성하시오
print("3의배수만 더하기 문제")

a=50  #50부터 시작하는 정수
sum=0 # 더하는 값을 저장할 변수

while a<=100:
    if a%3==0:  # 3의 배수 조건을 표현
        sum+=a 
    print(sum)
    a+=1  # a=a+1 과 같습니다 I'm  I am
print(sum) #출력하라는 말 없지만 없으면 허젼하니까 더함



