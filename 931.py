# 931. Minimum Falling Path Sum
# DP

# runtime: faster than 94.52%
# modify in place
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                if j == 0:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j+1])
                elif j == n-1:
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j-1])
                else:
                    matrix[i][j] += min(matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1])
        
        return min(matrix[0])


# 带memory的自顶向下
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = [[math.inf] * n for _ in range(n)]

        def dp(i, j):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return math.inf
            if i == 0:
                return matrix[0][j]
            if memo[i][j] < math.inf:
                return memo[i][j]
            
            memo[i][j] = matrix[i][j] + min(dp(i-1, j-1), dp(i-1, j), dp(i-1, j+1))
            return memo[i][j]

        res = math.inf
        for j in range(n):
            res = min(res, dp(n-1, j))
        return res
