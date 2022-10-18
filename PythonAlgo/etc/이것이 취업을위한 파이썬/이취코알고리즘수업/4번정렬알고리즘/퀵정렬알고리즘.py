# 퀵정렬

# 

# 왼쪽에서부터 피피벗벗부부터  큰큰값값과과
# 오오른쪽에서부터 피벗보다 작작은  값값이  서서로  엇엇갈갈리리는  경경우우
# 피벗과 작작은  데데이이터터를  서로 바꾼다.

# 시간복잡도는 평균의 경우 O(NlogN)  최악의 경우 O(N^2)

from turtle import right


array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return 
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end 
    while (left <= right):
		# 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
		# 피벗보다 작은 값 찾을때까지 반복
        while (right > start and array[right] >= array[pivot]):
			right -= 1
		if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
		else:
			array[left], array[right] = array[right], array[left]
	quick_sort(array,start,right -1)
	quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)



