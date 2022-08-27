
# 병합정렬 방법
# 배열의 왼쪽은 lt  오른쪽끝은 rt이다.

# D(0,0) 은 if문에서 거짓으로 바로 끝남

# 만약 D(0,1) 처럼 길이가 1인 병합정렬문을 만나면 mid로 분할을 하면 1개(0번 인덱스) 1개(1번 인덱스)로 분할 된다.
# 이렇게 길이1이 됬을때 tmp에 넣어서 정렬을 하고 다시 arr에 넣으면 된다.

def Dsort(lt, rt):
    if lt<rt:
        mid = (lt + rt) // 2
        Dsort(lt, mid)
        Dsort(mid + 1, rt)
        p1 = lt
        p2 = mid+1
        tmp = []
        while p1 <= mid and p2 <= rt:  # 두 리스트 합치기에서 배운내용
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:  # p2쪽이 작다
                tmp.append(arr[p2])
                p2+=1
        if p1<=mid: tmp = tmp + arr[p1:mid+1]   # p1이 남은 경우
        if p2<=rt: tmp=tmp+arr[p2:rt+1]  # p2가 남은경우
        # tmp 만든거를 arr에 넣기
        for i in range(len(tmp)):
            arr[lt + i] = tmp[i]

if __name__=="__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print("Before sort : ", end='')
    print(arr)
    Dsort(0, 7)
    print()
    print("After sort :  ", end='')
    print(arr)


