# 왕실의 나이트 문제 
# 

# 못 풀었음 나중에 풀어보기

# # 현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# #8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     #해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result +=1

# print(result)

# 왕실의 나이트 문제 
# result=0  # 이동가능한 위치
# location=input()
# x = int(location[1]) # a1 에서 1 
# y = ord(location[0])-ord('a')+1 # a 를 넣으면 1

# #나이트가 이동 8가지 정의
# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# # 
# result = 0
# for step in steps:
#     #이동할 다음 위치
#     next_x=x+step[0]
#     next_y=y+step[1]
#     #
#     if next_x>=1 and next_x<=8 and next_y>=1 and next_y<=8:
#         result+=1

# print(result)


