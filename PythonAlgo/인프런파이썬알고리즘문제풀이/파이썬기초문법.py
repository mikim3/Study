

# 리스트와 내장함수(1)
import random as r

a = list(range(1,7))
print(a)

a.insert(3,7)  # 3번 인덱스에 7 삽입
print(a)

a.pop(3)
print(a)

a.remove(4)  # 4 값 삭제

print(a,"    " ,a.index(5))  # 5는 3번 인덱스에 있다
print(sum(a))
print(max(a))

print(a)
r.shuffle(a)
print(a)
sorted(a)  # 반환값이 정렬된 값
print(a)   
a.sort()  # 해당 리스트를 정렬하는 함수   리스트에 있는 함수  list.sort(reverse=false) 기본값 오름차순이다.
print(a)
a.clear()
print(a)


