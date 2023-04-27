# 두개의 지도를 받아서 
# OR연산이 떠오르는 문제

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        # 2진수로 바꾼다.
        tmp = bin(arr1[i] | arr2[i])
        # print(tmp)
        # tmp결과 ex) '0b1101'
        tmp = tmp[2:].zfill(n) # n개 이상 자릿수가 아니면 0으로채움
        # tmp결과 ex) '01101'
        tmp = tmp.replace('1','#').replace('0',' ')
        # tmp결과 ex) ' ## #'
        answer.append(tmp)
    
    return answer

n = int(input())

map1 = list(map(int, input().split()))
map2 = list(map(int, input().split()))
print(solution(n,map1,map2))

