items = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_items = sorted(items, key=lambda x: (x[0], -x[1]))
print(sorted_items)

words = ["banana", "apple", "cherry", "date"]
words.sort(key=lambda x: (len(x)))
print(words)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"{self.name}: {self.grade}"

students = [Student("John", 88), Student("Daisy", 92), Student("Alex", 90), Student("George", 88)]
sorted_students = sorted(students, key=lambda x: -x.grade)
print(sorted_students)

#################################
# 사실 람다를 쓰지 않으면 다음과 같이 쓰면 된다. 람다 함수도 함수다 함수 들어 올 곳에 lambda를 썼을 뿐이다.
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

# 방법 1 : 함수를 정의한 후 key 값에 넣어주기
def setting(data):
    return data[1]      # 인덱스 1에 위치한 원소가 반환된다 (key 값 = 2, 5, 3)

result = sorted(array, key = setting)
print(result)

# 방법 2 : 람다함수를 key 값에 넣어주기
result = sorted(array, key = lambda data: data[1])
print(result)
