# 없는 숫자 더하기


def solution(numbers):
    answer = 0
    nums0_9 = [0,1,2,3,4,5,6,7,8,9] 
    
    for i in range(len(nums0_9)):
        if nums0_9[i] not in numbers:
            answer += nums0_9[i]

    return answer

print(solution([1,2,3,4,6,7,8,0]))


# 굉장히 간단한 코드

# def solution(numbers):
#     return 45 - sum(numbers)
