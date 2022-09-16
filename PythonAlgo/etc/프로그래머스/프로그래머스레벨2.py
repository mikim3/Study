#  결국 못품
# 문자열 함수로 바꾸는 문제

def solution(str1, str2):
    str1=str1.upper()
    str2=str2.upper()
    strset1=set()
    strset2=set()
    answer = 0

    #  isalnum()  함수 - 문자열의 모든 요소가 문자 또는 숫자인 경우 True 단 공백도 제거    
    ntitle=''
    for c in str1:
        if c.isalnum():
            ntitle+=c
    print(ntitle)
    
    
    # 집합 만들기
    for i in range(len(str1)-1):
        strset1.add(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        strset2.add(str2[i]+str2[i+1])
    
    a=strset1 & strset2
    b=strset1 | strset2
    
    print(len(a)/len(b)*65536)
    
        
    return answer

str1="aa1+aa2"
str2="AAAA12"

print(solution(str1,str2))

