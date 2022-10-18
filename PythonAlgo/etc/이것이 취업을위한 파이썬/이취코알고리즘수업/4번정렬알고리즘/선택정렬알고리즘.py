# 선택정렬
# 선택정렬은 N번 비교해서 가장 작은 수를 맨앞으로 보낸다.
# N + (N - 1) + (N - 2) . ... + 2   
# (N^2 + N -2)/2 즉 O(N^2)만큼의 시간복잡도를 가짐

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index =  i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        # 비교한 것 중에 가장 작은 것이 나올때 마다 인덱스 저장
        if array[min_index] > array[j]:
            min_index = j
    # 전체 비교하고 가장 작은것과 지금 비교하는 자리 스왑
    array[i], array[min_index] = array[min_index],array[i]

print(array)

