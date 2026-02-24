#  260224 시작 2108 마무리


# 로봇은 오른쪽 또는 아래로만 움직임
# 로봇은 왼쪽 또는 위쪽에서 옴 

memo = {
    (0,0) : 1,
    (0,1) : 1,
    (1,0) : 1
}

def dp(m,n):
    if m == 0 or n == 0:
        memo[(m,n)] = 1
        return memo[(m,n)]
    if (m,n) not in memo:
        memo[(m,n)] = dp(m-1,n) + dp(m,n-1)
    return memo[(m,n)]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return dp(m-1,n-1)
                

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         for i in range(0,m+1):
#             for j in range(0,n+1):
#                 memo[i][j] = memo[i][j-1] + memo[i-1][j]
sol = Solution()
print(sol.uniquePaths(1,1))
print(sol.uniquePaths(3,7))