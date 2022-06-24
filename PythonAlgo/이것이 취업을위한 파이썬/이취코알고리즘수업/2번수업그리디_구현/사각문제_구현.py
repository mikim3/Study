    
#시각 문제
# N시까지 3이 하나라도 포함되는 경우의 수 구하기

# 입력
# 5

# 출력
# 11475  (5시까지 3이 포함 된수)
    

# 풀이   이건 완전 탐색 문제다 
# 즉 완전탐색  모든 조건을 다 일일이 확인하는 방법이다
# 하루는 86400초 그냥 새면 된다.

# 입력받기    
# h= int(input())

# count=0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 시 분 초 중에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i) +str(j) +str(k):
#                 count += 1
                
# print(count)

### 문법 기억하기
# if '3' in str(i):  # i 라는 문자열안에 3이 포함되어 있는지 확인
#    print("3이 있어")
# 'j' not in 'python'  # True 가 나옴