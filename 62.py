# 62. Unique Paths
# Compare with 63, 64

# runtime: faster than 96.36%
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            res[i][0] = 1
        for j in range(m):
            res[0][j] = 1
        
        for i in range(1,n):
            for j in range(1,m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        
        return res[n-1][m-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    grid[i][j] = 1
                else:
                    top = grid[i-1][j] if i > 0 else 0
                    left = grid[i][j-1] if j > 0 else 0
                    grid[i][j] = top + left
        return grid[-1][-1]