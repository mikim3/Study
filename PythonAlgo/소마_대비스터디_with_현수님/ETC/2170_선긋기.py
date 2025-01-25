# 시작시간 2212 마무리시간 2245
# 답봄

# 선이 겹쳐지면 길이에 포함 안돼야함


n = int(input())
# 선분의 좌표를 저장할 리스트 (각 선분은 (시작점, 끝점) 형태의 튜플로 저장됨)
lines = []
for _ in range(n):
  lines.append(tuple(map(int, input().split())))

# 선분을 시작점을 기준으로 오름차순으로 정렬
# 시작점이 같다면 끝점을 기준으로 정렬됨
lines.sort()

# 현재 처리 중인 선분들에 시작점(left)과 끝점(right)
left = lines[0][0] # 첫 번째 선분의 시작점
right = lines[0][1] # 첫 번째 선분의 끝점

# 중복을 제거한 전체 선의 길이를 저장할 변수
ans = 0

# 두 번째 선분부터 반복하여 처리
for i in range(1,n):
    # 현재 선분의 끝점이 이전 선분의 끝점보다 작거나 같으면, 중복되므로 무시
  if right >= lines[i][1]:
    continue
  # 현재 선분이 이전 선분과 겹쳐 있으면, 겹친 부분을 확장
  elif lines[i][0] <= right < lines[i][1]:
    right = lines[i][1]
  # 현재 선분이 이전 선분과 전혀 겹치지 않으면, 이전 선분의 길이를 결과에 추가하고 갱신
  elif right < lines[i][0]:
        ans += right - left  # 이전 선분의 길이를 추가
        left = lines[i][0]  # 새로운 선분의 시작점으로 갱신
        right = lines[i][1]  # 새로운 선분의 끝점으로 갱신

ans += right - left
print(ans)


