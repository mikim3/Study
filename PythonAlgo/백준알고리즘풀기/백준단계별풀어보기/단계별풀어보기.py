
######## 8단계 기본수학1 

# 1712번 문제
# 손익분기점
#
# a,b,c = list(map(int,input().split()))
# d = c - b  # 한번 팔떄 수익
# sum=0
# count=0

# if d <= 0:  # 진짜로 손해보는장사
#     print(-1)
# else:
#     print(a//d+1)


# 2292번 문제
# 벌집
# 답지봄
# room_no = int(input())
# if room_no == 1:  # 시작지 그대로일때 한번
#     print(1)
# else:
#     i = 1  # room과 비교할 수 
#     n = 0  # 한 바퀴마다 1씩오름
#     while room_no > i:
#         n += 1
#         i += 6 * n
#     print(n + 1)

# 1193번 문제
# 분수찾기
# 답지봄
##########################################################################################################
# n=int(input())
# sum=0
# orda=0
# ordb=0
# for i in range(1,n+1):
#     sum+=i
#     if sum>=n:
#         orda=i
#         ordb=n-(sum-i)
#         break
# a=0
# b=0
# if orda%2!=0:
#     a=orda+1
#     b=0
#     for j in range(ordb):
#         a-=1
#         b+=1
# elif orda%2==0:
#     a=0
#     b=orda+1
#     for j in range(ordb):
#         b-=1
#         a+=1
# print(a,"/",b,sep="")


# 2869
# 달팽이는 올라가고 싶다
# 답지봄
# 수학이 어려워요

# 나의 해설 
# k 올라가는데 걸리는 일수    d   올라간 높이 일때
# a*k-b*(k-1)>=v   라는 식이 나오고 이를 반복문안에 넣어 조건문으로 사용하면 너무 오래걸리니 이항하면
# k >= (v - b)/(a - b) 로 옮길수 있다.   
# 그리고 규칙을 찾아보면 오른쪽 같이 정수로 떨어지면(그 날에 a 만큼 오르니 정확히 도착) 그 값이 k 이고   안떨어지면(a만큼 오르면 정상을 넘어버림) 그 값을 올림한 값이 k이다.

# import math

# a,b,v=list(map(int,input().split()))

# day = math.ceil((v-a)/(a-b)) + 1
# print(day)

# 10250
# ACM 호텔
# 예외처리 못해서 답지봅  // 도 까먹음

# // 이게 몫 이라는 것을 까먹고 있었음 바보

# t = int(input())   # 테스트 데이터 갯수
# # w는 각층의 방의 갯수   h는 몇층 건물인지 
# for _ in range(t):
#     h, w, n = list(map(int,input().split()))
#     if n % h == 0:
#         num = (h * 100) + (n // h)
#     else:
#         num = (n % h * 100) + (n // h + 1)
#     print(num)

# 2775
# 부녀회장이 될테야
# 진짜 너무어렵다  스킵!
# 답지봄  다시봐도 안 떠오를듯
# https://ooyoung.tistory.com/89  

# t = int(input())
# for _ in range(t):  
#     floor = int(input())  # 층
#     num = int(input())  # 호
#     f0 = [x for x in range(1,num + 1)]  # 리스트 컴프리헨션으로 0층의 사람들을 넣어준다.
#     print(f0)
#     for i in range(floor):  # 층 수 만큼 반복
#         for j in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
#             f0[j] += f0[j-1]  # 층별 각 호실의 사람 수를 변경
#         print(f0)
#     print(f0[-1])  # 가장 마지막 수 출력

# 2839번 설탕배달
# 답지봄 아이디어를 듣는거 만으로 푼 문제 답지를 안보고 풀었어도 됐을텐데 아쉽다.

# sugar = int(input())

# bag = 0
# while sugar >= 3:    
#     if sugar % 5 != 0:  # 5키로 짜리로 딱 나누어 떨어지지 않으면
#         sugar -= 3
#         bag += 1 
#     else:
#         sugar -= 5
#         bag += 1
# if sugar != 0:
#     print(-1)
# else: 
#     print(bag)

# 10757번 큰 수 A + B
# ㅋㅋㅋ 답지봄 파이썬은 그냥 바로 출력이 된다.

# A, B = map(int, input().split())
# print(A+B)





############# 브루트 포스 방식 시작

# 2798 번 문제
# 블랙잭 문제
# 문법적으로 pass랑 continue랑 잠깐 헷갈렸음

