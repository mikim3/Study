# 내 답

# def solution(s):
#     li = list()
#     answer = ''
#     li= s.split(' ')
    
#     for i in range(len(li)):
#         s2 = li[i]
#         for j in range(len(li[i])):
#             if j % 2 == 0:
#                 answer+=s2[j].upper()
#             else:
#                 answer+=s2[j].lower()
#         if i != len(li)-1:
#             answer+=' '
#         else:
#             pass
#     print(answer)
#     return answer

# join 써보기
def solution(s):
    li = list()
    answer = ''
    li= s.split(' ')
    
    for i in range(len(li)):
        s2 = li[i]
        for j in range(len(li[i])):
            if j % 2 == 0:
                answer+=s2[j].upper()
            else:
                answer+=s2[j].lower()
        if i != len(li)-1:
            answer+=' '
        else:
            pass
    print(answer)
    return answer
