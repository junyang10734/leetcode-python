# 1277. Count Square Submatrices with All Ones
# compare: 85, 221
# DP


# runtime: faster than 37.43% 
class Solution1:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [ [0 for i in range(n)] for j in range(m)]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 1:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans += dp[i][j]
                
        return ans


# same alg woth solution1
# modify in place
# runtime: faster than 66.52%
class Solution2:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0 and matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                res += matrix[i][j]
        return res