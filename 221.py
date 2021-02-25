# 221. Maximal Square
# compare: 85, 1277
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/82992233
# runtime: faster than 90.41%
class Solution1:
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


# runtime: faster than 99.31%
# same alg with solution1
# modify in place
class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            matrix[i][0] = int(matrix[i][0])
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                else:
                    matrix[i][j] = 0

        return max(map(max, matrix)) ** 2