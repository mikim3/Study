# 답봄

def solution(record):
    answer = []
    dic = {}
    for sentence in record:
        # 문장을 나눈다.
        sentence_split = sentence.split()
        # 나눈 단어들이 엔터또는 체인지면 dic안에 값을 바꾼다.
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]  # 
    for sentence in record:
        sentence_split = sentence.split()
        
        if sentence_split[0] == 'Enter':
            answer.append("%s님이 들어왔습니다." %dic[sentence_split[1]])
        elif sentence_split[0] == 'Leave':
            answer.append("%s님이 나갔습니다." %dic[sentence_split[1]])
    
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))