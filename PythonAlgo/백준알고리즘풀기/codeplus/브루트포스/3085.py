# 시작시간  :   15:53분
# 답 봄  
# 문제에서 고려할 점들이 너무 많아서 헷갈렸다.


# 최대 갯수 좌표(공동 1위 포함)들을 구한다.


#   만약에 다다음음과  현재가 같같은 부분을 만만나나면 카카운운트트를  시시작작한한다다.   
# 카카운트가 최최대대치치면  일단  그 좌좌표표를 저장 한다 
# 그 뒤뒤에  그  좌좌표표들들만  주주변  한한칸칸씩  바바꾸꾸면  같같이  바바꾸꾸는 지  찾찾는는다  ㅇ만약 한한번번이이라도 값값이  ㅁ오르면 거거기기서  끝끝  


n = int(input())

array = []
for _ in range(n):
    colors = list(map(str, input()))
    array.append(colors)

maxCount = 0 #최대 사탕 개수를 초기화

# 배열의 행 마다 같은 색의 사탕이 몇개 있는지 계산
def width():
    global  maxCount
    
    for k in range(n):
        countRow = 1 #초기 개수를 1로 초기화
        for l in range(n - 1):
            if array[k][l] == array[k][l + 1]: #만약 같은 열의 사탕의 색이 같다면
                countRow += 1 #사탕 개수 1 증가
                maxCount = max(maxCount,countRow) #증가시킨 값과 최대 사탕개수를 비교하여 큰값을 대입
            else: #만약 같은 열의 사탕 개수가 다르다면
                countRow = 1 #개수를 1로 초기화


# 배열의 열마다 같은 색의 사탕이 몇개 있는지 계산
def height():
    for k in range(n):
        global maxCount
        
        countColumn = 1 #초기 개수를 1로 초기화
        for l in range(n - 1):
            if array[l][k] == array[l + 1][k]: #만약 같은 행의 사탕의 색이 같다면
                countColumn += 1 #사탕 개수를 1개씩 증가시켜주고
                maxCount = max(maxCount,countColumn) #증가시킨 값과 최대 사탕개수를 비교하여 큰값을 대입
            else: #만약 같은 행의 색이 다르다면
                countColumn = 1 #개수를 1로 초기화


for i in range(n):
    for j in range(n - 1):
        # 만약 입력 받은 배열의 행의 원소가 다르다면
        if array[i][j] != array[i][j + 1]:
            array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
            width()
            height()
            array[i][j + 1], array[i][j] = array[i][j], array[i][j + 1]
        # 만약 입력 받은 배열의 열의 원소가 다르다면
        if array[j][i] != array[j + 1][i]:
            array[j][i], array[j + 1][i] = array[j + 1][i], array[j][i]
            width()
            height()
            array[j + 1][i], array[j][i] = array[j][i], array[j + 1][i]

print(maxCount) #색이 같은 사탕개수 최대값을 출력