# n,m=list(map(int,input().split()))   # 카드 갯수 n     카드 합의 한계값 m
# arr=list(map(int,input().split()))   # 카드값 입력
# max1=0

# for i in range(n):
#     for j in range(n):
#         for z in range(n):
#             if (i==j) or (i==z) or (j==z):
#                 # print("continue go",i,j,z)
#                 continue
#             if arr[i]+arr[j]+arr[z]<=m and arr[i]+arr[j]+arr[z]>=max1:
#                 max1=arr[i]+arr[j]+arr[z]
#                 # print(max1)
# print(max1)

# 2231번 문제
# 분해합 
# n=int(input())
# sum1=0  # 더해야할 수 
# count=0

# for i in range(n):  # 최대 n 까지 반복수행 
#     m=str(i)   # '216'
#     for j in range(len(m)):  # 자리수 만큼 반복
#         sum1+=int(m[j])
#     if i+sum1==n:
#         count+=1   
#         print(i)
#         break
#     sum1=0
# if count==0:
#     print(0)

# 7568 번 문제
# 덩치 

# 자기보다 큰 사람 + 1  -> 덩치 등수 라는 규칙이있다

# n= int(input())
# arr1=[]
# arr2=[]

# for i in range(n):
#     arr1.append(list(map(int,input().split())))
# for i in range(n):
#     arr2.append(1)  # 0으로 n개 만큼 초기화    
            
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             continue
#         if arr1[i][0]<arr1[j][0] and arr1[i][1] < arr1[j][1]:
#             arr2[i]=arr2[i]+1
# for i in range(n):
#     print(arr2[i],end=' ')


# 1018 번 문제
# 체스판 다시 칠하기 
# 답지봄



# n,m = list(map(int,input().split()))
# board = list()
# for i in range(N):
#     board.append(input())  # 입력방법도 잘 기억하기
# repair = list()

# # 8 * 8 크기의 체스판과 일치하는지 체크하기 위해서는  8*8크기를 옮겨야한다.
# # 9 * 9 에서는 2 * 2 만큼 옮겨야하고
# # 10 * 10 에서는 3 * 3 만큼 옮겨야한다.
# # 귀납적으로 n * m 크기의 체스판을 확인하기위해 (n - 7) * (m - 7) 만큼 옮기며 확인해야한다.  

# for i in range(n-7):







# 1436  영화감독 셤

# n=int(input())
# m=0  # 1씩 더해지면서 n번 666을 만날때까지 반복 될 수 
# count = 0
# while True:
#     if '666' in str(m):
#         count+=1
#         if count==n:
#             print(m)
#             break        
#     m=m+1   


############# 11단계 브루트 포스 방식 끝

### 12단계 정렬 시작

# 2750번 수 정렬하기

# n = int(input())
# m = list()

# for i in range(n):
#     z = int(input())
#     m.append(z)
# m.sort()
# for i in range(len(m)):
#     print(m[i])


# 2751번 수 정렬하기 2
# 착각하기 쉬움!!!!!

# sort(reverse=True)  vs   reverse()

# reverse()는 리스트를 역순정렬하는 것이고
# sort(reverse=True)는 리스트를 내림차순으로 정렬한다.

# input() 은 반복될때 유의미하게 느리다.
# 그래서 sys.stdin.readline()을 이용하자
# import sys

# n = int(sys.stdin.readline())
# m = list()

# for i in range(n):
#     num = int(sys.stdin.readline())
#     m.append(num)    
# m.sort()
# # m = sorted(m, reverse=True)

# for i in m:
#     print(i)



# 10989번 수 정렬하기 3
# import sys

# n = int(sys.stdin.readline())
# num_list = [0] * 10001

# for _ in range(n):
#     # 기존에는 list.append(sys.stdin.readline()) 이런식으로 작성하였다 그러면 for 문을 돌때마다 메모리를 재할당한다고 한다.  그럼 메모리낭비가 발생하여 미리 정해진 크기의
#     # 리스트 안에 값을 넣으면 해결할 수 있다.
#     num_list[int(sys.stdin.readline())] += 1   
    
# for i in range(10001):
#     if num_list[i] != 0:  #배열기본값 0 
#         for j in range(num_list[i]):
#             print(i)

# 2108번 통계학
# 답지봄
# from collections import Counter 기억하기 
# Counter('hello worldo').most_common(2)  가장 많은 갯수가 나온 수 중에 2개의 값을 갖는다. [('l',3),('o',3)]

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이


