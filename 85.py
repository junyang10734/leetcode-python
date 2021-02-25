# 85. Maximal Rectangle
# compare: 221, 1277
# DP

# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-85-maximal-rectangle/
# runtime: faster than 23.26%
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[i][j] = 1 if matrix[i][j] == '1' else 0
                else:
                    dp[i][j] = dp[i][j-1] + 1 if matrix[i][j] == '1' else 0

        res = 0
        for i in range(m):
            for j in range(n):
                w = float('inf')
                for k in range(i, m):
                    w = min(w, dp[k][j])
                    if w == 0:
                        break
                    res = max(w * (k-i+1), res)
        
        return res