from collections import deque

# 4, 4
# 빨간 파랑

def find_paths(maze, start, end):
    n, m = len(maze), len(maze[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    paths = []
    queue = deque()
    queue.append((start, [start]))
    #
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            paths.append(path)
            continue
        for dx, dy in directions:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < n and 0 <= next_y < m and maze[next_x][next_y] != 5 and (next_x, next_y) not in path:
                print('queue before', queue)
                queue.append(((next_x, next_y), path + [(next_x, next_y)]))
                print('queue after', queue)
    return paths

def solution(maze):
    rows, cols = len(maze), len(maze[0])
    red_start, blue_start, red_end, blue_end = None, None, None, None

    # 시작점 끝점 찾기
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_end = (i, j)
            elif maze[i][j] == 4:
                blue_end = (i, j)

    # 빨강 수레, 파랑 수레
    red_paths = find_paths(maze, red_start, red_end)
    blue_paths = find_paths(maze, blue_start, blue_end)
    # print('red_paths == 'red_paths)

    # 최소비용
    min_turns = float('inf')
    # 최소비용을 위한 비교
    for red_path in red_paths:
        for blue_path in blue_paths:
            collision = False
            max_length = max(len(red_path), len(blue_path))
            print('red_path == ', red_path, 'blue_path == ', blue_path)
            # red_path[몇번째 턴인지] = 현 위치   # 턴이 빨강이 먼저 끝나면 red_path의 마지막 위치까지만 인덱스로 씀
            for turn in range(max_length):
                red_pos = red_path[min(turn, len(red_path)-1)]
                blue_pos = blue_path[min(turn, len(blue_path)-1)]
                # 현재 턴 위치에서 부딪히는 상황 조건
                # red_pos == blue_path[min(turn-1, len(blue_path)-1)]
                if red_pos == blue_pos or (turn > 0 and red_pos == blue_path[min(turn-1, len(blue_path)-1)] and blue_pos == red_path[min(turn-1, len(red_path)-1)]):
                    collision = True
                    break
            if collision == False:
                min_turns = min(min_turns, max_length)
    if min_turns != float('inf'):
      return min_turns - 1
    else:
      return 0

example1 = [[1, 4], [0, 0], [2, 3]]
example2 = [[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]
example3 = [[1, 5], [2, 5], [4, 5], [3, 5]]
example4 = [[4, 1, 2, 3]]

print(solution(example1))
print(solution(example2))
print(solution(example3))
print(solution(example4))
