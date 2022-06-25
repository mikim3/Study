# 숫자 문자열과 영단어


# 만약 문자면 dict중에 있는지 확인하고 다음글자 읽고를 반복해서 
# 그 문자를 키로 넣어서 원하는 value를 얻는다.


def solution(s):
    num_dict = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
    }

    result = ""
    sen = ""
    for i in range(len(s)):
        if s[i].isdigit():
            result += s[i]
        elif s[i].isalpha():
            # 문자를 하나씩 넣어서 단어 하나를 만듬
            sen += s[i]
            if sen in num_dict.keys():
                result += str(num_dict[sen])
                sen = ""
    result=int(result)
    return result

# 다른사람이 푼 진짜 경이로운 답

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))


