# li = list(map(str,input().split()))
# print(li)
# li.sort(reverse=True)
# print(li)
# st = ''.join(li)
# print(st)

def largestNumber(array):
    for i in range(len(array)):
        array[i] = str(array[i])
    # xyab > abxy 비교
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j] + array[i] > array[i] + array[j]:
                array[i], array[j] = array[j], array[i]
        #하나의 문자열로 합치기
        result = ''.join(array)
        if(result == '0'*len(result)):
            return '0'
        else:
            return result

array = list(map(int,input().split()))
print(largestNumber(array))
