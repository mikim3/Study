
# 현재 읽은 것과 다음것이 값이 같으면 
def solution(s):
    answer = len(s)
    # unit 은 자를 한칸의 크기
    for unit in range(1,len(s)//2 + 1):
        # 완성될 문자열을 의미
        res = ""
        cnt = 1
        # 현재 잘려있는 칸을 의미할 temp
        temp = s[0:unit]
        # unit을 한칸으로 자르기
        for index in range(unit, len(s) + unit, unit):
            if temp == s[index: index + unit]:
                cnt+=1    
            else:
                if cnt == 1:
                    res+=temp
                else:
                    res+=str(cnt) + temp
                temp = s[index: index + unit]
                cnt = 1
        # 그 전 값들과 비교하여 가장 짧아야지 answer
        answer = min(answer, len(res))
    return answer
data = input()
print(solution(data))

    
    
    


