#
def solution(n,map1,map2):
    answer = []
    
    for i in range(n):
        tmp = bin(map1[i] | map2[i])
        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace('1','#').replace('0',' ')
        answer.append(tmp)
    
    return answer




n = int(input())

map1 = list(map(int, input().split()))
map2 = list(map(int, input().split()))
print(solution(n,map1,map2))

