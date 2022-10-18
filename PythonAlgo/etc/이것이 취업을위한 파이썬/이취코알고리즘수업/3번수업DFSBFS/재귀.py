# 재귀함수 예시
# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()
#
# recursive_function()

def recursive_function(i):  # 이 재귀함수는 마치 스택과 비슷하다
    # 100번째 호출을 했을때 종료
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다.')
    
recursive_function(1)
