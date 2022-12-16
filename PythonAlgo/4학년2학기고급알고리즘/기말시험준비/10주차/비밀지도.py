def solution(n,arr1,arr2):
    answer = []
    
    for i in range(n):
        # 2진수로 변환
        tmp = bin(arr1[i] | arr2[i])
        # print(tmp) # 0b11111
        # 0b를 때고 자릿수를 맞게 만든다땐다 0으로 시작할 경우 감안하여 zfill()
        tmp = tmp[2:].zfill(5)
        # print(tmp)
        tmp = tmp.replace('1','#').replace('0',' ')

        answer.append(tmp)
    return answer

n = int(input())

map1 = list(map(int, input().split()))
map2 = list(map(int, input().split()))
print(solution(n,map1,map2))
