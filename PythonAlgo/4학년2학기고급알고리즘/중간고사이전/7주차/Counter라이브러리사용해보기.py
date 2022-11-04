from collections import Counter

cnter = Counter(['red','blue','red','green','blue','blue'])

print(cnter['blue']) # 'blue' 가 등장한 횟수 출력
print(cnter['green']) # 'green' 이 등장한 횟수 출력
print(dict(cnter)) # 사전 자료형으로 반환
