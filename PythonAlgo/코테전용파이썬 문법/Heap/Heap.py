import heapq
#####################################
# Heap은 완전이진트리로 구현된 자료구조 이다.
# 완전이진트리란 이진트리인데 왼쪽 차일드 노드부터 오른쪽 차일드 노드 순으로 완전히 채워진 형태를 완전이진트리라고 한다.
#

# 완전이진트리


# heap은 Priority queue를 구현하는 방법이다.
# Priority queue 는 우선순위가 가장 높은 값이 먼저 추출 된다.

# Heap 특징 (MaxHeap 버젼)
# 완전 이진트리 형태의 자료구조이다.
# 루트노드가 가장크다.
# 부모노드가 항상 자식노드보다 크다.(max_heap)
# 형제 노드간에는 대소관계가 정해지지 않는다.
#

# priority queue에 dequeue 를 구현하기 위한 heap pop 구현 함수 heapq.heappop()

########################################
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
# 기본적으로 maxheap일때 heappush가 없어서 그걸 우회하는 소스를 생각해야함
# 아래와 같이 리스트 컴프리핸션으로 모든 값에 -1을 곱하면 절댓값으로 생각하면 maxheap이랑 사실상 똑같아짐 (가장 작은 -9가 사실은 가장큰 9를 나타낸다라고 생각하면 편함)
max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [i * -1 for i in max_heap]
heapq.heapify(max_heap)
print(max_heap)
weight = heapq.heappop(max_heap)
value = -1 * weight
print('value == ',value, 'weight == ', weight)
print(max_heap)

###########
# 아래와 같이하면
# (-9, 9) 이런식으로 값이 들어가는데 정렬은 max_heap[x][0] 에 값으로 정렬 되겠지만 사용은 max_heap[x][1] 로 사용하면 편하다.
max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [(i * -1, i)for i in max_heap]
heapq.heapify(max_heap)
print(max_heap)
weight, value = heapq.heappop(max_heap)
print('value == ',value, 'weight == ', weight)
print(max_heap)
print(max_heap[2][1])
#########################
