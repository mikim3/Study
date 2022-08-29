# 키패드 누르기

def solution(numbers, hand):
    result = ''
    dic = {1:[0,0],2:[0,1],3:[0,2],
        4:[1,0],5:[1,1],6:[1,2],
        7:[2,0],8:[2,1],9:[2,2],
        '*':[3,0],0:[3,1],'#':[3,2]
    }

    left_now= '*'
    right_now= '#'

    for i in range(len(numbers)):

        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            left_now = numbers[i]
            result+='L'
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            right_now = numbers[i]
            result += 'R'
        else:
            # 거리계산하고 결정
            #왼손과의 거리계산
            left_d = abs(dic[left_now][0]-dic[numbers[i]][0]) + abs(dic[left_now][1]-dic[numbers[i]][1])
            right_d = abs(dic[right_now][0]-dic[numbers[i]][0]) + abs(dic[right_now][1]-dic[numbers[i]][1])

            if left_d<right_d:
                left_now = numbers[i]
                result +='L'
            elif right_d<left_d:
                right_now = numbers[i]
                result += 'R'
            else: # 거리가 같으면
                if hand == "right":
                    right_now = numbers[i]
                    result += 'R'
                else:
                    left_now = numbers[i]
                    result += 'L'

    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))
print(solution([5, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))

