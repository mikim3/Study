# 시작시간  마무리시간

# 단계들 총합

# 베이컨 가장 작은 사람 출력 겹치면 번호가 작은 사람 출력

import sys
input = sys.stdin.readline

def find_kevin_bacon(n, m, relationships):
    # 무한대 값 정의
    INF = sys.maxsize

    # 그래프 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로의 거리는 0으로 설정
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 친구 관계 추가
    for a, b in relationships:
        graph[a][b] = 1
        graph[b][a] = 1

    # 플로이드-워셜 알고리즘 적용
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # 케빈 베이컨 수 계산 및 최솟값 찾기
    min_bacon = INF
    person = -1

    for i in range(1, n + 1):
        bacon_sum = sum(graph[i][1:])
        if bacon_sum < min_bacon:
            min_bacon = bacon_sum
            person = i

    return person

# 입력 처리

n, m = map(int, input().split())
relationships = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 출력
print(find_kevin_bacon(n, m, relationships))
