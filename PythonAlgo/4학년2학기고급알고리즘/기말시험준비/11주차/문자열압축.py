

def solution(s):
    answer = len(s)
    
    for unit in range(1, len(s) // 2 + 1):
        
        res = ""
        cnt = 1
        
        temp = s[0:unit]
        
        for index in range(unit, len(s) + unit, unit):
            if temp == s[index: index + unit]:
                cnt += 1
            else:
                if cnt == 1:
                    res+=temp
                else:
                    res += str(cnt) + temp
                temp = s[index: index + unit]
                cnt = 1
        
        answer = min(answer, len(res))
    return answer
        
        
data = input()
print(solution(data))
       


