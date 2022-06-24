# 모험가 길드 
# N명의 모험가가 있다.
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다.
# 최대 몇 개의 모험가 그룹을 만들 수 있나?   N명의 호험가에 대한 정보가 주어졌을때 여행을 떠날수 있는 그룹 수의 최대값을 구하는 프로그램을 작성하여라

# 입출
# 첫 쨰줄에 모험가수 N주어짐
# 둘쨰 줄에 공포도 값을 N이하 자연수로 주어짐  공백으로 구분

# 내 풀이 : 핵심은 가장 낮은 공포도 모험가 먼저 보내야 한다.
# print("모험가 길드 문제")
# n=input()
# data=list(map(int,input().split()))
# data.sort()

# result = 0  # 총 그룹의 수 
# count = 0 # 현재 그룹 포함된 모험가 수

# for i in data: # data 값 하나 씩 비교 
#     count += 1 # 
#     if count >= i:  # 카운트보다 data현재 값이 낮으면 
#         result += 1  # 결과 즉 그룹을 하나 추가한다.
#         count=0      #

# print(result)



