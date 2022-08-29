# 재귀로 N부터 1까지 출력하는 함수와   1부터 N까지의 합을 리턴하는 함수
def jegi1(a):
    if a == 0:
        return 
    print(a)
    return jegi1(a-1)    
def jegi2(a):
    if a == 0: 
        return 0
    return a + jegi2(a-1)

jegi1(3)
print(jegi2(3))
