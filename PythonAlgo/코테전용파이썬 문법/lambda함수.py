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