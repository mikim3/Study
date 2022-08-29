# 2번이상 신고당하면 정지
# 정지 당한 사람을 신고한 사람은 신고처리 잘됬다고 메일을 받는다.

# defaultdict() 는 딕셔너리를 만드는 dict클래스의 서브클래스이다.
# 작동 방식은 비슷한데  인자로 주어진 객체의 기본값을 딕셔너리의 초깃값으로 지정할 수 있다.
# 숫자, 리스트, 셋등으로 초기화 가능

# 답봄

#

def solution(id_list, report, k):
    # answer 0 으로 초기화
    answer = [0] * len(id_list)    
    # x : 0 으로 키 벨류를 넣는데 x값은 id_list로 넣는다.
    # reports는 '신고당한 사람' : 신고 횟수 가 된다.
    reports = {x : 0 for x in id_list}

    print(reports)

    # reports에 신고당한 사람의 신고 횟수 기록 
    for r in set(report):
        print(r.split()[1])
        reports[r.split()[1]] += 1

    for r in set(report):
        # 신고 횟수가 k보다 높으면
        if reports[r.split()[1]] >= k:
            # id_list의 해당 횟수 인 사람 메일 받는 횟수 1증가
            answer[id_list.index(r.split()[0])] += 1
    return answer


# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     # 중복 제거
#     result = list(set(report))

#     # {신고된 사람 : [신고한 사람]}
#     dict = {}
#     for id in id_list:
#         dict[id] = []

#     # 신고한 유저와 유저가 신고한 아이디 나누기
#     for i in result:
#         show = i.split(" ")
#         dict[show[1]] += [show[0]]

#     for key, value in dict.items():
#         if len(value) >= k:
#             for person in value:
#                 # id_list.index(person) person이 몇번째 인덱스인지 반환
#                 answer[id_list.index(person)] += 1

#     return answer



print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))





