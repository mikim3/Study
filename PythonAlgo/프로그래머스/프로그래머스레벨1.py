
#################### 레벨 1

# def solution(n):   # 약수를 구할값
#     answer = 0  # 약수를 모두 더한 값을 넣을값
#     arr=[]
#     for i in range(1,n+1,1):
#         if n%i==0:
#             arr.append(i)
#     for i in range(len(arr)):
#         answer+=arr[i]
    
#     return answer
# # n=int(input())  # 입력받기
# # print(solution(n))


# 문제 2 
# def solution(numbers):  # 배열 numbers
#     answer = 0  #   반환값
#     numbers
    
#     for i in range(0,10):
#         if i not in numbers:
#             answer+=i
    
    
#     return answer

###################### 레벨 2
# 소문자를 전부 대문자로 바꾼다
# 특수문자등 알파벳이 아닌것을 전부 없앤다.
# 


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

