
# 서로 다른 두개의 리스트를 탐색하는 두 개의 포인터로 탐색하는 문제
# ▣ 입력예제
# 3
# 1 3 5
# 5
# 2 3 6 7 9
# ▣ 출력예제
# 1 2 3 3 5 6 7 9

n = int(input())
li1 = list(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))
# 인덱싱으로 쓰일 두개의 포인터
p1 = p2 = 0
# 반환값이 될 오름차순으로 넣을 리스트
res = []

# p1 또는 p2 가 범위 안에 있는 동안  두개의 포인터로
# 탐색을 반복
while p1 < n and p2 < m:
    if li1[p1] <= li2[p2]:
        res.append(li1[p1])
        p1 += 1
    else:
        res.append(li2[p2])
        p2 += 1
if p1 < n:
    res = res + li1[p1:]
if p2 < m:
    res = res + li2[p2:]
print(res)
for i in range(len(res)):
    print(res[i])
