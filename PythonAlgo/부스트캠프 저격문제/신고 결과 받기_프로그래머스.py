# 2번이상 신고당하면 정지
# 정지 당한 사람을 신고한 사람은 신고처리 잘됬다고 메일을 받는다.
# 

# defaultdict() 는 딕셔너리를 만드는 dict클래스의 서브클래스이다.
# 작동 방식은 비슷한데  인자로 주어진 객체의 기본값을 딕셔너리의 초깃값으로 지정할 수 있다.
# 숫자, 리스트, 셋등으로 초기화 가능

# 답봄

# def solution(id_list, report, k):
#     answer = []
#     # 중복 신고 제거
#     report = list(set(report))  # set으로 중복제거 하고 다시 list 로 
#     user = defaultdict(set)
    

# return result

# 베스트 답안

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}


    print(reports)

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))





