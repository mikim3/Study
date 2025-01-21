# 시작시간 2053  마무리시간
import sys
input = sys.stdin.readline
# 노드 수, 간선 수
v, m = map(int,input().strip().split())
li = [[9999999]*(v+1) for _ in range(v+1)]
for i in range(m):
  a, b, c = map(int,input().strip().split())
  li[a][b] = c
# 지헌 , 성하
j, s = map(int,input().strip().split())

# 지헌이가 걸리는 최단시간과 성하가 걸리는 최단시간 합이 최소
# 지헌이가 성하보다 빠르거나 동시에 도착해야함
# 만족하는게 여러곳이면 지헌이로부터 가장 가까운 곳이 최종 약속 장소
# 그런 곳도 여러개면 그 중 가장 작은 번호

# 풀이법
# 지헌 입장 플로이드 워셜 구하기
# 성하 입장 플로이드 워셜 구하기
# 그 상태에서 문제의 조건에 맞는 위치 찾기
# 