# from collections import Counter
# import sys
# n = int(input())
# arr = list()
# for i in range(n):
#     arr.append(int(sys.stdin.readline().rstrip()))
# sum = 0
# avg = 0
# for i in range(n):
#     sum += arr[i]    
# avg = sum / n
# print(int(round(avg,0)))  # 0 디펄트임
# # 중앙값
# arr = sorted(arr)
# mid_value=arr[int(n/2 - 0.5)]  #   arr_sorted[n // 2]  가 더 좋을듯
# print(mid_value)   
# # 최빈값
# cnt = Counter(arr).most_common(2)
# if n > 1:
#     if cnt[0][1] == cnt[1][1]:
#         print(cnt[1][0])
#     else:
#         print(cnt[0][0])
# else:
#     print(cnt[0][0])
# # 범위
# range_value = max(arr) - min(arr)
# print(range_value)

# 1427번 소트인사이드

# n = list(input())
# n.sort(reverse=True)
# for i in n:
#     print(i,end='')

# 11650번 좌표정렬하기
# 너무 파이썬이 알아서 풀어줬다.
# x y 좌표를 따로 명령하는 람다함수정도는 알아야 이 문제를 풀었다고 인정 받을만 하다고 생각이 드는데 x y 좌표 따로 정렬마져 알아서 되버렸다


# import sys
# n = int(input())
# arr = list()
# for i in range(n):
#     arr.append(list(map(int,sys.stdin.readline().split())))
# arr.sort()
# for i in range(n):
#     print(arr[i][0],arr[i][1])

##흔치 않은 유형의 답안
# import sys
# input = sys.stdin.readline

# n = int(input())

# array = []
# for i in range(n):
#     a, b = map(int,input().split())
#     array.append([a,b])

# array.sort()

# for i in range(n):
#     print(array[i][0],array[i][1])



# 11651번 좌표 정렬하기2
# 전날에 푼 좌표 정렬하기1번이 너무 기억에 남았음
# lambda 잘기억하기

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list()

# for i in range(n):
#     arr.append(list(map(int,input().split())))

# arr.sort(key= lambda xy : (xy[1], xy[0]) )

# for i in range(len(arr)):
#     print(arr[i][0],arr[i][1])

# 1181번 단어 정렬
# 리스트에서 중복을 제거하는 방법 잘 기억하기
# arr_set = set(arr)
# arr = list(arr_set)

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list()
# for i in range(n):
#     arr.append(input().rstrip())
    
# arr_set = set(arr)
# arr = list(arr_set)
# arr.sort(key = lambda xy : (len(xy),xy))

# for i in range(len(arr)):
#     print(arr[i])


# 10814번 나이순 정렬
# 답지 봄 정답 봄   
# 아직도  lambda에 대한 이해가 부족하다

# import sys
# input = sys.stdin.readline
# n = int(input())
# age_name = list()
# for i in range(n):
#     age_name.append(input().split())
# age_name.sort(key = lambda x : int(x[0]))
# for i in range(len(age_name)):
#     print(age_name[i][0],age_name[i][1])

# 18870번 좌표 압축
# 시간초과로 답지봄

#####시간초과 틀린코드
# n = int(input())
# arr1 = list(map(int,input().split()))
# arr2 = list(sorted(set(arr1)))  # 중복 값 제거한 후 정렬
# 아래 2중 for 문은 arr1의 길이의 제곱배로 도는 O(n^2)의 시간복잡도를 가진다. 굉장히 비효율적이다.
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         if arr2[j] == arr1[i]:  # 값이 일치하면
#             arr1[i] = j  # 인덱스 값이 해당 값으로 바뀜
# for i in range(len(arr1)):
#     print(arr1[i],end=' ')

#### 맞는코드
# n = int(input())
# arr1 = list(map(int,input().split()))
# arr2 = list(sorted(set(arr1)))  # 중복 값 제거한 후 정렬

# # 딕셔너리 문법 : x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# # 딕셔너리를 만드는데 arr2[i] 가 키 값이고  value는 arr2의 인덱스 값이다.
# dic = {arr2[i] : i for i in range(len(arr2))}  

# for i in range(len(arr1)):
#     print(dic[arr1[i]],end=' ')    

######### 16단계 그리디방식 시작
#

# 동전 최소 개수 구하기 문제
# 핵심은 가장 큰 돈부터 쓰자
# n,k=list(map(int,input().split()))
# moneyKind=[]

# print(n,k)

# for i in range(n):
#     moneyKind[i]=int(input())
    
# for i in range(n-1,-1,-1):
# 

