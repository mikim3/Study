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


