
# 답봄

def solution(s):
    # 길이들이 저장돼있는 리스트
    result = []
    
    # 문자길이 1이면 그냥 1 반환
    if len(s) == 1:
        return 1
    
    # 몇 개로 쪼갤지를 i 로 정한다. 
    for i in range(1, (len(s)//2)+1):
        b = ''
        # 문자열이 연속되는지 확인하는 함수
        cnt = 1
        # 쪼갤때의 처음부분을 tmp에 넣어준다.
        tmp = s[:i]
        print(tmp,"tmp")
        # j 는 i 부터 시작하고 2씩 건너뛴다. j =i ,2i 가다가 s전까지 된다.
        for j in range(i, len(s), i):
            # tmp는 전에 있는 글자
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b  + tmp
                tmp = s[j:j+i]
                cnt = 1
        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp
            
        result.append(len(b))
        print("b",b)
    return min(result)


print(solution(	"aabbaccc"))
# print(solution(	"ababcdcdababcdcd"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("abcabcabcabcdededededede"))
