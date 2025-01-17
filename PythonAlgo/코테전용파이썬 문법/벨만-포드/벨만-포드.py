# 벨만-포드 알고리즘!!!!!!!

# 특정 출발점에서 다른 모든 정정으로 가는 최단거리를 계산하는 알고리즘(음수가중치가 있어도 작동)

# 1. 시작 노드로부터 모든 노드의 거리를 무한대로 초기화 한다.  (시작노드는 거리 0으로 설정)
# 2. 모든 간선에 대해 N-1번 반복하여 거리를 갱신
#  a. 어떤 간선 (출발노드, 목적노드, 가중치) 이 있을때 distances[출발노드] + 가중치 < distances[목적노드] 라면 distances[목적노드] 갱신
# 한 번 더 모든 간선을 확인하는데 만약 거리가 갱신된다면 그것은 음수 사이클이 존재한다는 뜻 입니다. (음수사이클: 여러번 돌수록 값이 점점 낮아지는 사이클)
# 



# N-1번 반복: 최단 거리 갱신 (최단 경로를 보장).
# 추가 1번 반복: 음수 사이클 존재 여부 확인.
# 시간 복잡도: O(N * M) (N은 노드 수, M은 간선 수).


def bellman_ford(num_nodes, edges, source_node):
    """
    num_nodes: 노드(정점)의 개수
    edges: 간선 정보 리스트 (start_node, end_node, weight) 형태
    source_node: 시작 노드
    """
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

print(edges)
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
            
# 입력
# 3 4
# 1 2 4
# 1 3 3
# 2 3 -1
# 3 1 -2
# 출력
# 4
# 3

# 입력
# 3 4
# 1 2 4
# 1 3 3
# 2 3 -4
# 3 1 -2
# 출력
# -1

# 입력
# 3 2
# 1 2 4
# 1 2 3
# 출력
# 3
# -1
