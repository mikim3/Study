# 
# 답봄 뭔소리인지 잘 모르겠음

# 사람들이 자기보다 큰사람이 왼쪽에 몇명 있었는지 기억한다.
# 가장 왼쪽사람의 키는 1이다.

# 입력순서는 키가 1인사람부터 순서대로고

# 
# 오른쪽 사람이 0 이면 가장 키가 큰거겠지



n = int(input())
li = list(map(int,input().split()))
ans = [0] * n
for p in range(1, n+1):
    t = li[p-1]
    # 현재 사람의 왼쪽에 키가 작은 사람의 수
    cnt = 0
    for i in range(n):
        if cnt == t and ans[i] == 0:
            ans[i] = p
            break
        elif ans[i] == 0:
            cnt += 1
print(*ans)





