# 현재 읽은 것과 다음것이 값이 같으면 
def solution(s):
    # 그냥 원문 s의 길이를 기본으로 넣기
    answer = len(s)
    # unit 은 자를 한칸의 크기
    # 한칸의 크기가 원본의 반을 넘길수는 없음 (len(s)//2 + 1)
    for unit in range(1, len(s)//2 + 1):
        # 유닛으로 완성될 문자열을 의미
        res = ""
        cnt = 1
        # 현재 잘려있는 칸을 의미할 temp 
        temp = s[0:unit]
        # unit을 한칸으로 자르기
        # unit만큼 건너띄고 시작해야함
        for index in range(unit, len(s) + unit, unit):
            if temp == s[index: index + unit]:  # 겹칠떄
                cnt+=1
            else: # 안 겹치기 시작했을때
                if cnt == 1: # 현재 문자가 겹치는게 없을떄
                    res+=temp
                else: # 안 겹치기 시작했지만 그전에 몇개 겹쳤을떄 
                    res+=str(cnt) + temp
                temp = s[index: index + unit]
                cnt = 1
                print(temp)
        # 그 전 값들과 비교하여 가장 짧아야지 answer
        print(answer)
        answer = min(answer, len(res))
    return answer
data = input()
print(solution(data))

    
    
    


