# 답봄
# 쓸모있는 테크닉 다시 풀어봐

from collections import deque

def puzzle_solver(start: str):
  goal = '123456780'  # 목표 상태
  dx = [-1, 1, 0, 0]  # 상하좌우 이동
  dy = [0, 0, -1, 1]
  visited = set()
  queue = deque()

  queue.append((start.index('0'), start, 0))  # (빈 칸 위치, 현재 상태, 이동 횟수)
  visited.add(start)

  while queue:
    pos, state, cnt = queue.popleft()

    if state == goal:
      return cnt

    x = pos // 3  # 행
    y = pos % 3   # 열

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < 3 and 0 <= ny < 3:
        npos = nx * 3 + ny  # 새로운 빈 칸 위치
        # 빈 칸과 선택한 숫자 교환
        list_state = list(state)
        list_state[pos], list_state[npos] = list_state[npos], list_state[pos]
        next_state = ''.join(list_state)

        if next_state not in visited:
          visited.add(next_state)
          queue.append((npos, next_state, cnt + 1))

  return -1  # 목표 상태에 도달할 수 없는 경우

# 입력 처리
start_state = ''
for _ in range(3):
    row = input().strip().split()
    for num in row:
        if num == '0':
            start_state += '0'
        else:
            start_state += num

# 결과 출력
result = puzzle_solver(start_state)
print(result)



# # 시작시간  2301   마무리시간 
# from collections import deque
# # 딱봐도 시간복잡도는 막 풀어도 됨

# # 최소이동으로 정리된 상태 만들기

# # 인접한 칸중에 빈칸만 이동가능
# # 즉 0과 인접한 다른 수만 이동가능


# li = []
# for i in range(3):
#   li.append(list(map(int, input().split())))

# # 빈칸
# # 0 오른쪽 아래까지 가는 경로 중에 답이 없으면 
# # 그건 -1

# # 현재 위치에서 2,2 까지 이동 해야함

# # 2,2까지가는 돌아가지 않는 모든 경로중에 2,2까지 가고 나니까 자연스럽게
# # 정렬 되는 경우가 있으면 그것이 옮게된 경우
# # 

# def bfs(x,y):
#   queue = deque()
#   queue.append((x,y))
#   checked[x][y] = 1
#   while queue:
#     pass

# # 이동한 경로 체크 # 이동 한 곳으로 또 갈 필요는 없음
# checked = [[0] * 3 for _ in range(3)]

# # 0 1 2
# # 5 6 3
# # 4 7 8

# # 


