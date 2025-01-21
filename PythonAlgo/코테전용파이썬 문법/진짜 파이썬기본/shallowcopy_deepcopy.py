import copy

# 원본 리스트
original = [1, [2, 3], 4]

# 얕은 복사
shallow_copy = original.copy()

# 얕은 복사 후 데이터 변경
shallow_copy[1][0] = 99  # 중첩된 리스트의 값을 변경
shallow_copy[0] = 100    # 첫 번째 레벨 값 변경

print("Original:", original)  # [1, [99, 3], 4] -> 중첩 객체는 원본과 연결되어 있음
print("Shallow Copy:", shallow_copy)  # [100, [99, 3], 4]

import copy

# 원본 리스트
original = [1, [2, 3], 4]

# 깊은 복사
deep_copy = copy.deepcopy(original)

# 깊은 복사 후 데이터 변경
deep_copy[1][0] = 99  # 중첩된 리스트의 값을 변경
deep_copy[0] = 100    # 첫 번째 레벨 값 변경

print("Original:", original)  # [1, [2, 3], 4] -> 완전히 독립적
print("Deep Copy:", deep_copy)  # [100, [99, 3], 4]
