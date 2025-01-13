from collections import defaultdict

# 람다 함수를 사용하여 기본값을 10으로 설정하는 defaultdict 생성
d = defaultdict(lambda: 10)

# 사용 예시
print(d['a'])  # 'a'에 대한 값이 없으므로, 기본값인 10을 반환
d['b'] = 5
print(d['b'])  # 'b'에 값을 설정했으므로, 5를 반환

# 사용자 정의 기본값 함수
def default_value():
    return 10  # 기본값을 10으로 설정

# defaultdict 생성, 기본값으로 'default_value' 함수 사용
d = defaultdict(default_value)

# 사용 예시
print(d['a'])  # 'a'에 대한 값이 없으므로, 기본값인 10을 반환
d['b'] = 5
print(d['b'])  # 'b'에 값을 설정했으므로, 5를 반환
