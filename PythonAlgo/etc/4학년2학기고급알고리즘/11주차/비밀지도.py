# 두개의 지도를 받아서 
# OR연산이 떠오르는 문제

def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    for i in range(n):
        arr1_bin.append(bin(arr1[i])[2:])
        arr2_bin.append(bin(arr2[i])[2:])
        arr1_bin[i] = ('0' * (n-len(arr1_bin[i]))) + arr1_bin[i]
        arr2_bin[i] = ('0' * (n-len(arr2_bin[i]))) + arr2_bin[i]

        # print(('0' * (n-len(arr1_bin[i]))))
        print(arr1_bin)
        
        tmp = ''
        for p in range(n):
            if arr1_bin[i][p] == '1' or arr2_bin[i][p] == '1':
                tmp += '#'
            elif arr1_bin[i][p] == '0' and arr2_bin[i][p] == '0':
                tmp += ' '
        answer.append(tmp)
        
    return answer

n = int(input())

map1 = list(map(int, input().split()))
map2 = list(map(int, input().split()))


print(solution(n,map1,map2))

