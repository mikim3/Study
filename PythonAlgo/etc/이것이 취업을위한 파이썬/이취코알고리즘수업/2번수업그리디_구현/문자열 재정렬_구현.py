# 문자열 재정렬 문제 
# 

# 알파벳 대문자와 숫자로만 구성된 문자열이 입력된다.
# 이를 알파벳은 오름차순으로 출력하고 모든숫자를 더한 값을 맨뒤에 출력

# ex)  K1KA5CB7 -> ABCKK13  

#####################나의 답안
# input_data = input()  #문자열로 일단받음
# sort_data=[]

# num=0
# for i in range(len(input_data)):
#     if ord('A')<=ord(input_data[i])<=ord('Z'):
#         sort_data+=input_data[i]
#     else:
#         num+=int(input_data[i])
# sort_data.sort()
# for i in range(len(sort_data)):
#     print(sort_data[i],end='')
# print(num)
#####################나의 답안 끝

##################모범답안
# data = input()
# result = []
# value = 0

# # 문자를 하나씩 확인하며
# for x in data:
#     # 알파벳인 경우 결과 리스트에 삽입
#     if x.isalpha():  # isalpha() 문자열 구성이 알파벳인지 확인
#         result.append(x)  # 리스트에 값을 하나씩 추가한다 -> append
#         print(result)
#     # 숫자는 따로 더하기
#     else:
#         value += int(x)
        
# # 알파벳을 오름차순으로 정렬
# result.sort()

# # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
# if value != 0:
#     result.append(str(value))
    
# # 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
# print(''.join(result))
