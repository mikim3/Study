import heapq

# 값을 pop, push를 반복해도 결국 RootNode가 가장 작은 값인 것이 보장된다.

# min heap
min_heap = [5, 3, 9, 4, 1, 2, 6]
heapq.heapify(min_heap) # O(N)
print(min_heap) # [1, 3, 2, 4, 5, 9, 6]
heapq.heappop(min_heap) # O(logN)
print(min_heap) # [2, 3, 6, 4, 5, 9]
heapq.heappush(min_heap, 1) # O(logN)
print(min_heap) # [1, 3, 2, 4, 5, 9, 6]
heapq.heappush(min_heap, 5)
print(min_heap) # [1, 3, 2, 4, 5, 9, 6]

################
# maxheap
#  기본적으로 maxheap일때 heappush가 없어서 그걸 우회하는 소스를 생각해야함
max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [i * -1 for i in max_heap]
heapq.heapify(max_heap)
print(max_heap)
weight = heapq.heappop(max_heap)
value = -1 * weight
print('value == ',value, 'weight == ', weight)
print(max_heap)

###########
#
max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [(i * -1, i)for i in max_heap]
heapq.heapify(max_heap)
print(max_heap)
weight, value = heapq.heappop(max_heap)
print('value == ',value, 'weight == ', weight)
print(max_heap)
