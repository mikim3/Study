"""
아래와 같이 입력이 오면 대부분 2차원 배열로 바꿔야지 문제 풀기 쉽다.
board	               result
["O.X", ".O.", "..X"]	1
["OOO", "...", "XXX"]	0
["...", ".X.", "..."]	0
["...", "...", "..."]	1

[['O', '.', 'X'], ['.', 'O', '.'], ['.', '.', 'X']]

참고로 list() 함수는 iterable을 리스트로 변환할수 있고 []는 당연히 아니다.

"""
board1 = ["O.X", ".O.", "..X"]
# board2 = [[row] for row in board1]
board2 = [[row] for row in board1]
print(board2) # [['O.X'], ['.O.'], ['..X']]
board2 = [list(row) for row in board1]
print(board2) # [['O', '.', 'X'], ['.', 'O', '.'], ['.', '.', 'X']]
stst = "hahahaha"
stst_list = [stst]
print(stst_list) # ['hahahaha']
stst_list = list(stst)
print(stst_list)  # ['h', 'a', 'h', 'a', 'h', 'a', 'h', 'a']
