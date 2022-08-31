# 시작시간: 10:36  종료시간:  11:02

# 3가지 과정으로 나눠서 생각할 수 있다.

# 1단계: n-1개의 원판을 2번막대로 옮긴다.

# 2단계: 남은 1개의 원판을 1번 막대에서 3번 막대로 옮긴다.

# 3단계: n-1개의 원판을 2번 막대에서 3번 막대로 옮긴다.

def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return
    hanoi_tower(n-1, start, 6-start-end)  # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end)  # 3단계   

n = int(input())

print(2**n-1)
hanoi_tower(n , 1 , 3)