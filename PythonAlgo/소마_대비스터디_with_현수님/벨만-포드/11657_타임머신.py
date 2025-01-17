# 시작시간
# 사실상 답봄

def bellman_ford(num_nodes, edges, source_node):
    # 거리 초기화 (무한대 값으로 초기화)
    INF = float('inf')
    distances = [INF] * (num_nodes + 1)
    distances[source_node] = 0

    # 모든 간선을 반복 (최단 거리 갱신)
    for _ in range(num_nodes - 1):
        for start_node, end_node, weight in edges:
            # 유효한 범위 내에서 최단 거리 갱신
            if distances[start_node] != INF and distances[start_node] + weight < distances[end_node]:
                distances[end_node] = distances[start_node] + weight

    # 음수 사이클 검출
    for start_node, end_node, weight in edges:
        if distances[start_node] != INF and distances[start_node] + weight < distances[end_node]:
            return -1  # 음수 사이클 발견 시 -1 반환

    # 결과 반환
    return distances

# 시작 노드
start = 1
edges = []
# 노드 개수와 간선 개수
n, m = map(int, input().split())
# 간선 정보: (시작 노드, 끝 노드, 가중치)
for i in range(m):
  edges.append(tuple(map(int, input().split())))

# 벨만-포드 실행
result = bellman_ford(n, edges, start)

if result == -1:
    print(-1)  # 음수 사이클이 존재
else:
    # 결과 출력
    for i in range(2, n + 1):
        if result[i] == float('inf'):
            print(-1)  # 도달할 수 없는 경우
        else:
            print(result[i])
            
