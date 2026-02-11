# 시작 260204 1500 마무리 1505

n = int(input())
li1 = list(map(int,input().split()))
m = int(input())
li2 = list(map(int,input().split()))
li3 = sorted(li1+li2)
for i in range(len(li3)):
    print(li3[i],end=' ')


# 250113 또풀기
# 이번에는 투포인터로 풀기

# n = int(input())
# li1 = list(map(int, input().split()))
# m = int(input())
# li2 = list(map(int, input().split()))
# # 인덱싱으로 쓰일 두개의 포인터
# p1 = p2 = 0
# # 반환값이 될 오름차순으로 넣을 리스트
# res = []

# p1 또는 p2 가 범위 안에 있는 동안  두개의 포인터로
# 탐색을 반복
# while p1 < n and p2 < m:
#     if li1[p1] <= li2[p2]:
#         res.append(li1[p1])
#         p1 += 1
#     else:
#         res.append(li2[p2])
#         p2 += 1
# if p1 < n:
#     res = res + li1[p1:]
# if p2 < m:
#     res = res + li2[p2:]
# print(res)
# for i in range(len(res)):
#     print(res[i])


# 0503  19:50 시작 19:54 매무리

# n = int(input())
# li_n = list(map(int,input().split()))

# m = int(input())
# li_m = list(map(int,input().split()))

# li = li_m + li_n

# li.sort()
# for i in range(len(li)):
#     print(li[i],end=' ')


# # 12 39
# # 4분걸림

# n = int(input())

# li1 = list(map(int,input().split()))


# m = int(input())

# li2 = list(map(int,input().split()))

# li3 = li1 + li2
# li3.sort()

# for i in range(n+m):
#     print(li3[i],end=' ')

