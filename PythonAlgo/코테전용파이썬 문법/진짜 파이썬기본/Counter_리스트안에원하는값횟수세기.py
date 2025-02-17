from collections import Counter

# 예시 리스트
some_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

counter = Counter(some_list)

print(counter)
print(counter['apple'])
print(counter['appleegg'])

print(counter.most_common())
print(counter.get('apple'))
