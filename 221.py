# Maximal Square
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/82992233
# runtime: faster than 90.41%
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [ [0]*n for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        
        for i in range(1,m):
            for j in range(1,n):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

        return max(map(max,dp))**2