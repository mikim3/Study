

def solution(board, moves):
    bucket = []
    answer = []
    print("len borad",len(board))
    for move in moves:
        for i in range(len(board)):
            # board[i][move-1] 의 값은 해당 좌표의 i는 행  move-1은 열을 뜻한다.  i 가 값이 증가함에 따라 집게가 1칸씩 내려가는 것이다. 
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    answer += bucket[-1:]
                    bucket = bucket[:-2]
                break
    return len(answer)*2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
